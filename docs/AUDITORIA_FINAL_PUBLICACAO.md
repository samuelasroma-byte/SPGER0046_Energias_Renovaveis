# Estrutura fontes e integridade do projeto

O projeto SPGER0046 reúne o estudo PVDAQ 2107, organizado em quatro seções e 19 subseções. A [proposta oficial](planejamento/Proposta_do_Capitulo_Recurso_Solar_FV.docx) define o escopo, os responsáveis e o cronograma. A [estrutura em JSON](estrutura_oficial_19_subsecoes.json) e a [matriz do capítulo](Matriz_19_Subsecoes.md) relacionam métodos, resultados e fontes.

## Materiais do capítulo

| Material | Identificação e acesso |
| --- | --- |
| Bibliografia prioritária | [39 referências B01–B39](../bibliografia/principal/README.md) e [correspondência B → A](../bibliografia/principal/Correspondencia_B_A.csv) |
| Acervo complementar | [91 documentos A](../references/README.md), distribuídos em 160 cópias de consulta |
| Ilustrações | [30 itens](../figuras/README.md): 25 gráficos, um fluxograma e quatro esquemas; 120 arquivos PNG/PDF |
| Tabelas e quadros | [16 tabelas e seis quadros](../outputs/tabelas/README.md), com documentos por seção |
| Equações | [61 relações](equacoes/README.md), com função, símbolos, unidades, aplicação e fonte no código |
| Dados e equipamentos | [Quatro CSVs brutos e metadados](../data/raw/README.md), 125 canais e inventários da instalação |
| Documentos técnicos | [Guia, dossiê, planejamento e quadros](README.md) |
| Reprodução | [Rotinas, dependências e convenções](REPRODUTIBILIDADE.md) |

O caso compreende abril a junho de 2024, em Arbuckle, Califórnia. POA, temperatura do ar e vento alimentam o modelo físico; a potência CA medida é a referência de avaliação. As hipóteses e os limites dos cenários constam no [dossiê](metodos/README.md).

## Distribuição por seção

| Seção | Responsáveis | Ilustrações | Tabelas lógicas | Quadros | Equações |
| --- | --- | --- | --- | --- | --- |
| 1 Recurso solar | Samuel | 4 | 0 | 2 | 6 |
| 2 Condições ambientais | Vannessa e Thais | 4 | 4 | 1 | 7 |
| 3 Modelagem fotovoltaica | Gabriela e Giulia | 9 | 3 | 2 | 18 |
| 4 Desempenho e validação | Júlia Ribeiro e Lucas Simão | 13 | 9 | 1 | 30 |
| Total | | 30 | 16 | 6 | 61 |

O [mapa editorial](Distribuicao_Editorial.md) e a [política de distribuição](../config/distribuicao_editorial.json) atribuem cada material a uma subseção. A Tabela 16 possui quatro partes de continuação; são 19 blocos de tabela para 16 tabelas lógicas. Os formatos PNG/PDF e os temas claro/escuro representam o mesmo item.

## Equações e convenções

O inventário distingue 37 relações das células de método do notebook e 24 relações complementares do código. As duas definições de constantes não integram a contagem. O modelo de Faiman corresponde a E3.03, em 3.2; a subseção 2.1 utiliza essa referência.

As 61 relações incluem 241 definições contextualizadas de símbolos. O campo de aplicação distingue conversão principal, estatísticas, indicadores, fundamentos, ilustrações, transposição, comparação CC PVWatts, ajuste empírico e balanço BIPV. Os documentos estão disponíveis em Word editável e PDF.

As convenções cobrem as unidades de U0 e U1, a conversão W/kW na integração, a irradiância de referência, os significados de ηref e γ, a potência do exemplo de 120 módulos e a do sistema de 2.880 módulos. Os termos Q do balanço BIPV representam potências em W. O modelo A usa POA medida, atenuação assumida, Faiman, CEC de diodo único, perdas CC, inversor PVWatts e perdas CA.

## Proveniência e integridade

O [inventário de origem](auditoria/Proveniencia_Arquivos_Integrados.csv) contém 156 registros, incluindo dez documentos Word, dois notebooks executados, quatro CSVs brutos, relatórios e 120 arquivos gráficos. Os hashes de origem correspondem às fontes arquivadas no [commit de integração](https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis/commit/d24eb3791fc08d4250e711f308742f7a20b7767d). A relação entre fontes e documentos de consulta consta em [Edicoes_Documentais.json](auditoria/Edicoes_Documentais.json).

Os dados brutos são conferidos pelo [manifesto PVDAQ](../data/raw/fontes_pvdaq.json). O conjunto está identificado pelo DOI [10.25984/1846021](https://doi.org/10.25984/1846021), com licença CC BY 4.0 no [OEDI](https://data.openei.org/submissions/4568) e no [Data.gov](https://catalog.data.gov/dataset/photovoltaic-data-acquisition-pvdaq-public-datasets). Os PNG têm 600 dpi e os PDF contêm elementos vetoriais.

O [guia técnico](metodos/Guia_Tecnico_Resumido_PVDAQ_2107.docx) apresenta a origem, o período, os equipamentos e as hipóteses comuns. O cadastro registra 19 grupos de 120 módulos, um de 160, um de 200 e três de 80, totalizando 2.880 módulos. A associação 20×6 é um exemplo didático.

## Bibliografia e acesso

O levantamento contém 829 obras únicas, 295 associações temáticas e 102 associações prioritárias, referentes a 39 obras B. As contagens de citações são identificadas por base e data. A seleção utiliza metadados e resumos e requer leitura das obras para sustentar afirmações e páginas citadas.

B19 é Kalogirou, segunda edição de 2014, sem PDF integral localizado. B20 é Luque e Hegedus, segunda edição de 2011, também pendente na íntegra; A034 é a primeira edição de 2003. N01 é a norma IEC 61724-1:2021, separada das 39 referências B e pendente. As [fontes alternativas](../references/Alternativas_e_Acesso.md) têm códigos próprios.

O inventário do Drive abrange 722 itens: 605 arquivos e 117 pastas. Destes arquivos, 156 têm correspondência com materiais do repositório e 449 são externos. Os externos incluem cópias distribuídas, pacotes, fontes bibliográficas e dados IFES; a contagem é de arquivos, não de obras distintas. PDFs de terceiros são acessados pelos índices, conforme as condições de uso.

O acesso ao repositório público permite leitura e download. A edição depende de conta com permissão e convite aceito; no Drive, prevalecem as permissões de cada arquivo. [Acesso e colaboração](ACESSO_E_COLABORACAO.md).

## Inventários e verificações

- [Figuras, legendas, resoluções e caminhos](auditoria/Inventario_Figuras.csv).
- [Distribuição das tabelas pelas subseções](auditoria/Distribuicao_Tabelas.csv).
- [Inventário do Drive](auditoria/Inventario_Drive_Completo.csv).
- [Arquivos externos](auditoria/Arquivos_Mantidos_Externamente.csv) e [registro de permissões](auditoria/Permissoes_Drive_Verificadas.csv).
- [Fontes por arquivo](auditoria/Materializacao_Remota.json) e [verificação de integridade na integração](auditoria/Verificacao_Remota_Arquivos.json).
- [Downloads públicos](auditoria/Verificacao_Downloads_Publicos.json): 24 arquivos, 90.889.009 bytes, HTTP 200 e hashes correspondentes ao commit de origem.
- [Testes científicos e ambiente](auditoria/Verificacao_Cientifica_Publicacao.json): entradas e observações separadas, grade temporal comum, métricas, energia e inversão exploratória.
- [Documentos, tabelas e gráficos](auditoria/Verificacao_Refinamento_Integracao.json) e [distribuição editorial](auditoria/Verificacao_Distribuicao_Editorial.json).
- [Guia técnico](auditoria/Guia_Tecnico_Resumido_Verificacao.json), [inventário de equações](auditoria/Verificacao_Inventario_Equacoes.json), [símbolos e unidades](auditoria/Revisao_Unidades_Equacoes.json) e [acesso aos documentos](auditoria/Verificacao_Acesso_Equacoes.json).
- [Arquivos de equações no Drive](auditoria/Publicacao_Drive_Equacoes.json) e [referências bibliográficas](auditoria/Publicacao_Referencias_PVDAQ.json).

As rotinas `verificar_organizacao.py`, `verificar_ciencia.py`, `verificar_refinamento.py`, `verificar_distribuicao_editorial.py`, `verificar_inventario_equacoes.py` e `verificar_acesso_equacoes.py` documentam os contratos científicos e documentais. O [ZIP do projeto](ENTREGA_ZIP.md) contém a identificação da revisão e o manifesto SHA-256 dos arquivos.
