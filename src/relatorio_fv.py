"""Accessible report and explicit evidence mapping, without claiming full-stage validation."""
from pathlib import Path
import json
import base64
import html
import pandas as pd
import editorial_fv as editorial


def coverage(ctx):
    root=ctx['root'];sections=editorial.assign_sections(root,json.loads((root/'docs/secoes_capitulo.json').read_text()))
    ids={r['id'] for r in ctx['figures']}
    records=[]
    for s in sections:
        figs=[f for f in s['figures'] if f in ids]
        row=dict(s);row['figures_available']='; '.join(figs)
        row['figures_not_generated']='; '.join(f for f in s['figures'] if f not in ids)
        row['execution_status']='calculado e exportado' if figs else 'fundamentação e quadro; experimento opcional não executado'
        records.append(row)
    out=root/'outputs/relatorios';out.mkdir(parents=True,exist_ok=True)
    flat=[]
    for r in records:
        flat.append({k:('; '.join(v) if isinstance(v,list) else v) for k,v in r.items()})
    pd.DataFrame(flat).to_csv(out/'Matriz_de_Cobertura_do_Capitulo.csv',index=False)
    md='# Matriz de cobertura do capítulo\n\nVersão '+ctx['config']['version']+'. As 19 subseções estão mapeadas. Cobertura teórica ou execução de um cenário não equivale à validação independente da etapa.\n\n'
    for r in records:
        md+='## '+r['id']+' '+r['title']+'\n\n'
        for label,key in [('Responsável','owner'),('Entradas','inputs'),('Método','method'),
                          ('Saídas','outputs'),('Evidência','evidence'),('Limite','limitation'),
                          ('Figuras disponíveis','figures_available'),('Situação de execução','execution_status')]:
            md+='**'+label+':** '+str(r[key])+'\n\n'
        md+='**Referências:** '+', '.join(r['refs'])+'.\n\n'
    (out/'Matriz_de_Cobertura_do_Capitulo.md').write_text(md)
    return records


def report(ctx):
    root=ctx['root'];rows=coverage(ctx);refs=json.loads((root/'references/referencias_projeto.json').read_text())
    escaped=html.escape;m=ctx['metrics'].iloc[0]
    body='<h1>Recurso solar e modelagem fotovoltaica</h1>'
    body+='<p>SPGER0046 UFPB · Farm Solar Array PVDAQ 2107 · versão '+ctx['config']['version']+' · abril a junho de 2024.</p>'
    body+='<p>A cadeia principal usa POA, temperatura do ar e vento locais para estimar potência AC e confrontá-la com o medidor. NASA POWER está fora desse percurso.</p>'
    body+=f'<p><strong>Comparação principal:</strong> {int(m.n)} pares; MBE {m.MBE:.3f} kW; MAE {m.MAE:.3f} kW; RMSE {m.RMSE:.3f} kW; nMBE {m.nMBE_percent:+.3f}%; nRMSE {m.nRMSE_percent:.3f}%; r {m.r:.5f}; R² {m.R2:.5f}.</p>'
    body+='<p>Esses indicadores descrevem o modelo físico e não uma certificação de sensores ou aprovação universal. Albedo, sujidade, associação elétrica equivalente e BIPV são hipóteses identificadas. Componentes reconstruídas da POA não têm validação independente.</p>'
    body+='<button id="theme" type="button" aria-pressed="false">Alternar fundo claro ou escuro</button>'
    body+='<nav aria-label="Sumário"><h2>Sumário das subseções</h2><ol>'
    for r in rows:body+='<li><a href="#sec'+r['id'].replace('.','_')+'">'+escaped(r['id']+' '+r['title'])+'</a></li>'
    body+='</ol></nav><p>Cada ID tem uma única subseção de inserção. Citar o item em outras partes sem repetir sua inclusão.</p><h2>Materiais para redação por seção</h2><ul>'
    rules=editorial.policy(root)
    if rules:
        for section in rules['sections']:
            path=section['directory']+'/tabelas/docx/Materiais_Tabulares_Secao_'+str(section['section']).zfill(2)+'.docx'
            body+='<li><a href="../../'+path+'">Tabelas e quadros exclusivos da seção '+str(section['section'])+'</a></li>'
        body+='<li><a href="../../docs/Distribuicao_Editorial.md">Mapa de inserção única</a></li>'
    body+='</ul><details><summary>Coleções consolidadas de consulta</summary><ul>'
    outputs=[('Tabelas editáveis','tabelas/docx/Tabelas_do_Projeto.docx'),
        ('Quadros editáveis','quadros/docx/Quadros_do_Projeto.docx'),
        ('Gráficos em Word','graficos/docx/Graficos_do_Projeto.docx'),
        ('Fluxogramas em Word','fluxogramas/docx/Fluxogramas_do_Projeto.docx'),
        ('Ilustrações FV em Word','figuras/docx/Ilustracoes_FV.docx'),
        ('Dossiê técnico por seção','dossie_tecnico/Dossie_Tecnico_por_Secao.docx')]
    for title,path in outputs:body+='<li><a href="../'+path+'">'+title+'</a></li>'
    body+='</ul></details><p><a href="Matriz_de_Cobertura_do_Capitulo.md">Matriz completa das 19 subseções</a></p>'
    for r in rows:
        body+='<section id="sec'+r['id'].replace('.','_')+'"><h2>'+escaped(r['id']+' '+r['title'])+'</h2>'
        body+='<details><summary>Descrição e método</summary><p>'+escaped(r['method'])+'</p><p><strong>Entradas:</strong> '+escaped(r['inputs'])+'</p><p><strong>Limite:</strong> '+escaped(r['limitation'])+'</p></details>'
        body+='<p><strong>Evidência:</strong> '+escaped(r['evidence'])+'. <strong>Responsável:</strong> '+escaped(r['owner'])+'.</p>'
        for fig in ctx['figures']:
            editorial.assign_figure(root,fig)
            if r['id'] not in fig['subsections']:continue
            images={}
            for theme in ['claro','escuro']:
                images[theme]=base64.b64encode((root/fig['files'][theme]['preview']).read_bytes()).decode()
            body+='<figure data-editorial-id="'+escaped(fig['id'])+'"><h3>'+escaped(fig['title'])+'</h3>'
            for theme in ['claro','escuro']:
                body+='<img class="fig-'+theme+'" src="data:image/png;base64,'+images[theme]+'" alt="'+escaped(fig['caption'])+'">'
            body+='<figcaption>'+escaped(fig['caption'])+'<p>Fonte: '+escaped(fig['source'])+'</p>Referências metodológicas: '+escaped(', '.join(fig['refs']))+'.</figcaption></figure>'
        if r['id']=='2.1':
            body+='<h3>Estatística descritiva</h3><div class="scroll">'+ctx['analytics_tables']['estatistica_descritiva'].drop(columns=['window','std_convention']).to_html(index=False,border=0,float_format=lambda x:f'{x:.3f}')+'</div>'
        if r['id']=='4.4':
            body+='<h3>Métricas gerais</h3><div class="scroll">'+ctx['metrics'].to_html(index=False,border=0,float_format=lambda x:f'{x:.4f}')+'</div>'
        body+='</section>'
    body+='<h2>Referências</h2>'
    for ref in refs:
        body+='<p id="'+ref['id']+'"><strong>'+ref['id']+'</strong> '+escaped(ref['citation'])+' <a href="'+escaped(ref['url'])+'">Fonte original</a>. '+escaped(ref['role'])+'.</p>'
    css='''body{--bg:#101820;--fg:#f5f7fa;--link:#70e5ff;--line:#536773;background:var(--bg);color:var(--fg);font:20px/1.65 Arial,sans-serif;margin:0}body.light{--bg:#fff;--fg:#161616;--link:#005b93;--line:#ccd3d8}main{max-width:1100px;margin:auto;padding:28px}h1{font-size:2rem}h2{font-size:1.45rem;margin-top:2em}h3{font-size:1.1rem}a{color:var(--link)}button{font-size:1rem;padding:12px;background:var(--bg);color:var(--fg);border:2px solid var(--link);border-radius:5px;cursor:pointer}summary{cursor:pointer;font-weight:bold}details{margin:12px 0}figure{margin:30px 0}img{display:block;width:100%;height:auto}figcaption{font-size:18px}.fig-claro{display:none}body.light .fig-claro{display:block}body.light .fig-escuro{display:none}.scroll{overflow-x:auto}table{border-collapse:collapse;font-size:17px}td,th{padding:9px;border-bottom:1px solid var(--line);text-align:left}nav ol{padding-left:28px}section{scroll-margin-top:20px}'''
    js='''document.getElementById("theme").addEventListener("click",()=>{const light=document.body.classList.toggle("light");document.getElementById("theme").setAttribute("aria-pressed",String(light));});'''
    page='<!doctype html><html lang="pt-BR"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Projeto FV versão '+ctx['config']['version']+'</title><style>'+css+'</style><body><main>'+body+'</main><script>'+js+'</script></body></html>'
    dest=root/'outputs/relatorios/Relatorio_do_Projeto.html';dest.write_text(page)
    return dest
