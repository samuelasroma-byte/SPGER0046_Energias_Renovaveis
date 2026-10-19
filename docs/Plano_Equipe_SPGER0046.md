# Plano da equipe para construir o capítulo SPGER0046

Recurso solar e modelagem da conversão fotovoltaica. Levantamento e proposta de trabalho em 18 de outubro de 2026. A divisão de seções e as datas abaixo vêm da proposta atual do grupo. A organização operacional é uma recomendação para discussão da equipe.

## Decisão de trabalho

Podemos iniciar a leitura e a redação com o acervo já disponível. Há fontes de base, artigos, trabalhos acadêmicos, dados observacionais e uma cadeia computacional executada que cobre as 19 subseções. Isso permite começar; a seleção das afirmações, a leitura crítica e a conferência das páginas citadas ainda cabem à equipe. A obtenção das edições exatas de B19 e B20 e da norma N01 deixa de ser condição para iniciar a escrita. Não se declarará conformidade normativa sem examinar os requisitos da norma.

Recomendo Drive e GitHub em conjunto. O Drive conserva a biblioteca de PDFs, os dados brutos, as versões gráficas e a redação compartilhada. O GitHub organiza o código, a configuração, os catálogos, os resultados selecionados e o histórico de revisões. Cada integrante terá uma entrada própria, mas as quatro seções usarão a mesma instalação, janela temporal e cadeia de dados.

## Onde ficaram os dois PDFs retirados

Eles não foram enviados à lixeira. Permanecem na pasta de materiais retirados (consulta no acervo da equipe), na raiz do Drive. Os dois originais são Solar_Energy_Engineering-Processes_and_Systems.pdf e pdf68.pdf. O primeiro é Kalogirou 2009, outra edição, sem folhas iniciais; o segundo contém apenas parte de Luque e Hegedus 2011. Sete cópias derivadas estão nas quatro subpastas Secao_01 a Secao_04. São duas obras, dois originais e sete cópias, totalizando nove arquivos PDF preservados. A090 e A091 ficam fora do acervo ativo.

## Acervo ativo conferido

| Material | Documentos distintos |
| --- | --- |
| Artigos | 63 |
| Livros | 9 |
| Dissertações | 3 |
| Teses | 3 |
| Relatórios e manuais | 12 |
| TCC | 1 |
| Normas técnicas | 0 |
| Total | 91 |


As 160 cópias nas 28 pastas de referências conferem, por identificador, com o catálogo atual: nenhum arquivo esperado ausente e nenhum extra nessas pastas. Uma obra útil a duas seções aparece em ambas, mas só conta uma vez entre os 91 documentos. Os nove livros incluem edições diferentes de uma mesma obra; a unidade desta contagem é o documento catalogado. O TCC é de Filipe Tawã Gomes, sobre microclima e placas fotovoltaicas. Não contamos o levantamento de 829 registros bibliográficos como PDFs disponíveis, nem incluímos dados, notebooks ou relatórios gerados nessa contagem.

| Seção | Responsáveis | Artigos | Livros | Diss. | Teses | Rel./manuais | TCC | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Samuel | 30 | 6 | 0 | 1 | 5 | 0 | 42 |
| 2 | Vannessa e Thais | 23 | 9 | 3 | 2 | 2 | 1 | 40 |
| 3 | Gabriela e Giulia | 17 | 7 | 2 | 3 | 8 | 0 | 37 |
| 4 | Júlia Ribeiro e Lucas Simão | 25 | 6 | 3 | 2 | 5 | 0 | 41 |


As cópias ocupam aproximadamente 1,12 GB; os documentos distintos somam aproximadamente 520,5 MB. Isso justifica usar links no GitHub. Os dois PDFs retirados estão excluídos desses totais. A contagem se refere ao acervo ativo do capítulo (consulta no acervo da equipe), e não a todos os arquivos de todo o Drive. A norma IEC 61724-1:2021 permanece ausente. O relatório A093 é apoio técnico e não é norma.

## Qual é o estudo que já existe

O projeto principal é Farm Solar Array, PVDAQ 2107, em Arbuckle, Califórnia, Estados Unidos. A configuração v1.2.2 seleciona de 1º de abril a 30 de junho de 2024, com fim exclusivo em 1º de julho, no fuso America/Los_Angeles. São 91 dias. Os índices exportados usam UTC; datas e horas locais devem ser identificadas nas legendas. O ano 2026 na fonte das figuras indica elaboração, não observação.

Os arquivos originais contêm observações além desse trimestre. Os limites dos quatro CSVs foram conferidos diretamente: as séries começam em janeiro e terminam em novembro de 2024, em datas distintas. Portanto, existir um arquivo com 2024 no nome não comprova um ano inteiro comum entre sensores. O recorte do estudo é definido pela configuração, não pelo nome do arquivo.

Entradas observacionais principais: irradiância no plano dos módulos, chamada POA, temperatura do ar e vento, medidos junto à instalação. O modelo estima temperatura operacional, potência do módulo, potência CC do arranjo, conversão no inversor, potência CA e energia. A potência CA medida pelo medidor local é a referência de comparação, não entrada da previsão física. NASA POWER não entra na cadeia principal atual; seus arquivos foram preservados como histórico.

Há 8.736 intervalos de 15 minutos no trimestre e 8.736 registros do medidor. A avaliação diurna usa 4.401 pares de 4.421 intervalos elegíveis, disponibilidade conjunta de 99,55%. POA e inversores são agregados de 5 para 15 minutos com exigência de três amostras por intervalo. O código não preenche lacunas. As 25 células de código do notebook consultado têm execução registrada e não apresentam saídas de erro. Nesta conferência foram lidos código, configuração, arquivos originais e resultados salvos; não se executou novamente a simulação.

O notebook registra RMSE de 61,59 kW, MAE de 50,30 kW, MBE de +31,77 kW, nRMSE de 14,99%, r de 0,9774 e R² de 0,9200 para o modelo físico sem escala empírica. O nRMSE usa a média observada dos mesmos pares. A alta correlação não elimina o viés. Um fator empírico é ajustado somente em abril; maio e junho são avaliações posteriores da mesma instalação. O texto deve manter esses resultados separados.

### Medição e cálculo

| Elemento | Natureza | O que a equipe pode afirmar |
| --- | --- | --- |
| POA, temperatura do ar, vento e potência CA | Medições locais | Existem entradas ambientais e geração observada para a comparação agregada |
| Temperatura operacional e curvas I–V e P–V | Modelos | Mostram comportamento calculado; não são ensaios medidos do módulo |
| GHI, DNI e DHI | Reconstrução exploratória da POA | Servem a exercícios de transposição; não têm validação local independente |
| Albedo, sujidade, ventilação e limite CA | Hipóteses ou sensibilidades | Explicitar valores e limites; o resíduo não identifica sozinho cada perda real |
| Fachada BIPV | Cenário hipotético | Análise em 1.037 horas elegíveis, sem fachada medida e sem trimestre integral de produção |

A energia integral observada do trimestre é 454,285 MWh no resultado salvo. Ela não deve ser combinada com irradiância restrita aos pares diurnos para calcular PR. Cada tabela e figura precisa dizer qual máscara foi usada.

A pasta Projeto_Energia_FV contém uma alternativa brasileira do IFES: CSVs tratados de dezembro de 2024 a julho de 2025 e um XLS de uma semana de janeiro de 2024. Seu LEIA_ME registra pendências temporais, de configuração e de representatividade da estação INMET. Essa base não alimenta os gráficos do estudo PVDAQ. Recomendo preservá-la como alternativa futura, mantendo o estudo já executado como caso comum do capítulo.

## Divisão do trabalho e interfaces

| Seção | Responsáveis | Trabalho central | Entrega à equipe |
| --- | --- | --- | --- |
| 1 Recurso solar | Samuel | Caracterizar recurso, geometria, medições e variabilidade | POA e geometria contextualizadas para as demais seções |
| 2 Condições ambientais | Vannessa e Thais | Explicar temperatura, vento, albedo, sujeira e instalação | Parâmetros e hipóteses de operação usados na seção 3 |
| 3 Conversão fotovoltaica | Gabriela e Giulia | Explicar modelos térmico, elétrico, inversor e energia | Potência e energia simuladas, mantendo a cadeia comum |
| 4 Desempenho e validação | Júlia Ribeiro e Lucas Simão | Integrar indicadores, perdas, erro e cenários BIPV | Comparação AC, limitações e interpretação dos resultados |


Na seção 4, a proposta atual atribui 4.1 e 4.5 a Júlia Ribeiro, e 4.2, 4.3 e 4.4 a Lucas Simão. A distribuição interna das demais duplas deve ser registrada na reunião. Cada integrante precisa escrever sua parte sabendo quais entradas recebe e quais resultados entrega à seção seguinte. A redação das seções 1 e 2 deve contextualizar as variáveis sem repetir a modelagem completa da seção 3; a seção 4 interpreta as saídas e seus limites.

Para cada subseção, entregar: pergunta e argumento central, fundamentos com equações e unidades, referência e página de cada afirmação técnica, figura ou tabela selecionada quando necessária, interpretação e limite da evidência. É melhor começar com 3 a 5 referências centrais por subseção e ampliar quando uma afirmação exigir outra fonte, em vez de exigir leitura integral de todos os PDFs.

## Como ler os gráficos existentes

Existem 30 figuras catalogadas: 25 gráficos, um fluxograma e quatro esquemas. As versões clara e escura, em PNG e PDF, são representações das mesmas 30 figuras, não 120 resultados independentes. O catálogo relaciona cada figura à sua subseção, legenda e natureza da evidência. Os 25 PNGs escuros foram localizados na pasta atual.

| Grupo | Pergunta respondida | Seção principal |
| --- | --- | --- |
| G01 e G02 | Como variam a geometria solar e o recurso medido | 1 |
| G03, G04, G20 e G22 | Como ambiente e hipóteses alteram temperatura e aproveitamento | 2 e 3 |
| G05 a G07 | Como o modelo calcula curvas elétricas e a conversão no inversor | 3 |
| G08 a G10 | Como potência e energia simuladas se comparam às medidas | 3 e 4 |
| G11, G12 e G21 | Como se organizam energia, perdas calculadas, produtividades e PR | 4 |
| G13 a G19 | Quanto o modelo erra e como os erros se distribuem | 4 |
| G23 | Como se reconstroem componentes de radiação a partir da POA | 1 e 3 |
| G24 e G25 | Como se comportam os cenários BIPV hipotéticos | 4.5 |

G01 e G23 ilustram 17/05/2024; G08 compara 17/05 e 04/05/2024. Curvas elétricas e esquemas não representam um dia observado. Gráficos mensais usam abril, maio e junho; gráficos de validação usam a máscara pareada, salvo indicação específica. A coleção completa não precisa entrar no capítulo: proponho selecionar inicialmente de 2 a 4 figuras por seção e remeter diagnósticos extensos ao material suplementar, conforme espaço e orientação da professora.

## Onde guardar cada material

| Material | Local principal | Organização |
| --- | --- | --- |
| PDFs dos 91 documentos | Drive, nas pastas por seção | Links e metadados no GitHub |
| Dados brutos e pacotes completos | Drive e fonte oficial | Manifesto com URL, tamanho e SHA-256 no GitHub |
| Código, notebooks e configuração | GitHub | Uma versão compartilhada e notebooks sem saídas incorporadas |
| Tabelas numéricas pequenas | GitHub após selecionar | CSV com período, unidades e máscara temporal |
| Figuras para o capítulo | GitHub após selecionar | Um arquivo por figura; listas por seção apontam para ele |
| 120 versões gráficas e DOCX completos | Drive | Guardar versões clara/escura e alta resolução |
| Texto em elaboração | Documento compartilhado no Drive | GitHub guarda versões consolidadas; escolher uma única fonte de edição |


O GitHub é apropriado para versionar o trabalho computacional e revisar mudanças. Para a escrita simultânea do capítulo por integrantes sem prática de Git, o documento compartilhado do Drive oferece um caminho mais simples. Não manter duas versões editáveis concorrentes do mesmo texto. Na reunião, escolher: documento compartilhado como texto oficial com cópias consolidadas no GitHub, ou Markdown/LaTeX no GitHub como texto oficial. Recomendo a primeira opção nesta etapa.

Os PDFs permanecem nas pastas atuais de Artigos, Livros, Dissertacoes, Teses e Relatorios_e_Manuais. No pacote preparado, cada seção tem listas desses materiais, com IDs e links para sua cópia no Drive. Isso atende à divisão por seção sem colocar as 160 cópias no histórico Git. As figuras selecionadas ficam em figuras/previas ou, depois da seleção final, em figuras/selecionadas; os índices por seção apontam para os mesmos arquivos. Dados brutos são recuperáveis pelas URLs oficiais e conferidos por hashes.

Como referência técnica, o GitHub avisa sobre arquivos acima de 50 MiB e bloqueia arquivos acima de 100 MiB no Git comum; uploads pelo navegador têm limite de 25 MiB por arquivo. Não é necessário começar com Git LFS se mantivermos PDFs e grandes saídas no Drive. A recomendação aqui é de organização e tamanho; a disponibilidade de um PDF não comprova permissão para redistribuí-lo publicamente. Por isso o pacote inclui referências e links, sem cópias dos livros e artigos.

## Estrutura preparada para o GitHub

O pacote reorganizado reaproveita o projeto computacional v1.2.2. Código científico e configurações foram preservados. Inclui dois notebooks sem saídas, bibliografia existente, inventário dos 91 documentos, listas por seção e tipo, índice das 30 figuras, seis prévias extraídas do notebook e modelos de tarefa e revisão. Não contém os 160 PDFs, grandes dados brutos ou resultados completos.

| Caminho | Uso pela equipe |
| --- | --- |
| README.md | Entrada única e orientações de uso |
| secoes/01_Recurso_Solar a 04_Desempenho_Perdas_Validacao | Roteiro, referências, figuras e tabelas de cada seção |
| notebooks e src | Uma cadeia computacional compartilhada |
| config | Instalação, período, modelos e hipóteses |
| references e bibliografia | Citações, inventário e seleção de referências |
| data/raw | Manifesto das fontes, orientação e hashes; dados obtidos separadamente |
| figuras/previas | Seis ilustrações para escolha; alta resolução permanece no Drive |
| docs | Plano, matriz das 19 subseções e auditoria dos arquivos |
| .github | Modelos para tarefas e revisões |

O repositório público foi identificado em 18/10/2026 como samuelasroma-byte/SPGER0046_Energias_Renovaveis, ID 1421239398. A estrutura técnica foi integrada após a autorização de Samuel. O nome do repositório não altera o código da disciplina. O histórico desta versão passa a ser acompanhado no GitHub.

## Rotina de trabalho

1. A equipe confirma o estudo PVDAQ 2107 e o período de abril a junho de 2024 como caso comum. Registra as hipóteses que serão discutidas e o texto oficial escolhido.
2. Cada integrante abre a pasta de sua seção, seleciona referências prioritárias, lê os trechos necessários e registra página, equação e aplicação. Não usa apenas o resumo ou a indicação automática do catálogo.
3. A redação passa por subseções; cada tabela e figura selecionada recebe identificação, período, unidades, origem e vínculo com a versão do cálculo. Gráficos de cenários são identificados como cenários.
4. Mudanças em código, configuração ou cálculo são propostas em uma branch curta, com uma tarefa e revisão por outro integrante. Branch é uma versão de trabalho; pull request é um pedido de revisão para incorporar a mudança. A versão principal permanece comum às quatro seções.
5. Ao incorporar um cálculo, atualizar conjuntamente os resultados afetados, o catálogo das figuras, as legendas e as interpretações. Evitar que cada seção execute parâmetros ou períodos diferentes sem registro.
6. A revisão cruzada confere as interfaces 1→2→3→4, elimina repetição e verifica correspondência entre afirmação, equação, citação e resultado. O integrador consolida o texto; a pessoa deve ser definida pela equipe.

## Cronograma já previsto no projeto

| Prazo | Responsáveis | Entrega |
| --- | --- | --- |
| Até 22/10/2026 | Cada integrante | Roteiro de subseção, referências prioritárias e início do texto |
| 27/10/2026 | Equipe | Slides preliminares e uma subseção redigida por integrante |
| 05/11/2026 | Cada integrante | Segunda subseção atribuída redigida; divisão interna a confirmar |
| 19/11/2026 | Equipe | Capítulo completo integrado, introdução e considerações finais |
| 26/11 a 01/12/2026 | Revisão cruzada | Conferir ciência, referências, continuidade, figuras e formatação |
| 01/12/2026 | Equipe | Correções incorporadas, slides finais e entrega |


O marco de 15/10 para estrutura e cronograma já consta da proposta como prazo anterior. Esta conferência não atesta o envio ou cumprimento das entregas. Recomendo usar a próxima reunião para confirmar responsáveis internos, texto oficial, figuras centrais e acesso da equipe às pastas.

## Critérios de conclusão

Cada subseção fica pronta quando possui argumento claro, equações definidas com unidades e fontes, referências lidas e verificadas, figuras/tabelas necessárias interpretadas e limites explícitos. No capítulo integrado, todos os autores devem usar as mesmas convenções de POA, potência, energia, PR e normalização dos erros.

A validação observacional disponível é da saída CA nessa instalação e nesse trimestre; ela não valida isoladamente a temperatura, as componentes de radiação, as strings reais ou os cenários BIPV. Não se deve transformar o trimestre em climatologia anual, nem atribuir todas as diferenças a uma perda física específica. A ausência da IEC impede alegações de conformidade com seus requisitos não examinados, mas não impede a redação fundamentada com as fontes disponíveis.

## Fontes para consulta

- Proposta atual de estrutura e cronograma (consulta no acervo da equipe).
- Projeto PVDAQ e dados preservados (consulta no acervo da equipe).
- Notebook principal executado (consulta no acervo da equipe).
- Biblioteca de PDFs por seção (consulta no acervo da equipe).
- Catálogo de figuras (consulta no acervo da equipe).
- [GitHub sobre tamanho dos arquivos](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).
- [GitHub sobre branches e revisão](https://docs.github.com/en/pull-requests/concepts/writing-code-for-a-project).

## Códigos do projeto

A identifica documentos disponíveis no acervo, B identifica as 39 referências sugeridas do levantamento inicial, N identifica norma complementar e R identifica referências metodológicas do pipeline. Os números são identificadores de catálogo, não ranking de qualidade. A090 e A091 continuam reservados aos materiais retirados e não foram reutilizados. A092 e A093 são os dois relatórios completos acrescentados como apoio.
