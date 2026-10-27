"""Revisão localizada da 1.1, redação das demais subseções e integração editorial."""
from pathlib import Path
from copy import deepcopy
import subprocess,json,re
from docx import Document
from docx.shared import Pt,Cm,RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT/'_trabalho_editorial'
WORK.mkdir(exist_ok=True)
(WORK/'apoio').mkdir(exist_ok=True)
M=ROOT/'manuscritos'

def style(doc):
    sec=doc.sections[0];sec.page_width=Cm(21);sec.page_height=Cm(29.7)
    sec.top_margin=Cm(3);sec.bottom_margin=Cm(2);sec.left_margin=Cm(3);sec.right_margin=Cm(2)
    for section in doc.sections:
        section.header_distance=Cm(2)
        header=section.header.paragraphs[0]
        header.clear();header.alignment=WD_ALIGN_PARAGRAPH.RIGHT
        header.paragraph_format.first_line_indent=Cm(0)
        run=header.add_run();run.font.name='Times New Roman';run.font.size=Pt(11)
        field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE')
        run._r.addnext(field)
    for name in ['Normal','Body Text','First Paragraph']:
        if name not in doc.styles:continue
        st=doc.styles[name];st.font.name='Times New Roman';st.font.size=Pt(14);st.font.color.rgb=RGBColor.from_string('000000')
        st.paragraph_format.line_spacing=1.35;st.paragraph_format.space_after=Pt(7)
        st.paragraph_format.alignment=WD_ALIGN_PARAGRAPH.JUSTIFY
        st.paragraph_format.first_line_indent=Cm(1.25)
    for name in ['Title','Heading 1','Heading 2','Heading 3']:
        if name not in doc.styles:doc.styles.add_style(name,WD_STYLE_TYPE.PARAGRAPH)
        st=doc.styles[name];st.font.name='Times New Roman';st.font.size=Pt(16 if name in ['Title','Heading 1'] else 14);st.font.bold=True;st.font.italic=False
        st.font.color.rgb=RGBColor.from_string('000000');st.paragraph_format.keep_with_next=True
        st.paragraph_format.first_line_indent=Cm(0);st.paragraph_format.space_before=Pt(12);st.paragraph_format.space_after=Pt(8)
    for p in doc.paragraphs:
        p.paragraph_format.widow_control=True
        if re.match(r'^1\.[1-4]\.\d+\s',p.text):p.style=doc.styles['Heading 2']
        if p.text.lower().startswith(('quadro de conceitos e convenções','critérios de validade e transição')):p.style=doc.styles['Heading 2']
        for r in p.runs:
            r.font.name='Times New Roman'
            r.italic=False
        if p.style.name in ['Title','Heading 1','Heading 2','Heading 3']:
            if p.text.strip():p.text=p.text.upper()
            for r in p.runs:r.bold=True
        if p._p.xpath('.//m:oMathPara') or p._p.xpath('.//m:oMath') and not p.text.strip():
            p.alignment=WD_ALIGN_PARAGRAPH.CENTER;p.paragraph_format.first_line_indent=Cm(0)
            p.paragraph_format.space_before=Pt(6);p.paragraph_format.space_after=Pt(7)
        if p.text.startswith('Fonte:') or p.text.startswith(('Corte vertical','Irradiância POA medida')):
            p.paragraph_format.first_line_indent=Cm(0);p.paragraph_format.line_spacing=1.1
            for r in p.runs:r.font.size=Pt(11)
            p.alignment=WD_ALIGN_PARAGRAPH.LEFT
        if p.text.startswith(('SPGER0046','Samuel Constantino Teixeira','Convenções:')):
            p.alignment=WD_ALIGN_PARAGRAPH.LEFT;p.paragraph_format.first_line_indent=Cm(0)
        # A herança da justificação não se aplica às referências nem aos metadados.
        if p.text.startswith(('DELINE,','DRIESSE,','DUFFIE,','NOAA GLOBAL','PVLIB CONTRIBUTORS','REDA,','SENGUPTA,','TEIXEIRA,')):
            p.alignment=WD_ALIGN_PARAGRAPH.LEFT;p.paragraph_format.first_line_indent=Cm(-.6);p.paragraph_format.left_indent=Cm(.6);p.paragraph_format.line_spacing=1.1
        for sup in p._p.xpath('.//m:sSup'):
            base=sup.find(qn('m:e'));exp=sup.find(qn('m:sup'))
            if base is not None and exp is not None and ''.join(exp.itertext()).replace('−','-')=='-2' and not ''.join(base.itertext()).replace('\u200b','').strip():
                omath=sup
                while omath.getparent() is not None and omath.tag!=qn('m:oMath'):omath=omath.getparent()
                prev=omath.getprevious()
                if prev is not None:
                    ts=prev.xpath('.//w:t')
                    if ts and (ts[-1].text or '').endswith('m'):
                        ts[-1].text=ts[-1].text[:-1]
                        base.find('.//'+qn('m:t')).text='m'
        for node in p._p.xpath('.//m:t'):
            if node.text:node.text=node.text.replace('\u200b','').replace('\u2062','')
        for mr in p._p.xpath('.//m:r'):
            pr=mr.find(qn('w:rPr'))
            if pr is None:pr=OxmlElement('w:rPr');mr.insert(0,pr)
            sz=pr.find(qn('w:sz'))
            if sz is None:sz=OxmlElement('w:sz');pr.append(sz)
            sz.set(qn('w:val'),'32' if p._p.xpath('.//m:oMathPara') or not p.text.strip() else '28')
    for tab in doc.tables:
        props=tab._tbl.tblPr
        borders=props.find(qn('w:tblBorders'))
        if borders is None:borders=OxmlElement('w:tblBorders');props.append(borders)
        for edge in ['top','left','bottom','right','insideH','insideV']:
            n=borders.find(qn('w:'+edge))
            if n is None:n=OxmlElement('w:'+edge);borders.append(n)
            n.set(qn('w:val'),'single');n.set(qn('w:sz'),'4');n.set(qn('w:color'),'D9D9D9')
        for row in tab.rows:
            pr=row._tr.get_or_add_trPr()
            if pr.find(qn('w:cantSplit')) is None:pr.append(OxmlElement('w:cantSplit'))
            for cell in row.cells:
                for p in cell.paragraphs:
                    p.paragraph_format.first_line_indent=Cm(0);p.paragraph_format.line_spacing=1.1
                    for r in p.runs:r.font.name='Times New Roman';r.font.size=Pt(11.5)
        if tab.rows:
            pr=tab.rows[0]._tr.get_or_add_trPr();hdr=OxmlElement('w:tblHeader');pr.append(hdr)
            for cell in tab.rows[0].cells:
                shade=cell._tc.get_or_add_tcPr().find(qn('w:shd'))
                if shade is None:shade=OxmlElement('w:shd');cell._tc.get_or_add_tcPr().append(shade)
                shade.set(qn('w:fill'),'F0F0F0')
                for p in cell.paragraphs:
                    for run in p.runs:run.bold=True

def simpletext(p,text):
    # Usado somente em parágrafos sem equações/campos.
    p.text=text

def replace_nodes(p,old,new):
    for t in p._p.xpath('.//w:t'):
        if old in (t.text or ''):t.text=t.text.replace(old,new)

def pandoc_doc(md,out,reference=None):
    cmd=['pandoc',str(md),'-f','markdown+tex_math_dollars','-t','docx','--resource-path='+str(md.parent),'-o',str(out)]
    if reference:cmd+=['--reference-doc',str(reference)]
    subprocess.run(cmd,check=True,capture_output=True)
    doc=Document(out)
    tags=re.findall(r'\\tag\{([^}]+)\}',md.read_text())
    if tags:
        candidates=[p for p in doc.paragraphs if p._p.xpath('.//m:oMathPara') and ''.join(p._p.xpath('.//m:t/text()')).startswith(('H','GHI'))]
        assert len(candidates)==len(tags),(len(candidates),tags)
        for paragraph,tag in zip(candidates,tags):
            math=paragraph._p.xpath('.//m:oMath')[0]
            label=OxmlElement('m:r');props=OxmlElement('m:rPr');sty=OxmlElement('m:sty');sty.set(qn('m:val'),'p');props.append(sty);label.append(props)
            text=OxmlElement('m:t');text.text='   ('+tag+')';label.append(text);math.append(label)
    style(doc);doc.save(out)

def revisar_11():
    base=ROOT/'insumos/Base_Manuscrito_1_1.docx'
    d=Document(base);p=d.paragraphs
    for idx,tag in [(7,'E1.01'),(18,'E1.02')]:
        math=p[idx]._p.xpath('.//m:oMath')[0]
        r=OxmlElement('m:r');label=OxmlElement('m:t');label.text='   ('+tag+')';r.append(label);math.append(r)
    simpletext(p[1],'SPGER0046 — Energias Renováveis | PPGER/UFPB\nCapítulo: Recurso solar e modelagem da conversão fotovoltaica\nSamuel Constantino Teixeira\nConvenções: norte 0°, sentido horário; geometria no ponto médio de cada intervalo.')
    replace_nodes(p[3],'2020, cap. 1–2','2020, p. 9–15')
    replace_nodes(p[6],'aparente ou geométrico, conforme a implementação e as correções adotadas','geométrico, sem correção de refração atmosférica')
    for paragraph in p:
        replace_nodes(paragraph,'2004, p. 577–589','2004, p. 577–578')
        if paragraph.text.startswith('A equação (E1.01)'):
            replace_nodes(paragraph,'577–589','577–578')
    replace_nodes(p[8],'2020, cap. 1','2020, p. 13–15')
    p[10].insert_paragraph_before('Denota-se por Aₛ o azimute adotado no capítulo. Duffie, Beckman e Blair (2020, p. 13) utilizam γₛ contado do sul, negativo a leste e positivo a oeste. A conversão para a convenção norte e sentido horário do SPA é:')
    conv=WORK/'apoio/conversao_azimute.md';conv.write_text(r'$$A_s=(\gamma_s+180^{\circ})\;\mathrm{mod}\;360^{\circ}.$$')
    tmp=WORK/'apoio/conversao_azimute.docx';subprocess.run(['pandoc',str(conv),'-o',str(tmp)],check=True,capture_output=True)
    p[10]._p.addprevious(deepcopy(next(x for x in Document(tmp).paragraphs if x._p.xpath('.//m:oMath'))._p))
    replace_nodes(p[16],'no manuscrito final, o valor numérico deve ser declarado de acordo com o algoritmo efetivamente utilizado','aqui se fixa Gsc = 1366,1 W/m² para reproduzir a implementação do projeto')
    replace_nodes(p[16],'2020, sec. 1.2–1.4','2020, p. 9; PVLIB CONTRIBUTORS, 2026')
    for node in p[16]._p.xpath('.//w:t'):
        if node.text:node.text=re.sub(r'sec\.\s*1\.2[–-]1\.4','p. 9; PVLIB CONTRIBUTORS, 2026',node.text)
    replace_nodes(p[22],'2020, cap. 2; SENGUPTA et al., 2024','2020, p. 9–10; SENGUPTA et al., 2024, cap. 2, p. 6–8')
    simpletext(p[23],'A aproximação secante é utilizada como interpretação geométrica de atmosfera plana ao nível do mar, para zenitais aproximadamente até 70°, no tratamento de Duffie, Beckman e Blair (2020, p. 9–10). Não deve ser extrapolada ao horizonte. A massa de ar relativa e sua correção de pressão para massa de ar absoluta precisam ser distinguidas em aplicações quantitativas.')
    p[20].insert_paragraph_before('A projeção extraterrestre usa o horizonte geométrico e é anulada quando o centro solar fica abaixo dele. O critério aproximado de 90,833° utilizado pela NOAA para nascer e pôr do Sol inclui refração atmosférica e tamanho angular do disco solar; responde a outra definição de evento e não deve ser aplicado como substituição automática desse recorte (NOAA GLOBAL MONITORING LABORATORY, [s. d.], p. 2).')
    simpletext(p[35],'A conferência bibliográfica foi localizada por páginas, com distinção entre obras catalogadas e evidências efetivamente verificadas. O livro de Duffie, Beckman e Blair (2020, p. 9) apresenta 0,00719 no termo em cos(2B) de sua equação 1.4.1b. O código conferido do pvlib 0.16.1 utiliza 0,000719. Para reproduzir os cálculos do projeto, adota-se este último coeficiente, mantendo registrada a divergência entre as fontes; a comparação não constitui uma investigação de erratas do editor.')
    simpletext(p[34],'O caso PVDAQ 2107 utiliza 38,996306° N, 122,134111° O e altitude de 10 m na configuração do projeto. A janela compreende 01/04 a 30/06/2024, no fuso America/Los_Angeles. O rótulo temporal indica o início de intervalos de 15 minutos; o SPA é avaliado 7 min 30 s depois. Em 17/05/2024, o fuso corresponde a UTC−7. A pressão é estimada da altitude, enquanto temperatura de refração de 12 °C e diferença de escalas temporais ΔT = 67 s são padrões mantidos da implementação, sem tratá-los como medições locais ou como atualização específica de efemérides.')
    simpletext(p[33],'Os ângulos são calculados pelo SPA de Reda e Andreas (2004; 2008), enquanto a irradiância extraterrestre normal é calculada separadamente pelo método Spencer. A rotina utiliza pvlib 0.16.1. O exemplo publicado do SPA foi reproduzido com os parâmetros da Tabela A5.1 (REDA; ANDREAS, 2008, p. A-15–A-16), obtendo zenital aparente de 50,111622° e azimute de 194,340241°, compatíveis com os valores de referência arredondados. Essa conferência verifica a implementação numérica; não valida o sensor POA nem a precisão de todas as entradas do estudo de caso.')
    simpletext(p[28],'O gráfico reúne naturezas distintas de informação. A POA provém da medição local agregada, enquanto zenital e incidência são calculados. Os dados integram o acervo PVDAQ (DELINE et al., 2021); o processamento e a seleção são documentados no projeto (TEIXEIRA et al., 2026). Para 17/05, há 96 posições temporais, 94 médias POA não ausentes e 68 intervalos com três amostras na agregação. A figura exibe 05 h a 21 h locais, sem interpolação. A proximidade temporal entre o máximo de POA e a maior altura solar não constitui validação independente do SPA, nem permite identificar isoladamente condições de nuvens, aerossóis ou vapor de água. Trata-se de um exemplo diário, e não de uma distribuição climatológica.')
    simpletext(p[27],'Figura G01 — POA observada e ângulos calculados no PVDAQ 2107, em 17/05/2024. POA: média de 15 minutos; posição solar no ponto médio. Fonte: dados preparados e configuração do projeto; cálculo de Samuel Constantino Teixeira, 2026. Zenital geométrico; incidência com zenital aparente, conforme a cadeia vigente.')
    for idx,img,width in [(26,'G01_recurso_geometria_claro.png',15.2)]:
        para=p[idx];para.clear();para.add_run().add_picture(str(ROOT/'figuras'/img),width=Cm(width));para.alignment=WD_ALIGN_PARAGRAPH.CENTER
        para.paragraph_format.first_line_indent=Cm(0)
    # A relação orbital é acrescentada sem substituir as equações OMML existentes.
    anchor=p[17]
    q=anchor.insert_paragraph_before('Na aproximação de Spencer implementada, E₀ é função do dia do ano n, com B = 2π(n − 1)/365 em radianos. Mantém-se o denominador 365 também para 2024, ano bissexto, conforme o método do software. O fator empregado é (PVLIB CONTRIBUTORS, 2026):')
    md=WORK/'apoio/spencer_omml.md';md.write_text(r'$$\begin{aligned}E_0={}&1.000110+0.034221\cos B+0.001280\sin B\\&+0.000719\cos(2B)+0.000077\sin(2B).\end{aligned}$$')
    temp=WORK/'apoio/spencer_omml.docx';subprocess.run(['pandoc',str(md),'-o',str(temp)],check=True,capture_output=True)
    eq=deepcopy(next(x for x in Document(temp).paragraphs if x._p.xpath('.//m:oMath'))._p)
    # O arranjo nativo de equações evita as células vazias da matriz produzida por aligned.
    math=eq.xpath('.//m:oMath')[0];matrix=math.find(qn('m:m'));arr=OxmlElement('m:eqArr')
    if matrix is not None:
        for row in matrix.findall(qn('m:mr')):
            line=OxmlElement('m:e')
            for cell in row.findall(qn('m:e')):
                for child in cell:line.append(deepcopy(child))
            arr.append(line)
        math.remove(matrix);math.append(arr)
    anchor._p.addprevious(eq)
    # Reorganiza somente a lista bibliográfica, mantendo as fontes efetivamente usadas.
    for pp in list(d.paragraphs):
        if pp.text.startswith(('GOMES,','DELINE,','DUFFIE,','NOAA GLOBAL','PVLIB CONTRIBUTORS','REDA,','SENGUPTA,')):
            pp._p.getparent().remove(pp._p)
    refs=[r for r in (ROOT/'bibliografia/Referencias_Verificadas.md').read_text().split('\n\n')[1:] if not r.startswith('DRIESSE,')]
    for ref in refs:
        pp=d.add_paragraph()
        for i,segment in enumerate(ref.split('**')):pp.add_run(segment).bold=bool(i%2)
    style(d);out=M/'1_1_Geometria_Solar.docx';d.save(out)
    return out

def run():
    one=revisar_11()
    # O arquivo integrado é construído a partir da 1.1 revisada e das novas subseções.
    md11=WORK/'apoio/1_1_integracao.md'
    media=WORK/'apoio/media_manuscrito'
    subprocess.run(['pandoc',str(one),'-t','markdown','--wrap=none','--extract-media='+str(media),'-o',str(md11)],check=True,capture_output=True)
    s=md11.read_text()
    # A legenda explícita já existe; o alt não deve gerar uma segunda legenda.
    s=re.sub(r'!\[[^\]]*\]', '![]', s)
    portable=ROOT/'figuras/Manuscrito_1_1';portable.mkdir(exist_ok=True)
    for image in media.rglob('*'):
        if image.is_file():
            target=portable/image.name
            target.write_bytes(image.read_bytes())
            s=s.replace(str(image), '../figuras/Manuscrito_1_1/'+image.name)
    s=re.split(r'(?im)^(?:#{1,6}\s+)?(?:\*\*)?Referências utilizadas(?:\*\*)?',s)[0]
    # Remove marcação de estilo do título numérico apenas na versão integrada.
    s=re.sub(r'(?m)^# (.+)',r'## \1',s)
    s=re.sub(r'(?m)^## (\*\*)?(1\.1\.\d+[^\n]*)',r'### \1\2',s)
    refs=(ROOT/'bibliografia/Referencias_Verificadas.md').read_text()
    individual=[]
    for slug in ['1_2_Grandezas_Radiometricas','1_3_Modulacao_Atmosferica','1_4_Medicao_e_Estimativa']:
        src=M/(slug+'.md');tmp=WORK/'apoio'/('individual_'+slug+'.md')
        used=('DUFFIE,','SENGUPTA,','TEIXEIRA,','DRIESSE,') if slug.startswith('1_2') else ('DUFFIE,','SENGUPTA,','TEIXEIRA,')
        localrefs='# Referências\n\n'+'\n\n'.join(r for r in refs.split('\n\n')[1:] if r.startswith(used))
        tmp.write_text(src.read_text()+'\n\n'+localrefs)
        out=M/(slug+'.docx');pandoc_doc(tmp,out,one);individual.append(out)
    text='# 1 FUNDAMENTOS E CARACTERIZAÇÃO DO RECURSO SOLAR\n\nSamuel Constantino Teixeira\n\n'+s
    for slug in ['1_2_Grandezas_Radiometricas','1_3_Modulacao_Atmosferica','1_4_Medicao_e_Estimativa']:
        part=(M/(slug+'.md')).read_text()
        part=re.sub(r'(?m)^## ',r'### ',part)
        part=re.sub(r'(?m)^# ',r'## ',part)
        text+='\n\n'+part
    text+='\n\n'+refs
    integrated=M/'Secao_01_Integrada.md';integrated.write_text(text)
    pandoc_doc(integrated,M/'Secao_01_Integrada.docx',one)
    # As notas contêm conteúdo oral de estudo e as fontes de cada quadro.
    manifest=json.loads((ROOT/'apresentacao/Conteudo_6_Slides.json').read_text())
    oral='# ROTEIRO ORAL DA SUBSEÇÃO 1.1\n\nSamuel Constantino Teixeira — apresentação preliminar de 29/10/2026\n\nOs seis quadros correspondem aos slides físicos 5 a 10 do arquivo coletivo, com numeração visível 4 a 9. O tempo individual não foi fixado no planejamento; este roteiro organiza a fala sem presumir uma duração autorizada.\n\n'
    for sl in manifest['slides']:
        oral+=f"## QUADRO {sl['physical']-4} — {sl['title']}\n\n{sl['notes']}\n\n{sl['source']}\n\n"
    oral+='## QUESTÕES PARA ESTUDO\n\nPor que o meio-dia solar difere de 12 h no relógio? Porque longitude, equação do tempo e convenção civil deslocam a correspondência entre posição solar e hora registrada.\n\nPor que SPA não fornece a GHI medida? Porque o algoritmo de posição solar não representa, por si só, a transferência radiativa na atmosfera.\n\nPor que a POA não é uma medição de GHI? Porque o sensor está em outro plano e integra contribuições com distribuição angular distinta.\n\nO valor 1366,1 W/m² é uma nova medida da constante solar? Não. É o parâmetro de referência mantido para reproduzir o método Spencer do projeto.\n\nO que demonstra a conferência com a Tabela A5.1? A consistência da implementação com um exemplo publicado, sem validação independente do conjunto de sensores do estudo.\n\nÉ possível identificar nuvens apenas pela G01? A forma da curva não discrimina de modo único os mecanismos atmosféricos e de medição.\n\n'
    oral+=refs;(ROOT/'apresentacao/Roteiro_Oral_6_Slides.md').write_text(oral)
    pandoc_doc(ROOT/'apresentacao/Roteiro_Oral_6_Slides.md',ROOT/'apresentacao/Roteiro_Oral_6_Slides.docx',one)
    pandoc_doc(ROOT/'documentacao/Conferencia_Cientifica_39_Evidencias.md',ROOT/'documentacao/Conferencia_Cientifica_39_Evidencias.docx',one)
    return [one,*individual,M/'Secao_01_Integrada.docx',ROOT/'apresentacao/Roteiro_Oral_6_Slides.docx']
if __name__=='__main__':
    print('\n'.join(str(p) for p in run()))
