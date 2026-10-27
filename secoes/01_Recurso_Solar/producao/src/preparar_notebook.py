"""Consolida o notebook existente após auditoria; não repete a bibliometria."""
from pathlib import Path
import json,hashlib,re,io,contextlib,traceback,os
ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent

def md(s):return {'cell_type':'markdown','id':hashlib.sha256(s.encode()).hexdigest()[:10],'metadata':{},'source':s.splitlines(True)}
def code(s):return {'cell_type':'code','id':hashlib.sha256(s.encode()).hexdigest()[:10],'metadata':{},'source':s.splitlines(True),'execution_count':None,'outputs':[]}
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

def build():
    source=json.loads((WORK/'fontes/nb0.ipynb').read_text())
    audit=[]
    for name in ['nb0','nb2']:
        p=WORK/'fontes'/(name+'.ipynb');nb=json.loads(p.read_text());cells=nb['cells']
        audit.append({'arquivo':name,'sha256':sha(p),'celulas':len(cells),'celulas_codigo':sum(c['cell_type']=='code' for c in cells),
          'codigo_com_execucao_registrada':sum(c['cell_type']=='code' and c.get('execution_count') is not None for c in cells),
          'erros_registrados':sum(o.get('output_type')=='error' for c in cells for o in c.get('outputs',[])),
          'limites':'O notebook 00 continha extração repetida, geração de estruturas e teste de sete slides; a extensão V2 não estava executada.' if name=='nb0' else 'Fundamentação coletiva anterior; não foi alterada nem reexecutada nesta continuidade.'})
    (ROOT/'documentacao/Auditoria_Notebooks_Entrada.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2))
    dependencies=['src/solar_secao01.py','src/curadoria_secao01.py','config/projeto.json','dados/poa_15min.csv',
      'bibliografia/Manifesto_Corpus_Secao_01.json','bibliografia/Protocolo_Analise_Sistemica.json',
      'bibliografia/Inventario_Fontes_Conferidas.json','bibliografia/Matriz_Evidencias.json',
      'bibliografia/Selecao_Critica.json','bibliografia/Status_Revisao.json','bibliografia/Protocolo_Bibliometrico_Herdado.json',
      'bibliografia/Obras_Prioritarias_Herdadas.csv',
      'src/confrontar_evidencias.py','src/finalizar_confronto.py','src/verificar_relacoes_fisicas.py','src/exportar_editorial.py',
      'src/editar_manuscritos.py','src/preparar_slides.py','bibliografia/Confronto_Cientifico_39_Evidencias.json',
      'bibliografia/Referencias_Verificadas.md','insumos/Base_Manuscrito_1_1.docx','apresentacao/Conteudo_6_Slides.json',
      'documentacao/Conferencia_Cientifica_39_Evidencias.md',
      'manuscritos/1_2_Grandezas_Radiometricas.md','manuscritos/1_3_Modulacao_Atmosferica.md','manuscritos/1_4_Medicao_e_Estimativa.md']
    hashes={p:sha(ROOT/p) for p in dependencies}
    c=[]
    c.append(md('# SPGER0046 — REVISÃO CIENTÍFICA ACESSÍVEL DA SEÇÃO 1\n\n**Samuel Constantino Teixeira — 1.1 a 1.4.** Continuidade do notebook v2 de 26/10/2026, consolidada em 27/10/2026. Reaproveita o portfólio, as sete lentes, a recuperação de passagens e a rastreabilidade. A bibliometria anterior não é repetida.\n\nAbra este arquivo dentro do pacote da Seção 1. Fora do pacote, a primeira célula recupera somente os arquivos públicos indispensáveis do repositório e confere seus hashes. PDFs de terceiros permanecem no acervo privado. As evidências já conferidas não são reclassificadas como nova leitura por uma reexecução.'))
    bootstrap='''from pathlib import Path
import sys, json, hashlib, urllib.request, importlib.util, subprocess

ROOTS = [Path.cwd(), Path.cwd().parent, Path.cwd()/"SPGER0046_Secao_01"]
BASE = next((p for p in ROOTS if (p/"src/solar_secao01.py").is_file()), Path.cwd()/"SPGER0046_Secao_01")
BASE.mkdir(parents=True, exist_ok=True)
for folder in ["manuscritos","figuras","apresentacao","documentacao","resultados"]:
    (BASE/folder).mkdir(exist_ok=True)
URL = "https://raw.githubusercontent.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis/main/secoes/01_Recurso_Solar/producao/"
HASHES = '''+repr(hashes)+'''
for rel, expected in HASHES.items():
    p = BASE/rel
    if not p.exists():
        p.parent.mkdir(parents=True, exist_ok=True)
        with urllib.request.urlopen(URL+rel) as response: data=response.read()
        assert hashlib.sha256(data).hexdigest()==expected, "Conteúdo remoto mudou: "+rel
        p.write_bytes(data)
    assert hashlib.sha256(p.read_bytes()).hexdigest()==expected, "Arquivo diferente do insumo conferido: "+rel
for mod, package in [("numpy","numpy>=2,<3"),("pandas","pandas>=2.2,<3"),("matplotlib","matplotlib>=3.9,<4"),("pvlib","pvlib==0.16.1"),("fitz","PyMuPDF>=1.24,<2"),("docx","python-docx>=1.1,<2")]:
    if importlib.util.find_spec(mod) is None:
        subprocess.run([sys.executable,"-m","pip","install","--quiet",package],check=True)
import pvlib
assert pvlib.__version__=="0.16.1", "Instale pvlib==0.16.1 e reinicie o kernel."
sys.path.insert(0,str(BASE/"src"))
print("Insumos e versão conferidos. Raiz:", BASE)
'''
    c+=[md('## 1 — AMBIENTE E ENTRADAS\n\nA verificação SHA-256 evita substituir silenciosamente a configuração ou os dados por outra versão. A rotina trabalha com a POA preparada do estudo, sem executar novamente a cadeia térmica ou elétrica.'),code(bootstrap)]
    c+=[md('## 2 — PORTFÓLIO E PROTOCOLO HERDADOS\n\nOs códigos B e as 23 associações são os registros anteriores da Seção 1. A quarta edição do handbook é registrada como A045 e não como leitura presumida de B36/2021.'),code('''corpus=json.loads((BASE/"bibliografia/Manifesto_Corpus_Secao_01.json").read_text())
protocolo=json.loads((BASE/"bibliografia/Protocolo_Analise_Sistemica.json").read_text())
anterior=json.loads((BASE/"bibliografia/Protocolo_Bibliometrico_Herdado.json").read_text())
assert len(corpus["refs"])==12
assert sum(len(s["B_codes"]) for s in corpus["subsections"])==23
assert len(protocolo["lentes"])==7
import pandas as pd
prioritarias=pd.read_csv(BASE/"bibliografia/Obras_Prioritarias_Herdadas.csv")
print("Recorte B:",len(corpus["refs"]),"obras; 23 associações; sete lentes.")
print("Portfólio coletivo herdado:",len(prioritarias),"associações;",prioritarias["id"].nunique(),"obras distintas.")
print("Escopo do protocolo anterior:",anterior["scope"])
print("As contagens descrevem arquivos recuperados; não constituem uma nova busca ou leitura integral.")
''')]
    c+=[md('## 3 — FONTES E ESTADOS DE LEITURA\n\nDisponibilidade, extração e leitura são estados diferentes. A lista registra arquivos e páginas conferidas. A reexecução valida a presença da matriz, mas não simula uma nova conferência intelectual.'),code('''inventario=json.loads((BASE/"bibliografia/Inventario_Fontes_Conferidas.json").read_text())
for f in inventario:
    print(f["codigo"],"|",f["status_leitura"],"| páginas PDF:",f["paginas_verificadas"])
assert sum(bool(f["paginas_verificadas"]) for f in inventario)==7
assert next(f for f in inventario if f["codigo"]=="B23")["leitura_integral"] is True
''')]
    c+=[md('## 4 — MATRIZ E SELEÇÃO CRÍTICA\n\nA rotina preserva 39 evidências bibliográficas localizadas, suas páginas e hashes. O campo “CONFERIDA_LOCALIZADA” não significa leitura integral de toda a obra. As decisões mantêm explícitas as edições ausentes e as fontes ainda não lidas.'),code('''from finalizar_confronto import run as revisar_portfolio
evidencias,selecao,status,resumo_confronto=revisar_portfolio(root=BASE)
from confrontar_evidencias import validar_registros
print(validar_registros(root=BASE))
print("Confronto registrado:",resumo_confronto["por_classificacao"])
from verificar_relacoes_fisicas import run as verificar_fisica
relacoes=verificar_fisica(root=BASE)
assert relacoes["falhas"]==0
print("Relações físicas verificadas:",relacoes["total"])
assert len(evidencias)==39 and len(selecao)==14
assert all(e["arquivo_sha256"] and e["pagina_texto_sha256"] and e["pagina_pdf"] for e in evidencias)
print("Evidências por subseção:",dict(pd.Series([e["subsecao"] for e in evidencias]).value_counts().sort_index()))
print("Método:",status["metodo"])
print("Revisão sistemática integral concluída:",status["revisao_sistematica_integral_concluida"])
''')]
    c+=[md('## 5 — GEOMETRIA SOLAR E IRRADIÂNCIA EXTRATERRESTRE\n\nA POA é observacional. SPA calcula ângulos e Spencer calcula irradiância extraterrestre. O caso permanece em America/Los_Angeles, com cálculo no meio de cada intervalo de 15 minutos. Os testes incluem o exemplo publicado do SPA, sem validar o sensor por essa comparação.'),code('''from solar_secao01 import run as calcular_geometria
dia,conferencia=calcular_geometria(root=BASE)
print("PVDAQ 2107 — 17/05/2024:",len(dia),"intervalos;")
print("POA não ausente:",conferencia["POA_observed_nonmissing_day"],"; intervalos com três amostras:",conferencia["POA_intervals_with_three_samples_day"])
print("SPA de referência: zenital aparente =",round(conferencia["reference_SPA_apparent_zenith_deg"],6),"°; azimute =",round(conferencia["reference_SPA_azimuth_deg"],6),"°")
print("Verificações:",", ".join(conferencia["checks_passed"]))
''')]
    c+=[md('## 6 — FIGURA G01 E LIMITES OBSERVACIONAIS\n\nO gráfico conserva lacunas e mostra 05h–21h no horário local, enquanto o CSV mantém o dia completo. A curva não demonstra céu claro nem isola efeitos de aerossóis ou nuvens. GHI/DNI/DHI locais independentes não estão presentes nessa seleção.'),code('''try:
    from IPython.display import display, Image, HTML
    display(Image(filename=str(BASE/"figuras/G01_recurso_geometria_escuro.png"),width=1050))
except ImportError:
    print("Visualização interativa indisponível neste executor; PNG/PDF foram exportados.")
print("Figura vetorial:",BASE/"figuras/G01_recurso_geometria_escuro.pdf")
print("Dados:",BASE/"resultados/G01_dados_verificados.csv")
''')]
    c+=[md('## 7 — RECUPERAÇÃO DE PASSAGENS CANDIDATAS\n\nA função abaixo reaproveita a busca local por descritores e a ideia de recuperação do notebook anterior. Ela é opcional, consulta somente PDFs autorizados e retorna candidatos com página e hash. Não realiza buscas bibliométricas externas, não aprova evidências e não reextrai arquivos quando existe cache. Consultas bilíngues reduzem o desencontro entre PDFs em inglês e perguntas em português.'),code('''import re, fitz
CONSULTAS={
 "1.1":"solar geometry zenith azimuth extraterrestrial Spencer geometria zenital",
 "1.2":"irradiance irradiation GHI DNI DHI POA radiometric irradiação",
 "1.3":"cloud aerosol precipitable water variability nuvens aerossóis",
 "1.4":"pyranometer pyrheliometer satellite reanalysis uncertainty medição incerteza"}
def candidatas_locais(pasta,subsecao,limite=8):
    pasta=Path(pasta); cache=BASE/"resultados/cache_privado";cache.mkdir(parents=True,exist_ok=True)
    tokens=set(CONSULTAS[subsecao].lower().split());result=[];vistos=set()
    for pdf in sorted(pasta.glob("*.pdf")):
        digest=hashlib.sha256(pdf.read_bytes()).hexdigest()
        if digest in vistos:continue
        vistos.add(digest);saved=cache/(digest+".json")
        if saved.exists():pages=json.loads(saved.read_text())
        else:
            with fitz.open(pdf) as d:pages=[p.get_text() for p in d]
            saved.write_text(json.dumps(pages,ensure_ascii=False))
        for n,text in enumerate(pages,1):
            score=sum(text.lower().count(t) for t in tokens)
            if score:result.append({"arquivo":pdf.name,"sha256":digest,"pagina_pdf":n,"pontuacao_lexical":score,"status":"CANDIDATA_NAO_CONFERIDA"})
    return sorted(result,key=lambda x:x["pontuacao_lexical"],reverse=True)[:limite]
print("Recuperação opcional definida; nenhuma nova busca ou extração foi acionada.")
''')]
    c+=[md('## 8 — PAINEL ACESSÍVEL DE ESTUDO\n\nTexto grande, fundo escuro e navegação por subseção. O painel usa as evidências já conferidas; é uma forma de leitura da matriz e não uma etapa adicional de aprovação.'),code('''import html
parts=["<!doctype html><html lang='pt-BR'><meta charset='utf-8'><title>Seção 1 — estudo</title><style>body{background:#000000;color:#ffffff;font:26px 'Times New Roman',serif;max-width:1050px;margin:35px auto;padding:20px;line-height:1.5}h1,h2,a{color:#ffd45c}article{margin-bottom:35px}:focus{outline:4px solid #ffd45c}</style><h1>SEÇÃO 1 — EVIDÊNCIAS PARA ESTUDO</h1>"]
parts.append("<nav>"+" · ".join("<a href='#s"+s+"'>"+s+"</a>" for s in ["1.1","1.2","1.3","1.4"])+"</nav>")
for sec in ["1.1","1.2","1.3","1.4"]:
    parts.append("<h2 id='s"+sec+"'>SUBSEÇÃO "+sec+"</h2>")
    for e in [x for x in evidencias if x["subsecao"]==sec]:
        parts.append("<article><p>"+html.escape(e["afirmacao_parafraseada"])+"</p><p><b>"+e["fonte"]+" — "+html.escape(e["pagina_impressa"])+"; PDF "+str(e["pagina_pdf"])+".</b> "+html.escape(e["limites"])+"</p></article>")
parts.append("</html>")
painel=BASE/"resultados/Painel_Estudo_Acessivel.html";painel.write_text("\\n".join(parts))
print("Painel acessível:",painel)
''')]
    c+=[md('## 9 — CONFERÊNCIA E CONTINUIDADE\n\nA escrita das quatro subseções e os seis slides foram preparados e conferidos separadamente. Esta execução reproduz cálculos, figura e matrizes, sem sobrescrever a apresentação coletiva ou simular publicação. O Beamer pode ser recompilado com XeLaTeX pelos fontes incluídos; PDF e PPTX não possuem sincronização bidirecional.'),code('''assert conferencia["pvlib"]=="0.16.1"
assert (BASE/"resultados/Conferencia_Calculos.json").is_file()
assert (BASE/"bibliografia/Matriz_Evidencias.csv").is_file()
assert painel.is_file()
final={"execucao":"concluída","evidencias_localizadas":len(evidencias),"busca_bibliometrica_reexecutada":False,"revisao_integral_ProKnowC":False,"figura":"G01","quadros_da_11":6}
(BASE/"resultados/Conferencia_Notebook.json").write_text(json.dumps(final,ensure_ascii=False,indent=2))
print(json.dumps(final,ensure_ascii=False,indent=2))
''')]
    c.insert(-2,md('## 9 — MANUSCRITOS EDITÁVEIS E PDF\n\nEsta célula gera os Word da 1.1 a 1.4, o integrado e o roteiro. A 1.1 preserva o manuscrito anterior. Pandoc produz equações nativas; LibreOffice exporta os PDFs de texto. Beamer/XeLaTeX compila os slides. Instale Pandoc, LibreOffice, XeLaTeX, Poppler e fontes URW antes de executar. Em Debian/Colab: `apt-get install pandoc libreoffice-writer texlive-xetex texlive-latex-extra fonts-urw-base35 poppler-utils`. A execução local não publica no Drive nem substitui o PPTX coletivo.'))
    c.insert(-2,code('''from exportar_editorial import exportar
editorial=exportar(root=BASE,gerar_pdf=True,gerar_beamer=True)
for arquivo in editorial["docx"]:
    assert (BASE/arquivo).is_file()
    print("Word editável:",arquivo)
print("Cadeia de exportação:",editorial["cadeia"])
'''))
    c[-2]=md('## 10 — CONFERÊNCIA DA EXECUÇÃO\n\nEsta execução reproduz cálculos, registros do confronto, figuras, Word e PDF. Reexecutar não constitui nova leitura intelectual nem aprovação científica. Após qualquer edição, confira visualmente os arquivos. PDF e PPTX não possuem sincronização bidirecional.')
    final_source=''.join(c[-1]['source']).replace('"evidencias_localizadas":len(evidencias)', '"evidencias_confrontadas_registradas":len(evidencias),"verificacoes_fisicas":relacoes["total"],"DOCX_exportados":len(editorial["docx"]),"PDF_texto_exportados":len(editorial["pdf"])')
    c[-1]=code(final_source)
    # As funções atuais substituem os geradores de esqueleto e a dupla extração; o histórico fica no Drive.
    source['cells']=c;source['metadata']['secao01_continuidade']={'data':'2026-10-27','origem_sha256':sha(WORK/'fontes/nb0.ipynb'),'preserva_portfolio':True,'slides_11':6,'bibliometria_reexecutada':False}
    source['metadata']['kernelspec']={'display_name':'Python 3','language':'python','name':'python3'}
    out=ROOT/'notebooks/00_Revisao_Cientifica_Acessivel_4_Subsecoes_v2_20261026.ipynb'
    out.write_text(json.dumps(source,ensure_ascii=False,indent=1))
    return out

def execute(p):
    import nbformat
    from IPython.core.interactiveshell import InteractiveShell
    from IPython.utils.capture import capture_output
    nb=nbformat.read(p,as_version=4)
    shell=InteractiveShell.instance();current=Path.cwd();os.chdir(ROOT);count=0
    try:
        for cell in nb.cells:
            if cell.cell_type!='code':continue
            count+=1;cell.execution_count=count
            with capture_output() as captured:result=shell.run_cell(cell.source,store_history=True)
            cell.outputs=[]
            if captured.stdout:cell.outputs.append(nbformat.v4.new_output('stream',name='stdout',text=captured.stdout))
            if captured.stderr:cell.outputs.append(nbformat.v4.new_output('stream',name='stderr',text=captured.stderr))
            for output in captured.outputs:cell.outputs.append(nbformat.v4.new_output('display_data',data=output.data,metadata=output.metadata))
            error=result.error_before_exec or result.error_in_exec
            if error:
                cell.outputs.append(nbformat.v4.new_output('error',ename=type(error).__name__,evalue=str(error),traceback=[]));raise error
        nb.metadata['secao01_continuidade']['executor']='IPython em processo local; mesmas células e saídas registradas; kernel externo indisponível neste ambiente'
    finally:os.chdir(current);nbformat.write(nb,p)
    nbformat.validate(nb)
    cells=[c for c in nb.cells if c.cell_type=='code'];errors=[o for c in cells for o in c.outputs if o.output_type=='error']
    assert all(c.execution_count is not None for c in cells) and not errors
    print(json.dumps({'executor':'IPython local, sem sockets','celulas_codigo_executadas':len(cells),'erros':len(errors),'notebook':str(p)},ensure_ascii=False))
if __name__=='__main__':execute(build())
