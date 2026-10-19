"""Topic protocol and explicit reading seeds for the photovoltaic chapter."""
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
DEST=ROOT/'bibliografia'
DEST.mkdir(exist_ok=True)
sections=json.loads((ROOT/'docs/secoes_capitulo.json').read_text())
queries={
'1.1':('solar position algorithm irradiance','solar position;solar geometry;zenith;extraterrestrial'),
'1.2':('solar irradiance components direct diffuse global','irradiance;diffuse;direct;global horizontal'),
'1.3':('solar irradiance atmospheric variability','variability;atmospheric;aerosol;cloud'),
'1.4':('solar radiation measurement uncertainty','measurement;uncertainty;pyranometer;solar resource'),
'2.1':('photovoltaic temperature efficiency','temperature;thermal;efficiency'),
'2.2':('photovoltaic albedo ground reflectance','albedo;reflectance;ground reflected'),
'2.3':('photovoltaic soiling shading losses','soiling;shading;dust;partial shade'),
'2.4':('photovoltaic optimum tilt orientation azimuth','tilt;orientation;azimuth;inclination'),
'3.1':('solar irradiance transposition tilted plane','transposition;tilted;plane of array;perez'),
'3.2':('photovoltaic module operating temperature model','module temperature;operating temperature;faiman;thermal model'),
'3.3':('photovoltaic single diode model parameters','single diode;single-diode;diode model;equivalent circuit'),
'3.4':('photovoltaic array mismatch series parallel','mismatch;interconnection;series;parallel'),
'3.5':('photovoltaic inverter efficiency model','inverter;clipping;conversion efficiency'),
'3.6':('photovoltaic energy yield prediction model','energy yield;energy prediction;performance model'),
'4.1':('photovoltaic energy losses degradation','losses;degradation;loss factor'),
'4.2':('photovoltaic specific yield performance parameters','specific yield;final yield;reference yield;performance parameters'),
'4.3':('photovoltaic performance ratio weather corrected','performance ratio;weather corrected;performance metrics'),
'4.4':('photovoltaic model validation error metrics','validation;rmse;mean absolute error;model comparison'),
'4.5':('building integrated photovoltaics semitransparent thermal optical','building integrated;building-integrated;bipv;semitransparent'),
}
for s in sections:
    s['query'],terms=queries[s['id']]
    s['relevance_terms']=terms.split(';')
    s['purpose']='Fundamentação teórica e indicação de leituras por tópico'
(DEST/'temas.json').write_text(json.dumps(sections,ensure_ascii=False,indent=2))
refs=json.loads((ROOT/'references/referencias_projeto.json').read_text())
seeds=[]
for r in refs:
    if r['id'] in ['R21','R22','R23','R24']:continue
    topics=[s['id'] for s in sections if r['id'] in s['refs']]
    if not topics:continue
    seeds.append(dict(seed_id=r['id'],title=r['title'],doi=r.get('doi') or '',
        authors=r['authors'],year=r['year'],url=r['url'],topics=topics,
        kind='artigo' if r.get('doi') and r['id']!='R01' else 'documentação técnica',
        role=r['role'],priority=2,verify_by_title=False))
    if r['id']=='R12':seeds[-1]['doi']='10.1109/PVSC.2005.1488451'
extra=[
('S01','Solar Engineering of Thermal Processes Photovoltaics and Wind','10.1002/9781119540328',list(queries),'livro','Geometria, radiação, transferência de calor e sistemas fotovoltaicos',2020),
('S02','Handbook of Photovoltaic Science and Engineering','10.1002/9780470974704',['1.2','2.1','2.3','3.2','3.3','3.4','3.5','3.6','4.1','4.2','4.3','4.5'],'livro','Fundamentos físicos, dispositivos, arranjos e integração',2011),
('S03','Solar Energy Engineering Processes and Systems','10.1016/C2011-0-07038-2',['1.1','1.2','1.3','1.4','2.1','2.2','2.4','3.1','3.2','3.6'],'livro','Recurso solar, geometria e modelagem de sistemas',2014),
('S04','Solar position algorithm for solar radiation applications','10.1016/j.solener.2003.12.003',['1.1'],'artigo','Artigo do algoritmo SPA usado no cálculo geométrico',2004),
('S05','On the temperature dependence of photovoltaic module electrical performance A review of efficiency power correlations','',['2.1','3.2'],'artigo de revisão','Relacionar temperatura e desempenho elétrico',2009),
('S06','The effect of spectral albedo on amorphous silicon and crystalline silicon solar photovoltaic device performance','',['2.2'],'artigo','Refletância do entorno e resposta espectral dos dispositivos',2013),
('S07','Impact of dust on solar photovoltaic performance Research status challenges and recommendations','',['2.3','4.1'],'artigo de revisão','Fundamentos e limites da avaliação de sujidade',2010),
('S08','Worldwide optimum tilt angles and ratios of sunlight incident upon tilted and tracked solar panels relative to horizontal panels','',['2.4'],'artigo','Inclinação e orientação na captação do recurso',2018),
('S09','Comprehensive Approach to Modeling and Simulation of Photovoltaic Arrays','10.1109/TPEL.2009.2013862',['3.3','3.4'],'artigo','Modelagem elétrica de módulos e arranjos',2009),
('S10','Computer simulation of the effects of electrical mismatches in photovoltaic cell interconnection circuits','10.1016/0379-6787(88)90059-2',['2.3','3.4'],'artigo','Mismatch e interconexão elétrica',1988),
('S11','Performance Model for Grid Connected Photovoltaic Inverters','10.2172/920449',['3.5'],'relatório','Modelo e caracterização de inversores conectados à rede',2007),
('S12','Photovoltaic Degradation Rates An Analytical Review','10.1002/pip.1182',['4.1'],'artigo de revisão','Perdas e degradação não se confundem com resíduos de um trimestre',2013),
('S13','Performance Parameters for Grid Connected PV Systems','10.1109/PVSC.2005.1488451',['3.6','4.2','4.3'],'artigo','Produtividades, PR e parâmetros de desempenho',2005),
('S14','Weather Corrected Performance Ratio','10.2172/1078057',['4.3'],'relatório','Efeito meteorológico no PR',2013),
('S15','Advantages of the mean absolute error MAE over the root mean square error RMSE in assessing average model performance','10.3354/cr030079',['4.4'],'artigo','Interpretação complementar de MAE, RMSE e viés',2005),
('S16','Building integrated photovoltaic products A state-of-the-art review and future research opportunities','10.1016/j.solmat.2011.12.016',['4.5'],'artigo de revisão','Materiais, funções construtivas e desempenho BIPV',2012),
('S17','A key review of building integrated photovoltaic BIPV systems','10.1016/j.jestch.2017.01.009',['4.5'],'artigo de revisão','Integração arquitetônica, elétrica e térmica',2017),
('S18','Best Practices Handbook for the Collection and Use of Solar Resource Data for Solar Energy Applications Third Edition','10.2172/1778700',['1.2','1.3','1.4','3.1'],'relatório','Medição, qualidade e representatividade dos dados solares',2021),
('S19','Experimental investigation of the temperature distribution in a BIPV façade','10.1051/epjpv/2024032',['4.5'],'artigo','Exemplo experimental recente de temperatura em fachada BIPV',2024),
('S20','Semi-Transparent Building Integrated Photovoltaic Solar Glazing Investigations of Electrical and Optical Performances for Window Applications in Tropical Region','10.1155/2019/6096481',['4.5'],'artigo','Desempenho elétrico e óptico de vidros fotovoltaicos semitransparentes',2019),
]
for sid,title,doi,topics,kind,role,year in extra:
    # A general solar textbook is not a primary source for error-metric debates.
    if sid=='S01':topics=[x for x in topics if x not in ['4.4','4.5']]
    seeds.append(dict(seed_id=sid,title=title,doi=doi,authors='',year=year,url='',topics=topics,
        kind=kind,role=role,priority=6 if sid=='S20' else 3 if kind=='livro' else 4,verify_by_title=not bool(doi)))
    if sid=='S03':
        seeds[-1]['authors']='Soteris A. Kalogirou'
        seeds[-1]['authorship_source']='https://shop.elsevier.com/subjects/books/physical-sciences-and-engineering/engineering-and-technology/general-engineering/engineering-general?page=15'
(DEST/'sementes.json').write_text(json.dumps(seeds,ensure_ascii=False,indent=2))
config={'version':'1.0.0','scope':'fundamentação teórica; sem busca de lacuna ou alegação de revisão sistemática',
    'from_year':1950,'through_date':'2026-10-16','recent_from_year':2021,
    'openalex_per_query':25,'openalex_recent_per_query':12,'crossref_per_query':20,
    'institutional_per_query':25,'request_timeout_seconds':25,'maximum_attempts':2,
    'credentials':['OPENALEX_API_KEY','SCOPUS_API_KEY','WOS_API_KEY','IEEE_API_KEY'],
    'model_notebook_drive_id':'ID_RESTRITO_DA_EQUIPE',
    'model_notebook_modified_time':'2026-09-12T04:01:14.298Z',
    'ranking':'Relevância temática, obras de método, livros de base, citações separadas por base e complemento recente',
    'interpretation':'Mais citados significa entre resultados recuperados e filtrados, na base e data indicadas; não ranking mundial exaustivo.'}
(DEST/'protocolo.json').write_text(json.dumps(config,ensure_ascii=False,indent=2))
print('Protocolo:',len(sections),'subseções;',len(seeds),'sementes; sem credenciais gravadas')
