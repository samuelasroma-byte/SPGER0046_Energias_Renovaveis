"""Exporta Word e PDF localmente; não grava a apresentação coletiva remota."""
from pathlib import Path
import json,subprocess,shutil,concurrent.futures
ROOT=Path(__file__).resolve().parents[1]

def exportar(root=ROOT,gerar_pdf=True,gerar_beamer=True):
    root=Path(root)
    required=['pandoc','xelatex','pdftocairo']+(['soffice'] if gerar_pdf else [])
    missing=[p for p in required if not shutil.which(p)]
    if missing:raise RuntimeError('Instale os executáveis: '+', '.join(missing)+'. Em Debian/Colab: apt-get install pandoc libreoffice-writer texlive-xetex texlive-latex-extra fonts-urw-base35 poppler-utils')
    from editar_manuscritos import run as manuscritos
    from preparar_slides import assets,manifest,beamer
    if gerar_beamer:assets();beamer(manifest())
    items=manuscritos()+[root/'documentacao/Conferencia_Cientifica_39_Evidencias.docx']
    pdfs=[]
    if gerar_pdf:
        def convert(p):
            profile=root/'_trabalho_editorial'/('lo_'+p.stem)
            r=subprocess.run(['soffice','-env:UserInstallation='+profile.resolve().as_uri(),'--headless','--convert-to','pdf','--outdir',str(p.parent),str(p)],capture_output=True,text=True,timeout=180)
            out=p.with_suffix('.pdf');assert r.returncode==0 and out.is_file() and out.stat().st_size>5000,(p,r.stdout,r.stderr)
            return out
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:pdfs=list(pool.map(convert,items))
    result={'docx':[str(p.relative_to(root)) for p in items],'pdf':[str(p.relative_to(root)) for p in pdfs],
      'slides_pdf':'apresentacao/Subsecao_1_1_Beamer.pdf' if gerar_beamer else None,
      'cadeia':{'1.1_DOCX':'python-docx sobre manuscrito existente; equações OMML e novas equações via Pandoc',
        '1.2_a_1.4_DOCX':'Markdown e LaTeX → Pandoc → Word com equações nativas',
        'PDF_manuscritos':'LibreOffice a partir dos DOCX','PDF_slides':'Beamer → XeLaTeX'},
      'publicacao_remota_executada':False,'necessita_conferencia_visual_apos_edicao':True}
    (root/'resultados/Exportacao_Editorial.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    return result
if __name__=='__main__':print(json.dumps(exportar(),ensure_ascii=False,indent=2))
