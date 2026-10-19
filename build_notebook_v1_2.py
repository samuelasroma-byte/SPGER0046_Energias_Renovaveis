"""Build v1.2 with separate titles, collapsible descriptions and real exports."""
from pathlib import Path
import io,zipfile,base64,hashlib,json
import nbformat as nbf
ROOT=Path(__file__).resolve().parent
SECTIONS=json.loads((ROOT/'docs/secoes_capitulo.json').read_text())
files=['bibliografia/formatacao_abnt.py','src/projeto_fv.py','src/refinamento_fv.py','src/relatorio_fv.py','src/editorial_fv.py',
       'config/projeto.json','config/modulo_cec.json','config/inversor_cec.json','config/distribuicao_editorial.json',
       'data/raw/fontes_pvdaq.json','docs/secoes_capitulo.json','scripts/gerar_documentos.py','scripts/gerar_dossie_tecnico.py','scripts/gerar_tabulares_por_secao.py',
       'references/referencias_projeto.json','references/Referencias_do_Projeto.md','references/referencias_projeto.bib']
buf=io.BytesIO()
with zipfile.ZipFile(buf,'w',zipfile.ZIP_DEFLATED) as z:
    for name in files:z.writestr(name,(ROOT/name).read_bytes())
packed=buf.getvalue()
cells=[]
def md(s):cells.append(nbf.v4.new_markdown_cell(s))
def code(s):cells.append(nbf.v4.new_code_cell(s))
def title(s):md(s)
def description(s):md('<details>\n<summary>Descrição e método</summary>\n\n'+s+'\n\n</details>')
title('# SPGER0046 Recurso solar e modelagem fotovoltaica')
description('**Versão 1.2.2.** Farm Solar Array PVDAQ 2107, Califórnia, abril a junho de 2024. '
    'Entradas: POA, temperatura do ar e vento locais. Saída: geração AC calculada, comparada com o medidor. '
    'NASA POWER não é usado na cadeia principal. Cada subseção possui título, descrição separada e código/resultados. '
    'As descrições usam HTML details fechado por padrão; a renderização e o recolhimento por título variam entre JupyterLab e Colab. '
    'O relatório HTML exportado conserva os blocos recolhíveis. A execução local não simula a autenticação Google nem a interface Colab.')
md('**Como usar:** execute as células na ordem. As saídas ficam em outputs, separadas em tabelas, quadros, graficos, fluxogramas e figuras. '
   'Cada figura final possui PDF vetorial e PNG a 600 dpi nos temas claro e escuro em secoes. Quatro DOCX separados reúnem as tabelas e quadros de cada seção; as coleções consolidadas servem para consulta. '
   'A exportação pessoal ao Drive é opcional e exige autenticação no Colab. '
   '**Inserção editorial única:** cada figura, gráfico e tabela possui somente uma subseção responsável. Usar o mapa config/distribuicao_editorial.json e citar o ID em outras partes, sem reinserir o material. As quatro versões de uma ilustração são alternativas de formato e tema.\n\n'
   '**Sumário:** '+ ' · '.join('['+s['id']+'](#sec_'+s['id'].replace('.','_')+')' for s in SECTIONS))
title('## 0 Preparação e sistema de referência')
description('O modelo representa uma instalação real. Equipamentos: 2.880 módulos e 24 inversores. '
    'P₀ de normalização=893 kWp; soma de placa=892,8 kWp; soma STC CEC=891,648 kWp. '
    'O equivalente 20×6 não é cabeamento verificado. Nenhuma lacuna diurna é interpolada. '
    'Os arquivos oficiais são baixados apenas se o ZIP local estiver ausente, com conferência SHA-256.')
code('''from pathlib import Path
import sys,subprocess,importlib.util,importlib.metadata,os,json,base64,io,zipfile,hashlib
if importlib.util.find_spec("packaging") is None:
    subprocess.run([sys.executable,"-m","pip","install","packaging"],check=True)
from packaging.requirements import Requirement
requirements={"numpy":"numpy>=2,<3","pandas":"pandas>=2.2,<3","scipy":"scipy>=1.13,<2",
    "matplotlib":"matplotlib>=3.9,<4","pvlib":"pvlib==0.16.1","python-docx":"python-docx>=1.1,<2","Pillow":"Pillow>=10,<13"}
missing=[]
for package,req in requirements.items():
    try:
        if importlib.metadata.version(package) not in Requirement(req).specifier:missing.append(req)
    except importlib.metadata.PackageNotFoundError:missing.append(req)
if missing:subprocess.run([sys.executable,"-m","pip","install",*missing],check=True)
support=base64.b64decode("__PACKED__")
assert hashlib.sha256(support).hexdigest()=="__HASH__"
ROOT=next((p for p in [Path.cwd(),*Path.cwd().parents] if (p/"src/projeto_fv.py").exists()),None)
if ROOT is None:ROOT=Path.cwd()/"Projeto_FV_PVDAQ_2107_2024"
update=not (ROOT/"config/projeto.json").exists()
if not update:update=json.loads((ROOT/"config/projeto.json").read_text()).get("version")!="1.2.2"
if not (ROOT/"config/distribuicao_editorial.json").exists():update=True
if update:
    with zipfile.ZipFile(io.BytesIO(support)) as archive:
        for item in archive.infolist():
            dest=(ROOT/item.filename).resolve()
            assert dest.is_relative_to(ROOT.resolve())
            if dest.exists():
                backup=ROOT/"backup_antes_v1_2"/item.filename
                backup.parent.mkdir(parents=True,exist_ok=True)
                if not backup.exists():backup.write_bytes(dest.read_bytes())
            dest.parent.mkdir(parents=True,exist_ok=True)
            dest.write_bytes(archive.read(item.filename))
sys.path.insert(0,str(ROOT/"src"))
import projeto_fv as fv,refinamento_fv as rf,relatorio_fv as rel,editorial_fv as editorial
import importlib
for module in [fv,rf,rel,editorial]:importlib.reload(module)
import numpy as np,pandas as pd,pvlib
from IPython.display import display,Markdown,HTML
display(HTML("<style>.text_cell_render,.jp-RenderedHTMLCommon{font:20px/1.65 Arial,sans-serif}.dataframe{font-size:17px}td,th{padding:8px}summary{cursor:pointer}</style>"))
CFG=fv.load_config(ROOT)
EXECUTAR_INVERSAO_EXPLORATORIA=True
GERAR_DOCX=True
REUTILIZAR_FIGURAS_VERIFICADAS=True
TEMA_VISUALIZACAO="escuro"
SALVAR_RESULTADOS_NO_DRIVE=False
PASTA_RESULTADOS_ID="ID_RESTRITO_DA_EQUIPE"
print("Versão",CFG["version"],"| NASA POWER fora da cadeia principal")
display(pd.DataFrame([{"biblioteca":k,"versão":importlib.metadata.version(k)} for k in requirements]))
'''.replace('__PACKED__',base64.b64encode(packed).decode()).replace('__HASH__',hashlib.sha256(packed).hexdigest()))
title('### 0.1 Auditoria e cálculo da cadeia principal')
description('O filtro diurno usa NOAA ≥10° para preservar o denominador da auditoria; SPA calcula a geometria no meio dos intervalos. '
    'Carimbos são tratados como início de intervalos locais America/Los_Angeles, interpretando PST8PDT dos metadados. '
    'Posição representativa em +7,5 minutos para as médias de 15 minutos e +30 minutos para a inversão horária; convenção temporal documentada, sem otimização por defasagem da geração. '
    'As médias de 15 minutos dos canais de 5 minutos exigem três amostras. O fator empírico secundário usa somente abril.')
code('''CTX=fv.complete_pipeline(ROOT,make_plots=False,include_nasa=False,reverse=EXECUTAR_INVERSAO_EXPLORATORIA)
D,A=CTX["data"],CTX["model_a"]
print("Cobertura conjunta diurna:",100*CTX["audit"]["available_daylight_15m"]/CTX["audit"]["expected_daylight_15m"],"%")
print("O quadro de disponibilidade dos dados é exibido exclusivamente em 1.4.")
''')
title('### 0.2 Exportações e diagnósticos')
description('Dados e filtros idênticos geram os dois temas. Cada figura possui fonte, legenda, natureza da evidência e subseção no catálogo. '
    'Cada ilustração é exibida somente na sua subseção de inserção editorial. As demais subseções a citam sem repetir a exibição.')
code('''rf.generate_all(CTX,reuse_checked=REUTILIZAR_FIGURAS_VERIFICADAS)
rel.coverage(CTX)
print("Figuras:",len(CTX["figures"]),"| arquivos finais PDF/PNG:",4*len(CTX["figures"]))
print("Saídas:",ROOT/"outputs")
''')
group_titles={1:'Fundamentos e caracterização do recurso solar',
2:'Condições ambientais e de entorno da conversão fotovoltaica',
3:'Modelagem da conversão fotovoltaica',4:'Avaliação de desempenho perdas e validação'}
owners={1:'Samuel',2:'Vannessa e Thais',3:'Gabriela e Giulia',4:'Júlia Ribeiro e Lucas Simão'}
goals={1:'Caracterizar e representar o recurso solar.',2:'Relacionar ambiente e instalação à irradiância e à temperatura.',
3:'Transformar as entradas em temperatura, potência e energia.',4:'Quantificar desempenho e confrontar a geração calculada com observações.'}
special={
'1.1':'display(D[["zenith","azimuth","aoi_deg","dni_extra_Wm2","extraterrestrial_horizontal_Wm2"]].iloc[40:45].round(3))',
'1.2':'print("POA é medida. GHI/DNI/DHI disponíveis são estimativas da inversão.")',
'1.3':'display(CTX["analytics_tables"]["criterio_dias_ilustrativos"].iloc[[0,-1]])',
'1.4':'display(pd.DataFrame([CTX["audit"]])); display(fv.data_status())',
'2.1':'display(CTX["analytics_tables"]["estatistica_descritiva"].iloc[:4])',
'2.2':'display(CTX["environment_scenarios"]) if len(CTX["environment_scenarios"]) else print("Albedo: cenário omitido sem inversão.")',
'2.3':'display(CTX["environment_sensitivity"])',
'2.4':'display(pd.DataFrame([CFG["site"]]))',
'3.1':'display(pd.DataFrame([CTX.get("reverse_summary",{"executed":False})]))',
'3.2':'display(pd.DataFrame([{k:CFG["assumptions"][k] for k in ["faiman_u0","faiman_u1","faiman_temperature_used_as_cell_proxy"]}]))',
'3.3':'print("Curvas CEC calculadas; não são varreduras experimentais.")',
'3.4':'display(CTX["analytics_tables"]["arranjo_equivalente_diurno"].head().round(3))',
'3.5':'display(CTX["capacity_sensitivity"].round(4))',
'3.6':'display(CTX["analytics_tables"]["energia_e_indicadores_mensais"].round(3))',
'4.1':'display(CTX["energy_stages"].round(3)); display(CTX["operational_flags"].head())',
'4.2':'display(CTX["analytics_tables"]["energia_e_HSP_diurna_pareada"][["day_local","PSH_POA_paired_h","paired_intervals"]].head().round(4))',
'4.3':'display(CTX["yields"].round(5))',
'4.4':'display(CTX["metrics"].round(5)); display(CTX["analytics_tables"]["metricas_por_mes"].round(4)); display(pd.DataFrame([CTX["meter_inverter_consistency"]]).round(4))',
'4.5':'display(CTX["bipv_comparison"].round(4)) if "bipv_comparison" in CTX else print("BIPV omitido sem inversão.")'}
for group in range(1,5):
    title('# '+str(group)+' '+group_titles[group])
    description(goals[group]+' **Responsável:** '+owners[group]+'.')
    for s in SECTIONS:
        if not s['id'].startswith(str(group)+'.'):continue
        title('## '+s['id']+' '+s['title']+' <a id="sec_'+s['id'].replace('.','_')+'"></a>')
        description(s['method']+'\n\n**Entradas:** '+s['inputs']+'\n\n'+s['equation']+
            '\n\n**Evidência:** '+s['evidence']+'. **Limite:** '+s['limitation']+
            '\n\n**Saídas:** '+s['outputs']+' **Referências:** '+', '.join(s['refs'])+'.')
        code(special[s['id']]+'\nrf.show(CTX,'+repr(s['figures'])+',TEMA_VISUALIZACAO)')
title('# 5 Referências')
description('Inventário das fontes dos dados, modelos e limites. O levantamento teórico por tópico está no notebook bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb e em bibliografia/outputs/. Não substitui leitura crítica e redação final. '
    'Fontes NASA pertencem ao histórico/comparação de produtos, sem entrada na cadeia principal.')
code('''REFERENCIAS=json.loads((ROOT/"references/referencias_projeto.json").read_text())
for r in REFERENCIAS:
    display(Markdown("**"+r["id"]+"** — "+r["citation"]+"\\n\\n"+r["url"]+"\\n\\nUso: "+r["role"]))
''')
title('# 6 Documentos e relatório')
description('Quatro DOCX editoriais contêm apenas as tabelas e quadros atribuídos a cada seção. As seis coleções consolidadas e o dossiê servem como consulta da execução. Papel A4, margens superior/esquerda de 3 cm e inferior/direita de 2 cm; Times New Roman 12 no texto nativo, com títulos de tabelas e figuras centralizados. '
    'O relatório HTML possui tema alternável e descrições recolhíveis. Conferência visual de Word requer renderizador disponível.')
code('''if GERAR_DOCX:
    python_documentos=os.environ.get("CODEX_PRIMARY_RUNTIME_PYTHON",sys.executable)
    subprocess.run([python_documentos,str(ROOT/"scripts/gerar_documentos.py")],check=True)
    subprocess.run([python_documentos,str(ROOT/"scripts/gerar_tabulares_por_secao.py")],check=True)
    subprocess.run([python_documentos,str(ROOT/"scripts/gerar_dossie_tecnico.py")],check=True)
    display(pd.DataFrame([{"arquivo":str(p.relative_to(ROOT)),"bytes":p.stat().st_size} for p in sorted((ROOT/"secoes").glob("*/tabelas/docx/*.docx"))]))
print(rel.report(CTX))
print("Matriz:",ROOT/"outputs/relatorios/Matriz_de_Cobertura_do_Capitulo.md")
''')
title('# 7 Pacote de resultados e exportação opcional ao Drive')
description('Ative SALVAR_RESULTADOS_NO_DRIVE para uma execução pessoal no Colab. A célula cria uma pasta datada com a hierarquia preservada; '
    'autenticação é pessoal, sem tokens no notebook. O pacote contém todas as saídas locais.')
code('''ZIP_RESULTADOS=editorial.zip_results(CTX)
print("Resultados compactados:",ZIP_RESULTADOS)
try:
    IS_COLAB=importlib.util.find_spec("google.colab") is not None
except ModuleNotFoundError:IS_COLAB=False
if SALVAR_RESULTADOS_NO_DRIVE and IS_COLAB:
    display(fv.sync_outputs_drive(CTX,PASTA_RESULTADOS_ID))
elif SALVAR_RESULTADOS_NO_DRIVE:
    print("Exportação configurada para Colab; arquivos locais prontos.")
else:
    print("Saídas locais concluídas. Exportação pessoal ao Drive desativada por padrão.")
''')
nb=nbf.v4.new_notebook(cells=cells,metadata={
 'kernelspec':{'display_name':'Python 3','language':'python','name':'python3'},
 'language_info':{'name':'python','version':'3.12'},'project_version':'1.2.2',
 'description_folding':'HTML details in separate Markdown cells; renderer dependent'})
nbf.validate(nb)
target=ROOT/'notebooks/01_Projeto_FV_Quatro_Secoes.ipynb';nbf.write(nb,target)
print('Notebook construído:',len(cells),'células;',sum(c.cell_type=='code' for c in cells),'células de código')
