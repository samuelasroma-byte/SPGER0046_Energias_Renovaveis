# SPGER0046 — SEÇÃO 1: FUNDAMENTOS E CARACTERIZAÇÃO DO RECURSO SOLAR

Samuel Constantino Teixeira — PPGER/UFPB. Continuidade científica e editorial de 27/10/2026.

## Entrega e arquivos oficiais

Os seis quadros de 1.1 ocupam os slides físicos **5 a 10**, com numeração visível **4 a 9**, no [PPTX coletivo existente](https://docs.google.com/presentation/d/1U3Btzt1RiKhBIgUeus2DfkFz5d6Uf8rd/edit). O arquivo coletivo permanece a fonte oficial da apresentação de 29/10. O pacote contém os materiais de Samuel, sem criar outra apresentação coletiva.

| Produto | Caminho neste pacote |
|---|---|
| Seis slides de 1.1, em PDF e Beamer | `apresentacao/Subsecao_1_1_Beamer.pdf` e `.tex` |
| Seis slides de Samuel em PowerPoint | `apresentacao/Subsecao_1_1_Alto_Contraste.pptx` |
| Roteiro oral dos seis quadros | `apresentacao/Roteiro_Oral_6_Slides.docx` e `.pdf` |
| Manuscrito 1.1 revisado | `manuscritos/1_1_Geometria_Solar.docx` |
| Manuscritos 1.2, 1.3 e 1.4 | `manuscritos/1_2_Grandezas_Radiometricas.docx`, `1_3_Modulacao_Atmosferica.docx`, `1_4_Medicao_e_Estimativa.docx` |
| Seção integrada | `manuscritos/Secao_01_Integrada.docx` e `.pdf` |
| Materiais da apresentação final, restritos à Seção 1 | `apresentacao/Materiais_Apresentacao_Secao_01.pdf` e `.tex`, 12 quadros |
| Notebook consolidado e executado | `notebooks/00_Revisao_Cientifica_Acessivel_4_Subsecoes_v2_20261026.ipynb` |
| Curadoria e evidências | `bibliografia/Matriz_Corpus_e_Curadoria_Secao_01.xlsx`, `Matriz_Evidencias.csv` e `.json` |
| Confronto científico das 39 afirmações | `bibliografia/Confronto_Cientifico_39_Evidencias.csv` e `.json`; aba `Confronto_Cientifico` da planilha |
| Protocolo e pendências | `bibliografia/Protocolo_Revisao_Estruturada.md` e `Status_Revisao.json` |
| Figuras e equações vetoriais | `figuras/`, com arquivos PDF, SVG e fontes LaTeX |
| Conferência científica e visual | `documentacao/Relatorio_Conferencia.md` |

## Reprodução dos cálculos e do notebook

Use Python 3.12 e instale `python -m pip install -r requirements.txt`. Abra o notebook na pasta `notebooks/` ou execute, a partir desta raiz, `python src/solar_secao01.py` para reproduzir os cálculos e a G01. O notebook aceita tanto a estrutura local do pacote quanto a recuperação dos insumos públicos do GitHub; confere SHA-256 e exige pvlib 0.16.1. Sua reexecução não publica no Drive nem altera o PPTX coletivo.

A POA preparada, a configuração e os parâmetros do projeto foram preservados. O notebook tem dez células de código executadas por IPython, sem erros; o ambiente restringe sockets para um kernel externo. As saídas registradas incluem os cálculos, os pareceres de leitura e sete DOCX exportados. O arquivo de fundamentação coletiva anterior foi auditado e permaneceu inalterado. A auditoria das entradas está em `documentacao/Auditoria_Notebooks_Entrada.json`.

Os cálculos usam o ponto médio dos intervalos de 15 minutos, fuso America/Los_Angeles, SPA para posição solar e Spencer para a irradiância extraterrestre. A POA é observada; os ângulos e as grandezas extraterrestres são calculados. Não há medições locais independentes de GHI, DNI e DHI neste recorte. Consulte `resultados/Conferencia_Calculos.json` para hipóteses, verificações e limites.

## Reprodução editorial

Os fontes Beamer compilam com **XeLaTeX**, TikZ, fontspec e as fontes URW Nimbus Roman, localizadas no ambiente de produção em `/usr/share/fonts/opentype/urw-base35/`. Em outro sistema, ajuste o caminho das fontes nos preâmbulos ou instale o pacote equivalente. Compile na pasta `apresentacao/`, mantendo `figuras/` como pasta irmã. Não há sincronização bidirecional entre PDF e PPTX.

Os DOCX contêm equações nativas e solicitam Times New Roman. Os cinco manuscritos usam corpo 12 e títulos/fontes das ilustrações em 10. A 1.1 tem cinco equações destacadas; a integrada tem oito, numeradas sequencialmente entre parênteses à direita, com chamada anterior e definição dos termos depois. As relações curtas no texto permanecem em linha. `documentacao/Catalogo_Equacoes_Manuscrito.json` registra a correspondência. As duas figuras do manuscrito têm título acima e fonte breve abaixo à esquerda; os SVG são vetoriais, com alternativa PNG de 3.600 pixels de largura (pelo menos 600 dpi no tamanho inserido). Os quadros são centralizados, com grade de 1 ponto e todas as três colunas centralizadas.

Os PDFs foram conferidos com a substituta métrica Nimbus Roman disponível no ambiente. Os scripts `editar_manuscritos.py`, `padronizar_manuscritos.py`, `preparar_slides.py` e `materiais_secao_completa.py` registram a produção editorial; `insumos/Base_Manuscrito_1_1.docx` preserva a entrada de 1.1. A etapa de padronização recebe os DOCX recém-gerados pelo editor, antes da exportação em PDF. O script de manutenção `preparar_notebook.py` requer as duas entradas históricas privadas auditadas, enquanto o **notebook entregue é autônomo com os insumos públicos do pacote**.

A célula editorial do notebook e `python src/exportar_editorial.py` geram Word e PDF. Instale antes `pandoc`, `libreoffice-writer`, `texlive-xetex`, `texlive-latex-extra`, `fonts-urw-base35` e `poppler-utils`. O DOCX da 1.1 é revisado com python-docx; Pandoc compõe as novas equações e converte as demais subseções. LibreOffice exporta os PDFs dos manuscritos. Os slides PDF são compilados por XeLaTeX a partir de Beamer. A geração editorial não é uma aplicação integral do ProKnow-C nem uma publicação automática.

Na revisão de formatação, foram reexecutadas apenas as células 1, 9 e 10 do notebook, por IPython local, preservando as saídas científicas anteriores das células 2 a 8. A célula 9 usa `gerar_beamer=False`; cálculos solares, matriz de 39 afirmações, entradas e PPTX foram preservados. A conferência está em `documentacao/Conferencia_Execucao_Editorial.json` e `documentacao/Padronizacao_Editorial_Manuscritos.json`.

Nos seis quadros, o fundo e todas as figuras são pretos, com texto branco e destaques amarelos/cianos. O PPTX mantém SVG e PNG opaco de alta resolução. A conferência inclui uma cópia temporária que força o uso de PNG para verificar compatibilidade.

## Estado da revisão

A curadoria reúne **39 evidências localizadas de cinco PDFs**, com páginas e hashes; apenas o documento NOAA de duas páginas foi lido integralmente. A carteira B herdada contém 12 obras distintas e 23 associações às quatro subseções. A quarta edição de Sengupta (2024) foi conferida como A045; isso não equivale a ler a terceira edição B36 (2021).

As 39 afirmações receberam parecer analítico: 16 diretas, 18 diretas com restrições, uma com derivação e quatro com inferência. B11 foi conferida nas pp. 1 e 9–11, como apoio adicional sobre os limites da inversão; o README B27 foi lido e a citação de B24 foi confirmada em material institucional DOE/NREL, p. 25. B36 foi inspecionada e excluída como prova devido a defeitos no PDF. B19/B20 não foram usadas como prova porque suas edições exatas não estavam no recorte. A matriz distingue essas decisões da leitura efetiva e não conta 39 afirmações como 39 estudos independentes.

O método é uma revisão estruturada **inspirada no ProKnow-C**, com síntese crítica integrativa. A aplicação integral do ProKnow-C **não foi concluída**. O protocolo e os resultados bibliométricos anteriores foram recuperados, sem repetir as buscas. Edições ausentes, textos ainda não lidos e verificações pendentes estão registrados na seleção crítica. PDFs integrais de terceiros e caches privados não integram a publicação.

## Cronograma oficial preservado

29/10: apresentação preliminar de 1.1; 05/11: 1.2 e 1.3; 12/11: 1.4; 19/11: seção revisada; 26/11 a 01/12: revisão cruzada; 03/12: apresentação final. A redação atual antecipa os insumos desses marcos e permanece sujeita à revisão acadêmica do autor e à integração coletiva.
