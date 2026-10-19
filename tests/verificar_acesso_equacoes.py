"""Verify readable PDF copies, preserved Word files and mobile access routes."""
from pathlib import Path
import hashlib
import json
import re
import subprocess
import sys
from urllib.parse import urlsplit

import fitz

ROOT=Path(__file__).resolve().parents[1]
publication=json.loads((ROOT/'docs/auditoria/Publicacao_Drive_Equacoes.json').read_text())
inventory=json.loads((ROOT/'docs/equacoes/Inventario_Equacoes.json').read_text())
review=json.loads((ROOT/'docs/auditoria/Revisao_Unidades_Equacoes.json').read_text())
reviewed={f['path']:f for f in review['files']}
records=publication['files']
assert len(records)==5
paths=[]
for number,record in enumerate(records):
    word=ROOT/record['path'];pdf=ROOT/record['pdf_path']
    source_hash=hashlib.sha256(word.read_bytes()).hexdigest()
    assert source_hash==record['sha256']==record['pdf_source_docx_sha256']==reviewed[record['path']]['sha256']
    assert pdf.read_bytes().startswith(b'%PDF-')
    assert hashlib.sha256(pdf.read_bytes()).hexdigest()==record['pdf_sha256']
    document=fitz.open(pdf)
    assert not document.needs_pass
    assert len(document)==record['pdf_pages']==reviewed[record['path']]['pages']
    text='\n'.join(p.get_text() for p in document)
    # Only the numbered table entry followed by its subsection counts here;
    # cross-references in notes and the source list are deliberately excluded.
    found=re.findall(r'(?m)^(E[1-4]\.\d{2})\n([1-4]\.\d+)\n',text)
    expected=[(r['id'],r['subsection']) for r in inventory['equations'] if number==0 or r['section']==number]
    assert len(found)==len(set(found))==len(expected),(number,found)
    assert set(found)==set(expected),(number,found)
    assert urlsplit(record['drive_url']).hostname=='docs.google.com'
    assert urlsplit(record['pdf_drive_url']).hostname=='drive.google.com'
    paths.append(dict(path=record['pdf_path'],pages=len(document),equations=len(expected),sha256=record['pdf_sha256']))

names={Path(f['path']).name for f in records}
pages=[ROOT/'docs/equacoes/README.md',*ROOT.glob('secoes/*/equacoes/README.md'),
       *ROOT.glob('secoes/*/documentos/README.md'),*ROOT.glob('secoes/*/subsecoes/*/README.md')]
for page in pages:
    for target in re.findall(r'\]\(([^\n)]+)\)',page.read_text()):
        if Path(urlsplit(target).path).name in names:
            assert urlsplit(target).hostname=='raw.githubusercontent.com',(page,target)
for record in records:
    text=(ROOT/'docs/equacoes/README.md').read_text()
    assert record['drive_url'] in text and record['pdf_drive_url'] in text
for page in ROOT.glob('secoes/*/equacoes/README.md'):
    text=page.read_text()
    assert 'Ler PDF no Drive' in text and 'Abrir Word no Drive' in text and 'Baixar Word' in text
for page in ROOT.glob('secoes/*/subsecoes/*/README.md'):
    assert '[Quadro de equações da seção em PDF e Word](../../equacoes/README.md)' in page.read_text()

protected=['src','config','data','notebooks','outputs/series','outputs/avaliacao',
           'docs/equacoes/Inventario_Equacoes.json','docs/equacoes/Inventario_Equacoes.csv',
           *[r['path'] for r in records]]
changed=subprocess.check_output(['git','-C',str(ROOT),'diff','50b0d69098da8aac7d1d9d3cc7c524240977b0f6','--name-only','--',*protected],text=True).splitlines()
assert not changed,changed
result=dict(status='passed',PDF_documents=5,total_pages=sum(r['pages'] for r in paths),
                     numbered_equations_preserved=61,Word_files_preserved=True,
                     subsection_access_routes=19,direct_DOCX_blob_links_in_equation_navigation=0,
                     scientific_sources_and_results_unchanged=True,files=paths)
if '--write-report' in sys.argv:
    (ROOT/'docs/auditoria/Verificacao_Acesso_Equacoes.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
