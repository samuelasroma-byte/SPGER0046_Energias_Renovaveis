"""Standalone notebook with the WCNPS credential names and chapter-specific outputs."""
from pathlib import Path
import base64,hashlib,io,json,zipfile
import nbformat as nbf

ROOT=Path(__file__).resolve().parents[1]
BIB=ROOT/'bibliografia'
buffer=io.BytesIO()
with zipfile.ZipFile(buffer,'w',zipfile.ZIP_DEFLATED) as z:
    for name in ['bibliografia_fv.py','formatacao_abnt.py','word_referencias_abnt.py','temas.json','sementes.json','protocolo.json']:
        z.writestr(name,(BIB/name).read_bytes())
bundle=buffer.getvalue();cells=[]
def md(source):cells.append(nbf.v4.new_markdown_cell(source))
def code(source):cells.append(nbf.v4.new_code_cell(source))
def description(source):md('<details>\n<summary>Descrição e método</summary>\n\n'+source+'\n\n</details>')
md('# Fundamentação teórica do capítulo fotovoltaico')
description('SPGER0046 UFPB. Levantamento de livros, artigos, relatórios e fontes de método para as quatro seções e 19 subseções. '
 'Adaptação do notebook multibase WCNPS da pasta Artigo/Bibliometria. Esta versão não busca lacuna científica nem produz uma revisão sistemática automática. '
 'As saídas identificam DOI, autoria, ano, periódico ou editora, acesso, tópico e citações separadas por base e data. '
 'Livros e artigos não são classificados como se tivessem cobertura bibliométrica idêntica.')
md('## 0 Preparação e local de trabalho')
description('O código pode executar em Jupyter ou Colab. Credenciais são lidas de variáveis de ambiente ou dos mesmos Secrets usados no WCNPS: '
 'OPENALEX_API_KEY, SCOPUS_API_KEY, WOS_API_KEY e IEEE_API_KEY. Nenhuma chave é exibida ou gravada. '
 'Sem as chaves institucionais, o levantamento continua com Crossref e OpenAlex e registra as bases não executadas. '
 'O notebook executado já permite consultar os resultados. NOVA_COLETA=False reutiliza o retrato documentado; True cria outra pasta de respostas e consulta novamente.')
code('''from pathlib import Path
import sys,subprocess,importlib.util,importlib.metadata,json,io,zipfile,base64,hashlib
from datetime import datetime,timezone,date
requirements={"requests":"requests>=2.32,<3","pandas":"pandas>=2.2,<3","docx":"python-docx>=1.1,<2"}
missing=[requirement for module,requirement in requirements.items() if importlib.util.find_spec(module) is None]
if missing:subprocess.run([sys.executable,"-m","pip","install",*missing],check=True)
import pandas as pd
from IPython.display import display,Markdown,HTML
display(HTML("<style>.text_cell_render,.jp-RenderedHTMLCommon{font:20px/1.65 Arial,sans-serif}summary{cursor:pointer}.dataframe{font-size:17px}td,th{padding:8px}</style>"))
BIB=next((p/"bibliografia" for p in [Path.cwd(),*Path.cwd().parents] if (p/"bibliografia/temas.json").exists()),None)
if BIB is None:BIB=Path.cwd()/"Projeto_FV_PVDAQ_2107_2024/bibliografia"
BIB.mkdir(parents=True,exist_ok=True)
support=base64.b64decode("__BUNDLE__")
assert hashlib.sha256(support).hexdigest()=="__SHA__"
with zipfile.ZipFile(io.BytesIO(support)) as archive:
    for item in archive.infolist():
        target=(BIB/item.filename).resolve();assert target.is_relative_to(BIB.resolve())
        if not target.exists():target.write_bytes(archive.read(item.filename))
sys.path.insert(0,str(BIB))
import bibliografia_fv as bibliography
import importlib;importlib.reload(bibliography)
CONSULTAR_REDE=True
NOVA_COLETA=False
SURVEY=bibliography.Survey(BIB,live=CONSULTAR_REDE)
if NOVA_COLETA:
    SURVEY.raw=BIB/"raw"/("consulta_"+datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S"))
    SURVEY.raw.mkdir(parents=True,exist_ok=True)
    SURVEY.cfg["through_date"]=date.today().isoformat()
print("Saídas:",SURVEY.out)
print("Chaves presentes:",{provider:bool(value) for provider,value in SURVEY.keys.items()})
'''.replace('__BUNDLE__',base64.b64encode(bundle).decode()).replace('__SHA__',hashlib.sha256(bundle).hexdigest()))
md('## 1 Protocolo e consultas dos 19 tópicos')
description('As consultas do protocolo preservam os tópicos do plano. Obras de método e livros entram como sementes explícitas. '
 'A seleção automática exige termos específicos no título, além da pertinência temática. Isso evita promover artigos de células ou física solar '
 'a referências sobre inversores ou variabilidade do recurso terrestre somente por terem muitas citações.')
code('''display(pd.DataFrame(SURVEY.topics)[["id","title","owner","query"]].rename(columns={"id":"Subseção","title":"Tópico","owner":"Responsável","query":"Consulta"}))
print(SURVEY.cfg["ranking"])
''')
md('## 2 Coleta multibase com rastreabilidade')
description('As respostas originais ficam em raw e as consultas efetivas em outputs/logs. O retrato padrão é limitado ao protocolo de 16/10/2026. '
 'Consultas são limitadas por tópico, sem alegação de exaustividade. A chave pode não conferir acesso ao conteúdo integral ou a todos os campos de uma base. '
 'Falhas e ausência de credenciais não são representadas como buscas bem-sucedidas ou zero publicações.')
code('''REGISTROS=SURVEY.collect()
display(SURVEY.availability)
display(pd.DataFrame(REGISTROS).groupby("source").size().rename("Registros"))
print("Registros normalizados:",len(REGISTROS))
''')
md('## 3 Deduplicação classificação e seleção de leituras')
description('DOI normalizado é a primeira chave. Sem DOI, usa-se título normalizado e ano, preservando edições distintas. '
 'As citações de bases diferentes não são somadas. A guia combina livro, métodos específicos, trabalhos citados no conjunto recuperado e complemento recente. '
 'Leitura integral e conferência de páginas ou equações continuam necessárias antes da redação.')
code('''OBRAS=SURVEY.consolidate()
LEITURAS=SURVEY.select()
RESUMO=SURVEY.export()
display(pd.DataFrame([RESUMO]).drop(columns=["source_status"]))
display(pd.DataFrame(LEITURAS).groupby("topic").size().rename("Leituras indicadas"))
''')
titles={1:'Recurso solar',2:'Ambiente e montagem',3:'Conversão fotovoltaica',4:'Desempenho e validação'}
topics=json.loads((BIB/'temas.json').read_text())
for number in range(1,5):
    md('# '+str(number)+' '+titles[number])
    description('Referências para a seção '+str(number)+'. A lista completa, o ranking recuperado e os DOI estão nos CSV e documentos por seção.')
    for topic in topics:
        if not topic['id'].startswith(str(number)+'.'):continue
        md('## '+topic['id']+' '+topic['title'])
        description('Responsável: '+topic['owner']+'. '+topic['method']+'\n\nLimite do estudo de caso: '+topic['limitation'])
        code('''for work in [w for w in SURVEY.selected if w["topic"]=="__TOPIC__"]:
    display(Markdown("**"+work["id"]+" — "+work["selection_role"]+"**\\n\\n"+bibliography.citation(work)+
        "\\n\\nDOI: "+("https://doi.org/"+work["doi"] if work["doi"] else "não informado")+
        "\\n\\n"+bibliography.counts(work)+"\\n\\nAcesso: "+(work["oa_url"] or work["url"])))
'''.replace('__TOPIC__',topic['id']))
md('# 5 Documentos exportações e execução')
description('Word por subseção; Markdown e CSV por seção; catálogo consolidado e relações por tópico; BibTeX e RIS para gerenciadores de referências. '
 'Os formatos bibliográficos não importam automaticamente no Zotero nem publicam no GitHub. O grupo pode versionar o código e os resultados depois.')
code('''print("Word:",SURVEY.out/"Referencias_por_Subsecao.docx")
print("BibTeX:",SURVEY.out/"referencias_fundamentacao.bib")
print("RIS:",SURVEY.out/"referencias_fundamentacao.ris")
display(pd.DataFrame([{"Arquivo":str(p.relative_to(SURVEY.out)),"Bytes":p.stat().st_size} for p in sorted(SURVEY.out.rglob("*")) if p.is_file()]))
assert set(w["topic"] for w in SURVEY.selected)==set(t["id"] for t in SURVEY.topics)
assert all(w["title"] and (w["doi"] or w["url"]) for w in SURVEY.selected)
assert not any("Solar Dynamics Observatory" in w["title"] or "polymer tandem" in w["title"].lower() for w in SURVEY.selected)
print("Conferência: 19 tópicos com referências efetivas e origem identificada.")
''')
nb=nbf.v4.new_notebook(cells=cells,metadata={'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},
 'language_info':{'name':'python','version':'3.12'},'project_version':'1.0.0',
 'purpose':'Fundamentação teórica por tópico, adaptação do modelo WCNPS, sem busca de lacuna'})
nbf.validate(nb)
target=BIB/'02_Fundamentacao_Teorica_por_Subsecao.ipynb';nbf.write(nb,target)
print(target.name,len(cells),'células;',sum(c.cell_type=='code' for c in cells),'códigos')
