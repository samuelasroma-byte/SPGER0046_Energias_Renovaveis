"""Check real files, relative navigation, binary integrity and chapter contracts."""
from pathlib import Path
import csv, hashlib, json, re, subprocess
from urllib.parse import unquote, urlsplit

ROOT=Path(__file__).resolve().parents[1]
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def files():
    return [ROOT/p for p in subprocess.check_output(['git','-C',str(ROOT),'ls-files'],text=True).splitlines()]
def check():
    tracked=files();broken=[];links=0
    for p in tracked:
        if p.suffix!='.md':continue
        for target in re.findall(r'\]\(([^\n]*?)\)',p.read_text()):
            target=target.strip().split(' "',1)[0].strip('<>')
            if not target or target.startswith('#') or urlsplit(target).scheme:continue
            name=unquote(target.split('#',1)[0].split('?',1)[0]);links+=1
            dest=(p.parent/name).resolve()
            if not dest.exists():broken.append({'source':str(p.relative_to(ROOT)),'target':target})
    source=list(csv.DictReader((ROOT/'docs/auditoria/Proveniencia_Arquivos_Integrados.csv').open(encoding='utf-8-sig')))
    mismatches=[]
    for r in source:
        p=ROOT/r['caminho_github']
        if not p.is_file() or p.stat().st_size!=int(r['bytes']) or digest(p)!=r['sha256']:mismatches.append(r['caminho_github'])
    structural=json.loads((ROOT/'docs/estrutura_oficial_19_subsecoes.json').read_text())
    assert len(structural['subsecoes'])==19
    assert len(list(ROOT.glob('secoes/*/subsecoes/*/README.md')))==19
    refs=json.loads((ROOT/'bibliografia/principal/Referencias_B01_B39.json').read_text())
    assert {r['code'] for r in refs}=={f'B{x:02d}' for x in range(1,40)}
    a=list(csv.DictReader((ROOT/'references/acervo_disponivel.csv').open(encoding='utf-8-sig')))
    assert len(a)==len({r['id'] for r in a})==91
    figs=json.loads((ROOT/'docs/auditoria/Inventario_Figuras.json').read_text())
    assert len(figs)==30 and sum(len(f['files']) for f in figs)==120
    for f in figs:
        assert set(f['files'])=={'claro_png','escuro_png','claro_pdf','escuro_pdf'}
        assert all((ROOT/p).is_file() for p in f['files'].values())
        assert all(all(abs(d-600)<.1 for d in v['dpi']) for v in f['resolution'].values())
    assert len([p for p in tracked if p.suffix=='.docx'])==10
    scientific_dirs=['src/','config/','data/processed/','bibliografia/outputs/']
    changed=subprocess.check_output(['git','-C',str(ROOT),'diff','--cached','--name-only','--diff-filter=M'],text=True).splitlines()
    scientific_modified=[p for p in changed if any(p.startswith(d) for d in scientific_dirs)]
    # Newly added DOCX and indices are allowed; existing scientific files must match the original base.
    assert not scientific_modified,scientific_modified
    result={'tracked_files':len(tracked),'relative_links_checked':links,'broken_relative_links':broken,'source_copies_checked':len(source),'sha256_mismatches':mismatches,'subsections':19,'B_references':39,'A_documents':91,'illustrations':30,'graphic_files':120,'DOCX':10,'scientific_files_modified':scientific_modified}
    print(json.dumps(result,ensure_ascii=False,indent=2))
    assert not broken and not mismatches,'Invalid links or changed original bytes.'
    return result
if __name__=='__main__':check()
