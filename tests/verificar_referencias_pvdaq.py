"""Check the official dataset citation, stable 39 codes and preserved originals."""
from pathlib import Path
import csv
import hashlib
import json
import re
import subprocess

from docx import Document
import fitz

ROOT = Path(__file__).resolve().parents[1]
BASE = 'a1fb8f881e71061799a6ef231802b73e490701ac'


def main():
    meta = json.loads((ROOT / 'references/pvdaq_dataset_citacao.json').read_text())
    original = ROOT / 'bibliografia/outputs/Referencias_por_Subsecao.docx'
    assert hashlib.sha256(original.read_bytes()).hexdigest() == 'b4382b53d4e75b711fb95fe3ad3d8e8bfd801015e5c24841c33c8ed752c00b61'
    rows = json.loads((ROOT / 'bibliografia/principal/Referencias_B01_B39.json').read_text())
    baseline = json.loads(subprocess.check_output([
        'git', '-C', str(ROOT), 'show', BASE + ':bibliografia/principal/Referencias_B01_B39.json']))
    assert len(rows) == 39 and {r['code'] for r in rows} == {f'B{i:02}' for i in range(1, 40)}
    assert [r for r in rows if r['code'] != 'B24'] == [r for r in baseline if r['code'] != 'B24']
    b24 = next(r for r in rows if r['code'] == 'B24')
    assert b24['reference'] == meta['citation_abnt'] and b24['method_codes'] == ['R01']
    assert len(meta['authors']) == 6 and meta['year'] == 2021
    assert meta['subset']['analysis_start_local'] == '2024-04-01'
    assert meta['subset']['analysis_end_exclusive_local'] == '2024-07-01'

    def blocks(document):
        result = {}; current = None
        for p in document.paragraphs:
            match = re.match(r'REFERÊNCIA (B\d{2})', p.text)
            if match:
                current = match[1]; result[current] = []
            if current:
                result[current].append(p.text)
        return {key: '\n'.join(value).strip() for key, value in result.items()}
    updated = ROOT / 'bibliografia/atualizada/Referencias_por_Subsecao_Atualizadas.docx'
    old_doc, new_doc = Document(original), Document(updated)
    old_blocks, new_blocks = blocks(old_doc), blocks(new_doc)
    assert set(new_blocks) == set(old_blocks) and len(new_blocks) == 39
    assert all(new_blocks[b] == old_blocks[b] for b in old_blocks if b != 'B24')
    assert meta['citation_abnt'] in new_blocks['B24']
    assert len(new_doc.tables) == len(old_doc.tables) == 4
    assert [t._tbl.xml for t in old_doc.tables] == [t._tbl.xml for t in new_doc.tables]

    sources = json.loads((ROOT / 'data/raw/fontes_pvdaq.json').read_text())
    assert len(sources) == 5
    for source in sources:
        assert source['url'].startswith(meta['subset']['source_prefix'])
        assert hashlib.sha256((ROOT / 'data/raw' / source['file']).read_bytes()).hexdigest() == source['sha256']
    publication = json.loads((ROOT / 'docs/auditoria/Publicacao_Referencias_PVDAQ.json').read_text())
    for record in publication['files']:
        assert hashlib.sha256((ROOT / record['path']).read_bytes()).hexdigest() == record['sha256']
        assert record['verified_download']
    pdf = fitz.open(ROOT / 'bibliografia/atualizada/Referencias_por_Subsecao_Atualizadas.pdf')
    text = '\n'.join(p.get_text() for p in pdf)
    assert len(pdf) == publication['pdf_pages']
    assert set(re.findall(r'REFERÊNCIA (B\d{2})', text)) == set(new_blocks)
    assert meta['doi'] in text and '2021' in text and '2024' in text
    correspondence = list(csv.DictReader((ROOT / 'bibliografia/principal/Correspondencia_B_A.csv').open(encoding='utf-8-sig')))
    assert len(correspondence) == 39
    assert next(r for r in correspondence if r['codigo_B'] == 'B24')['referencia_ABNT'] == meta['citation_abnt']
    for filename in ['referencias_fundamentacao.bib', 'referencias_fundamentacao.ris']:
        value = (ROOT / 'bibliografia/atualizada' / filename).read_text()
        assert value.count(meta['doi']) == 1 and meta['title'] in value
    print(json.dumps({'references': 39, 'unchanged_references': 38, 'source_files_verified': 5,
                      'updated': 'B24', 'access_documentation': 'B27', 'PDF_pages': len(pdf),
                      'original_Word_preserved': True, 'Drive_readback_verified': True}))


if __name__ == '__main__': main()
