"""Acabamento dos manuscritos sem alterar seu conteúdo científico.

Aplica a escolha editorial do autor: quadros com entrelinhas simples e sem
espaço antes/depois, expressões estrangeiras em itálico e figuras de 13,5 cm.
Siglas, expansões formais de siglas, unidades, URLs e identificadores técnicos
permanecem em sua forma original. Não reexecuta cálculos ou curadoria.
"""
from copy import deepcopy
import re

W='http://schemas.openxmlformats.org/wordprocessingml/2006/main'
NS={'w':W,'m':'http://schemas.openxmlformats.org/officeDocument/2006/math',
    'wp':'http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing',
    'a':'http://schemas.openxmlformats.org/drawingml/2006/main'}
Q=lambda name:'{'+W+'}'+name
def xp(element,query):
    from lxml import etree as E
    return E.XPath(query,namespaces=NS)(element)
FIGURA_LARGURA_CM=13.5

# Termos encontrados no recorte e termos editoriais exemplificados pelo autor.
# A lista não acrescenta palavras ao manuscrito; só formata ocorrências reais.
TERMOS=[
 r'et\s+al\.',r'a\s+priori',r'a\s+posteriori',r'in\s+situ',r'in\s+vitro',
 r'in\s+vivo',r'ad\s+hoc',r'apud',r'ibidem',r'idem',
 r'plane\s+of\s+array',r'Farm\s+Solar\s+Array',r'pvlib',r'Python',
 r'Markdown',r'Bootstrap',r'software',r'datasets?',r'handbook',r'pixel',
 r'clear[ -]sky',
 r'Solar engineering of thermal processes, photovoltaics and wind',
 r'General solar position calculations',
 r'Solar position algorithm for solar radiation applications',
 r'Best practices handbook for the collection and use of solar resource data for solar energy applications',
 r'A continuous form of the Perez diffuse sky model for forward and reverse transposition',
 r'Solar Energy',r'Public Datasets',r'Revised January 2008'
]
PATTERNS=[re.compile(r'(?<!\w)(?:'+s+r')(?!\w)',re.I) for s in TERMOS]
EXPANSOES=[
 'National Solar Radiation Database','Solar Position Algorithm',
 'Photovoltaic Data Acquisition','National Renewable Energy Laboratory',
 'NOAA GLOBAL MONITORING LABORATORY','PVLIB CONTRIBUTORS'
]

def propriedades(element,tag):
    from lxml import etree as E
    found=element.find(Q(tag))
    if found is None:
        found=E.Element(Q(tag));element.insert(0,found)
    return found

def definir(element,tag,values):
    from lxml import etree as E
    node=element.find(Q(tag))
    if node is None:node=E.SubElement(element,Q(tag))
    for k,v in values.items():node.set(Q(k),str(v))
    return node

def italicos(xml):
    from lxml import etree as E
    records=[]
    for pi,p in enumerate(xp(xml,'.//w:p')):
        runs=xp(p,'.//w:r')
        texts=[''.join(t.text or '' for t in r.findall(Q('t'))) for r in runs]
        full=''.join(texts)
        if not full:continue
        protected=[]
        for pattern in [r'https?://\S+',r'America/[A-Za-z_]+']:
            protected += [(m.start(),m.end()) for m in re.finditer(pattern,full)]
        for name in EXPANSOES:
            protected += [(m.start(),m.end()) for m in re.finditer(re.escape(name),full)]
        flags=[False]*len(full);matches=[]
        for pat in PATTERNS:
            for m in pat.finditer(full):
                a,b=m.span()
                selected=[j for j in range(a,b) if not any(x<=j<y for x,y in protected)]
                if selected:
                    for j in selected:flags[j]=True
                    matches.append(m.group())
        if not matches:continue
        cursor=0
        for run,s in zip(runs,texts):
            local=flags[cursor:cursor+len(s)];cursor+=len(s)
            if not any(local):continue
            parent=run.getparent();at=parent.index(run);rpr=run.find(Q('rPr'));pos=0;pieces=[]
            for child in run:
                if child.tag==Q('rPr'):continue
                if child.tag!=Q('t'):
                    nr=E.Element(Q('r'),attrib=dict(run.attrib))
                    if rpr is not None:nr.append(deepcopy(rpr))
                    nr.append(deepcopy(child));pieces.append(nr);continue
                txt=child.text or '';end=pos+len(txt);start=pos
                while start<end:
                    style=local[start];stop=start+1
                    while stop<end and local[stop]==style:stop+=1
                    nr=E.Element(Q('r'),attrib=dict(run.attrib))
                    if rpr is not None:nr.append(deepcopy(rpr))
                    if style:
                        rp=propriedades(nr,'rPr')
                        definir(rp,'i',{'val':'1'});definir(rp,'iCs',{'val':'1'})
                    nt=deepcopy(child);nt.text=txt[start-pos:stop-pos]
                    nt.set('{http://www.w3.org/XML/1998/namespace}space','preserve')
                    nr.append(nt);pieces.append(nr);start=stop
                pos=end
            parent.remove(run)
            for nr in pieces:parent.insert(at,nr);at+=1
        records.append({'paragrafo':pi,'ocorrencias':sorted(set(matches))})
    return records

def quadros_compactos(xml):
    tables=xp(xml,'.//w:tbl');paragraphs=0
    for table in tables:
        for cell in xp(table,'./w:tr/w:tc'):
            tcpr=propriedades(cell,'tcPr');margins=definir(tcpr,'tcMar',{})
            for side in ['top','bottom']:definir(margins,side,{'w':'40','type':'dxa'})
            for p in xp(cell,'./w:p'):
                pr=propriedades(p,'pPr')
                definir(pr,'spacing',{'before':'0','after':'0','line':'240','lineRule':'auto','beforeAutospacing':'0','afterAutospacing':'0'})
                definir(pr,'jc',{'val':'center'});paragraphs+=1
    return {'quadros':len(tables),'paragrafos':paragraphs,'entrelinhas':'simples (240/auto)',
            'antes_pt':0,'depois_pt':0,'margem_vertical_celula_pt':2,'colunas_centralizadas':[1,2,3]}

def figuras_menores(xml):
    target=round(FIGURA_LARGURA_CM*360000);indent=round((16-FIGURA_LARGURA_CM)/2/2.54*1440);records=[]
    for drawing in xp(xml,'.//w:drawing'):
        extent=drawing.find('.//{'+NS['wp']+'}extent')
        if extent is None:continue
        oldx=int(extent.get('cx'));oldy=int(extent.get('cy'));newy=round(oldy*target/oldx)
        extent.set('cx',str(target));extent.set('cy',str(newy))
        for e in xp(drawing,'.//a:xfrm/a:ext'):e.set('cx',str(target));e.set('cy',str(newy))
        p=drawing.getparent()
        while p is not None and p.tag!=Q('p'):p=p.getparent()
        if p is not None:
            for adjacent in [p.getprevious(),p.getnext()]:
                if adjacent is not None and adjacent.tag==Q('p'):
                    text=''.join(xp(adjacent,'.//w:t/text()'))
                    if text.startswith(('Figura ','Fonte:')):
                        definir(propriedades(adjacent,'pPr'),'ind',{'left':indent,'right':indent,'firstLine':0})
        records.append({'largura_anterior_cm':round(oldx/360000,3),'largura_atual_cm':FIGURA_LARGURA_CM,'altura_atual_cm':round(newy/360000,3)})
    return records

def aplicar_revisao_xml(xml):
    """Idempotente nos espaçamentos e dimensões; preserva todos os textos."""
    before=xp(xml,'.//w:t/text()')
    original=''.join(before)
    quadros=quadros_compactos(xml);figuras=figuras_menores(xml);termos=italicos(xml)
    assert ''.join(xp(xml,'.//w:t/text()'))==original
    return {'quadros':quadros,'figuras':figuras,'termos_italicos':termos,
            'excecoes':'siglas, expansões formais de siglas, unidades, nomes de autores/instituições e identificadores técnicos'}

def aplicar_revisao_documento(doc):
    return aplicar_revisao_xml(doc.element)
