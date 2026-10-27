"""Integra apenas slides 5–10 em um PPTX recuperado imediatamente antes da gravação.
Preserva byte a byte os demais slides, relações, temas e contribuições.
"""
from pathlib import Path
import zipfile,posixpath,json,hashlib,sys
from lxml import etree as E
R='http://schemas.openxmlformats.org/package/2006/relationships'
P='http://schemas.openxmlformats.org/presentationml/2006/main'
DR='http://schemas.openxmlformats.org/officeDocument/2006/relationships'
CT='http://schemas.openxmlformats.org/package/2006/content-types'
def xml(b):return E.fromstring(b)
def dump(e):return E.tostring(e,encoding='UTF-8',xml_declaration=True,standalone=True)
def relpath(p):return posixpath.join(posixpath.dirname(p),'_rels',posixpath.basename(p)+'.rels')
def resolve(p,t):return t.lstrip('/') if t.startswith('/') else posixpath.normpath(posixpath.join(posixpath.dirname(p),t))

def merge(base,authored,output,report):
    z=zipfile.ZipFile(base);a=zipfile.ZipFile(authored)
    data={n:z.read(n) for n in z.namelist()};copied={};allowed={'[Content_Types].xml','ppt/presentation.xml','ppt/_rels/presentation.xml.rels'}
    content=xml(data['[Content_Types].xml']);act=xml(a.read('[Content_Types].xml'))
    def addtype(old,new):
        for e in act:
            if e.tag.endswith('Override') and e.get('PartName')=='/'+old:
                if not any(x.get('PartName')=='/'+new for x in content):
                    n=E.SubElement(content,'{'+CT+'}Override');n.set('PartName','/'+new);n.set('ContentType',e.get('ContentType'))
        ext=new.rsplit('.',1)[-1]
        for e in act:
            if e.tag.endswith('Default') and e.get('Extension')==ext and not any(x.get('Extension')==ext for x in content):
                n=E.SubElement(content,'{'+CT+'}Default');n.set('Extension',ext);n.set('ContentType',e.get('ContentType'))
    def cp(old):
        if old in copied:return copied[old]
        if old.startswith('ppt/slides/slide') and old.endswith('.xml'):return old
        new=posixpath.join(posixpath.dirname(old),'s01r2_'+posixpath.basename(old));copied[old]=new
        assert new not in data,'Colisão de parte existente: '+new
        data[new]=a.read(old);addtype(old,new)
        rp=relpath(old)
        if rp in a.namelist():
            rel=xml(a.read(rp))
            for e in rel:
                if e.get('TargetMode')=='External':continue
                dest=cp(resolve(old,e.get('Target')));e.set('Target',posixpath.relpath(dest,posixpath.dirname(new)))
            data[relpath(new)]=dump(rel)
        return new
    for i in range(5,11):
        part=f'ppt/slides/slide{i}.xml';rp=relpath(part);allowed.update([part,rp])
        oldrel=xml(data[rp]);layout=next(e.get('Target') for e in oldrel if e.get('Type').endswith('/slideLayout'))
        rel=xml(a.read(rp))
        for e in rel:
            if e.get('Type').endswith('/slideLayout'):e.set('Target',layout)
            elif e.get('TargetMode')!='External':
                dest=cp(resolve(part,e.get('Target')));e.set('Target',posixpath.relpath(dest,posixpath.dirname(part)))
        data[part]=a.read(part);data[rp]=dump(rel)
    masters=[v for k,v in copied.items() if k.startswith('ppt/notesMasters/') and k.endswith('.xml') and '/theme/' not in k]
    if masters:
        pres=xml(data['ppt/presentation.xml']);rels=xml(data['ppt/_rels/presentation.xml.rels'])
        lst=pres.find('{'+P+'}notesMasterIdLst')
        if lst is None:
            lst=E.Element('{'+P+'}notesMasterIdLst');pos=1 if pres.find('{'+P+'}sldMasterIdLst') is not None else 0;pres.insert(pos,lst)
        for j,m in enumerate(masters):
            rid='rIdSecao01ConfrontoNotes'+str(j)
            assert not any(e.get('Id')==rid for e in rels)
            e=E.SubElement(rels,'{'+R+'}Relationship',Id=rid,Type=DR+'/notesMaster',Target=posixpath.relpath(m,'ppt'))
            n=E.SubElement(lst,'{'+P+'}notesMasterId');n.set('{'+DR+'}id',rid)
        data['ppt/presentation.xml']=dump(pres);data['ppt/_rels/presentation.xml.rels']=dump(rels)
    data['[Content_Types].xml']=dump(content)
    changed=[n for n in z.namelist() if data[n]!=z.read(n)]
    assert set(changed)<=allowed,(set(changed)-allowed)
    unchanged=[i for i in range(1,19) if i not in range(5,11)]
    assert all(data[f'ppt/slides/slide{i}.xml']==z.read(f'ppt/slides/slide{i}.xml') for i in unchanged)
    out=Path(output);out.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED) as o:
        for n,b in data.items():o.writestr(n,b)
    result={'changed_original_parts':changed,'new_parts':sorted(set(data)-set(z.namelist())),
        'slides_changed':[5,6,7,8,9,10],'slides_unchanged_byte_for_byte':unchanged,
        'source_sha256':hashlib.sha256(Path(base).read_bytes()).hexdigest(),
        'output_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
        'count_source_slides':18,'preserves_original_presentation_id_list':True,
        'notes':'Alterações globais limitadas ao registro das notas e aos tipos de conteúdo; demais contribuições preservadas.'}
    Path(report).write_text(json.dumps(result,ensure_ascii=False,indent=2))
    return result
if __name__=='__main__':
    print(json.dumps(merge(*sys.argv[1:5]),ensure_ascii=False,indent=2))
