# Fundamentação teórica por seção e subseção

O levantamento bibliográfico apoia as quatro seções e 19 subseções do capítulo SPGER0046, com livros, artigos, relatórios e fontes metodológicas. A seleção utiliza metadados e resumos; não constitui revisão sistemática nem substitui a leitura integral das obras citadas.

## Comece pelas leituras selecionadas

O [guia bibliográfico](atualizada/README.md) relaciona as 19 subseções às 39 referências B01–B39, com responsáveis e aplicação. Os quatro arquivos Markdown em outputs/por_secao detalham finalidade de leitura e distribuição. O arquivo outputs/obras_prioritarias.csv permite filtrar as obras; BibTeX e RIS apoiam a organização das citações.

O catálogo consolidado contém todos os resultados recuperados. Ele inclui candidatos fora da seleção final para preservar a rastreabilidade. A seleção de leitura é menor e usa critérios específicos de título, assunto, fonte de método e complemento recente. O grupo deve ler os textos antes de citar uma conclusão, equação ou página.

## Como foi feita a seleção

1. Preservar os 19 tópicos do plano e explicitar suas consultas.
2. Acrescentar sementes de livros, métodos utilizados e relatórios técnicos. As obras são resolvidas por DOI ou título; os DOI novos e títulos são conferidos nos índices consultados.
3. Consultar Crossref e OpenAlex, incluindo um recorte recente de 2021 a 2026 ordenado por citações. Os limites por consulta estão em protocolo.json.
4. Deduplicar primeiro por DOI normalizado. Sem DOI, usar título normalizado e ano; não unir edições diferentes por semelhança vaga. O relatório NREL de Marion e o artigo de congresso correspondente compartilham o DOI conhecido.
5. Filtrar candidatos por termos específicos no título, evitando promover trabalhos de física solar ou materiais de célula a referências sobre recurso terrestre ou inversores.
6. Combinar livro de base, fontes do método, trabalhos muito citados no conjunto recuperado e complemento recente. Candidatos recentes sem semente exigem pelo menos dez citações no OpenAlex; isso não é certificação de qualidade.

As contagens de OpenAlex, Crossref, Scopus, Web of Science e IEEE permanecem em colunas distintas, com a data da consulta. Elas não são somadas. Campo vazio significa indisponível; não foi substituído por zero. O ranking de mais citados vale para o conjunto recuperado e filtrado, não para toda a literatura mundial. Livros, edições, relatórios e artigos têm coberturas bibliométricas diferentes.

O Handbook of Photovoltaic Science and Engineering é referenciado pela edição com copyright 2011; o índice registra seu lançamento eletrônico em dezembro de 2010. Ambos os anos ficam documentados no catálogo quando disponíveis.

## Bases e credenciais

Crossref e OpenAlex forneceram os registros da coleta. Os clientes Scopus, Web of Science e IEEE Xplore requerem credenciais e não foram utilizados na coleta registrada. O estado de cada base está em outputs/logs/estado_bases.csv.

No Colab, configurar as credenciais OPENALEX_API_KEY, SCOPUS_API_KEY, WOS_API_KEY e IEEE_API_KEY nos Secrets ou nas variáveis de ambiente. As credenciais não integram os resultados exportados; o acesso depende da licença de cada base.

## Executar novamente

Abra 02_Fundamentacao_Teorica_por_Subsecao.ipynb e execute as células na ordem. O notebook já está executado para consulta dos resultados. NOVA_COLETA=False reaproveita o retrato armazenado e as datas originais de consulta. NOVA_COLETA=True cria uma pasta datada de respostas e atualiza a data final do protocolo para uma coleta nova. CONSULTAR_REDE=False permite reproduzir apenas os arquivos em cache.

Pela linha de comando, na raiz do projeto:

    python scripts/construir_notebook_fundamentacao.py
    python scripts/executar_notebook.py --notebook bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb

## Arquivos e origem

- temas.json: tópico, consulta, responsável e vínculo com o plano.
- sementes.json: obras de base e finalidade de uso.
- protocolo.json: escopo, limites e identificação do notebook WCNPS usado como modelo.
- formatacao_abnt.py e word_referencias_abnt.py: formatação compartilhada e organização do guia Word.
- raw/: respostas bibliográficas originais, com fonte e instante de coleta.
- outputs/catalogo_consolidado.csv: todos os candidatos deduplicados.
- outputs/catalogo_por_subsecao.csv: candidatos que passaram no filtro por tópico.
- outputs/obras_prioritarias.csv e leituras_prioritarias.json: seleção orientadora de leitura.
- outputs/top_citados_por_subsecao.csv: ranking dentro dos resultados recuperados.
- outputs/complementos_recentes.csv: recorte recente elegível.
- outputs/por_secao/: quatro listas Markdown e CSV.
- outputs/logs/: consultas, estado das bases e resolução das sementes.
- outputs/referencias_fundamentacao.bib e .ris: exportações bibliográficas.

Documentação dos serviços: https://help.openalex.org/api/ ; https://www.crossref.org/documentation/retrieve-metadata/rest-api/ ; https://dev.elsevier.com/documentation/SCOPUSSearchAPI.wadl ; https://developer.clarivate.com/apis/wos-starter ; https://developer.ieee.org/docs/ .

O protocolo registra a estrutura multibase usada como referência. Os resultados do levantamento e os índices por seção estão disponíveis neste repositório.
