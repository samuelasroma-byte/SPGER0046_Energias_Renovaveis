"""Atualiza as 23 fichas estruturais por associação e acrescenta quatro fichas A045."""
from pathlib import Path
import json,csv
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
FIELDS=['id_ficha','subsecao','referencia_B','arquivo_fonte_sha256','pagina_pdf','pagina_impressa','trecho_curto_verificado','afirmacao_parafraseada','conceito_ou_equacao','unidades_ou_convencoes','lente_sistemica','limites_e_incertezas','revisor','data_revisao','status']
def run(root=ROOT):
    root=Path(root);b=root/'bibliografia'
    portfolio=json.loads((b/'Manifesto_Corpus_Secao_01.json').read_text())
    evid=json.loads((b/'Matriz_Evidencias.json').read_text())
    inv={r['codigo']:r for r in json.loads((b/'Inventario_Fontes_Conferidas.json').read_text())}
    rows=[]
    for section in portfolio['subsections']:
        sec=section.get('id') or section.get('number') or section.get('subsecao')
        if sec is None:sec=section['code']
        sec=str(sec).replace('_','.')
        for code in [*section['B_codes'],'A045']:
            direct=[e for e in evid if e['fonte']==code and e['subsecao']==sec]
            shared=False
            if not direct and code in inv and inv[code]['paginas_verificadas']:
                direct=[e for e in evid if e['fonte']==code];shared=True
            row={k:'' for k in FIELDS}
            row.update(id_ficha=sec.replace('.','_')+'_'+code,subsecao=sec,referencia_B=code,revisor='Conferência assistida por IA',data_revisao='2026-10-27',status='PENDENTE_LEITURA')
            if direct:
                row.update(arquivo_fonte_sha256=inv[code]['sha256'],pagina_pdf=';'.join(str(x) for x in sorted({e['pagina_pdf'] for e in direct})),
                  pagina_impressa=';'.join(dict.fromkeys(e['pagina_impressa'] for e in direct)),
                  afirmacao_parafraseada=' | '.join(e['id']+': '+e['afirmacao_parafraseada'] for e in direct),
                  conceito_ou_equacao='; '.join(dict.fromkeys(e['equacao_figura_conceito'] for e in direct)),
                  unidades_ou_convencoes='; '.join(dict.fromkeys(e['unidades_convencoes'] for e in direct)),
                  lente_sistemica='L01–L07 conforme protocolo; conferir cada evidência, sem aprovação automática',
                  limites_e_incertezas=('Obra compartilhada: evidências da mesma fonte em outras subseções; não são novas leituras. ' if shared else '')+' | '.join(dict.fromkeys(e['limites'] for e in direct)),
                  status='LEITURA_LOCALIZADA_COMPARTILHADA' if shared else 'CONFERIDA_LOCALIZADA')
            elif code=='B29':row.update(status='CONFERIDA_DIGITAL',afirmacao_parafraseada='Método Spencer e implementação pvlib 0.16.1 conferidos; ver Evidencias_Computacionais_e_Inferencias.json.',limites_e_incertezas='Documentação/código não possuem paginação PDF. Não é uma leitura integral de artigo.')
            elif code=='B26':row.update(status='CONTEXTO_ONLINE_CONFERIDO',afirmacao_parafraseada='Tutorial contextualiza o sistema Farm Solar Array/PVDAQ 2107.',limites_e_incertezas='Contexto, sem uso como fundamento principal das equações.')
            elif code=='B24':row.update(status='PROVENIENCIA_CONFERIDA',afirmacao_parafraseada='Citação do dataset e DOI confirmados em DOE/NREL 2024, PDF p. 25; CSV e configuração conferidos separadamente.',limites_e_incertezas='A página de destino DOI não estava acessível; não se alega leitura de todos os dados brutos.')
            elif code=='B11':row.update(status='LEITURA_COMPLEMENTAR_CONFERIDA',arquivo_fonte_sha256=inv[code]['sha256'],pagina_pdf='1;9;10;11',pagina_impressa='1;9;10;11',afirmacao_parafraseada='Alvos GTI modelados separam teste numérico da inversão e avaliação observacional; soluções múltiplas e limites discutidos.',limites_e_incertezas='Aplicado ao limite de validação independente; modelo de transposição permanece na Seção 3.')
            elif code=='B27':row.update(status='DOCUMENTACAO_CONFERIDA',afirmacao_parafraseada='README oficial lido integralmente: acesso, formatos, identificadores e separação do acervo PVDAQ.',limites_e_incertezas='Não é leitura dos datasets completos nem prova de componentes medidas no recorte PVDAQ 2107.')
            elif code in {'B19','B20','B36'}:row.update(status='NAO_SELECIONADA_COMO_PROVA',limites_e_incertezas='Edições B19/B20 ausentes no recorte; PDF B36 com defeitos de representação. Decisões documentadas, sem substituição silenciosa.')
            else:row['limites_e_incertezas']='Fonte/edição ainda sem conteúdo conferido para uso como prova direta; ver Selecao_Critica.json.'
            rows.append(row)
    assert len(rows)==27 and len({r['id_ficha'] for r in rows})==27
    with (b/'03_Fichas_Curadoria.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS);w.writeheader();w.writerows(rows)
    result={'fichas_B_herdadas':23,'novas_associacoes_A045':4,'total_fichas_associativas':27,'evidencias_localizadas_na_matriz':39,'estados':dict(Counter(r['status'] for r in rows)),'nota':'Uma ficha por associação; uma evidência por afirmação localizada. Os números não são intercambiáveis.'}
    (root/'documentacao/Conferencia_Fichas.json').write_text(json.dumps(result,ensure_ascii=False,indent=2))
    return result
if __name__=='__main__':print(json.dumps(run(),ensure_ascii=False,indent=2))
