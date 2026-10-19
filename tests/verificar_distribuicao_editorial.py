"""Regression checks for exclusive editorial placement and unchanged evidence."""
from pathlib import Path
from collections import Counter
from contextlib import redirect_stdout
from html.parser import HTMLParser
import ast
import base64
import hashlib
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

import nbformat
import pandas as pd
from lxml import etree

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/'src'),str(ROOT/'scripts')]
import editorial_fv as editorial
import projeto_fv as fv
import refinamento_fv as rf
import relatorio_fv as rel

rules=json.loads((ROOT/'config/distribuicao_editorial.json').read_text())
sections={str(s['section']):s for s in rules['sections']}
chapter=json.loads((ROOT/'docs/secoes_capitulo.json').read_text())
valid={s['id'] for s in chapter}
for family in ['figures','csv_tables','word_tables','frames']:
    items=rules[family]
    assert len({i['id'] for i in items})==len(items),family
    assert all(i['owner_subsection'] in valid for i in items),family
assert [len(rules[k]) for k in ['figures','csv_tables','word_tables','frames']]==[30,24,16,6]

def links(page):
    return [(page.parent/p.split('#',1)[0]).resolve()
            for p in re.findall(r'\]\(([^\n]*?)\)',page.read_text())
            if not re.match(r'\w+://|#',p)]

inventory=json.loads((ROOT/'docs/auditoria/Inventario_Figuras.json').read_text())
by_id={f['id']:f for f in inventory}
subpages=list(ROOT.glob('secoes/*/subsecoes/*/README.md'))
assert len(subpages)==19
roots=[ROOT/s['directory']/'README.md' for s in rules['sections']]
graphic_paths=set()
for item in rules['figures']:
    ident=item['id'];owner=item['owner_subsection'];record=by_id[ident]
    assert record['subsections']==owner
    assert [s['id'] for s in chapter if ident in s['figures']]==[owner]
    assert len(record['files'])==4
    for variant,relative in record['files'].items():
        path=ROOT/relative;theme,fmt=variant.split('_')
        assert path==editorial.figure_path(ROOT,ident,theme,fmt) and path.is_file()
        assert path not in graphic_paths;graphic_paths.add(path)
    # All four alternatives appear together in one section and one subsection.
    expected=ROOT/sections[owner[0]]['directory']
    for pages,target in [(roots,expected/'README.md'),(subpages,expected/'subsecoes'/owner.replace('.','_')/'README.md')]:
        found=[p for p in pages if ROOT/record['files']['claro_png'] in links(p)]
        assert found==[target],(ident,found,target)

for page in ROOT.glob('secoes/**/*.md'):
    own_section=page.relative_to(ROOT).parts[1]
    for path in links(page):
        if path in graphic_paths:
            assert path.relative_to(ROOT).parts[1]==own_section,(page,path)
    assert not any(name in page.read_text() for name in [
        'Graficos_do_Projeto.docx','Tabelas_do_Projeto.docx','Quadros_do_Projeto.docx',
        'Ilustracoes_FV.docx','Fluxogramas_do_Projeto.docx']),page

for item in rules['csv_tables']:
    target=ROOT/item['path'];owner=item['owner_subsection']
    found=[p for p in subpages if target in links(p)]
    expected=ROOT/sections[owner[0]]['directory']
    assert found==[expected/'subsecoes'/owner.replace('.','_')/'README.md'],item['id']
    pages=list(ROOT.glob('secoes/*/tabelas/README.md'))
    assert [p for p in pages if target in links(p)]==[expected/'tabelas/README.md']

# Compare actual editable cell values, independently of the extraction code.
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def word_tables(path):
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None
        body=etree.fromstring(archive.read('word/document.xml')).find('w:body',ns)
    current=None;result={}
    for element in body:
        text=''.join(element.xpath('.//w:t/text()',namespaces=ns))
        match=re.match(r'(Tabela|Quadro) (\d+)\s*[—–-]',text)
        if match:current=('T' if match[1]=='Tabela' else 'Q')+str(int(match[2])).zfill(2)
        if element.tag=='{'+ns['w']+'}tbl':
            assert current
            result.setdefault(current,[]).append([
                [''.join(cell.xpath('.//w:t/text()',namespaces=ns)) for cell in row.findall('w:tc',ns)]
                for row in element.findall('w:tr',ns)])
    return result

original={**word_tables(ROOT/'outputs/tabelas/docx/Tabelas_do_Projeto.docx'),
          **word_tables(ROOT/'outputs/quadros/docx/Quadros_do_Projeto.docx')}
seen=Counter();word_files=[]
for section in rules['sections']:
    path=ROOT/section['directory']/f"tabelas/docx/Materiais_Tabulares_Secao_{section['section']:02d}.docx"
    word_files.append(path);actual=word_tables(path)
    own=[r for r in rules['word_tables']+rules['frames'] if r['owner_subsection'][0]==str(section['section'])]
    assert set(actual)=={r['id'] for r in own},path
    seen.update(actual.keys())
    for ident,blocks in actual.items():
        if ident.startswith('T') or ident in ['Q01','Q02']:
            assert blocks==original[ident],ident
        else:
            assert len(blocks)==1
            for row in blocks[0][1:]:
                subsection=re.match(r'[1-4]\.\d+',row[0])[0]
                ids=re.search(r'Figuras: ([^.]+)\.',row[1])[1].split(', ')
                expected=[f['id'].split('_')[0] for f in rules['figures'] if f['owner_subsection']==subsection]
                assert ids==expected,(ident,subsection,ids,expected)
assert len(seen)==22 and set(seen.values())=={1}
assert len(original['T16'])==4

protected=['src/projeto_fv.py','config/projeto.json','config/modulo_cec.json',
           'config/inversor_cec.json','data','outputs/tabelas/csv','outputs/series',
           'outputs/avaliacao','bibliografia/outputs',
           'notebooks/originais_executados','bibliografia/originais_executados']
changed=subprocess.check_output(['git','-C',str(ROOT),'diff',rules['base_commit'],'--name-only','--',*protected],text=True).splitlines()
assert not changed,changed

nb=nbformat.read(ROOT/'notebooks/01_Projeto_FV_Quatro_Secoes.ipynb',as_version=4)
nbformat.validate(nb)
cells={};current=None;shown=Counter()
for cell in nb.cells:
    if cell.cell_type=='markdown':
        match=re.match(r'^## ([1-4]\.\d+) ',cell.source)
        if match:current=match[1]
    elif 'rf.show(CTX,' in cell.source:
        cells[current]=cell.source
        call=next(n for n in ast.walk(ast.parse(cell.source)) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='show')
        ids=ast.literal_eval(call.args[1]);shown.update(ids)
        assert ids==[f['id'] for f in rules['figures'] if f['owner_subsection']==current]
assert set(cells)==valid and len(shown)==30 and set(shown.values())=={1}
bootstrap=next(c.source for c in nb.cells if c.cell_type=='code' and 'support=base64' in c.source)
encoded=re.search(r'b64decode\([\'\"]([A-Za-z0-9+/=]+)',bootstrap)[1]
with zipfile.ZipFile(io.BytesIO(base64.b64decode(encoded))) as bundle:
    for relative in ['src/editorial_fv.py','src/relatorio_fv.py','src/refinamento_fv.py',
                     'config/distribuicao_editorial.json','docs/secoes_capitulo.json',
                     'scripts/gerar_tabulares_por_secao.py']:
        assert bundle.read(relative)==(ROOT/relative).read_bytes(),relative

class ReportPlacement(HTMLParser):
    def __init__(self):super().__init__();self.section=None;self.placements=[]
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='section':self.section=attrs['id'].replace('sec','').replace('_','.')
        if tag=='figure':self.placements.append((attrs['data-editorial-id'],self.section))
    def handle_endtag(self,tag):
        if tag=='section':self.section=None

# Run the 19 presentation cells against a real physical calculation in a disposable copy.
with tempfile.TemporaryDirectory(prefix='fv_editorial_') as temporary:
    root=Path(temporary)
    shutil.copytree(ROOT/'config',root/'config')
    shutil.copytree(ROOT/'src',root/'src')
    (root/'data').mkdir();(root/'data/raw').symlink_to(ROOT/'data/raw',target_is_directory=True)
    (root/'docs').mkdir();shutil.copy(ROOT/'docs/secoes_capitulo.json',root/'docs/secoes_capitulo.json')
    shutil.copytree(ROOT/'references',root/'references')
    with redirect_stdout(io.StringIO()):
        ctx=fv.complete_pipeline(root,make_plots=False,include_nasa=False)
        rf.analytics(ctx)
        displayed=[]
        def show(context,ids,theme):displayed.extend(ids)
        from types import SimpleNamespace
        env=dict(CTX=ctx,D=ctx['data'],A=ctx['model_a'],CFG=ctx['config'],pd=pd,fv=fv,
                 rf=SimpleNamespace(show=show),display=lambda *args:None,TEMA_VISUALIZACAO='escuro')
        for code in cells.values():exec(compile(code,'notebook subsection','exec'),env)
    assert Counter(displayed)==shown
    assert ctx['audit']['available_daylight_15m']==4401
    assert abs(ctx['metrics'].iloc[0].nRMSE_percent-14.991130565767405)<1e-8
    # A tiny fixture replaces only preview bytes; all scientific records stay real.
    (root/'preview.png').write_bytes(base64.b64decode('iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAwMCAO+j0XcAAAAASUVORK5CYII='))
    ctx['figures']=[]
    for item in inventory:
        record=dict(item,subsections=['1.1','4.5'],refs=item['refs'].split(', '),
                    files={t:{'preview':'preview.png'} for t in ['claro','escuro']})
        ctx['figures'].append(record)
    parser=ReportPlacement();parser.feed(rel.report(ctx).read_text())
    expected={(r['id'],r['owner_subsection']) for r in rules['figures']}
    assert len(parser.placements)==30 and set(parser.placements)==expected
    for section in rules['sections']:
        destination=root/section['directory']/word_files[section['section']-1].relative_to(ROOT/section['directory'])
        destination.parent.mkdir(parents=True,exist_ok=True);shutil.copy(word_files[section['section']-1],destination)
    archive=editorial.zip_results(ctx)
    with zipfile.ZipFile(archive) as bundle:
        assert all(str(p.relative_to(ROOT)) in bundle.namelist() for p in word_files)
        assert 'config/distribuicao_editorial.json' in bundle.namelist()

result=dict(status='passed',illustrations=30,final_graphic_files=120,
            illustrations_per_section=[sum(r['owner_subsection'][0]==str(i) for r in rules['figures']) for i in range(1,5)],
            CSV_files=24,logical_Word_tables=16,frames=6,section_Word_documents=4,
            duplicate_placements=0,subsections_checked=19,notebook_subsection_cells_executed=19,
            HTML_figure_placements=30,original_numerical_cells_preserved=True,
            original_data_and_physics_unchanged=True,embedded_support_matches_sources=True)
if '--write-report' in sys.argv:
    (ROOT/'docs/auditoria/Verificacao_Distribuicao_Editorial.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
