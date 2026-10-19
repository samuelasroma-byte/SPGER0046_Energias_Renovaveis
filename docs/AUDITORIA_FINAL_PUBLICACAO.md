# Auditoria da reorganização e publicação — SPGER0046

Data: 19/10/2026. Repositório público: [SPGER0046_Energias_Renovaveis](https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis).

## Conteúdo científico integrado

A proposta oficial foi lida integralmente e seus 19 títulos foram transcritos para a navegação. As quatro seções conservam a divisão Samuel; Vannessa e Thais; Gabriela e Giulia; Júlia Ribeiro e Lucas Simão. A divisão de 4.1/4.5 para Júlia e 4.2–4.4 para Lucas também foi preservada. O documento anterior de arquitetura contém 17 subseções e permanece arquivado, sem substituir a proposta atual.

- [Proposta original em Word](planejamento/Proposta_do_Capitulo_Recurso_Solar_FV.docx).
- [Estrutura oficial em JSON](estrutura_oficial_19_subsecoes.json) e [matriz das 19 subseções](Matriz_19_Subsecoes.md).
- [Bibliografia principal B01–B39](../bibliografia/principal/README.md) e [correspondência B → A](../bibliografia/principal/Correspondencia_B_A.csv).
- [91 documentos A complementares](../references/README.md).
- [30 ilustrações, 120 PNG/PDF finais](../figuras/README.md).
- [Documentos Word](README.md), [tabelas](../outputs/tabelas/README.md) e [reprodução](REPRODUTIBILIDADE.md).

## Integridade e fontes

Foram recuperadas e integradas 156 cópias de arquivos de origem, com tamanho e SHA-256 registrados. Entre elas estão dez DOCX originais, dois notebooks executados, quatro CSVs brutos completos, tabelas que faltavam, relatórios e os 120 arquivos gráficos finais. Os PNG foram conferidos em 600 dpi; os PDFs conservaram os elementos vetoriais. Os gráficos não foram regenerados.

O conteúdo existente de `src`, `config`, dados preparados, tabelas numéricas já publicadas e catálogos bibliométricos foi preservado. As adaptações dos testes limitam-se às novas localizações dos arquivos, à inclusão do Word completo dos gráficos e ao uso de diretório temporário para não reescrever as saídas entregues. Não foram alteradas hipóteses, equações ou métricas de referência.

Os originais executados dos notebooks permanecem acessíveis junto aos notebooks de trabalho. O manifesto `checksums_sha256.json` anterior é um registro histórico do pacote anterior; os novos inventários distinguem essa versão dos arquivos atuais. A varredura de credenciais, incluindo pacotes de apoio embutidos nos notebooks, não encontrou padrões de tokens, chaves de acesso ou chaves privadas.

## Bibliografia

Os números do levantamento foram confirmados nos arquivos originais: 829 obras únicas, 295 associações temáticas, 102 prioritárias e 39 obras B distintas. As 102 associações do Word correspondem às 102 associações do CSV. Referências ABNT, tipos de obra, contagens de citações, bases e datas foram preservados; não há alegação de leitura integral ou revisão sistemática concluída.

B19, Kalogirou 2014, continua sem PDF da 2ª edição. B20, Luque e Hegedus 2011, continua sem PDF integral da 2ª edição; A034 é a 1ª edição de 2003. N01, IEC 61724-1:2021, segue separada e pendente. As edições e fontes alternativas estão identificadas sem substituições silenciosas.

## Materiais externos e permissões

A árvore do Drive contém 722 itens, sendo 605 arquivos e 117 pastas. Todos os 605 arquivos tiveram metadados de permissão consultados nesta auditoria: `anyone/reader`. Nenhuma permissão de edição foi ampliada. A permissão por link não transfere direitos autorais nem concede edição no GitHub.

Dos 605 arquivos de origem, 156 têm cópias integrais identificadas nesta integração e 449 permanecem listados individualmente como externos. A contagem externa inclui cópias distribuídas, pacotes, versões anteriores, fontes bibliográficas e dados IFES fora do caso principal; não representa 449 obras distintas nem 449 falhas.

- [Graficos_do_Projeto.docx](../outputs/graficos/docx/Graficos_do_Projeto.docx): 14.465.317 bytes, original integral incluído pelo Git. Os 25 gráficos também estão disponíveis separadamente em todos os formatos e temas.
- [2107_electrical_data_2024.csv](../data/raw/2107_electrical_data_2024.csv): 63.287.121 bytes, original integral incluído pelo Git. Os quatro CSVs estão no repositório e mantêm fontes oficiais e hashes no [índice de dados](../data/raw/README.md).
- PDFs bibliográficos de terceiros: mantidos em links individuais enquanto a autorização de redistribuição pública não estiver comprovada. Não foram republicados como se fossem documentos autorais.

O conjunto PVDAQ está identificado por DOI 10.25984/1846021, com licença CC BY 4.0 no [registro oficial Data.gov](https://catalog.data.gov/dataset/photovoltaic-data-acquisition-pvdaq-public-datasets) e no [OEDI](https://data.openei.org/submissions/4568), consultados em 19/10/2026. Os CSVs publicados mantêm a atribuição e os hashes originais.

A conexão GitHub confirmou leitura e escrita para o proprietário. Os nomes GitHub dos seis integrantes não foram fornecidos nesta missão; o estado dos convites individuais permanece por confirmar. O acesso público permite leitura e download, e edição depende de convite aceito ou contribuição por pull request.

## Inventários e evidências

- [Proveniência, arquivos reais e SHA-256](auditoria/Proveniencia_Arquivos_Integrados.csv).
- [Figuras, legendas, resoluções e caminhos](auditoria/Inventario_Figuras.csv).
- [Distribuição das tabelas pelas subseções](auditoria/Distribuicao_Tabelas.csv).
- [Inventário completo do Drive](auditoria/Inventario_Drive_Completo.csv).
- [Arquivos mantidos externamente e motivos](auditoria/Arquivos_Mantidos_Externamente.csv).
- [Permissões individuais dos 605 arquivos](auditoria/Permissoes_Drive_Verificadas.csv).

## Verificação remota e entrega

A recuperação dos originais terminou com sucesso no [GitHub Actions, execução 39245482869](https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis/actions/runs/39245482869). O commit [d24eb3791fc08d4250e711f308742f7a20b7767d](https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis/commit/d24eb3791fc08d4250e711f308742f7a20b7767d) contém as 156 cópias originais conferidas: 95 já estavam presentes e 61 foram recuperadas e incluídas. O envio pelo GitHub Actions resolveu a limitação de tamanho do transporte anterior e manteve os originais completos.

A cópia obtida novamente do GitHub passou pela auditoria de estrutura, navegação e integridade. Foram conferidos 19 diretórios de subseções, as referências B01–B39, os 91 documentos A catalogados, 120 PNG/PDF finais, dez DOCX e todos os tamanhos e SHA-256 das 156 cópias. Não houve divergência de bytes nem link relativo quebrado. Os diretórios científicos `src`, `config`, `data/processed`, `outputs/series` e `outputs/avaliacao` são idênticos à base anterior `5c1ba24c334ae65c05da29ef7d30c9efd53fc2ca`.

Foram realizados 24 downloads públicos sem autenticação, totalizando 90.889.009 bytes: os dez documentos Word, os dois notebooks executados, os quatro CSVs completos e oito amostras PNG/PDF distribuídas pelas quatro seções. Todos retornaram HTTP 200 e coincidiram com o tamanho e SHA-256 esperados, incluindo o Word de 14,5 MB e o CSV elétrico de 63,3 MB. Esses testes usam URLs permanentes do commit, preservando a evidência mesmo após novas revisões.

Os testes `verificar_organizacao.py`, `verificar_ciencia.py` e `verificar_refinamento.py` passaram. A verificação científica incluiu separação entre entradas e observações, grade temporal comum, métricas recalculadas, conservação de energia e execução física com e sem o caminho exploratório de inversão. Os arquivos finais mantêm 600 dpi nos PNG, elementos vetoriais nos PDF e tabelas editáveis nos Word.

- [Resultado da recuperação, arquivo por arquivo](auditoria/Materializacao_Remota.json).
- [Auditoria executada no GitHub](auditoria/Verificacao_Remota_Arquivos.json).
- [Evidência dos 24 downloads públicos](auditoria/Verificacao_Downloads_Publicos.json).
- [Testes científicos e versões do ambiente](auditoria/Verificacao_Cientifica_Publicacao.json).
- [Verificação dos documentos, tabelas e 120 gráficos](auditoria/Verificacao_Refinamento_Integracao.json).
- [PR de integração da entrega à main](https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis/pull/1).

O [índice de documentos](README.md) oferece download direto dos dez Word. O projeto completo pode ser obtido em [ZIP da main](https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis/archive/refs/heads/main.zip). Leitura e download dos arquivos publicados são públicos. As pendências de edições bibliográficas, da norma N01 e dos convites de edição estão identificadas acima e não são apresentadas como resolvidas.

## Guia técnico de orientação da equipe

Em 19/10/2026 foi acrescentado o [guia técnico resumido do PVDAQ 2107 em Word](metodos/Guia_Tecnico_Resumido_PVDAQ_2107.docx), com três páginas e links para os dados, equipamentos, configuração e dossiê completo. É uma síntese nova para as quatro seções; as dez cópias DOCX originais e os 156 arquivos de origem permanecem intactos. A revisão conferiu a distribuição real dos grupos no JSON original: 19×120, 1×160, 1×200 e 3×80, totalizando 2.880 módulos. A orientação e o esclarecimento sobre a simplificação do dossiê original estão no [índice de métodos](metodos/README.md). O [registro de verificação do guia](auditoria/Guia_Tecnico_Resumido_Verificacao.json) contém tamanho, SHA-256, fontes e revisão visual das três páginas.

## Correção de repetições na distribuição editorial

Em 19/10/2026, a revisão comparou a proposta oficial, o notebook e os índices. As 30 ilustrações tinham 44 indicações nos índices das quatro seções; 11 itens apareciam em mais de uma seção. A pertinência temática múltipla foi substituída por uma única subseção de inserção para cada figura, gráfico, tabela e quadro. O [mapa editorial](Distribuicao_Editorial.md) e a [política em JSON](../config/distribuicao_editorial.json) registram as atribuições.

| Seção | Ilustrações | Tabelas lógicas Word | Quadros |
| --- | --- | --- | --- |
| 1 — recurso solar | 4 | 0 | 2 |
| 2 — ambiente | 4 | 4 | 1 |
| 3 — modelagem | 9 | 3 | 2 |
| 4 — desempenho e validação | 13 | 9 | 1 |
| Total | 30 | 16 | 6 |

Seis ilustrações foram movidas para suas seções responsáveis, totalizando 24 arquivos PNG/PDF realocados sem mudar seus bytes. As 120 exportações finais, os 24 CSVs, as 156 cópias de origem e os dez Word originais permanecem íntegros. A Tabela 16 é um único item com quatro blocos de continuação; os 19 blocos XML do Word original não representam 19 tabelas distintas.

Foram acrescentados quatro Word editáveis, cada um contendo somente as tabelas e quadros da respectiva seção. Os valores das células numéricas coincidem integralmente com os originais. Nos quadros de planejamento derivados, apenas as listas de figuras foram alinhadas à atribuição exclusiva. As 21 páginas dos quatro documentos foram renderizadas e inspecionadas; os documentos consolidados originais permanecem como consulta histórica.

Os 19 índices de subseção, os quatro índices de seção, o catálogo, a matriz, o notebook de trabalho, seu pacote de apoio e o gerador HTML usam a mesma atribuição. O teste executou as 19 células de apresentação sobre o cálculo físico em diretório temporário e conferiu 30 inclusões únicas no HTML, ausência de vínculos a ilustrações de outras seções e ausência de repetição nos documentos tabulares por seção. Os testes de organização, ciência e refinamento também passaram. Hipóteses físicas, equações, dados brutos, dados preparados e saídas numéricas não foram alterados.

[Verificação da distribuição editorial](auditoria/Verificacao_Distribuicao_Editorial.json) · [Teste reproduzível](../tests/verificar_distribuicao_editorial.py). Em outras partes do capítulo, citar o ID já inserido; os temas claro/escuro e os formatos PNG/PDF são alternativas de um mesmo item.

## Inventário de equações das 19 subseções

Em 19/10/2026 foi concluído o [inventário de equações](equacoes/README.md), com um Word geral e quatro Word exclusivos por seção. O levantamento identificou 38 ocorrências de relações no notebook, correspondentes a 37 relações distintas porque Faiman aparecia em 2.1 e 3.2. A equação recebe um único ID E3.03 e local de inserção em 3.2; em 2.1 deve ser citada por remissão. As duas definições de constantes não foram contadas como equações adicionais.

Os quadros distinguem o núcleo N, de 37 relações, das 24 relações de apoio C verificadas no código. Cada linha informa ID, subseção de inserção, equação nativa editável, função, símbolos e referências metodológicas. Os itens de apoio documentam o método e não impõem a inclusão de todas as 61 relações no texto final. A distribuição total é de 6, 7, 18 e 30 relações nas seções 1 a 4, respectivamente.

O teste conferiu a cobertura das 19 subseções, as 37 relações distintas do notebook, a localização das funções citadas, as 61 equações nativas no documento geral e a distribuição sem repetição dos IDs entre os quatro documentos individuais. Os modelos, parâmetros, dados brutos, dados preparados e resultados numéricos permanecem inalterados. [Registro da verificação](auditoria/Verificacao_Inventario_Equacoes.json) · [Teste reproduzível](../tests/verificar_inventario_equacoes.py).

As 31 páginas finais foram renderizadas e inspecionadas: 13 no documento geral e 3, 3, 5 e 7 nos documentos das seções 1 a 4. As barras de média foram normalizadas como construções nativas do Word para preservar sua aparência no renderizador. As cinco cópias foram salvas na [pasta de equações do Google Drive](https://drive.google.com/drive/folders/1yfwwArqBTVwPt7EYer9DlHL1vmeO5V7B), dentro do planejamento da equipe, e baixadas novamente para conferência integral de SHA-256. [Comprovante das cinco cópias](auditoria/Publicacao_Drive_Equacoes.json).
