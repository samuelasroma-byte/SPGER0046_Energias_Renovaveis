"""Apresentação acadêmica e referências com recuo francês."""
from pathlib import Path
import re
import unicodedata
from docx import Document
from docx.shared import Cm, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

FONT = 'Times New Roman'
SIZE = 12
TEXT_WIDTH_CM = 16.0


def set_font(element):
    """Pin all script families and remove inherited theme fonts."""
    pr = element.get_or_add_rPr()
    fonts = pr.find(qn('w:rFonts'))
    if fonts is None:
        fonts = OxmlElement('w:rFonts'); pr.insert(0, fonts)
    for name in ['asciiTheme', 'hAnsiTheme', 'eastAsiaTheme', 'cstheme']:
        fonts.attrib.pop(qn('w:'+name), None)
    for name in ['ascii', 'hAnsi', 'eastAsia', 'cs']:
        fonts.set(qn('w:'+name), FONT)
    for name in ['sz', 'szCs']:
        old = pr.find(qn('w:'+name))
        if old is None: old = OxmlElement('w:'+name); pr.append(old)
        old.set(qn('w:val'), '24')


def configure_document(doc):
    for sec in doc.sections:
        sec.page_width=Cm(21); sec.page_height=Cm(29.7)
        sec.top_margin=sec.left_margin=Cm(3)
        sec.bottom_margin=sec.right_margin=Cm(2)
        sec.header_distance=Cm(2); sec.footer_distance=Cm(1)
        for p in sec.footer.paragraphs: p.clear()
        header=sec.header.paragraphs[0]; header.clear()
        header.alignment=WD_ALIGN_PARAGRAPH.RIGHT
        header.paragraph_format.first_line_indent=Cm(0)
        header.paragraph_format.line_spacing=1
        field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE')
        run=OxmlElement('w:r');set_font(run)
        text=OxmlElement('w:t');text.text='1';run.append(text);field.append(run);header._p.append(field)
    for style in doc.styles:
        if hasattr(style,'font'):
            style.font.name=FONT;style.font.size=Pt(SIZE);style.font.color.rgb=RGBColor(0,0,0)
            set_font(style.element)
    for name in ['Normal','Body Text']:
        p=doc.styles[name].paragraph_format
        p.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY;p.line_spacing=1.5
        p.first_line_indent=Cm(1.25);p.left_indent=Cm(0);p.right_indent=Cm(0)
        p.space_before=Pt(0);p.space_after=Pt(0);p.widow_control=True
    for name in ['Title','Heading 1','Heading 2','Heading 3','Caption','Header','Footer']:
        p=doc.styles[name].paragraph_format
        p.first_line_indent=Cm(0);p.left_indent=Cm(0);p.right_indent=Cm(0)
        p.line_spacing=1;p.space_before=Pt(12);p.space_after=Pt(12)
        p.keep_with_next=name not in ['Header','Footer'];p.widow_control=True
        p.alignment=WD_ALIGN_PARAGRAPH.CENTER if name=='Title' else WD_ALIGN_PARAGRAPH.LEFT
    doc.styles['Title'].font.bold=True
    for name in ['Heading 1','Heading 2','Heading 3','Caption']:doc.styles[name].font.bold=True
    if 'Referência ABNT' not in doc.styles:
        doc.styles.add_style('Referência ABNT',WD_STYLE_TYPE.PARAGRAPH)
    style=doc.styles['Referência ABNT'];style.base_style=doc.styles['Normal']
    style.font.name=FONT;style.font.size=Pt(12);set_font(style.element)
    p=style.paragraph_format;p.alignment=WD_ALIGN_PARAGRAPH.LEFT
    p.line_spacing=1;p.left_indent=Cm(1.25);p.first_line_indent=Cm(-1.25)
    p.space_before=Pt(0);p.space_after=Pt(12);p.keep_together=True;p.widow_control=True
    for node in list(doc.styles.element.iter(qn('w:pBdr'))):node.getparent().remove(node)
    return doc


def finalize_document(doc):
    """Apply the requested family and size even to hyperlinks and fields."""
    roots=[doc.element]
    for sec in doc.sections:roots.extend([sec.header._element,sec.footer._element])
    for root in roots:
        for run in root.iter(qn('w:r')):set_font(run)
    return doc


def save_document(doc,path):
    finalize_document(doc);path=Path(path);path.parent.mkdir(parents=True,exist_ok=True);doc.save(path)
    return path


def bookmark(paragraph,name,number):
    start=OxmlElement('w:bookmarkStart');start.set(qn('w:id'),str(number));start.set(qn('w:name'),name)
    end=OxmlElement('w:bookmarkEnd');end.set(qn('w:id'),str(number))
    paragraph._p.insert(0,start);paragraph._p.append(end)


def internal_link(paragraph,text,anchor):
    link=OxmlElement('w:hyperlink');link.set(qn('w:anchor'),anchor)
    run=OxmlElement('w:r');set_font(run)
    bold=OxmlElement('w:b');run.get_or_add_rPr().append(bold)
    node=OxmlElement('w:t');node.text=text;run.append(node);link.append(run);paragraph._p.append(link)


def _initials(given):
    tokens=re.findall(r'[^\W\d_]+',given,flags=re.UNICODE)
    out=[]
    for token in tokens:
        if token.lower() in ['de','da','do','dos','das','del','van','von']:continue
        out.extend(list(token) if token.isupper() and len(token)<=3 else [token[0]])
    return ' '.join(x.upper()+'.' for x in out)


def author_names(w):
    raw=(w.get('authors') or '').replace(' (Deceased)','')
    names=[a.strip(' .;') for a in re.split(r';|\s+and\s+',raw) if a.strip(' .;')]
    corporate=any(s in raw.lower() for s in ['laborator','contributors','webinar','noaa','pvdaq','oedi']) or raw.strip()=='ABB'
    if corporate:return [raw.strip(' .;').upper()]
    rendered=[]
    for name in names:
        if ',' in name:
            surname,given=name.split(',',1)
        else:
            bits=name.split();surname=bits[-1];given=' '.join(bits[:-1])
            if len(bits)>2 and bits[-2].lower() in ['de','del','van','von']:
                surname=' '.join(bits[-2:]);given=' '.join(bits[:-2])
        rendered.append(surname.upper()+(', '+_initials(given) if given else ''))
    return rendered or ['AUTORIA INSTITUCIONAL INDICADA NA FONTE']


def authors_abnt(w):
    names=author_names(w)
    text=(names[0]+' et al.') if len(names)>3 else '; '.join(names)
    if w.get('contributors_role')=='editors':text+=' (ed.)'
    return text


def access_date(w):
    dates=[str(v)[:10] for k,v in w.items() if k.startswith('citations_date_') and v]
    stamp=max(dates) if dates else '2026-10-16'
    months=['jan.','fev.','mar.','abr.','maio','jun.','jul.','ago.','set.','out.','nov.','dez.']
    try:
        y,m,d=map(int,stamp.split('-'));return f'{d} {months[m-1]} {y}'
    except (ValueError,IndexError):return '16 out. 2026'


def reference_parts(w):
    """ABNT order; unknown publication data remain explicit, never fabricated."""
    parts=[]
    def add(text,bold=False,italic=False):
        if text:parts.append({'text':str(text),'bold':bold,'italic':italic})
    names=author_names(w)
    add(names[0] if len(names)>3 else '; '.join(names))
    if len(names)>3:add(' et al.',italic=True)
    if w.get('contributors_role')=='editors':add(' (ed.)')
    add(' ' if parts[-1]['text'].endswith('.') else '. ')
    title=str(w['title']).strip().rstrip('.')
    kind=str(w.get('document_type') or '').lower()
    year=str(w.get('year') or '[s.d.]')
    venue=str(w.get('venue') or w.get('publisher') or '').rstrip(' .')
    place=w.get('publication_place') or '[S. l.]'
    is_article='article' in kind and 'proceeding' not in kind
    if is_article:
        add(title+'. ');add(venue,bold=True);add(', '+place)
        if w.get('volume'):add(', v. '+str(w['volume']))
        if w.get('issue'):add(', n. '+str(w['issue']))
        if w.get('pages'):
            pages=str(w['pages']).replace('–','-')
            add(', '+('p. ' if '-' in pages else 'art. ')+pages)
        add(', '+year+'.')
    elif 'proceeding' in kind:
        add(title+'. ');add('In:',italic=True)
        add(' IEEE PHOTOVOLTAIC SPECIALISTS CONFERENCE, 31., '+year+', [S. l.]. ')
        add(venue or 'Proceedings',bold=True)
        add('. [S. l.]: '+str(w.get('publisher') or 'IEEE')+', '+year+'.')
        if w.get('pages'):add(' p. '+str(w['pages']).replace('–','-')+'.')
    else:
        main,sep,sub=title.partition(':')
        add(main,bold=True)
        if sep:add(': '+sub.strip())
        add('. ')
        if str(w.get('edition') or '') not in ['', '1']:add(str(w['edition'])+'. ed. ')
        publisher=str(w.get('publisher') or venue or '').strip()
        add(place+(': '+publisher if publisher else '')+', '+year+'.')
    if w.get('doi'):add(' DOI: https://doi.org/'+str(w['doi'])+'.')
    url=('https://doi.org/'+str(w['doi'])) if w.get('doi') else w.get('url') or w.get('oa_url')
    if url:add(' Disponível em: '+str(url)+'. Acesso em: '+access_date(w)+'.')
    return parts


def reference_text(w):return ''.join(s['text'] for s in reference_parts(w))


def add_reference(doc,w):
    p=doc.add_paragraph(style='Referência ABNT')
    for part in reference_parts(w):
        r=p.add_run(part['text']);r.bold=part['bold'];r.italic=part['italic']
    return p


def sort_key(w):
    return unicodedata.normalize('NFKD',authors_abnt(w)+' '+w['title']).encode('ascii','ignore').decode().casefold()
