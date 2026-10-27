"""Mantém SVG e substitui os PNGs de compatibilidade por imagens reais opacas."""
from pathlib import Path
import json,zipfile,posixpath,io
from lxml import etree as E
from PIL import Image,ImageDraw

NS={'p':'http://schemas.openxmlformats.org/presentationml/2006/main','a':'http://schemas.openxmlformats.org/drawingml/2006/main',
    'r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships','asvg':'http://schemas.microsoft.com/office/drawing/2016/SVG/main'}

def run(pptx,root=None):
    root=Path(root or Path(__file__).resolve().parents[1]);pptx=Path(pptx)
    with zipfile.ZipFile(pptx) as z:data={n:z.read(n) for n in z.namelist()}
    manifest=json.loads((root/'apresentacao/Conteudo_6_Slides.json').read_text());results=[]
    for s in manifest['slides']:
        part=f"ppt/slides/slide{s['physical']}.xml"
        doc=E.fromstring(data[part]);rels=E.fromstring(data[f"ppt/slides/_rels/slide{s['physical']}.xml.rels"])
        links={r.get('Id'):r.get('Target') for r in rels}
        # O modelo importado tem um retângulo de fundo que cobre p:bg.
        backgrounds=[]
        for shape in doc.findall('.//p:sp',NS):
            ext=shape.find('./p:spPr/a:xfrm/a:ext',NS)
            if ext is not None and int(ext.get('cx'))>12000000 and int(ext.get('cy'))>6800000:
                paint=shape.find('./p:spPr/a:solidFill/a:srgbClr',NS)
                assert paint is not None;paint.set('val','000000');backgrounds.append(shape)
        assert len(backgrounds)==1,(s['physical'],'fundo não localizado')
        assets=[e for e in s['elements'] if e['kind']=='asset'];pics=doc.findall('.//p:pic',NS)
        assert len(pics)==len(assets),(s['physical'],len(pics),len(assets))
        for asset,pic in zip(assets,pics):
            off=pic.find('.//a:xfrm/a:off',NS);ext=pic.find('.//a:xfrm/a:ext',NS)
            assert abs(int(off.get('x'))/9525-asset['x'])<.02 and abs(int(off.get('y'))/9525-asset['y'])<.02
            assert abs(int(ext.get('cx'))/9525-asset['w'])<.02
            alt=pic.find('.//p:cNvPr',NS);alt.set('name',asset['name']);alt.set('descr',asset['name']+' — figura científica de alto contraste; fonte e dados no pacote reproduzível')
            blip=pic.find('.//a:blip',NS);svg=pic.find('.//asvg:svgBlip',NS)
            assert blip is not None and svg is not None
            for node,ext in [(blip,'png'),(svg,'svg')]:
                rid=node.get('{'+NS['r']+'}embed');target=links[rid]
                path=target.lstrip('/') if target.startswith('/') else posixpath.normpath(posixpath.join('ppt/slides',target))
                data[path]=(root/'figuras'/(asset['name']+'.'+ext)).read_bytes()
                if ext=='png':
                    image=Image.open(io.BytesIO(data[path]));assert image.width>100 and image.height>20
                    assert image.mode in ['RGB','RGBA']
                    if image.mode=='RGBA':assert image.getextrema()[-1]==(255,255),'PNG não opaco'
                    # Remove só a franja de rasterização da borda da página PDF.
                    # A margem LaTeX é de 3 pt (12,5 px a 300 dpi), sem conteúdo.
                    image=image.convert('RGB');ImageDraw.Draw(image).rectangle((0,0,image.width-1,image.height-1),outline='black',width=3)
                    buffer=io.BytesIO();image.save(buffer,format='PNG');data[path]=buffer.getvalue()
                    results.append({'slide':s['physical'],'figura':asset['name'],'fallback_px':list(image.size),'png_bytes':len(data[path]),'svg_preservado':True})
        data[part]=E.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone=True)
    assert len(results)==9
    with zipfile.ZipFile(pptx,'w',zipfile.ZIP_DEFLATED) as z:
        for n,b in data.items():z.writestr(n,b)
    (root/'documentacao/Compatibilidade_Figuras_PPTX.json').write_text(json.dumps(results,ensure_ascii=False,indent=2))
    return results

def somente_png(source,output):
    with zipfile.ZipFile(source) as z:data={n:z.read(n) for n in z.namelist()}
    for i in range(5,11):
        key=f'ppt/slides/slide{i}.xml';doc=E.fromstring(data[key])
        for node in doc.findall('.//asvg:svgBlip',NS):node.getparent().remove(node)
        data[key]=E.tostring(doc,xml_declaration=True,encoding='UTF-8',standalone=True)
    with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as z:
        for n,b in data.items():z.writestr(n,b)

def extrair_parte(source,output):
    """Extrai os seis quadros e elimina partes não alcançáveis da apresentação."""
    with zipfile.ZipFile(source) as z:data={n:z.read(n) for n in z.namelist()}
    pkg='http://schemas.openxmlformats.org/package/2006/relationships'
    pres=E.fromstring(data['ppt/presentation.xml']);rels=E.fromstring(data['ppt/_rels/presentation.xml.rels'])
    lst=pres.find('p:sldIdLst',NS);selected=set()
    for i,node in enumerate(list(lst),1):
        if 5<=i<=10:selected.add(node.get('{'+NS['r']+'}id'))
        else:lst.remove(node)
    assert len(selected)==6
    for r in list(rels):
        if r.get('Type','').endswith('/slide') and r.get('Id') not in selected:rels.remove(r)
    data['ppt/presentation.xml']=E.tostring(pres,xml_declaration=True,encoding='UTF-8',standalone=True)
    data['ppt/_rels/presentation.xml.rels']=E.tostring(rels,xml_declaration=True,encoding='UTF-8',standalone=True)
    def relpart(part):
        return posixpath.join(posixpath.dirname(part),'_rels',posixpath.basename(part)+'.rels') if part else '_rels/.rels'
    keep=set()
    def visit(part):
        if part in keep:return
        if part:keep.add(part)
        rp=relpart(part)
        if rp not in data:return
        keep.add(rp)
        for rel in E.fromstring(data[rp]):
            if rel.get('TargetMode')=='External':continue
            t=rel.get('Target');target=t.lstrip('/') if t.startswith('/') else posixpath.normpath(posixpath.join(posixpath.dirname(part),t))
            assert target in data,target
            visit(target)
    visit('')
    ct=E.fromstring(data['[Content_Types].xml'])
    for node in list(ct):
        if node.tag.endswith('Override') and node.get('PartName','').lstrip('/') not in keep:ct.remove(node)
    data['[Content_Types].xml']=E.tostring(ct,xml_declaration=True,encoding='UTF-8',standalone=True);keep.add('[Content_Types].xml')
    if 'docProps/app.xml' in keep:
        app=E.fromstring(data['docProps/app.xml'])
        for node in app:
            if E.QName(node).localname=='Slides':node.text='6'
            if E.QName(node).localname in ['HeadingPairs','TitlesOfParts']:app.remove(node)
        data['docProps/app.xml']=E.tostring(app,xml_declaration=True,encoding='UTF-8',standalone=True)
    with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED) as z:
        for n in sorted(keep):z.writestr(n,data[n])
    assert sum(n.startswith('ppt/slides/slide') and n.endswith('.xml') for n in keep)==6

if __name__=='__main__':
    import sys
    print(json.dumps(run(sys.argv[1]),ensure_ascii=False,indent=2))
