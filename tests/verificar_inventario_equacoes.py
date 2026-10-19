"""Check complete source coverage, native Word maths and exclusive section IDs."""
from pathlib import Path
from collections import Counter
import ast
import hashlib
import json
import re
import subprocess
import sys
import zipfile
from lxml import etree

ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'docs/equacoes/Inventario_Equacoes.json').read_text())
rows=data['equations'];ids=[r['id'] for r in rows]
assert len(rows)==len(set(ids))==61
assert Counter(r['origin'] for r in rows)=={'N':37,'C':24}
assert [sum(r['section']==s for r in rows) for s in range(1,5)]==[6,7,18,30]
source=json.loads(subprocess.check_output(['git','-C',str(ROOT),'show',data['source_commit']+':docs/secoes_capitulo.json'],text=True))
assert {r['subsection'] for r in rows}=={r['id'] for r in source}
assert len(source)==19
occurrences=[];parameters=[]
for section in source:
    fragments=re.split(r',\\(?:qquad|quad)\s*',section['equation'].strip('$').strip().rstrip('.'))
    for formula in fragments:
        if formula.startswith(r'\Delta t=') or formula.startswith(r'G_{\mathrm{ref}}='):
            parameters.append(formula);continue
        found=[r for r in rows if r['origin']=='N' and section['id'] in r['notebook_subsections']
               and (formula==r['notebook_fragment'] or section['id']=='2.1' and r['id']=='E3.03')]
        assert len(found)==1,(section['id'],formula)
        occurrences.append(found[0]['id'])
assert len(occurrences)==38 and len(parameters)==2
assert set(occurrences)=={r['id'] for r in rows if r['origin']=='N'}
assert [key for key,n in Counter(occurrences).items() if n>1]==['E3.03']
thermal=next(r for r in rows if r['id']=='E3.03')
assert thermal['subsection']=='3.2' and thermal['notebook_subsections']==['2.1','3.2']
# This revision annotates the delivered equations; it must not silently replace
# any formula, move an insertion ID or turn a scenario into the physical model.
previous=json.loads(subprocess.check_output(['git','-C',str(ROOT),'show',data['annotation_base_commit']+':docs/equacoes/Inventario_Equacoes.json'],text=True))
assert [(r['id'],r['subsection'],r['latex']) for r in rows]==[(r['id'],r['subsection'],r['latex']) for r in previous['equations']]

def normalized_math(value):
    value=re.sub(r'\\operatorname\{[^}]+\}', '', value)
    value=value.replace(r'\mathrm{abril}','')
    value=re.sub(r'\\(?:left|right|cos|sin|tan|max|min|sum|prod|exp|frac|sqrt|in)(?![A-Za-z])', '', value)
    value=value.replace(r'\,','').replace(r'\{','').replace(r'\}','')
    return re.sub(r'[{}\s]','',value)

for row in rows:
    assert row['application_class'] and row['application'] and row['code_correspondence']
    details=row['symbol_details']
    assert details and len({s['latex'] for s in details})==len(details),row['id']
    formula=normalized_math(row['latex'])
    for s in sorted(details,key=lambda s:len(normalized_math(s['latex'])),reverse=True):
        assert all(s[key].strip() for key in ['symbol','latex','description','unit'])
        formula=formula.replace(normalized_math(s['latex']),'')
    # A forgotten variable (including a dependent variable or index) remains
    # alphabetic/LaTeX after removing operators, constants and declared symbols.
    assert not re.search(r'[A-Za-zÀ-ÿ\\]',formula),(row['id'],formula)

by_id={r['id']:r for r in rows}
cfg=json.loads((ROOT/'config/projeto.json').read_text())
assert data['parameters']['eta_ref_inverter']==cfg['assumptions']['inverter_eta_ref']
assert data['parameters']['eta_ref_bipv']==cfg['bipv']['reference_efficiency']
assert data['parameters']['bipv_gamma_per_C']==cfg['bipv']['gamma_pdc_per_C']
assert by_id['E3.06']['application_class']=='comparacao'
assert by_id['E2.07']['application_class']=='fundamento'
assert by_id['E3.03']['application_class']==by_id['E3.04']['application_class']=='principal'
assert all(by_id[f'E4.{n:02d}']['application_class']=='bipv' for n in range(20,31))
assert {s['key']:s['unit'] for s in by_id['E3.03']['symbol_details']}['u0']=='W/(m²·K)'
assert {s['key']:s['unit'] for s in by_id['E3.03']['symbol_details']}['u1']=='W·s/(m³·K)'
assert all(s['unit']=='W' for n in range(26,31) for s in by_id[f'E4.{n:02d}']['symbol_details'] if s['key'].startswith('heat_'))

references={r['id'] for r in json.loads((ROOT/'references/referencias_projeto.json').read_text())}
for row in rows:
    assert row['function'] and row['symbols'] and row['latex']
    assert str(row['section'])==row['subsection'][0]
    assert set(row['refs']) <= references
    path,locator=row['source_locator'].split('::');file=ROOT/path
    assert file.is_file()
    if file.suffix=='.py':
        functions={n.name for n in ast.walk(ast.parse(file.read_text())) if isinstance(n,ast.FunctionDef)}
        assert locator in functions,row['id']

ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main',
    'm':'http://schemas.openxmlformats.org/officeDocument/2006/math'}
def word_records(path):
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None
        assert not [n for n in archive.namelist() if n.startswith('word/media/')],path
        xml=etree.fromstring(archive.read('word/document.xml'))
        assert not xml.xpath('//w:pBdr',namespaces=ns)
    result={}
    for row in xml.xpath('//w:tbl/w:tr',namespaces=ns):
        cells=row.findall('w:tc',ns)
        label=''.join(cells[0].xpath('.//w:t/text()',namespaces=ns))
        match=re.match(r'(E[1-4]\.\d{2})([1-4]\.\d+)$',label)
        if not match:continue
        ident,sub=match.groups();assert ident not in result
        equations=cells[1].xpath('.//m:oMath',namespaces=ns)
        assert len(equations)==1,(path,ident)
        tokens=''.join(equations[0].xpath('.//m:t/text()',namespaces=ns))
        if ident=='E4.12':assert tokens.count('|')==2,(path,ident,tokens)
        if ident=='E3.04':assert '[' in tokens and ']' in tokens,(path,ident,tokens)
        symbols=''.join(cells[2].xpath('.//w:t/text()',namespaces=ns))
        application=''.join(cells[3].xpath('.//w:t/text()',namespaces=ns))
        for s in by_id[ident]['symbol_details']:
            assert f'{s["symbol"]}: {s["description"]} [{s["unit"]}]' in symbols,(path,ident,s)
        assert by_id[ident]['application'] in application,(path,ident)
        result[ident]=(sub,tokens,symbols,application)
    assert len(xml.xpath('//m:oMath',namespaces=ns))==len(result)
    return result

general=ROOT/'docs/equacoes/Inventario_Geral_Equacoes_SPGER0046.docx'
all_records=word_records(general)
assert set(all_records)==set(ids)
seen=Counter();files=[general]
for number,folder in enumerate(sorted((ROOT/'secoes').iterdir()),1):
    if not folder.is_dir():continue
    path=folder/f'equacoes/Quadro_Equacoes_Secao_{number:02d}.docx'
    files.append(path);records=word_records(path)
    expected={r['id'] for r in rows if r['section']==number}
    assert set(records)==expected
    for ident,value in records.items():assert value==all_records[ident],ident
    seen.update(records.keys())
assert set(seen)==set(ids) and set(seen.values())=={1}
protected=['src/projeto_fv.py','src/refinamento_fv.py','config','data',
           'outputs/tabelas/csv','outputs/series','outputs/avaliacao',
           'notebooks/originais_executados','bibliografia/outputs']
changes=subprocess.check_output(['git','-C',str(ROOT),'diff',data['source_commit'],'--name-only','--',*protected],text=True).splitlines()
assert not changes,changes
result=dict(status='passed',subsections=19,notebook_relation_occurrences=38,
            unique_notebook_relations=37,code_support_relations=24,total_relations=61,
            parameter_definitions_excluded=2,relations_per_section=[6,7,18,30],
            duplicate_insertion_IDs=0,native_editable_Word_math=True,
            original_inventory_formulas_and_locations_preserved=True,
            equations_with_complete_symbol_descriptions_and_units=len(rows),
            symbol_definitions_across_equations=sum(len(r['symbol_details']) for r in rows),
            application_counts=dict(Counter(r['application'] for r in rows)),
            Word_documents=5,source_commit=data['source_commit'],
            physical_sources_data_and_results_unchanged=True,
            files=[dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,
                        sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
                        md5=hashlib.md5(p.read_bytes()).hexdigest()) for p in files])
if '--write-report' in sys.argv:
    (ROOT/'docs/auditoria/Verificacao_Inventario_Equacoes.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
