"""Verify complete, reproducible snapshots rather than arbitrary working files."""
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import zipfile

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('delivery', ROOT / 'scripts/empacotar_entrega.py')
delivery = importlib.util.module_from_spec(spec); spec.loader.exec_module(delivery)


def main():
    with tempfile.TemporaryDirectory() as directory:
        base = Path(directory); repo = base / 'repo'; repo.mkdir()
        def git(*args):
            return subprocess.check_output(['git', '-C', str(repo), *args]).decode().strip()
        git('init', '-q'); git('config', 'user.name', 'Fixture')
        git('config', 'user.email', 'fixture@example.invalid')
        (repo / 'README.md').write_text('primeira versão\n')
        (repo / 'equações.docx').write_bytes(b'PK\0\x80Word original')
        git('add', '--', 'README.md', 'equações.docx'); git('commit', '-qm', 'primeira')
        commit = git('rev-parse', 'HEAD')
        (repo / 'README.md').write_text('edição local não publicada')
        (repo / 'temporario.zip').write_bytes(b'exclude')
        first = delivery.package(repo, commit, base / 'first')
        second = delivery.package(repo, commit, base / 'second')
        assert first['sha256'] == second['sha256'], 'Non-reproducible ZIP'
        with zipfile.ZipFile(base / 'first' / delivery.ASSET) as archive:
            assert archive.read(delivery.PREFIX + 'README.md') == 'primeira versão\n'.encode()
            assert delivery.PREFIX + 'temporario.zip' not in archive.namelist()
        (repo / 'novo.pdf').write_bytes(b'%PDF-new')
        git('add', '--', 'novo.pdf'); git('commit', '-qm', 'PDF adicional')
        latest = delivery.package(repo, 'HEAD', base / 'latest')
        assert latest['tracked_files'] == 3 and latest['commit'] != commit
        with zipfile.ZipFile(base / 'latest' / delivery.ASSET) as archive:
            assert archive.read(delivery.PREFIX + 'novo.pdf') == b'%PDF-new'
        delivery.verify_archive(base / 'latest' / delivery.ASSET, latest['commit'])
        print(json.dumps({'deterministic': True, 'exact_commit': True,
                          'untracked_excluded': True, 'new_file_included': True}))


if __name__ == '__main__': main()
