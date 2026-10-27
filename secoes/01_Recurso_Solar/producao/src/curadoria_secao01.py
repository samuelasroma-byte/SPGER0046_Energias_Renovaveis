"""Curadoria localizada reaproveitando o portfólio B e sem repetir buscas bibliométricas."""
from pathlib import Path
import json,csv,hashlib,re
import fitz

ROOT=Path(__file__).resolve().parents[1]
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()

# Afirmações parafraseadas após cotejo das páginas; não são saídas de um classificador.
EVIDENCIAS=[
 ('1.1','B12',27,'9','A distância Terra–Sol modifica a irradiância extraterrestre normal.','Distância e E0','W/m²','Leitura localizada; coeficiente de Spencer cotejado com o código.','1.1.3; slide 7'),
 ('1.1','B12',31,'13','Zenital é contado desde a vertical; elevação é seu complemento.','E1.01; D01','graus','Esquema geométrico; sem refração.','1.1.2; slide 5'),
 ('1.1','B12',33,'15','A relação esférica liga latitude, declinação e ângulo horário ao zenital.','E1.01','graus/radianos','A equação elementar não substitui todos os termos do SPA.','1.1.2; slide 6'),
 ('1.1','B12',31,'13','O livro adota origem azimutal no sul, com sinais distintos da convenção SPA.','Convenções','graus','Conversão de origem explicitada; não transcrever convenções como equivalentes.','1.1.2; D01'),
 ('1.1','B12',27,'9','A aproximação secante da massa de ar é apresentada para zenitais até cerca de 70°.','Massa de ar','adimensional','Não extrapolar ao horizonte.','1.1.4'),
 ('1.1','B23',1,'1','O tempo solar verdadeiro depende de longitude, fuso e equação do tempo.','Tempo e ângulo horário','min; h; graus','Algoritmo aproximado; não é a implementação SPA utilizada.','1.1.2; roteiro oral'),
 ('1.1','B23',2,'2','A formulação de nascer e pôr do Sol acrescenta uma correção aproximada ao horizonte.','Horizonte','graus','Critério de horizonte aparente difere do recorte geométrico de G0h.','1.1.3'),
 ('1.1','B31',1,'577','O artigo SPA explicita azimute desde o norte e longitude positiva para leste.','SPA e orientação','graus','Convenção utilizada no capítulo.','1.1.2; slides 5 e 8'),
 ('1.1','B31',2,'578','A precisão angular atribuída ao SPA se refere ao cálculo de posição solar.','Escopo do algoritmo','graus','Não representa a incerteza de um sensor de irradiância.','1.1.2; 1.1.7'),
 ('1.1','B32',16,'10','O tratamento topocêntrico distingue elevação sem e com refração.','Zenital geométrico/aparente','graus','Refração depende de pressão e temperatura; continuação na p. 11/PDF17.','1.1.2; 1.1.7'),
 ('1.1','B32',37,'A-15','O exemplo numérico informa data, fuso, localização, pressão, altitude, temperatura e ΔT.','Teste SPA','unidades de entrada declaradas','Exemplo de implementação; não é observação PVDAQ.','Conferencia_Calculos.json'),
 ('1.1','B32',38,'A-16','A continuação da Tabela A5.1 apresenta zenital e azimute usados na conferência numérica.','Teste SPA','graus','Comparação com os valores arredondados da tabela.','Conferencia_Calculos.json'),
 ('1.1','A045',34,'cap. 2-5','A referência extraterrestre varia com o inverso do quadrado da distância.','G0n','W/m²','Não equivale à irradiância de superfície.','1.1.3; slide 7'),
 ('1.1','A045',37,'cap. 2-8','A orientação solar local inclui elevação e azimute horário a partir do norte.','D01','graus','Azimute indefinido no zênite é uma consequência geométrica.','1.1.2; slide 5'),
 ('1.2','B12',28,'10','Irradiação é obtida pela integração temporal da irradiância.','E1.03 e E1.04','W/m²; J/m²','A soma utiliza a duração e o significado dos registros.','1.2.1'),
 ('1.2','A045',38,'cap. 2-9','DNI, DHI e GHI diferem pelo campo angular e pelo plano de recepção.','Componentes','W/m²','Grandezas do campo radiativo descendente.','1.2.2'),
 ('1.2','A045',39,'cap. 2-10','A equação de fechamento soma direta projetada e difusa horizontal.','E1.05','W/m²','Medições precisam ser compatíveis em banda, campo angular e tempo.','1.2.2'),
 ('1.2','A045',39,'cap. 2-10','DNI e DHI estimadas a partir de GHI dependem de modelos de separação.','Decomposição','W/m²','Não constituem medições adicionais independentes.','1.2.2'),
 ('1.2','A045',30,'cap. 2-1','Superfícies fotovoltaicas podem receber contribuições descendentes e refletidas.','POA','W/m²','Modelos de transposição pertencem à subseção 3.1.','1.2.3'),
 ('1.3','A045',35,'cap. 2-6','A atmosfera atua sobre a radiação ao longo de um percurso dependente da posição solar.','Massa de ar e atenuação','adimensional','A secante é uma aproximação limitada.','1.3.1'),
 ('1.3','A045',36,'cap. 2-7','Absorção e espalhamento têm efeitos físicos distintos sobre o campo radiativo.','Modulação atmosférica','qualitativo','Redistribuição angular não equivale à absorção.','1.3.1'),
 ('1.3','A045',245,'cap. 6-2','Nuvens produzem rampas e podem causar intensificação local de curta duração.','Variabilidade por nuvens','escala sub-horária','Não classificar céu claro apenas pela forma de POA.','1.2.3; 1.3.2'),
 ('1.3','A045',202,'cap. 5-10','Aerossóis e vapor de água são descritos por propriedades ópticas e quantidades de coluna.','AOD; água precipitável','propriedades espectrais/coluna','Umidade relativa superficial não substitui água precipitável.','1.3.3'),
 ('1.3','A045',244,'cap. 6-1','A variabilidade deve ser definida em relação ao intervalo temporal e à área.','Variabilidade','tempo e espaço declarados','Não generalizar um dia para climatologia.','1.3.4'),
 ('1.3','A045',245,'cap. 6-2','A variabilidade depende da componente de irradiância e da escala de análise.','DNI/GHI/GTI','W/m² e escalas','Agregação espacial pode suavizar oscilações rápidas.','1.3.4'),
 ('1.3','A045',260,'cap. 6-17','Nuvens, relevo e fatores locais limitam extrapolações espaciais do recurso.','Representatividade','domínio espacial','Pixel menor não garante, sozinho, maior exatidão.','1.3.4; 1.4.3'),
 ('1.3','A045',267,'cap. 6-24','A resolução temporal afeta a variabilidade que pode ser representada na série.','Agregação temporal','s; min; h','Interpolação não recupera variabilidade não observada.','1.3.2; 1.4.3'),
 ('1.4','A045',58,'cap. 3-3','Medições locais apoiam avaliação do recurso e conferência de modelos.','Observações de superfície','mensurando declarado','Existem custos de instalação, operação e manutenção.','1.4.1'),
 ('1.4','A045',60,'cap. 3-5','A montagem e o campo de visão distinguem medidas GHI, DHI, DNI e POA.','Instrumentação','W/m²; plano de montagem','Um sensor não mede todas as componentes simultaneamente.','1.4.1'),
 ('1.4','A045',61,'cap. 3-6','Termopilhas e sensores fotoelétricos têm respostas espectrais e temporais diferentes.','Resposta de sensores','s e banda espectral','A especificação nominal não encerra a incerteza de campo.','1.4.1'),
 ('1.4','A045',62,'cap. 3-7','Pireliômetros requerem alinhamento com o Sol e possuem campo de visão limitado.','Medição DNI','ângulo/campo de visão','Inclui uma região circumsolar conforme o instrumento.','1.2.2; 1.4.1'),
 ('1.4','A045',161,'cap. 4-1','Avaliação e controle de qualidade tratam dados suspeitos e realimentam a operação.','Qualidade','flags e registros','Completude não é sinônimo de exatidão.','1.4.4'),
 ('1.4','A045',175,'cap. 4-15','Uma única medição inclinada impõe limitações ao controle de qualidade radiométrico.','POA e QC','W/m²','Ausência de referências independentes limita o diagnóstico.','1.4.4'),
 ('1.4','A045',285,'cap. 7-1','Modelos de satélite e adaptação local ampliam a caracterização do recurso.','Estimativa remota','resolução e grandeza declaradas','Irradiância de superfície é saída de modelagem.','1.4.2'),
 ('1.4','A045',286,'cap. 7-2','Reanálises produzem séries históricas de GHI a partir de sistemas atmosféricos.','Reanálise','produto e versão declarados','Não representam estações radiométricas em cada ponto.','1.4.2'),
 ('1.4','A045',292,'cap. 7-8','Modelos físicos de satélite podem recuperar nuvens e usar transferência radiativa.','Satélite','entradas e saídas documentadas','Não tratar a estimativa superficial como leitura direta do sensor orbital.','1.4.2'),
 ('1.4','A045',325,'cap. 8-4','Um ano meteorológico típico é uma construção estatística com finalidade própria.','TMY e representatividade','ano sintético','Não reconstitui um período histórico específico nem preserva todos os extremos.','1.3.4; 1.4.2'),
 ('1.4','A045',444,'cap. 10-5','Incerteza depende do mensurando e de contribuições da medição e da calibração.','Incerteza','mensurando e unidade','Uma métrica de erro não resume toda a incerteza.','1.4.4'),
 ('1.4','A045',445,'cap. 10-6','Modelos, entradas, propagação e referência contribuem para a incerteza estimada.','Incerteza de modelos','domínio de avaliação','Contribuições podem depender do local e período.','1.4.4')
]

def run(root=ROOT,source_root=None):
    root=Path(root);out=root/'bibliografia';out.mkdir(exist_ok=True)
    portfolio=json.loads((out/'Manifesto_Corpus_Secao_01.json').read_text())
    specs={
      'B12':('B12_A001_Duffie_Beckman_Blair_2020_5ed.pdf','https://doi.org/10.1002/9781119540328'),
      'B23':('insumos/B23_A082_NOAA_Calculo_Posicao_Solar.pdf','https://gml.noaa.gov/grad/solcalc/solareqns.PDF'),
      'B31':('insumos/B31_Reda_Andreas_2004_SPA.pdf','https://doi.org/10.1016/j.solener.2003.12.003'),
      'B32':('SPA_Reda_Andreas_2008.pdf','https://doi.org/10.2172/15003974'),
      'A045':('A045_Sengupta_2024_4ed_Apoio_A.pdf','https://docs.nrel.gov/docs/fy24osti/88300.pdf'),
      'A003':('A003_Jager_2014_Fundamentos_Solares_obra_distinta_B19.pdf','ISBN/edição do arquivo disponível; não usada como evidência')}
    oldinv=out/'Inventario_Fontes_Conferidas.json'
    inventory=json.loads(oldinv.read_text()) if oldinv.exists() else []
    byid={x['codigo']:x for x in inventory}
    if source_root:
        for code,(name,url) in specs.items():
            path=Path(source_root)/name
            with fitz.open(path) as d:
                pages=sorted({r[2] for r in EVIDENCIAS if r[1]==code})
                byid[code]={'codigo':code,'arquivo':path.name,'sha256':sha(path),'paginas_pdf':len(d),'paginas_verificadas':pages,
                  'leitura_integral':code=='B23','status_leitura':'integral' if code=='B23' else ('localizada' if pages else 'não lida'),
                  'fonte':url,'uso':'complementar não utilizado' if code=='A003' else 'evidência localizada'}
        inventory=list(byid.values());oldinv.write_text(json.dumps(inventory,ensure_ascii=False,indent=2))
    rows=[]
    for i,(sec,code,page,printed,claim,eq,unit,limit,dest) in enumerate(EVIDENCIAS,1):
        src=byid.get(code)
        if not src:raise ValueError('Inventário rastreável ausente: '+code)
        pagehash=''
        if source_root:
            path=Path(source_root)/specs[code][0]
            with fitz.open(path) as d:
                text=d[page-1].get_text()
                assert len(text.strip())>60,(code,page)
                pagehash=hashlib.sha256(text.encode()).hexdigest()
        rows.append(dict(id=f'EV{i:03}',subsecao=sec,fonte=code,pagina_pdf=page,pagina_impressa=printed,
          afirmacao_parafraseada=claim,equacao_figura_conceito=eq,unidades_convencoes=unit,limites=limit,
          destino=dest,arquivo_sha256=src['sha256'],pagina_texto_sha256=pagehash,status='CONFERIDA_LOCALIZADA',
          natureza='síntese bibliográfica',revisao='cotejo assistido por IA em 27/10/2026',leitura_integral=src['leitura_integral'],url=src['fonte']))
    # Reexecução sem PDFs conserva os hashes de páginas já conferidas, sem inventar uma nova leitura.
    old=out/'Matriz_Evidencias.json'
    if not source_root and old.exists():
        earlier={x['id']:x for x in json.loads(old.read_text())}
        for row in rows:row['pagina_texto_sha256']=earlier.get(row['id'],{}).get('pagina_texto_sha256','')
    old.write_text(json.dumps(rows,ensure_ascii=False,indent=2))
    with (out/'Matriz_Evidencias.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=rows[0].keys());w.writeheader();w.writerows(rows)
    decisions=[]
    selected={'B12','B23','B29','B31','B32'}
    for code,item in portfolio['refs'].items():
        if code in selected:decision='prioritária; leitura localizada' if code!='B23' else 'complementar; leitura integral de 2 páginas'
        elif code in {'B19','B20'}:decision='pendente; edição exata ausente'
        elif code=='B24':decision='dados preparados conferidos; metadados DOI herdados'
        elif code=='B26':decision='contexto online conferido; fora da fundamentação principal'
        elif code=='B27':decision='documentação catalogada; leitura pendente'
        elif code=='B11':decision='complementar; foco em transposição da subseção 3.1; leitura pendente'
        else:decision='PDF da 3ª edição disponível; leitura pendente; não confundir com A045/2024'
        decisions.append({'codigo':code,'autor_ano':item['author_year'],'edicao':item['edition'],'selecao':decision,
          'integral_disponivel':item['access_status'],'paginas_verificadas':','.join(map(str,byid.get(code,{}).get('paginas_verificadas',[]))),
          'papel':'fundamento de afirmações verificadas' if code in selected else 'complemento/contexto/pendência',
          'limite':item.get('note',''),'fonte':item.get('source_url','')})
    decisions.append({'codigo':'A045','autor_ano':'Sengupta et al. (ed.), 2024','edicao':'4ª edição; NREL/TP-5D00-88300',
      'selecao':'prioritária complementar; leitura localizada','integral_disponivel':'PDF disponível e conferido localmente',
      'paginas_verificadas':','.join(map(str,byid['A045']['paginas_verificadas'])),'papel':'atmosfera, componentes, medição e incertezas',
      'limite':'não substitui silenciosamente a referência B36/2021','fonte':byid['A045']['fonte']})
    decisions.append({'codigo':'A003','autor_ano':'Jäger et al., 2014','edicao':'obra distinta de B19 e B20','selecao':'disponível; não lida; não utilizada como prova',
      'integral_disponivel':'PDF disponível','paginas_verificadas':'','papel':'complemento potencial','limite':'não resolve falta das edições B19/B20','fonte':''})
    (out/'Selecao_Critica.json').write_text(json.dumps(decisions,ensure_ascii=False,indent=2))
    summary={'metodo':'revisão estruturada inspirada no ProKnow-C, com síntese crítica integrativa',
      'revisao_sistematica_integral_concluida':False,'buscas_bibliometricas_reexecutadas':False,
      'carteira_B_herdada':12,'associacoes_B_subsecoes_herdadas':23,'fontes_documentais_PDF_inventariadas':len(inventory),
      'PDFs_com_leitura_localizada_ou_integral':sum(bool(x['paginas_verificadas']) for x in inventory),
      'evidencias_bibliograficas_conferidas':len(rows),'referencias_complementares_adicionadas':['A045','A003'],
      'criterios':['pertinência à pergunta da subseção','conteúdo acessível para conferência','identidade e edição corretas','método e limites explícitos','fonte primária para algoritmo ou implementação'],
      'pendencias':['B19 e B20: edições exatas ausentes','B11 e B36/2021: leitura ainda pendente','B27: documentação não lida','verificação do registro DOI B24 bloqueada pela recuperação web; dados preparados conferidos','protocolo de busca completo anterior e contagens de reconhecimento científico não reexecutados ou inferidos'],
      'parecer':'Fundamentação localizada suficiente para a redação atual; não representa conclusão integral das etapas ProKnow-C.'}
    (out/'Status_Revisao.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2))
    return rows,decisions,summary
if __name__=='__main__':
    import sys
    _,_,s=run(source_root=sys.argv[1] if len(sys.argv)>1 else None);print(json.dumps(s,ensure_ascii=False,indent=2))
