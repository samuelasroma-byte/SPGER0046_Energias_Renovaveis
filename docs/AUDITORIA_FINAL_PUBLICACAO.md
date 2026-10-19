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

## Verificação remota

A integração está preparada na branch `integracao/reorganizacao-cientifica-20261019`, a partir de `5c1ba24c334ae65c05da29ef7d30c9efd53fc2ca`. A publicação, os downloads de amostras, a comparação da árvore remota e a incorporação à `main` estão em execução. Este trecho será atualizado com os resultados efetivamente observados antes da entrega final.
