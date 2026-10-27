"""Uma fonte de conteúdo para Beamer e transferência editorial ao PPTX."""
from pathlib import Path
import json,subprocess,html
import fitz
from concurrent.futures import ThreadPoolExecutor

ROOT=Path(__file__).resolve().parents[1]
A=ROOT/'apresentacao';F=ROOT/'figuras'
BG='000000';FG='FFFFFF';Y='FFD45C';C='70DCF5'

def latex_asset(stem,body,preamble=''):
    tex=r'''\documentclass[border=3pt]{standalone}
\usepackage{amsmath,amssymb,xcolor,fontspec,tikz}
\usetikzlibrary{arrows.meta,angles,quotes,positioning}
\setmainfont{NimbusRoman-Regular.otf}[Path=/usr/share/fonts/opentype/urw-base35/,BoldFont=NimbusRoman-Bold.otf,ItalicFont=NimbusRoman-Italic.otf,BoldItalicFont=NimbusRoman-BoldItalic.otf]
\definecolor{fg}{HTML}{FFFFFF}\definecolor{bg}{HTML}{000000}
\definecolor{yel}{HTML}{FFD45C}\definecolor{cya}{HTML}{70DCF5}
'''+preamble+'\n\\begin{document}\n\\pagecolor{bg}\\color{fg}\n'+body+'\n\\end{document}\n'
    (F/(stem+'.tex')).write_text(tex)
    p=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error','-output-directory',str(F),str(F/(stem+'.tex'))],capture_output=True,text=True)
    if p.returncode:raise RuntimeError(p.stdout[-2300:])
    subprocess.run(['pdftocairo','-svg',str(F/(stem+'.pdf')),str(F/(stem+'.svg'))],check=True,capture_output=True)
    subprocess.run(['pdftocairo','-png','-singlefile','-r','300',str(F/(stem+'.pdf')),str(F/stem)],check=True,capture_output=True)

def assets():
    F.mkdir(exist_ok=True)
    eqs={
      'EQ_zenital':r'$\displaystyle\cos\theta_z=\sin\phi\,\sin\delta+\cos\phi\,\cos\delta\,\cos\omega$',
      'EQ_elevacao':r'$\displaystyle\alpha_s=90^{\circ}-\theta_z$',
      'EQ_horario':r'$\displaystyle\omega=15^{\circ}\!\left(\frac{t_{\rm sol}}{1\,\mathrm{h}}-12\right)$',
      'EQ_distancia':r'$\displaystyle G_{0n}=G_{\rm sc}\left(\frac{r_0}{r}\right)^2=G_{\rm sc}E_0$',
      'EQ_spencer':r'$\displaystyle\begin{aligned}E_0={}&1{,}000110+0{,}034221\cos B+0{,}001280\sin B\\&+0{,}000719\cos(2B)+0{,}000077\sin(2B)\end{aligned}$',
      'EQ_projecao':r'$\displaystyle G_{0h}=G_{0n}\,\max\!\left(0,\cos\theta_z\right)$'
    }
    pool=ThreadPoolExecutor(max_workers=3)
    jobs=[pool.submit(latex_asset,s,b) for s,b in eqs.items()]
    geo=r'''\begin{tikzpicture}[x=1cm,y=1cm,>=Stealth,font=\large]
\path[fill=bg](-.9,-1.35)rectangle(10.7,4.7);
\node[fg,font=\bfseries\large] at (2,4.35){CORTE VERTICAL};
\draw[fg,->,thick](-.45,0)--(4.4,0)node[below left]{horizontal};
\draw[fg,->,thick](0,-.2)--(0,3.8)node[right]{zênite};
\draw[yel,->,very thick](0,0)--(2.35,3.55)node[above right]{Sol};
\draw[yel,thick](.8,0)arc[start angle=0,end angle=56.5,radius=.8];
\node[yel] at (1.1,.43){$\alpha_s$};
\draw[cya,thick](0,1.4)arc[start angle=90,end angle=56.5,radius=1.4];
\node[cya] at (.55,1.73){$\theta_z$};
\fill[fg](0,0)circle(.055);\node[fg,below right]at(0,-.35){observador};
\node[fg,font=\bfseries\large] at (7.95,4.35){VISTA EM PLANTA};
\begin{scope}[shift={(7.8,1.35)}]
\draw[fg,->,thick](0,-1.65)--(0,1.8)node[above]{N};
\draw[fg,->,thick](-1.8,0)--(1.95,0)node[right]{L};
\node[fg,below]at(0,-1.65){S};\node[fg,left]at(-1.8,0){O};
\draw[yel,->,very thick](0,0)--(1.6,-.95);
\draw[yel,->,thick](0,.95)arc[start angle=90,end angle=-30,radius=.95];
\node[yel]at(1.25,.65){$A_s$};
\end{scope}
\node[fg] at (7.9,-1.0){azimute desde N, horário};
\end{tikzpicture}'''
    latex_asset('D01_geometria',geo)
    flow=r'''\begin{tikzpicture}[x=1cm,y=1cm,>=Stealth,font=\large,
 box/.style={draw=fg,thick,text=fg,align=center,minimum height=1.9cm,text width=3.35cm,inner sep=8pt}]
\path[fill=bg](-.35,-1.45)rectangle(14.8,4.35);
\node[box,minimum height=4.2cm] (in) at(1.8,1.35){\textcolor{yel}{\textbf{LOCAL E TEMPO}}\\[9pt]38,996306° N\\122,134111° O\\altitude: 10 m\\[6pt]data, hora e fuso};
\node[box] (spa) at(7.1,2.65){\textcolor{yel}{\textbf{SPA}}\\[5pt]$\theta_z$, $\alpha_s$, $A_s$};
\node[box] (sp) at(7.1,0){\textcolor{yel}{\textbf{SPENCER}}\\[5pt]$G_{0n}(n)$};
\node[box,minimum height=2.7cm] (out) at(12.6,1.35){\textcolor{yel}{\textbf{PROJEÇÃO}}\\[9pt]$G_{0h}=$\\$G_{0n}\max(0,\cos\theta_z)$};
\draw[cya,->,very thick](in.east)--++(.55,0)|-(spa.west);
\draw[cya,->,very thick](in.east)--++(.55,0)|-(sp.west);
\draw[cya,->,very thick](spa.east)--++(.6,0)|-(out.west);
\draw[cya,->,very thick](sp.east)--++(.6,0)|-(out.west);
\end{tikzpicture}'''
    latex_asset('D02_fluxo_geometria',flow)
    for j in jobs:j.result()
    pool.shutdown()

def t(text,x,y,w,h,size=30,color=FG,bold=False):return dict(kind='text',text=text,x=x,y=y,w=w,h=h,size=size,color=color,bold=bold)
def a(name,x,y,w,h):return dict(kind='asset',name=name,x=x,y=y,w=w,h=h)

def manifest():
    slides=[]
    def add(title,subtitle,els,source,note):
        i=len(slides);slides.append(dict(number=i+4,physical=i+5,title=title,subtitle=subtitle,elements=els,source=source,notes=note))
    add('1.1 · GEOMETRIA SOLAR','A direção do Sol organiza a projeção do feixe direto.',[
      a('D01_geometria',55,215,710,365),
      t('Ângulo zenital',800,220,410,45,33,Y,True),t('Da vertical até a direção do Sol.',800,265,410,80),
      t('Elevação solar',800,365,410,45,33,Y,True),t('Da horizontal até a direção do Sol.',800,410,410,80),
      a('EQ_elevacao',810,505,365,52),
      t('Norte 0° · Leste 90° · Sul 180° · Oeste 270°',65,595,1150,40,28,Y)
    ],'Fontes: Duffie, Beckman e Blair (2020), p. 13; Sengupta et al. (2024), cap. 2, p. 8.',
    'Definir a direção solar sem confundir direção com fluxo medido. O esquema é didático e não representa uma observação. θz é contado da vertical e αs da horizontal. A vista em planta define A_s, azimute horário desde o norte. No livro Duffie, γ_s parte do sul, negativo para leste e positivo para oeste: A_s=(γ_s+180°) mod 360°. No zênite o azimute é indefinido. Fontes verificadas: B12 p. 13/PDF31; A045 cap. 2-8/PDF37.')
    add('1.1 · RELAÇÃO DO ÂNGULO ZENITAL','Relação esférica para a direção solar geométrica.',[
      a('EQ_zenital',80,220,1120,80),
      t('φ — latitude',75,350,335,45,34,Y,True),t('Posição do observador;\nnorte positivo.',75,405,335,85),
      t('δ — declinação',460,350,335,45,34,Y,True),t('Posição solar em relação\nao equador celeste.',460,405,335,85),
      t('ω — ângulo horário',850,350,360,45,34,Y,True),t('Rotação em relação\nao meio-dia solar.',850,405,360,85),
      a('EQ_horario',75,510,570,90),
      t('Manhã: ω < 0°\nTarde: ω > 0°',695,520,475,85,30),
      t('Ângulos em graus na exposição; conversão para radianos no código.',75,610,1130,35,26,Y)
    ],'Fontes: Duffie, Beckman e Blair (2020), p. 13–15; Reda e Andreas (2008), p. 10–11.',
    'A equação relaciona latitude, declinação e ângulo horário e expressa a trigonometria esférica. ω=0 no meio-dia solar, que não coincide necessariamente com 12h civis. A notação t_sol está em horas de tempo solar verdadeiro; ω=15°(t_sol/1h−12). Não misturar graus e radianos em sin/cos. Esta equação elementar não inclui refração; no SPA zenith e apparent_zenith são saídas distintas. Fontes: B12 pp.13–15/PDF31–33; B32 pp.10–11/PDF16–17.')
    add('1.1 · IRRADIÂNCIA EXTRATERRESTRE','Referência radiativa anterior à interação com a atmosfera.',[
      a('EQ_distancia',65,195,700,75),t('Gsc = 1 366,1 W m⁻²\nValor fixado no pvlib do projeto.',820,190,390,85,28),
      a('EQ_spencer',100,300,1080,110),
      t('B = 2π(n − 1)/365; n = dia do ano; B em radianos.',100,430,1090,38,28,Y),
      a('EQ_projecao',230,500,820,65),
      t('G₀h é referência extraterrestre; GHI é irradiância na superfície.',70,600,1140,40,29,Y)
    ],'Fontes: Duffie, Beckman e Blair (2020), p. 9; pvlib 0.16.1, get_extra_radiation.',
    'O inverso do quadrado relaciona a irradiância normal à distância Terra–Sol. Spencer aproxima o fator orbital E0; não calcula nuvens, absorção nem radiação difusa. Aqui Gsc=1366,1 W/m² é uma constante de compatibilidade da implementação, não uma nova determinação metrológica da constante solar. O coeficiente de cos(2B) é 0,000719 conforme código conferido do pvlib 0.16.1; o exemplar B12 apresenta 0,00719 na equação 1.4.1b, divergência registrada na conferência. A projeção usa o zenital geométrico e é anulada com o Sol abaixo do horizonte. O ano 2024 é bissexto, mas o denominador 365 é mantido para reproduzir o método do projeto.')
    add('1.1 · IMPLEMENTAÇÃO COMPUTACIONAL','SPA e Spencer recebem entradas temporais e cumprem funções distintas.',[
      a('D02_fluxo_geometria',95,200,1090,370),
      t('Rótulo = início · Δt = 15 min · cálculo em t + 7 min 30 s',80,575,1140,40,29,Y),
      t('Em 17/05/2024: America/Los_Angeles = UTC−7.',80,620,1140,36,28)
    ],'Fontes: configuração do projeto PVDAQ 2107; Reda e Andreas (2008); pvlib 0.16.1.',
    'Mostrar as duas ramificações: localização e instante alimentam o SPA; o dia do ano alimenta Spencer; zenital e G0n entram na projeção. Não há dependência conceitual de Spencer em relação ao SPA. POA representa médias de 15 minutos, rotuladas pelo início; os ângulos são calculados 7min30s depois. A pressão é estimada da altitude de 10 m; temperatura de refração 12°C e ΔT=67s são padrões de compatibilidade mantidos do projeto. São parâmetros do cálculo, não medições atmosféricas. A comparação com o exemplo publicado do SPA verifica a implementação, e não valida os sensores do PVDAQ.')
    add('1.1 · PVDAQ 2107 EM 17/05/2024','Arbuckle, Califórnia · 38,996306° N; 122,134111° O · 10 m',[
      a('G01_recurso_geometria_escuro',50,195,795,445),
      t('POA medida',885,225,335,42,33,Y,True),t('Média em intervalos\nde 15 minutos.',885,275,335,83),
      t('Ângulos calculados',885,385,335,45,33,Y,True),t('SPA e orientação\ndo arranjo.',885,435,335,83),
      t('Inclinação: 25°\nAzimute: 180°',885,545,335,85,30)
    ],'G01 — Fonte: POA/PVDAQ 2107 e cálculos SPA da equipe. Curvas no ponto médio; sem interpolação.',
    'A POA é observacional; os ângulos são calculados. A janela do gráfico é 05h–21h locais; o CSV preserva as 96 posições do dia. Há 94 médias POA não ausentes e 68 intervalos com três amostras originais. Não preencher lacunas. A incidência utiliza zenital aparente e orientação 25°/180°, conforme a configuração coletiva, enquanto a projeção extraterrestre usa zenital geométrico. Não interpretar o máximo próximo do meio-dia como validação independente do SPA nem declarar céu claro apenas pela forma da curva. Os dados são um exemplo diário de abril–junho/2024; não estabelecem climatologia ou efeito atmosférico causal. GHI/DNI/DHI locais independentes não estão disponíveis nesta seleção. Fontes: CSV observado preparado, configuração vigente, B32.')
    add('1.1 · SÍNTESE E LIMITES','A geometria estabelece o referencial para caracterizar o recurso solar.',[
      t('A GEOMETRIA FORNECE',75,210,1130,45,34,Y,True),t('Direção solar, duração do dia e fator de projeção do feixe.',75,265,1130,50,32),
      t('A ATMOSFERA MODIFICA',75,350,1130,45,34,Y,True),t('Transmissão, absorção e espalhamento da radiação.',75,405,1130,50,32),
      t('A OBSERVAÇÃO PERMITE CONFRONTAR',75,490,1130,45,34,Y,True),t('Irradiância no plano do sensor e evolução temporal medida.',75,545,1130,50,32),
      t('1.2 — Irradiância e irradiação; componentes GHI, DNI, DHI e POA.',75,615,1130,35,27,Y)
    ],'Fontes: Duffie, Beckman e Blair (2020), p. 9–15; Sengupta et al. (2024), cap. 2, p. 5–10.',
    'Retomar a distinção entre referência geométrica e irradiância efetiva. A geometria fornece o referencial; a atmosfera modifica o campo radiativo. Os sensores permitem confrontar grandezas compatíveis, mas um sensor POA não constitui uma medição independente de cada componente horizontal. Massa de ar relativa é uma ligação com a atmosfera: secante do zenital apenas em domínio moderado, sem validade no horizonte; parametrizações devem distinguir pressão e refração. A próxima subseção formaliza irradiância, irradiação e componentes. Não antecipar modelos térmicos, elétricos nem de desempenho dos colegas.')
    # Dimensões já ajustadas à proporção intrínseca, independentemente do importador PPTX.
    for slide in slides:
        for e in slide['elements']:
            if e['kind']=='asset':
                with fitz.open(F/(e['name']+'.pdf')) as pdf:ratio=pdf[0].rect.width/pdf[0].rect.height
                w=min(e['w'],e['h']*ratio);h=w/ratio
                e['x']+=(e['w']-w)/2;e['y']+=(e['h']-h)/2;e['w']=w;e['h']=h
    (A/'Conteudo_6_Slides.json').write_text(json.dumps({'width':1279.967979,'height':720,'slides':slides},ensure_ascii=False,indent=2))
    return slides

def esc(s):
    repl={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}'}
    result=''.join(repl.get(c,c) for c in s).replace('\n',r'\\')
    return result.replace('G₀h',r'$G_{0h}$').replace('G₀n',r'$G_{0n}$').replace('m⁻²',r'm$^{-2}$')

def beamer(slides,stem='Subsecao_1_1_Beamer'):
    out=[r'''\documentclass[aspectratio=169]{beamer}
\usepackage{fontspec,tikz,graphicx,xcolor}
\setmainfont{NimbusRoman-Regular.otf}[Path=/usr/share/fonts/opentype/urw-base35/,BoldFont=NimbusRoman-Bold.otf,ItalicFont=NimbusRoman-Italic.otf,BoldItalicFont=NimbusRoman-BoldItalic.otf]
\setsansfont{NimbusRoman-Regular.otf}[Path=/usr/share/fonts/opentype/urw-base35/,BoldFont=NimbusRoman-Bold.otf,ItalicFont=NimbusRoman-Italic.otf,BoldItalicFont=NimbusRoman-BoldItalic.otf]
\setbeamertemplate{navigation symbols}{}
\definecolor{bg}{HTML}{000000}\definecolor{ink}{HTML}{FFFFFF}\definecolor{yel}{HTML}{FFD45C}
\setbeamercolor{background canvas}{bg=bg}
\setbeamercolor{normal text}{fg=ink,bg=bg}
\setbeamersize{text margin left=0pt,text margin right=0pt}
\begin{document}''']
    def node(text,x,y,w,size,color=FG,bold=False):
        f=size*0.35433;lead=f*1.08
        cmd=r'\bfseries ' if bold else ''
        colorname = 'yel' if color==Y else 'ink'
        return (f'\\node[anchor=north west,inner sep=0pt,text width={w*.125:.5f}mm,align=left,text={colorname},font=\\fontsize{{{f:.4f}}}{{{lead:.4f}}}\\selectfont {cmd}] '
        f'at ([xshift={x*.125:.5f}mm,yshift=-{y*.125:.5f}mm]current page.north west) {{{esc(text)}}};')
    for s in slides:
        stamp='SPGER0046  ·  03 DEZ 2026' if stem=='Materiais_Apresentacao_Secao_01' else 'SPGER0046  ·  29 OUT 2026'
        out.extend([r'\begin{frame}[plain]',r'\begin{tikzpicture}[remember picture,overlay]',node('UFPB  ·  CEAR  ·  PPGER',55.68,10,480,20,FG,True),node(stamp,912,10,310,20),
          r'\draw[yel,line width=.12mm] ([xshift=6mm,yshift=-4.56mm]current page.north west)--([xshift=153.84mm,yshift=-4.56mm]current page.north west);',
          node(s['title'],55.68,61,1165,41,FG,True),node(s['subtitle'],59.52,140,1150,29,Y)])
        for e in s['elements']:
            if e['kind']=='text':out.append(node(e['text'],e['x'],e['y'],e['w'],e['size'],e['color'],e['bold']))
            else:
                out.append(f"\\node[anchor=north west,inner sep=0pt] at ([xshift={e['x']*.125:.4f}mm,yshift=-{e['y']*.125:.4f}mm]current page.north west) {{\\includegraphics[width={e['w']*.125:.4f}mm,height={e['h']*.125:.4f}mm,keepaspectratio]{{../figuras/{e['name']}.pdf}}}};")
        out.extend([node(s['source'],60,653,1160,17),
          r'\draw[yel,line width=.10mm] ([xshift=6mm,yshift=-84.48mm]current page.north west)--([xshift=153.84mm,yshift=-84.48mm]current page.north west);',
          node('Recurso solar e modelagem da conversão fotovoltaica',55.68,691,1109,16),node(str(s['number']),1180,689,50,20,Y,True),r'\end{tikzpicture}',r'\end{frame}'])
    out.append(r'\end{document}');(A/(stem+'.tex')).write_text('\n'.join(out))
    for _ in range(2):
        p=subprocess.run(['xelatex','-interaction=nonstopmode','-halt-on-error',stem+'.tex'],cwd=A,capture_output=True,text=True)
        if p.returncode:raise RuntimeError(p.stdout[-2200:])

if __name__=='__main__':
    assets();beamer(manifest())
