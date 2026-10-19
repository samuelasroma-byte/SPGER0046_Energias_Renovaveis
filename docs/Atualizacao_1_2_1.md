# Atualização editorial e fundamentação teórica 1.2.1

Esta atualização organiza materiais para a redação do capítulo SPGER0046. Mantém o plano oficial de quatro seções e 19 subseções, os responsáveis e os cinco arquivos originais do PVDAQ 2107.

## Documentos e figuras

Os títulos dos documentos, tabelas, quadros e figuras foram centralizados. As tabelas numéricas continuam editáveis, com fonte 12 e três linhas horizontais; os quadros mantêm a grade completa. A fonte dos resultados foi padronizada para “Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026).”. O ano indica a elaboração, enquanto as observações são de 2024. As referências de método aparecem separadamente.

O Word geral de gráficos incorpora as 30 figuras: 25 gráficos, um fluxograma e quatro esquemas. Os documentos específicos de fluxograma e ilustrações permanecem disponíveis. As versões PDF vetoriais e PNG a 600 dpi, claras e escuras, são as mesmas figuras verificadas anteriormente.

## Dossiê técnico

O dossiê está organizado pelas quatro seções e reúne localização, séries, unidades, conversões, meteorologia, montagem, módulos, inversores, parâmetros CEC, hipóteses e limites de validação. Inclui um apêndice dos 125 canais. Os arquivos CSV/JSON complementares preservam os 2.224 campos finais dos metadados, inventários e estatísticas por canal.

Foram explicitadas a divergência mono-Si/Multi-c-Si entre PVDAQ e CEC, as datas de cadastro distintas, a extensão histórica do JSON e dos CSV, o limite AC e a topologia não comprovados. O canal AC do inversor 15 foi associado pelo identificador único 149653, preservando os dois nomes originais.

## Levantamento para fundamentação

O notebook multibase WCNPS da pasta Artigo/Bibliometria foi usado como referência de estrutura e nomes de Secrets; o arquivo original não foi modificado. A adaptação busca fundamentação por tópico, sem busca de lacuna. A coleta efetiva utilizou Crossref e OpenAlex. Scopus, Web of Science e IEEE Xplore estão implementados, mas não foram consultados aqui porque seus Secrets pertencem ao ambiente Colab do usuário.

O retrato contém 829 obras deduplicadas e 39 prioritárias, incluindo três livros, distribuídas pelos 19 tópicos. As contagens de citações permanecem separadas por base e data. O ranking se restringe aos resultados recuperados e filtrados. Metadados e resumos orientaram a seleção; a leitura integral, a indicação de páginas e a redação são etapas do grupo.

A segunda edição do Handbook of Photovoltaic Science and Engineering foi conferida no frontispício da Wiley, DOI 10.1002/9780470974704.fmatter. O valor indexado foi preservado, e a edição e a função de editores foram corrigidas nas referências e exportações.

## Execução e continuidade

O notebook físico preserva 25 células executadas; o bibliográfico contém 24. Os resultados físicos não foram recalibrados nesta atualização. Os dados AC locais continuam como referência para a comparação do modelo; não constituem validação independente de componentes reconstruídas ou do cenário BIPV.

O pacote completo inclui código, configurações, respostas bibliográficas, dados e documentos. O pacote preparado para GitHub contém ambos os notebooks com saídas removidas, sem respostas brutas bibliográficas nem dados originais volumosos. A publicação no GitHub é uma etapa posterior.
