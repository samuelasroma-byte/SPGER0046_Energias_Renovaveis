# Fundamentação teórica por seção e subseção

Este levantamento apoia a redação das quatro seções do capítulo fotovoltaico SPGER0046 UFPB. O notebook adapta o modelo multibase do WCNPS em Artigo/Bibliometria para indicar livros, artigos, relatórios e fontes de método por tópico. Não procura uma lacuna e não se apresenta como revisão sistemática ou leitura integral automática.

## Comece pelas leituras selecionadas

Abra outputs/Referencias_por_Subsecao.docx: quatro quadros mapeiam os 19 tópicos aos códigos B01 a B39, que levam às referências completas em ordem alfabética. Cada referência ocupa seu próprio bloco e informa as subseções de aplicação. O texto nativo usa Times New Roman 12; as referências têm entrelinhas simples, separação de 12 pontos e o recuo francês de 1,25 cm solicitado pela equipe. Consulte também os quatro arquivos Markdown em outputs/por_secao. Eles relacionam cada obra à subseção, à finalidade de leitura e ao responsável do plano. O arquivo outputs/obras_prioritarias.csv permite filtrar, e os arquivos BibTeX e RIS apoiam a organização das citações.

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

Os cinco clientes estão implementados. Nesta execução, Crossref e OpenAlex forneceram registros. As chaves Scopus, WOS e IEEE ficam nos Secrets do Colab do usuário e não estavam disponíveis neste ambiente. O estado de cada base aparece em outputs/logs/estado_bases.csv; não se afirma que as três bases institucionais foram consultadas nesta execução.

No Colab, use os nomes já adotados pelo notebook WCNPS: OPENALEX_API_KEY, SCOPUS_API_KEY, WOS_API_KEY e IEEE_API_KEY. Também são aceitas variáveis de ambiente com esses nomes. Nenhuma chave é exibida, incluída nas respostas em cache ou exportada. Ter uma chave não garante a mesma cobertura ou licença de uma base institucional.

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

O notebook WCNPS original permanece preservado. Este código e as referências podem ser incorporados ao repositório do grupo na etapa de integração com GitHub.
