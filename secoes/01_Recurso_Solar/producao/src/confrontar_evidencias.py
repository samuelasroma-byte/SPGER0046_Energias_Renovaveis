"""Confronto documental das 39 afirmações, distinto da busca bibliométrica.

Os pareceres são registros de leitura assistida, não decisões de um classificador.
A execução confere integridade e trechos âncora; não simula nova leitura intelectual.
"""
from pathlib import Path
import json,re,csv,hashlib,unicodedata
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]

# id, trecho âncora curto, classificação, parecer e consequência editorial.
PARECERES=[
('EV001','Variation of the earth-sun distance','DIRETA','A p. 9 vincula a variação orbital à irradiância normal. A equação 1.4.1b do exemplar imprime 0,00719; o código pvlib 0.16.1 imprime 0,000719. Há divergência documental real, conferida também na imagem da página.','Manter 0,000719 para reproduzir a implementação e registrar a divergência; não reproduzir o coeficiente do livro como se fosse o executado.'),
('EV002','the angle between the vertical and the line to the sun','DIRETA','As definições de zenital e elevação são explícitas na p. 13. A elevação complementa o zenital no mesmo referencial geométrico.','Identificar zenital geométrico no esquema; não confundir com o ângulo de incidência em superfície inclinada.'),
('EV003','the angle of incidence is the zenith angle','DIRETA','A equação 1.6.5, p. 15, resulta de inclinação zero e coincide com a relação apresentada. O SPA acrescenta correções astronômicas/topocêntricas.','Manter a equação esférica como fundamento; não apresentá-la como descrição integral do SPA.'),
('EV004','east of south are negative','DIRETA_COM_RESTRICAO','Duffie usa origem no sul. Reda/Andreas usa norte e sentido horário; as convenções não são intercambiáveis sem conversão.','Usar A_s para o azimute adotado e explicitar A_s=(gamma_s+180 graus) mod 360 graus; no zênite a projeção horizontal e o azimute são indefinidos.'),
('EV005','at sea level','DIRETA_COM_RESTRICAO','A p. 9 limita explicitamente a aproximação secante a 0–70 graus e ao nível do mar; a p. 10 discute a curvatura terrestre para zenitais maiores.','Acrescentar nível do mar ao domínio didático. Distinguir massa relativa e correção de pressão; não extrapolar a secante ao horizonte.'),
('EV006','the true solar time','DIRETA_COM_RESTRICAO','NOAA relaciona tempo solar verdadeiro, equação do tempo, longitude e fuso. É uma aproximação diferente do SPA e usa 366 no ano bissexto.','Usar NOAA apenas como explicação do tempo solar; manter o denominador 365 do Spencer executado e não fundir os dois procedimentos.'),
('EV007','size of the solar disk','DIRETA_COM_RESTRICAO','NOAA fixa 90,833 graus para nascer/pôr, combinando refração e tamanho do disco. Esse limiar não é o horizonte geométrico do centro solar.','Explicitar disco solar e refração; manter max(0,cos zenital) como convenção geométrica do cálculo extraterrestre.'),
('EV008','measured from north and eastward','DIRETA','O resumo do artigo informa a mudança de origem azimutal e longitude positiva para leste.','Conservar norte 0 graus e sentido horário em figuras, código, configurações e texto.'),
('EV009','In this report we describe a procedure','DIRETA_COM_RESTRICAO','A p. 578 atribui incerteza angular ao SPA e explicita sensibilidade às escalas de tempo e DUT1. Não é uma avaliação do sensor PVDAQ.','Não transferir a incerteza publicada do algoritmo ao sensor, à irradiância nem ao caso com entradas padrão.'),
('EV010','without atmospheric refraction correction','DIRETA_COM_RESTRICAO','As equações 41–44, pp. 10–11, separam elevação sem refração, correção dependente de pressão/temperatura e elevação corrigida.','Manter zenital geométrico na projeção extraterrestre e declarar zenital aparente no cálculo de incidência adotado no projeto.'),
('EV011','Date = October 17, 2003','DIRETA','O exemplo A.5, p. A-15, fornece todos os parâmetros usados no teste, incluindo fuso fixo -7, pressão 820 mbar e deltaT 67 s.','Reproduzir o exemplo com 82000 Pa e o deslocamento UTC fixo publicado; não substituir pelo fuso civil atual de Denver.'),
('EV012','194.34024','DIRETA_COM_RESTRICAO','A Tabela A5.1, p. A-16, imprime zenital 50,11162 e azimute 194,34024 graus. Os resultados calculados coincidem ao arredondar a cinco casas.','Usar tolerância de 0,000005 grau, correspondente a meia unidade da última casa impressa; isso verifica implementação e arredondamento, não calibração.'),
('EV013','The Earth’s elliptical orbit','DIRETA','A equação 2-1 do handbook contém explicitamente o fator (r0/r)^2. O parâmetro solar do projeto é fixado para reprodutibilidade.','Manter Gsc=1366,1 W/m2 como parâmetro do software, sem denominá-lo uma determinação metrológica atual da constante solar.'),
('EV014','eastward from true north','DIRETA','A seção 2.4.1 confirma elevação e azimute topocêntricos e a convenção norte/leste. A indeterminação no zênite é consequência geométrica da projeção nula.','Distinguir definição documentada de consequência matemática; uniformizar A_s nas figuras.'),
('EV015','found by integration of irradiance','DIRETA_COM_DERIVACAO','Duffie define a integral temporal. A soma de médias por duração é derivação matemática sob a hipótese de que o registro representa média do intervalo.','Identificar E1.04 como forma discreta derivada; somar apenas intervalos válidos e não apresentar energia parcial como energia de toda a janela.'),
('EV016','three fundamental irradiance components','DIRETA','A seção 2.5 define DNI, DHI e GHI no espectro solar de onda curta e pelos respectivos campos angulares.','Acrescentar solar/onda curta quando o texto disser irradiância descendente total; distinguir a componente direta ideal da região angular do instrumento.'),
('EV017','fundamental expression called the closure equation','DIRETA_COM_RESTRICAO','A equação 2-2 contém a soma direta projetada mais difusa. A compatibilidade de banda, plano e suporte temporal é condição de aplicação às medidas.','Manter fechamento para o Sol acima do horizonte; um resíduo de medidas exige diagnóstico instrumental e temporal, sem atribuição automática.'),
('EV018','decomposition','DIRETA_COM_INFERENCIA','A p. 2-10 trata a separação de componentes como modelagem empírica. Driesse et al., pp. 9–11, distinguem o teste de inversão com GTI modelada do confronto com medidas.','Citar Driesse et al. no limite de identificação: reconvergência ao valor de entrada verifica consistência do procedimento, não valida componentes com observações independentes.'),
('EV019','radiation reflected from the ground','DIRETA','A introdução do capítulo 2 inclui a contribuição refletida quando está no campo de visão do coletor; a seção 2.5.1 detalha a recepção no plano inclinado.','Conservar a decomposição conceitual da POA e reservar os modelos de transposição e albedo às seções responsáveis.'),
('EV020','atmospheric path length or air mass','DIRETA_COM_RESTRICAO','A seção 2.4 relaciona percurso óptico e posição solar; a secante é uma aproximação para zenitais baixos.','Vincular ao domínio especificado em Duffie e separar caminho óptico, transmitância e irradiância.'),
('EV021','Scattering redistributes the radiation','DIRETA','A p. 2-7 distingue captura/absorção e redistribuição angular por espalhamento, inclusive retorno ao espaço.','Manter a distinção física; não interpretar espalhamento exclusivamente como energia perdida do sistema terrestre.'),
('EV022','the cloud enhancement phenomenon','DIRETA_COM_RESTRICAO','A seção 6.2.1 descreve rampas e intensificação local por geometria de nuvens, inclusive valores superiores à referência extraterrestre horizontal.','Não usar G0h como teto universal de observações de curta duração nem diagnosticar céu claro pela forma da G01.'),
('EV023','total column water vapor','DIRETA_COM_INFERENCIA','A seção 5.6 define AOD espectral e água precipitável integrada na coluna. A não equivalência com umidade relativa superficial decorre de mensurandos e dimensões diferentes.','Marcar essa não equivalência como inferência física da definição; não alegar medição de AOD/PW no PVDAQ a partir de POA.'),
('EV024','during a specific period','DIRETA','A introdução do capítulo 6 exige definir período e área antes de quantificar variabilidade.','Não generalizar o dia mostrado nem o trimestre para distribuição climatológica ou tendência de longo prazo.'),
('EV025','dependent on the irradiance component','DIRETA_COM_RESTRICAO','A p. 6-2 diferencia variabilidade entre componentes e descreve suavização espacial de rampas em áreas maiores.','Informar grandeza e escala; não transferir resultados de DNI instantânea a médias mensais de GHI.'),
('EV026','uncertainty when attempting to extrapolate solar resource data','DIRETA_COM_INFERENCIA','A seção 6.3 documenta heterogeneidade por nuvens, relevo e propriedades atmosféricas. A ausência de garantia de exatidão por pixel menor é inferência sobre os fatores do modelo.','Separar resolução nominal de exatidão e exigir comparação local; não apresentar uma relação monotônica universal resolução/erro.'),
('EV027','temporal variability is a direct function','DIRETA_COM_INFERENCIA','A seção 6.5 associa variabilidade representada à resolução. A interpolação simples não identifica, por si só, oscilações subintervalo desconhecidas.','Qualificar a frase sobre interpolação: ela não demonstra recuperação exata da variabilidade ausente sem hipóteses/informação adicionais.'),
('EV028','time-consuming and expensive','DIRETA','A seção 3.1 apresenta as medições locais como referência para modelos e enumera instalação, operação e manutenção.','Manter o papel das observações, sem presumir que todo registro local esteja calibrado ou isento de erros.'),
('EV029','Mounted in the plane of the PV module array','DIRETA_COM_RESTRICAO','A Tabela 3-1 distingue GHI, DHI, DNI e POA por montagem e campo de visão. Sistemas com sombra rotativa alternam observações e calculam DNI; não são três canais simultâneos independentes.','Restringir a afirmação a um sensor em uma montagem fixa; não excluir a existência de sistemas de medição alternada.'),
('EV030','very fast time-response characteristics','DIRETA','A p. 3-6 contrasta termopilhas e sensores fotoelétricos em resposta temporal e espectral.','Distinguir tecnologia de sensor de exatidão de campo; não atribuir ao sensor PVDAQ uma tecnologia não conferida em metadados.'),
('EV031','circumsolar region','DIRETA_COM_RESTRICAO','A seção 3.2.1.1 explicita rastreamento, colimação e contribuição circumsolar no campo de visão finito.','Não equiparar sem ressalva DNI instrumental a um feixe matemático de ângulo sólido nulo.'),
('EV032','flagging suspicious or erroneous data','DIRETA','O capítulo 4 distingue avaliação posterior dos dados e realimentação do controle operacional.','Registrar lacunas e flags; disponibilidade de uma média e completude das amostras são indicadores diferentes.'),
('EV033','especially when only a single radiometer exists locally','DIRETA_COM_RESTRICAO','A p. 4-15 relata dificuldades de QC de GTI/POA de campo, sobretudo com um radiômetro. É uma limitação, não impossibilidade de todo teste.','Escrever que a POA isolada restringe testes que exigem componentes independentes; preservar os controles de cadência e disponibilidade que continuam possíveis.'),
('EV034','Site-adaptation models have been used','DIRETA_COM_RESTRICAO','O capítulo 7 resume satélites e adaptação usando observações locais de curto prazo para ajustar séries longas.','Não pressupor que essa adaptação foi executada no estudo; descrevê-la como método disponível.'),
('EV035','reanalysis mode for historical time series','DIRETA','A p. 7-2 identifica ERA5/MERRA-2 como reanálises de modelos atmosféricos. A irradiância superficial é estimada, não uma estação em cada célula.','Manter distinção de origem; qualquer resolução ou desempenho numérico requer produto, versão e avaliação próprios.'),
('EV036','derives cloud optical properties','DIRETA','A p. 7-8 descreve duas etapas: propriedades de nuvens a partir de radiâncias e cálculo superficial por transferência radiativa.','Distinguir radiância orbital observada de irradiância superficial estimada.'),
('EV037','TMY data are not designed to provide meteorological extremes','DIRETA_COM_RESTRICAO','A p. 8-4 descreve concatenação de meses típicos e exclui o uso para um período histórico específico ou condições extremas de projeto.','Não chamar TMY de ano observado integral nem usá-lo para reconstituir abril–junho de 2024.'),
('EV038','the measurand has four general sources of uncertainty','DIRETA_COM_RESTRICAO','A seção 10.2 exige mensurando, unidade e incerteza, enumerando contribuições de instrumento, aquisição, ambiente e calibração.','Não usar completude, correlação ou uma métrica de erro como estimativa completa da incerteza; nenhuma incerteza do sensor foi calculada nesta seção.'),
('EV039','uncertainty in its input data','DIRETA_COM_RESTRICAO','A p. 10-6 enumera modelo, entradas, propagação, referência, variabilidade interanual e tendências. A quantificação depende de lugar e período.','Manter discussão conceitual e encaminhar a quantificação de desempenho à Seção 4, sem criar valores de incerteza não executados.')
]

def normalize(s):
    s=unicodedata.normalize('NFKD',s).lower()
    return re.sub(r'[^a-z0-9]+',' ',s).strip()

def produzir(root=ROOT,fontes_dir=None):
    root=Path(root);b=root/'bibliografia';E=json.loads((b/'Matriz_Evidencias.json').read_text())
    inv={r['codigo']:r for r in json.loads((b/'Inventario_Fontes_Conferidas.json').read_text())}
    details=[]
    for eid,anchor,classification,reason,change in PARECERES:
        row=next(x for x in E if x['id']==eid);source=inv[row['fonte']]
        check='registrado após leitura';pagehash=row['pagina_texto_sha256']
        if fontes_dir:
            import fitz
            candidates=list(Path(fontes_dir).rglob(source['arquivo']))
            assert candidates,'Fonte não localizada: '+source['arquivo']
            f=candidates[0]
            assert hashlib.sha256(f.read_bytes()).hexdigest()==row['arquivo_sha256'],eid+' fonte mudou'
            with fitz.open(f) as pdf:page=pdf[row['pagina_pdf']-1].get_text()
            assert normalize(anchor) in normalize(page),(eid,anchor)
            assert hashlib.sha256(page.encode()).hexdigest()==pagehash,eid+' página mudou'
            check='arquivo, página e trecho âncora conferidos'
        if row['fonte'] in ['B12','B23','B31','B32'] or eid in ['EV013','EV014']:
            confrontation='Duffie pp. 9–15, NOAA p. 1–2 e SPA pp. 10–11: comparar fórmulas, convenções e hipóteses; não são medições PVDAQ.'
        elif eid in ['EV015','EV016','EV017','EV018','EV019']:
            confrontation='Duffie p. 10; handbook cap. 2-9–2-11; Driesse et al. pp. 9–11 para o limite de validação da inversão.'
        elif row['subsecao']=='1.3':
            confrontation='Comparação entre definições do cap. 2, propriedades do cap. 5 e escalas do cap. 6 do mesmo handbook; não contabilizar como estudos independentes.'
        elif eid in ['EV028','EV029','EV030','EV031','EV032','EV033']:
            confrontation='Comparação entre definições radiométricas, Tabela 3-1, resposta do instrumento e limitações de QC do cap. 4; mesma coletânea.'
        else:
            confrontation='Comparação entre métodos do cap. 7, representatividade/TMY do cap. 8 e fontes de incerteza do cap. 10; mesma coletânea.'
        details.append(dict(id=eid,subsecao=row['subsecao'],fonte=row['fonte'],pagina_pdf=row['pagina_pdf'],pagina_impressa=row['pagina_impressa'],
            afirmacao_analisada=row['afirmacao_parafraseada'],trecho_ancora=anchor,classificacao=classification,parecer_analitico=reason,
            confronto=confrontation,consequencia_editorial=change,arquivo_sha256=row['arquivo_sha256'],pagina_texto_sha256=pagehash,
            verificacao_integridade=check,revisor='Leitura comparativa assistida por IA; não revisão por pares',data='2026-10-27'))
    assert len(details)==39 and len({r['id'] for r in details})==39
    (b/'Confronto_Cientifico_39_Evidencias.json').write_text(json.dumps(details,ensure_ascii=False,indent=2))
    with (b/'Confronto_Cientifico_39_Evidencias.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(details[0]));w.writeheader();w.writerows(details)
    summary={'evidencias_analisadas':39,'por_classificacao':dict(Counter(d['classificacao'] for d in details)),
      'sem_suporte_documental_detectado':0,'alteracoes':'Qualificações de domínio, origem de inferências, conversão azimutal e limite de validação da inversão.',
      'metodo':'Leitura de páginas e confronto com afirmações, equações e hipóteses; integridade automatizada não substitui o julgamento registrado.',
      'nao_implica':['leitura integral de todos os livros','revisão por pares','ProKnow-C integral','calibração do sensor PVDAQ']}
    (root/'documentacao/Resultado_Confronto_Cientifico.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
    return details,summary

def validar_registros(root=ROOT,fontes_dir=None):
    root=Path(root);rows=json.loads((root/'bibliografia/Confronto_Cientifico_39_Evidencias.json').read_text())
    assert len(rows)==39 and all(r['parecer_analitico'] and r['consequencia_editorial'] for r in rows)
    if fontes_dir:return produzir(root,fontes_dir)[1]
    return {'pareceres_de_leitura_registrados':len(rows),'nova_leitura_alegada':False,'verificacao_dos_PDFs_privados':'Forneça fontes_dir para conferir hashes, páginas e trechos do acervo autorizado.'}
if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--fontes',type=Path);args=p.parse_args()
    _,s=produzir(fontes_dir=args.fontes);print(json.dumps(s,ensure_ascii=False,indent=2))
