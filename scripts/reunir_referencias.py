"""Inventory all technical sources used in this project; no citation ranking."""
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
dataset=json.loads((ROOT/'references/pvdaq_dataset_citacao.json').read_text())
rows=[
('R01',dataset['title'],' and '.join(dataset['authors']),dataset['year'],'0; 1.4; 4.4','Dados medidos e documentação da instalação; licença CC BY 4.0','https://data.openei.org/submissions/4568',dataset['subset']['raw_manifest'],'10.25984/1846021'),
('R02','PVDAQ access tools and openEDI documentation','PVDAQ / openEDI',None,'0; 1.4','Documentação de acesso, formatos e proveniência','https://github.com/NatLabRockies/pvdaq_access','',None),
('R03','Solar Position Algorithm for Solar Radiation Applications — NREL/TP-560-34302','Reda, I. and Andreas, A.',2008,'1.1; 3.1','Posição solar e cálculo do ângulo zenital; revisão do relatório','https://docs.nlr.gov/docs/fy08osti/34302.pdf','methods/SPA_Reda_Andreas_2008.pdf',None),
('R04','General Solar Position Calculations','NOAA Global Monitoring Laboratory',None,'0; 1.1','Aproximação usada somente para reproduzir o critério de disponibilidade diurna','https://gml.noaa.gov/grad/solcalc/solareqns.PDF','',None),
('R05','get_extra_radiation — Spencer method; pvlib 0.16.1','pvlib contributors',2026,'1.1','Irradiância extraterrestre; constante de referência 1366,1 W/m² do software','https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.irradiance.get_extra_radiation.html','',None),
('R06','Modeling daylight availability and irradiance components from direct and global irradiance','Perez, R. and Ineichen, P. and Seals, R. and Michalsky, J. and Stewart, R.',1990,'2.2; 3.1','Modelo de transposição difusa; fonte original','https://doi.org/10.1016/0038-092X(90)90055-H','','10.1016/0038-092X(90)90055-H'),
('R07','Assessing the outdoor operating temperature of photovoltaic modules','Faiman, D.',2008,'2.1; 3.2','Modelo térmico e interpretação de seus coeficientes','https://doi.org/10.1002/pip.813','','10.1002/pip.813'),
('R08','Improvement and validation of a model for photovoltaic array performance','De Soto, W. and Klein, S. A. and Beckman, W. A.',2006,'3.3; 3.4','Base física da parametrização do diodo único; implementação CEC identificada separadamente','https://doi.org/10.1016/j.solener.2005.06.010','','10.1016/j.solener.2005.06.010'),
('R09','pvlib python: a python package for modeling solar energy systems','Holmgren, W. F. and Hansen, C. W. and Mikofski, M. A.',2018,'1–4','Referência do software; versão efetivamente usada 0.16.1','https://joss.theoj.org/papers/10.21105/joss.00884','','10.21105/joss.00884'),
('R10','calcparams_cec and retrieve_sam — pvlib 0.16.1','pvlib contributors',2026,'3.3; 3.5','Implementação CEC e origem dos parâmetros SAM preservados em JSON','https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.pvsystem.calcparams_cec.html','config/modulo_cec.json; config/inversor_cec.json',None),
('R11','PVWatts Version 5 Manual — NREL/TP-6A20-62641','Dobos, A. P.',2014,'3.3; 3.5','Conversão CC–CA e comparação CC por coeficiente térmico','https://docs.nlr.gov/docs/fy14osti/62641.pdf','methods/PVWatts_v5_Dobos_2014.pdf',None),
('R12','Performance Parameters for Grid-Connected PV Systems — NREL/CP-520-37358','Marion, B. and others',2005,'4.1; 4.2; 4.3','Produtividades, PR e perdas normalizadas','https://docs.nlr.gov/docs/fy05osti/37358.pdf','methods/Performance_Parameters_Marion_2005.pdf',None),
('R13','TRIO-20.0/27.6-TL-US — Product Manual','ABB',None,'3.5','Limites e configurações do inversor; configuração efetiva da usina não comprovada','https://library.e.abb.com/public/9ddffa465aa146bfa43bd0854abbcc81/TRIO-20.0-27.6-TL-US_Product_Manual.pdf','methods/ABB_TRIO_20_27_US_Manual.pdf',None),
('R14','A continuous form of the Perez diffuse sky model for forward and reverse transposition','Driesse, A. and Jensen, A. R. and Perez, R.',2024,'1.2; 3.1; 4.5','Transposição inversa exploratória; Erbs-Driesse e Perez-Driesse','https://doi.org/10.1016/j.solener.2023.112093','','10.1016/j.solener.2023.112093'),
('R15','ghi_from_poa_driesse_2024 — pvlib 0.16.1','pvlib contributors',2026,'3.1','Implementação e critérios numéricos da inversão POA→GHI','https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.irradiance.ghi_from_poa_driesse_2024.html','',None),
('R16','Reverse transposition limitations — pvlib 0.16.1','Driesse, A.',2026,'1.4; 3.1; 4.4','Demonstra a possibilidade de soluções não únicas; fechamento não é validação independente','https://pvlib-python.readthedocs.io/en/v0.16.1/gallery/irradiance-transposition/plot_rtranpose_limitations.html','',None),
('R17','A model for deriving the direct normal and diffuse horizontal irradiance from the global tilted irradiance','Marion, B.',2015,'3.1','Método alternativo GTI-DIRINT, citado para comparação; não executado nesta versão','https://doi.org/10.1016/j.solener.2015.10.024','','10.1016/j.solener.2015.10.024'),
('R18','erbs_driesse — pvlib 0.16.1','pvlib contributors',2026,'1.2; 3.1','Decomposição estimada de GHI em DNI e DHI, baseada em relação empírica','https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.irradiance.erbs_driesse.html','',None),
('R19','Expanding Solar Energy Opportunities: From Rooftops to Building Integration','U.S. Department of Energy',None,'4.5','Contexto introdutório de BIPV; não fornece validação da fachada hipotética','https://www.energy.gov/cmei/systems/articles/expanding-solar-energy-opportunities-rooftops-building-integration','',None),
('R20','Energy Performance Ratings for Windows, Doors, and Skylights','U.S. Department of Energy',None,'4.5','Definição de SHGC e transmissão visível; o SHGC do cenário não é certificado','https://www.energy.gov/energysaver/energy-performance-ratings-windows-doors-and-skylights','',None),
('R21','POWER Hourly API','NASA POWER',None,'Histórico v1.0; 1.4','Fonte complementar da versão anterior; não utilizada no percurso principal v1.1','https://power.larc.nasa.gov/docs/services/api/temporal/hourly/','methods/NASA_POWER_Hourly_API.html',None),
('R22','CERES SYN1deg hourly GHI, DNI and DHI methodology','NASA POWER',None,'Histórico v1.0; 1.4','Produto solar em grade da versão anterior; não utilizado no percurso principal v1.1','https://power.larc.nasa.gov/docs/methodology/energy-fluxes/syn1deg/','methods/NASA_POWER_SYN1deg.html',None),
('R23','Meteorological Data Overview — MERRA-2','NASA POWER',None,'Histórico v1.0; 1.4','Meteorologia em grade da versão anterior; não utilizada no percurso principal v1.1','https://power.larc.nasa.gov/docs/methodology/meteorology/','data/raw/fonte_nasa.json',None),
('R24','Proposta de estrutura do capítulo: Recurso solar e modelagem da conversão fotovoltaica','Equipe SPGER0046 / UFPB',2026,'Planejamento','Documento interno que define as quatro seções; não é referência científica de um modelo','ACERVO_RESTRITO_DA_EQUIPE','docs/Plano_do_Capitulo_Fonte_Drive_20261016.txt',None),
('R25','Solar Data Tools demo — Farm Solar Array','PV Analytics Webinar',2024,'0; 1.4; 4.4','Contexto complementar de qualidade e operação; não usado para remover erros altos','https://pv-tutorials.github.io/2024_Analytics_Webinar/solar-data-tools-demo.html','',None),
('R26','openEDI PVDAQ dataset documentation','openEDI',None,'0; 1.4','Estrutura e documentação geral dos dados abertos','https://github.com/openEDI/documentation/blob/main/pvdaq.md','',None),
('R27','Root mean square error (RMSE) or mean absolute error (MAE)? Arguments against avoiding RMSE in the literature','Chai, T. and Draxler, R. R.',2014,'4.4','Métricas complementares para avaliação, com definição explícita de sinal e normalização neste projeto','https://gmd.copernicus.org/articles/7/1247/2014/','','10.5194/gmd-7-1247-2014'),
('R28','Soiling Losses','Sandia National Laboratories / PVPMC',None,'2.3','Mecanismo de atenuação por sujidade e interpretação de hipóteses','https://pvpmc.sandia.gov/modeling-guide/1-weather-design-inputs/shading-soiling-and-reflection-losses/soiling-losses/','',None),
('R29','Plane of Array (POA) Irradiance','Sandia National Laboratories / PVPMC',None,'1.2; 2.2; 2.4; 3.1','Componentes da POA e cuidado com correções já incorporadas à medição','https://pvpmc.sandia.gov/modeling-guide/1-weather-design-inputs/plane-of-array-poa-irradiance/','',None),
('R30','Performance Ratio','Sandia National Laboratories / PVPMC',None,'4.2; 4.3','Definição de Yr e PR; especificação da referência de irradiância','https://pvpmc.sandia.gov/modeling-guide/5-ac-system-output/pv-performance-metrics/performance-ratio/','',None),
]
refs=[]
for rid,title,authors,year,sections,role,url,local,doi in rows:
    refs.append({'id':rid,'title':title,'authors':authors,'year':year,'sections':sections,'role':role,'url':url,'doi':doi,'local_copy':local or 'Consulta por URL/DOI; PDF não incluído','accessed':'2026-10-16','citation':f'{authors}. {title}. {year or "s.d."}.'})
    if rid=='R01':refs[-1].update(citation=dataset['citation_abnt'],accessed=dataset['accessed'])
p=ROOT/'references';p.mkdir(exist_ok=True)
(p/'referencias_projeto.json').write_text(json.dumps(refs,indent=2,ensure_ascii=False))
md='# Referências e fontes do projeto — v1.2\n\nInventário das fontes científicas, técnicas, de dados e de planejamento usadas neste projeto. Não constitui uma revisão bibliográfica concluída nem uma seleção por número de citações. Fontes NASA da versão anterior são preservadas como histórico e não são entradas da validação elétrica atual. Os identificadores permanecem estáveis; R27–R30 foram acrescentadas para os diagnósticos e as hipóteses ambientais.\n\n'
bib=[]
for x in refs:
    md+=f'## {x["id"]} — {x["title"]}\n\n{x["citation"]}\n\nSeções: {x["sections"]}. Uso: {x["role"]}.\n\nFonte: {x["url"]}\n\nDOI: {x["doi"] or "não informado"}. Cópia local: {x["local_copy"]}. Consulta: {x["accessed"]}.\n\n'
    fields={'author':x['authors'],'title':x['title'],'url':x['url'],'note':x['role']+'; acesso em '+x['accessed']}
    if x['year']:fields['year']=str(x['year'])
    if x['doi']:fields['doi']=x['doi']
    bib.append('@misc{'+x['id']+',\n'+',\n'.join('  '+k+' = {'+str(v).replace('{','').replace('}','')+'}' for k,v in fields.items())+'\n}')
(p/'Referencias_do_Projeto.md').write_text(md)
(p/'referencias_projeto.bib').write_text('\n\n'.join(bib)+'\n')
print('Referências inventariadas:',len(refs))
