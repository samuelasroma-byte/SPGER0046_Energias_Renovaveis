"""Package only a fully executed and checked delivery; keep original inputs intact."""
from pathlib import Path
import json,hashlib,zipfile,shutil
import nbformat
ROOT=Path(__file__).resolve().parents[1]
DELIVERY=ROOT.parent/'entrega_projeto_fv/v1_2_2'
DELIVERY.mkdir(parents=True,exist_ok=True)
nb=nbformat.read(ROOT/'notebooks/01_Projeto_FV_Quatro_Secoes.ipynb',as_version=4)
assert nb.metadata.project_version=='1.2.2'
assert all(c.execution_count is not None for c in nb.cells if c.cell_type=='code')
check=json.loads((ROOT/'outputs/relatorios/verificacao_refinamento.json').read_text())
assert check['status']=='passed' and check['DOCX']==6
abnt=json.loads((ROOT/'outputs/relatorios/Verificacao_Documentos_ABNT.json').read_text())
assert abnt['status']=='passed' and len(abnt['documents'])==7
visual=json.loads((ROOT/'outputs/relatorios/Conferencia_Visual.json').read_text())
assert visual['project_version']=='1.2.2' and visual['documents']==7 and visual['status']=='passed'
bib_nb=nbformat.read(ROOT/'bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb',as_version=4)
assert all(c.execution_count is not None for c in bib_nb.cells if c.cell_type=='code')
assert not any(o.output_type=='error' for c in bib_nb.cells if c.cell_type=='code' for o in c.outputs)

def include(path):
    relative=path.relative_to(ROOT)
    return (path.is_file() and '__pycache__' not in path.parts
        and '.git' not in path.parts and not path.name.endswith(('.pyc','.tmp'))
        and not (path.name.startswith('.') and path.name not in ['.gitignore','.gitattributes','.env.example'])
        and path.name!='checksums_sha256.json'
        and path.name!='Resultados_Execucao_Projeto_FV.zip')
paths=sorted(p for p in ROOT.rglob('*') if include(p))
hashes={p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
(ROOT/'checksums_sha256.json').write_text(json.dumps(hashes,indent=2,ensure_ascii=False))
paths.append(ROOT/'checksums_sha256.json')
full=DELIVERY/'Projeto_FV_PVDAQ_2107_2024_Completo.zip'
with zipfile.ZipFile(full,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in paths:z.write(p,(Path(ROOT.name)/p.relative_to(ROOT)).as_posix())
with zipfile.ZipFile(full) as z:assert z.testzip() is None
results=DELIVERY/'Resultados_Projeto_FV_2024.zip'
with zipfile.ZipFile(results,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in paths:
        if p.is_relative_to(ROOT/'outputs'):z.write(p,p.relative_to(ROOT/'outputs').as_posix())
with zipfile.ZipFile(results) as z:assert z.testzip() is None
github=DELIVERY/'SPGER0046_Projeto_Pronto_para_GitHub.zip'
with zipfile.ZipFile(github,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in paths:
        r=p.relative_to(ROOT).as_posix()
        if r.startswith(('outputs/','historico/','bibliografia/raw/')) or p.suffix.lower() in ['.pdf','.zip','.ipynb']:continue
        if r in ['bibliografia/outputs/registros_normalizados.json','bibliografia/outputs/catalogo_completo.json','bibliografia/outputs/leituras_prioritarias.json']:continue
        if r in ['docs/Plano_do_Capitulo_Fonte_Drive_20261016.txt','config/destinos_drive.json']:continue
        z.write(p,r)
    for path,executed in [('notebooks/01_Projeto_FV_Quatro_Secoes.ipynb',nb),('bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb',bib_nb)]:
        small=nbformat.from_dict(json.loads(nbformat.writes(executed)))
        for cell in small.cells:
            if cell.cell_type=='code':cell.outputs=[];cell.execution_count=None
        small.metadata.pop('execution',None)
        z.writestr(path,nbformat.writes(small))
bibliography=DELIVERY/'Fundamentacao_Teorica_Projeto_FV.zip'
with zipfile.ZipFile(bibliography,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in paths:
        if p.is_relative_to(ROOT/'bibliografia'):
            z.write(p,p.relative_to(ROOT).as_posix())
with zipfile.ZipFile(bibliography) as z:assert z.testzip() is None
manifest=[]
for p in [full,results,github,bibliography]:
    manifest.append({'file':str(p),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(DELIVERY/'pacotes_e_hashes.json').write_text(json.dumps(manifest,indent=2))
print(json.dumps(manifest,indent=2))
