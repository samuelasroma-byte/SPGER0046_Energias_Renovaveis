"""Package every file in an exact Git commit and verify its SHA-256 manifest."""
from __future__ import annotations

import argparse
import csv
from datetime import datetime, timezone
import hashlib
import io
import json
from pathlib import Path
import subprocess
import zipfile

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'SPGER0046_Energias_Renovaveis/'
ASSET = 'SPGER0046_Projeto_Completo.zip'


def git(repo, *args):
    return subprocess.check_output(['git', '-C', str(repo), *args])


def sha256_file(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def verify_archive(path, expected_commit=None):
    """Re-read every archived byte; the manifest covers the complete Git tree."""
    with zipfile.ZipFile(path) as archive:
        names = archive.namelist()
        assert len(names) == len(set(names)), 'Duplicate archive entries'
        metadata = json.loads(archive.read(PREFIX + 'ENTREGA.json'))
        if expected_commit:
            assert metadata['commit'] == expected_commit
        manifest = list(csv.DictReader(io.StringIO(
            archive.read(PREFIX + 'MANIFESTO_SHA256.csv').decode('utf-8'))))
        expected = {PREFIX + r['path'] for r in manifest}
        expected |= {PREFIX + 'ENTREGA.json', PREFIX + 'MANIFESTO_SHA256.csv'}
        assert set(names) == expected, 'Missing or unexpected archive files'
        assert len(manifest) == metadata['tracked_files']
        for row in manifest:
            info = archive.getinfo(PREFIX + row['path'])
            assert info.file_size == int(row['bytes']), row['path']
            with archive.open(info) as stream:
                digest = hashlib.file_digest(stream, 'sha256').hexdigest()
            assert digest == row['sha256'], row['path']
    return metadata


def package(repo, ref, output):
    repo = Path(repo).resolve()
    output = Path(output).resolve()
    if output == repo or repo in output.parents:
        raise ValueError('Save delivery assets outside the Git working tree.')
    output.mkdir(parents=True, exist_ok=True)
    commit = git(repo, 'rev-parse', '--verify', ref + '^{commit}').decode().strip()
    tree = git(repo, 'rev-parse', commit + '^{tree}').decode().strip()
    timestamp = int(git(repo, 'show', '-s', '--format=%ct', commit))
    date = datetime.fromtimestamp(timestamp, timezone.utc)
    zipdate = (max(1980, date.year), date.month, date.day,
               date.hour, date.minute, date.second)
    entries = []
    for raw in git(repo, 'ls-tree', '-r', '-z', '--full-tree', commit).split(b'\0'):
        if not raw:
            continue
        header, name = raw.split(b'\t', 1)
        mode, kind, oid = header.decode().split()
        if kind != 'blob' or mode not in {'100644', '100755'}:
            raise ValueError('Unsupported Git entry: ' + name.decode())
        path = name.decode('utf-8')
        if path in {'ENTREGA.json', 'MANIFESTO_SHA256.csv'}:
            raise ValueError('Reserved delivery metadata name: ' + path)
        entries.append((path, mode, oid))
    entries.sort()
    metadata = {
        'project': PREFIX.rstrip('/'), 'commit': commit, 'tree': tree,
        'commit_date_utc': date.isoformat(), 'tracked_files': len(entries),
        'docx_files': sum(p.endswith('.docx') for p, _, _ in entries),
        'pdf_files': sum(p.endswith('.pdf') for p, _, _ in entries),
        'equation_documents': [p for p, _, _ in entries
                               if '/equacoes/' in '/' + p
                               and p.endswith(('.docx', '.pdf'))],
        'scope': 'Todos os arquivos versionados neste commit; PDFs de terceiros acessados por links permanecem externos.',
        'verification': 'MANIFESTO_SHA256.csv identifica caminho, tamanho, SHA-256 e objeto Git de cada arquivo versionado.',
    }

    def info(path, mode='100644'):
        result = zipfile.ZipInfo(PREFIX + path, zipdate)
        result.compress_type = zipfile.ZIP_DEFLATED
        result.create_system = 3
        result.external_attr = int(mode, 8) << 16
        return result

    target = output / ASSET
    temporary = target.with_suffix('.zip.tmp')
    manifest = io.StringIO(newline='')
    writer = csv.DictWriter(manifest, ['path', 'bytes', 'sha256', 'git_blob'])
    writer.writeheader()
    process = subprocess.Popen(['git', '-C', str(repo), 'cat-file', '--batch'],
                               stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    try:
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED,
                             compresslevel=6, allowZip64=True) as archive:
            for path, mode, oid in entries:
                process.stdin.write((oid + '\n').encode()); process.stdin.flush()
                actual_oid, kind, size = process.stdout.readline().decode().split()
                assert actual_oid == oid and kind == 'blob'
                remaining = int(size)
                digest = hashlib.sha256()
                with archive.open(info(path, mode), 'w', force_zip64=True) as stream:
                    while remaining:
                        chunk = process.stdout.read(min(1024 * 1024, remaining))
                        if not chunk:
                            raise EOFError(path)
                        stream.write(chunk); digest.update(chunk)
                        remaining -= len(chunk)
                assert process.stdout.read(1) == b'\n'
                writer.writerow({'path': path, 'bytes': size,
                                 'sha256': digest.hexdigest(), 'git_blob': oid})
            archive.writestr(info('ENTREGA.json'),
                             json.dumps(metadata, ensure_ascii=False, indent=2) + '\n')
            archive.writestr(info('MANIFESTO_SHA256.csv'), manifest.getvalue())
        process.stdin.close()
        if process.wait() != 0:
            raise RuntimeError('git cat-file failed')
        verify_archive(temporary, commit)
        temporary.replace(target)
    finally:
        if process.poll() is None:
            process.kill(); process.wait()
        process.stdout.close()
        if temporary.exists():
            temporary.unlink()
    digest = sha256_file(target)
    (output / (ASSET + '.sha256')).write_text(digest + '  ' + ASSET + '\n')
    report = {**metadata, 'archive': ASSET, 'bytes': target.stat().st_size,
              'sha256': digest, 'verified_files': len(entries),
              'verification': 'Todos os arquivos do ZIP reabertos e conferidos pelo manifesto SHA-256.'}
    (output / 'Verificacao_Pacote.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2) + '\n')
    notes = (
        'Projeto completo no commit `' + commit + '`.\n\n'
        'Inclui bibliografia em Word e PDF, identificação da fonte PVDAQ/OEDI, '
        'guia técnico, inventário geral e quatro quadros de equações em Word e PDF, '
        'notebooks, dados versionados, figuras, tabelas e índices das 19 subseções.\n\n'
        'O ZIP reúne ' + str(len(entries)) + ' arquivos versionados. '
        'O manifesto interno permite conferir cada arquivo. '
        'Os PDFs de terceiros com acesso externo continuam disponíveis pelos links do acervo.\n\n'
        'SHA-256 do ZIP: `' + digest + '`.\n')
    (output / 'Notas_Entrega.md').write_text(notes)
    return report


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, default=ROOT)
    parser.add_argument('--ref', default='HEAD')
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(package(args.repo, args.ref, args.output), ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
