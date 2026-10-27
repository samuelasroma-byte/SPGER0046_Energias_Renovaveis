"""Apoio da Seção 1 em Beamer/PDF; não altera o PPTX coletivo de 29/10."""
from preparar_slides import manifest,beamer,t,a,latex_asset,FG,Y,A,F
import fitz,copy,json

def run():
    latex_asset('EQ_integracao',r'$\displaystyle H_{[t_1,t_2]}=\int_{t_1}^{t_2}G(t)\,\mathrm{d}t$')
    latex_asset('EQ_fechamento',r'$\displaystyle\mathrm{GHI}=\mathrm{DNI}\cos\theta_z+\mathrm{DHI}$')
    slides=copy.deepcopy(manifest())
    def add(title,sub,elements,source,notes):
        slides.append(dict(number=len(slides)+1,physical=len(slides)+1,title=title,subtitle=sub,elements=elements,source=source,notes=notes))
    add('1.2 · IRRADIÂNCIA E IRRADIAÇÃO','A irradiância é potência por área; a irradiação é energia por área.',[
      a('EQ_integracao',240,220,800,115),
      t('IRRADIÂNCIA G',75,385,510,45,35,Y,True),t('W/m²\nPlano e suporte temporal definidos.',75,445,510,100,32),
      t('IRRADIAÇÃO H',715,385,510,45,35,Y,True),t('J/m², Wh/m² ou kWh/m²\nIntervalo de integração declarado.',715,445,510,100,32),
      t('Médias de intervalo: somar G médio × duração, somente nos intervalos válidos.',75,590,1120,65,28,Y)
    ],'Fonte: Duffie, Beckman e Blair (2020), p. 10.','Distinguir amostras instantâneas, médias e energia acumulada. A soma dos intervalos disponíveis não reconstitui lacunas.')
    add('1.2 · COMPONENTES DA RADIAÇÃO','A unidade é comum; a direção e o plano de recepção são diferentes.',[
      a('EQ_fechamento',100,230,1080,80),
      t('DNI',75,380,210,45,35,Y,True),t('Direta normal à direção solar.',300,380,850,55,32),
      t('DHI',75,450,210,45,35,Y,True),t('Difusa recebida na horizontal.',300,450,850,55,32),
      t('GHI',75,520,210,45,35,Y,True),t('Global recebida na horizontal.',300,520,850,55,32),
      t('POA',75,590,210,45,35,Y,True),t('Irradiância no plano do arranjo.',300,590,850,55,32)
    ],'Fonte: Sengupta et al. (2024), cap. 2, p. 9–10; cap. 3, p. 5.','Equação para o Sol acima do horizonte, com definições radiométricas compatíveis. GHI/DNI/DHI reconstruídas da POA não são medições locais independentes.')
    add('1.3 · MODULAÇÃO ATMOSFÉRICA','Absorção e espalhamento modificam o campo radiativo.',[
      t('NUVENS',75,235,340,45,35,Y,True),t('Obstrução do feixe.\nRedistribuição difusa.\nVariações rápidas.',75,310,340,210,32),
      t('AEROSSÓIS',470,235,340,45,35,Y,True),t('Profundidade óptica.\nAbsorção e\nespalhamento.',470,310,340,210,32),
      t('VAPOR DE ÁGUA',865,235,350,45,35,Y,True),t('Absorção espectral.\nQuantidade integrada\nna coluna.',865,310,350,210,32),
      t('POA isolada não permite separar quantitativamente esses mecanismos.',75,575,1130,70,31,Y)
    ],'Fonte: Sengupta et al. (2024), cap. 2, p. 6–7; cap. 5, p. 10.','Não converter fundamento físico geral em atribuição causal específica do dia observado. Umidade relativa superficial e água precipitável são grandezas distintas.')
    add('1.3 · VARIABILIDADE E ESCALAS','A componente, o intervalo e o domínio espacial definem a análise.',[
      t('NO TEMPO',75,220,1120,45,35,Y,True),t('Ciclo diário, sazonalidade e variações meteorológicas.',75,280,1120,65,32),
      t('NO ESPAÇO',75,370,1120,45,35,Y,True),t('Nuvens e relevo limitam a extrapolação entre localidades.',75,430,1120,65,32),
      t('NA RESOLUÇÃO',75,520,1120,45,35,Y,True),t('Médias temporais suavizam flutuações; um dia não estabelece climatologia.',75,580,1120,65,31)
    ],'Fonte: Sengupta et al. (2024), cap. 6, p. 1–2, 17 e 24–25.','O estudo PVDAQ cobre 91 dias de 2024. Não extrapolar a amostra para distribuição anual ou mecanismos climáticos sem dados adicionais.')
    add('1.4 · MEDIÇÃO E ESTIMATIVA','Cada fonte caracteriza o recurso com suporte e limites próprios.',[
      t('SUPERFÍCIE',75,225,300,45,34,Y,True),t('Instrumento, plano, calibração e manutenção.',405,225,800,60,31),
      t('SATÉLITE',75,320,300,45,34,Y,True),t('Observação orbital e modelo para a superfície.',405,320,800,60,31),
      t('REANÁLISE',75,415,300,45,34,Y,True),t('Modelo atmosférico com assimilação de observações.',405,415,800,60,31),
      t('ATLAS',75,510,300,45,34,Y,True),t('Síntese espacial de um indicador e período definidos.',405,510,800,60,31),
      t('Estimativas em grade requerem avaliação de representatividade local.',75,605,1120,40,29,Y)
    ],'Fonte: Sengupta et al. (2024), cap. 3, p. 3–7; cap. 7, p. 1–3 e 8.','Um pixel não é uma estação; um atlas não é necessariamente uma fonte independente da base que o compõe. A interpretação depende do produto e de sua versão.')
    add('1.4 · REPRESENTATIVIDADE E INCERTEZA','Comparar exige compatibilizar o que foi observado ou estimado.',[
      t('GRANDEZA E PLANO',75,220,1120,45,34,Y,True),t('POA, GHI, DNI e DHI mantêm definições distintas.',75,275,1120,55,32),
      t('TEMPO E AMOSTRA',75,365,1120,45,34,Y,True),t('Fuso, rótulo, integração, lacunas e intervalos comuns.',75,420,1120,55,32),
      t('FONTES DE INCERTEZA',75,510,1120,45,34,Y,True),t('Instrumento, entradas, modelo e referência de avaliação.',75,565,1120,55,32)
    ],'Fonte: Sengupta et al. (2024), cap. 4, p. 1; cap. 10, p. 5–6.','Completude e incerteza são indicadores diferentes. A Seção 1 entrega entradas e limites às etapas de ambiente, conversão e desempenho, sem desenvolver o conteúdo dos colegas.')
    for n,s in enumerate(slides,1):
        s['number']=n;s['physical']=n
        if n<=6:continue
        for e in s['elements']:
            if e['kind']=='asset':
                with fitz.open(F/(e['name']+'.pdf')) as d:ratio=d[0].rect.width/d[0].rect.height
                w=min(e['w'],e['h']*ratio);h=w/ratio;e['x']+=(e['w']-w)/2;e['y']+=(e['h']-h)/2;e['w']=w;e['h']=h
    (A/'Conteudo_Secao_01.json').write_text(json.dumps(slides,ensure_ascii=False,indent=2))
    beamer(slides,'Materiais_Apresentacao_Secao_01')
    # Mantém o PDF de 29/10 com seis quadros e a numeração do arquivo coletivo.
    beamer(manifest())
if __name__=='__main__':run()
