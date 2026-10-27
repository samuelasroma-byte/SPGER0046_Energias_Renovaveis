"""Mantém as decisões da leitura crítica e sua aplicação editorial rastreável."""
from pathlib import Path
import json,hashlib
from collections import Counter
from curadoria_secao01 import run as curadoria
from confrontar_evidencias import produzir

ROOT=Path(__file__).resolve().parents[1]

def run(root=ROOT,fontes=None):
    root=Path(root);b=root/'bibliografia'
    inv=json.loads((b/'Inventario_Fontes_Conferidas.json').read_text())
    if fontes:
        import fitz
        for code,name,pages,state in [
          ('B11','B11_Driesse_Jensen_Perez_2024.pdf',[1,9,10,11],'localizada; metodologia e conclusões da inversão confrontadas'),
          ('B36','B36_Sengupta_2021_3ed.pdf',[26,28,29,55],'inspeção visual e textual; arquivo com defeitos; excluído como prova')]:
            f=Path(fontes)/name
            with fitz.open(f) as d:n=len(d)
            r={'codigo':code,'arquivo':name,'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'paginas_pdf':n,
              'paginas_verificadas':pages,'leitura_integral':False,'status_leitura':state,
              'fonte':'https://doi.org/10.1016/j.solener.2023.112093' if code=='B11' else 'https://elib.dlr.de/143117/',
              'uso':'limites da validação de inversão' if code=='B11' else 'não utilizado como fundamento direto'}
            inv=[x for x in inv if x['codigo']!=code]+[r]
        (b/'Inventario_Fontes_Conferidas.json').write_text(json.dumps(inv,ensure_ascii=False,indent=2))
    rows,decisions,status=curadoria(root=root)
    details,summary=produzir(root=root,fontes_dir=fontes)
    byid={r['id']:r for r in details}
    for r in rows:
        a=byid[r['id']]
        r.update(classificacao_cientifica=a['classificacao'],parecer_analitico=a['parecer_analitico'],
          consequencia_editorial=a['consequencia_editorial'],confronto=a['confronto'])
    (b/'Matriz_Evidencias.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2))
    import csv
    with (b/'Matriz_Evidencias.csv').open('w',encoding='utf-8-sig',newline='') as f:
        w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
    metadata=[
      {'codigo':'B11','identidade':'Driesse; Jensen; Perez. Solar Energy 267 (2024), 112093. DOI 10.1016/j.solener.2023.112093',
       'conteudo_conferido':'PDF pp. 1 e 9–11; alvos de GTI modelados para testar a inversão; distinguir correção numérica de validação com medidas independentes.'},
      {'codigo':'B24','identidade':'Deline; Perry; Deceglie; Muller; Sekulic; Jordan. Photovoltaic Data Acquisition (PVDAQ) Public Datasets. 21 dez. 2021. DOI 10.25984/1846021',
       'fonte_de_conferencia':'Golnas; Gentry; White. Open-Source Tools & Open-Access Solar Data. DOE/NREL, 2024, PDF p. 25.',
       'url_conferida':'https://www.energy.gov/sites/default/files/2024-05/Data_Tools_Webina..._Comms_Final.pdf',
       'limite':'Citação recuperada em fonte institucional; a página de destino DOI não foi acessível. Não constitui verificação de todos os canais brutos.'},
      {'codigo':'B27','identidade':'NatLabRockies/pvdaq_access, README oficial',
       'url_conferida':'https://github.com/NatLabRockies/pvdaq_access',
       'conteudo_conferido':'README integral: separação do acervo público e Solar Data Bounty Prize, identificadores, formatos e metadados; não leitura de todos os datasets.'},
      {'codigo':'A045','identidade':'Handbook 4ª ed., 2024, NREL/TP-5D00-88300; DOI 10.2172/2448063',
       'url_conferida':'https://research-hub.nlr.gov/en/publications/best-practices-handbook-for-the-collection-and-use-of-solar-resou-4/'},
      {'codigo':'B36','decisao':'Arquivo da 3ª edição inspecionado; texto e figuras com recursos ausentes/sobrepostos. Não selecionado como prova. A045 é a 4ª edição efetivamente lida, com identidade própria.'},
      {'codigo':'B19/B20','decisao':'Não selecionadas como prova nesta versão porque as edições exatas não estavam no recorte inspecionado; não substituídas por livros de outros autores/edições.'}]
    (root/'documentacao/Conferencia_Referencias_Complementares.json').write_text(json.dumps(metadata,ensure_ascii=False,indent=2))
    counts=Counter(x['classificacao'] for x in details)
    report='''# Conferência científica da Seção 1

Samuel Constantino Teixeira — PPGER/UFPB — 27 de outubro de 2026

As 39 afirmações da matriz foram confrontadas com as páginas indicadas, as equações, as convenções e os limites de uso. O confronto sustenta a redação com as qualificações registradas: 16 relações diretas, 18 relações diretas com restrições, uma com derivação matemática e quatro com inferência explicitada. A leitura foi assistida por IA; não corresponde a revisão por pares, leitura integral dos livros ou aplicação integral do ProKnow-C.

## Correções físicas e bibliográficas

A convenção azimutal do capítulo parte do norte e cresce no sentido horário. O livro de Duffie, Beckman e Blair parte do sul; a conversão foi explicitada como Aₛ = (γₛ + 180°) mod 360°. O símbolo Aₛ identifica o azimute nos diagramas. No zênite a projeção horizontal se anula e o azimute é indefinido.

A aproximação secante para massa de ar recebeu o domínio indicado no livro: nível do mar e zenitais de até aproximadamente 70°. O critério NOAA de 90,833° para nascer e pôr do Sol inclui refração e tamanho angular do disco; não substitui o recorte geométrico da projeção extraterrestre.

O coeficiente de cos(2B) é 0,000719 no pvlib 0.16.1 executado, enquanto o exemplar do livro imprime 0,00719 na p. 9. A implementação mantém o coeficiente do software e o denominador 365, inclusive no ano bissexto, com a divergência registrada. O SPA calcula posição; Spencer calcula irradiância extraterrestre.

A reprodução da Tabela A5.1 do SPA foi conferida contra o arredondamento a cinco casas decimais, com tolerância de 0,000005°. Essa tolerância é numérica e não expressa a incerteza do sensor ou a exatidão das entradas PVDAQ.

GHI, DNI e DHI foram delimitadas ao campo solar de ondas curtas e a planos, bandas e intervalos compatíveis. A soma discreta de médias para obter irradiação foi identificada como derivação da integral. Reconstituir componentes e reproduzir a POA de entrada não as valida como observações independentes. Driesse, Jensen e Perez (2024, pp. 9–11) distinguem testes da solução inversa com alvos modelados e comparação com observações.

Inferências sobre umidade superficial e água precipitável, resolução de pixel e exatidão, e interpolação temporal foram separadas das definições diretamente documentadas. Uma montagem fixa não oferece todas as componentes independentes; sistemas de sombra rotativa alternam medidas e calculam DNI. A POA isolada restringe certos testes de qualidade, mas não impede controles de cadência, lacunas e disponibilidade.

## Decisões sobre as fontes

B11 passou por leitura das pp. 1 e 9–11. O README oficial B27 foi lido. A autoria e o DOI de B24 foram confirmados na p. 25 de material institucional DOE/NREL de 2024, mantendo a indicação de que o destino DOI não estava acessível. O arquivo B36/2021 foi inspecionado e excluído como prova devido a defeitos de representação; a quarta edição A045 foi lida e registrada separadamente. B19 e B20 permanecem no catálogo histórico, sem uso como prova nesta versão.

## Rastreabilidade e arquivos editáveis

Confronto_Cientifico_39_Evidencias.csv e a aba Confronto_Cientifico da planilha contêm afirmação, página, classificação, justificativa, consequência editorial e hashes. O notebook executa verificações de integridade e relações físicas e exporta os DOCX editáveis. Reexecutar o código não simula uma nova leitura intelectual das referências. PDFs integrais de terceiros permanecem no acervo autorizado.

Os manuscritos estão em Times New Roman, com equações nativas do Word. Os PDFs de texto são exportados por LibreOffice. Os slides são compilados em Beamer com XeLaTeX; PDF e PPTX compartilham o conteúdo declarado, sem sincronização bidirecional. Diagramas, equações e gráficos dos seis quadros usam fundo preto opaco, textos brancos e destaques amarelos/cianos. O PPTX inclui vetores e imagens PNG válidas para compatibilidade.
'''
    (root/'documentacao/Conferencia_Cientifica_39_Evidencias.md').write_text(report)
    return rows,decisions,status,summary

if __name__=='__main__':
    import argparse
    p=argparse.ArgumentParser();p.add_argument('--fontes',type=Path);a=p.parse_args()
    print(json.dumps(run(fontes=a.fontes)[-1],ensure_ascii=False,indent=2))
