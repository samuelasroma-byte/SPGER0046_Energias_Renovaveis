"""Independent checks on final files, mathematical consistency and notebook execution."""
from pathlib import Path
import io,json,zipfile,tempfile,shutil,sys,re
import numpy as np
import pandas as pd
from PIL import Image
import fitz
import nbformat
from lxml import etree
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'outputs';CSV=OUT/'tabelas/csv'
sys.path.insert(0,str(ROOT/'src'))
import projeto_fv as fv

catalog=json.loads((ROOT/'docs/auditoria/Inventario_Figuras.json').read_text())
assert len({r['id'] for r in catalog})==len(catalog)
checked=[]
for r in catalog:
    pdf_text=[]
    for theme,bg in [('claro',(255,255,255)),('escuro',(16,24,32))]:
        for fmt in ['pdf','png']:
            p=ROOT/r['files'][theme+'_'+fmt];assert p.exists() and p.stat().st_size>1000
            if fmt=='png':
                with Image.open(p) as im:
                    im.verify()
                with Image.open(p) as im:
                    assert im.width==3780,(p.name,im.size)
                    assert all(abs(x-600)<1 for x in im.info['dpi'])
                    assert tuple(im.convert('RGB').getpixel((0,0)))==bg
            else:
                with fitz.open(p) as pdf:
                    assert len(pdf)==1
                    assert all(f[2]!='Type3' for f in pdf[0].get_fonts())
                    assert not pdf[0].get_images(),'Elemento rasterizado não previsto: '+p.name
                    text=pdf[0].get_text()
                    assert text.strip(),'PDF sem textos vetoriais: '+p.name
                    pdf_text.append(text)
            checked.append(str(p.relative_to(ROOT)))
    assert pdf_text[0]==pdf_text[1],'Textos diferentes entre temas: '+r['id']
    assert r['same_numeric_geometry_between_themes']

ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
def attr(node,name):return node.get('{'+ns['w']+'}'+name)
# All six generated ABNT documents retain their original bytes;
# the planning and reference guides are separate.
docxs=list(OUT.rglob('*.docx'))+[ROOT/'docs/metodos/Dossie_Tecnico_por_Secao.docx']
assert len(docxs)==6
tables_count=0
for p in docxs:
    with zipfile.ZipFile(p) as z:
        assert z.testzip() is None
        xml=etree.fromstring(z.read('word/document.xml'))
        styles=etree.fromstring(z.read('word/styles.xml'))
        assert not styles.xpath('//w:pBdr',namespaces=ns),'Regra decorativa herdada nos títulos'
        for sz in xml.xpath('//w:tbl//w:rPr/w:sz',namespaces=ns):assert attr(sz,'val')=='24'
        for t in xml.xpath('//w:tbl',namespaces=ns):
            borders=t.find('w:tblPr/w:tblBorders',ns)
            assert borders is not None
            if p.name=='Tabelas_do_Projeto.docx':
                for edge in ['left','right','insideH','insideV']:
                    assert attr(borders.find('w:'+edge,ns),'val')=='nil'
                for edge in ['top','bottom']:
                    b=borders.find('w:'+edge,ns);assert attr(b,'val')=='single' and attr(b,'sz')=='12'
                rows=t.findall('w:tr',ns)
                for i,row in enumerate(rows):
                    for cell in row.findall('w:tc',ns):
                        cb=cell.find('w:tcPr/w:tcBorders',ns)
                        for edge in ['left','right']:assert attr(cb.find('w:'+edge,ns),'val')=='nil'
                        if i==0:
                            assert attr(cb.find('w:top',ns),'val')=='single'
                            assert attr(cb.find('w:bottom',ns),'val')=='single'
                        elif i==len(rows)-1:assert attr(cb.find('w:bottom',ns),'val')=='single'
                        else:assert attr(cb.find('w:bottom',ns),'val')=='nil'
                tables_count+=1
            elif p.name=='Quadros_do_Projeto.docx':
                for edge in ['top','left','right','bottom','insideH','insideV']:
                    assert attr(borders.find('w:'+edge,ns),'val')=='single'

y=pd.read_csv(CSV/'yields.csv').iloc[0]
daily=pd.read_csv(CSV/'energia_e_HSP_diurna_pareada.csv')
monthly=pd.read_csv(CSV/'energia_e_indicadores_mensais.csv')
assert np.isclose(daily.E_measured_kWh.sum(),y.E_AC_observed_kWh)
assert np.isclose(daily.E_modeled_kWh.sum(),y.E_AC_model_kWh)
assert np.isclose(daily.PSH_POA_paired_h.sum(),y.Yr_h)
assert np.isclose(monthly.E_observed_paired_kWh.sum(),y.E_AC_observed_kWh)
assert np.isclose(y.PR_observed_paired,y.Yf_observed_kWh_kWp/y.Yr_h)
assert np.isclose(y.Lc_model_h+y.Ls_model_h,y.Yr_h-y.Yf_model_kWh_kWp)

nb=nbformat.read(ROOT/'notebooks/originais_executados/01_Projeto_FV_Quatro_Secoes.ipynb',as_version=4)
nbformat.validate(nb)
codes=[c for c in nb.cells if c.cell_type=='code']
assert [c.execution_count for c in codes]==list(range(1,len(codes)+1))
assert not any(o.output_type=='error' for c in codes for o in c.outputs)
sections=[]
for i,c in enumerate(nb.cells):
    if c.cell_type=='markdown' and re.match(r'^## [1-4]\.\d ',c.source):
        sections.append(c.source.split()[1])
        assert '\n' not in c.source
        assert nb.cells[i+1].cell_type=='markdown' and nb.cells[i+1].source.startswith('<details>')
        assert nb.cells[i+2].cell_type=='code'
assert sections==[f'{s}.{i}' for s,n in [(1,4),(2,4),(3,6),(4,5)] for i in range(1,n+1)]
matrix=pd.read_csv(OUT/'relatorios/originais/Matriz_de_Cobertura_do_Capitulo.csv')
assert len(matrix)==19 and matrix.figures_not_generated.isna().all()

# Run the non-inverse path in a separate disposable root, preserving delivered outputs.
with tempfile.TemporaryDirectory(prefix='fv_sem_inversao_') as tmp:
    root=Path(tmp)
    shutil.copytree(ROOT/'config',root/'config')
    (root/'data').mkdir();(root/'data/raw').symlink_to(ROOT/'data/raw',target_is_directory=True)
    ctx=fv.complete_pipeline(root,make_plots=False,include_nasa=False,reverse=False)
    assert 'reverse_diagnostics' not in ctx and 'bipv_balance' not in ctx and 'nasa' not in ctx
    assert ctx['audit']['available_daylight_15m']==4401
    assert np.isclose(ctx['metrics'].iloc[0].nRMSE_percent,14.991130565767405)
result={'status':'passed','figures':len(catalog),'final_PDF_PNG_files':len(checked),
        'DOCX':len(docxs),'numerical_tables':tables_count,'chapter_subsections':19,
        'executed_code_cells':len(codes),'reverse_disabled_electrical_path':'passed',
        'tables_style':'three horizontal rules; 12pt; editable',
        'frames_style':'full grid; 12pt; editable','same_pdf_text_between_themes':True}
(ROOT/'docs/auditoria/Verificacao_Refinamento_Integracao.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
print(json.dumps(result,ensure_ascii=False,indent=2))
