# Plano de trabalho da equipe

Recurso solar e modelagem da conversão fotovoltaica, SPGER0046, PPGER/UFPB. Planejamento das quatro seções e 19 subseções, com responsáveis, materiais, critérios de redação e cronograma.

## Decisão de trabalho

A redação utiliza o acervo de livros, artigos e trabalhos acadêmicos, os dados observacionais e a cadeia computacional comum às 19 subseções. Cada afirmação técnica requer leitura da fonte e conferência da página citada. B19, B20 e N01 estão pendentes nas edições integrais indicadas; a conformidade normativa depende do exame dos requisitos da norma.

O GitHub é o ambiente central de redação, revisão e organização da equipe. O Drive conserva os PDFs, os dados brutos e as versões gráficas, acessíveis pelos índices do repositório. Código, configuração, catálogos, resultados e histórico de revisões ficam organizados no GitHub. Cada integrante terá uma entrada própria, mas as quatro seções usarão a mesma instalação, janela temporal e cadeia de dados.

## Materiais parciais e outras edições

A090 corresponde a Solar_Energy_Engineering-Processes_and_Systems.pdf, de Kalogirou (2009), sem folhas iniciais; A091 corresponde a pdf68.pdf, trecho da segunda edição de Luque e Hegedus (2011). Os dois originais e sete cópias ficam na pasta de materiais retirados, fora do acervo ativo, na raiz do Drive. Os códigos A090 e A091 identificam esses documentos e não são reutilizados.

## Acervo bibliográfico

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


O catálogo contém 91 documentos, distribuídos em 160 cópias nas 28 pastas de referências. Uma obra pode atender a mais de uma seção. Os nove livros incluem edições diferentes; a unidade de contagem é o documento catalogado. O TCC é de Filipe Tawã Gomes, sobre microclima e placas fotovoltaicas. Os 829 registros bibliográficos do levantamento, os dados, notebooks e relatórios do projeto não integram essa contagem de PDFs.

| Seção | Responsáveis | Artigos | Livros | Diss. | Teses | Rel./manuais | TCC | Total |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Samuel | 30 | 6 | 0 | 1 | 5 | 0 | 42 |
| 2 | Vannessa e Thais | 23 | 9 | 3 | 2 | 2 | 1 | 40 |
| 3 | Gabriela e Giulia | 17 | 7 | 2 | 3 | 8 | 0 | 37 |
| 4 | Júlia Ribeiro e Lucas Simão | 25 | 6 | 3 | 2 | 5 | 0 | 41 |


As cópias ocupam aproximadamente 1,12 GB; os documentos distintos somam aproximadamente 520,5 MB. Isso justifica usar links no GitHub. Os dois PDFs retirados estão excluídos desses totais. A contagem se refere ao [acervo ativo do capítulo](https://drive.google.com/drive/folders/1Ko7bngE2QGAChdqNUVib-Ls7j7d25kTe), e não a todos os arquivos de todo o Drive. A norma IEC 61724-1:2021 permanece ausente. O relatório A093 é apoio técnico e não é norma.

## Estudo de caso

O projeto principal é Farm Solar Array, PVDAQ 2107, em Arbuckle, Califórnia, Estados Unidos. A configuração v1.2.2 seleciona de 1º de abril a 30 de junho de 2024, com fim exclusivo em 1º de julho, no fuso America/Los_Angeles. São 91 dias. Os índices exportados usam UTC; datas e horas locais devem ser identificadas nas legendas. O ano 2026 na fonte das figuras indica elaboração, não observação.

Os arquivos originais contêm observações além desse trimestre. Os limites dos quatro CSVs foram conferidos diretamente: as séries começam em janeiro e terminam em novembro de 2024, em datas distintas. Portanto, existir um arquivo com 2024 no nome não comprova um ano inteiro comum entre sensores. O recorte do estudo é definido pela configuração, não pelo nome do arquivo.

Entradas observacionais principais: irradiância no plano dos módulos, chamada POA, temperatura do ar e vento, medidos junto à instalação. O modelo estima temperatura operacional, potência do módulo, potência CC do arranjo, conversão no inversor, potência CA e energia. A potência CA medida pelo medidor local é a referência de comparação, não entrada da previsão física. NASA POWER não entra na cadeia principal atual; seus arquivos foram preservados como histórico.

O trimestre contém 8.736 intervalos de 15 minutos e 8.736 registros do medidor. A avaliação diurna usa 4.401 pares de 4.421 intervalos elegíveis, com disponibilidade conjunta de 99,55%. POA e inversores são agregados de 5 para 15 minutos, com três amostras por intervalo e sem preenchimento de lacunas. O notebook possui 25 células de código com execução registrada. A reprodução está descrita em [Executar e reproduzir o projeto](REPRODUTIBILIDADE.md).

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

A pasta Projeto_Energia_FV contém uma base alternativa do IFES: CSVs tratados de dezembro de 2024 a julho de 2025 e um XLS de uma semana de janeiro de 2024. Seu LEIA_ME identifica pendências temporais, de configuração e de representatividade da estação INMET. Essa base é independente do estudo PVDAQ e não alimenta seus gráficos.

## Divisão do trabalho e interfaces

| Seção | Responsáveis | Trabalho central | Entrega à equipe |
| --- | --- | --- | --- |
| 1 Recurso solar | Samuel | Caracterizar recurso, geometria, medições e variabilidade | POA e geometria contextualizadas para as demais seções |
| 2 Condições ambientais | Vannessa e Thais | Explicar temperatura, vento, albedo, sujeira e instalação | Parâmetros e hipóteses de operação usados na seção 3 |
| 3 Conversão fotovoltaica | Gabriela e Giulia | Explicar modelos térmico, elétrico, inversor e energia | Potência e energia simuladas, mantendo a cadeia comum |
| 4 Desempenho e validação | Júlia Ribeiro e Lucas Simão | Integrar indicadores, perdas, erro e cenários BIPV | Comparação AC, limitações e interpretação dos resultados |


Na seção 4, a proposta atual atribui 4.1 e 4.5 a Júlia Ribeiro, e 4.2, 4.3 e 4.4 a Lucas Simão. A distribuição interna das demais duplas deve ser registrada na reunião. Cada integrante precisa escrever sua parte sabendo quais entradas recebe e quais resultados entrega à seção seguinte. A redação das seções 1 e 2 deve contextualizar as variáveis sem repetir a modelagem completa da seção 3; a seção 4 interpreta as saídas e seus limites.

Cada subseção deve conter argumento central, fundamentos, equações com unidades, referências com páginas, materiais gráficos pertinentes, interpretação e limites da evidência. A leitura inicial pode se concentrar em 3 a 5 referências centrais, com ampliação conforme as afirmações desenvolvidas.

## Como ler os gráficos existentes

O catálogo contém 30 ilustrações: 25 gráficos, um fluxograma e quatro esquemas. Cada item possui versões clara e escura em PNG e PDF, totalizando 120 arquivos. O catálogo identifica subseção, legenda e natureza da evidência.

| Grupo | Pergunta respondida | Seção principal |
| --- | --- | --- |
| G01 e G02 | Como variam a geometria solar e o recurso medido | 1 |
| G03, G20 e G22; G04 | Como ambiente e hipóteses alteram temperatura e aproveitamento | 2; G04 em 3.2 |
| G05 a G07 | Como o modelo calcula curvas elétricas e a conversão no inversor | 3 |
| G08 a G10 | Como potência e energia simuladas se comparam às medidas | 3.6 |
| G11, G12 e G21 | Como se organizam energia, perdas calculadas, produtividades e PR | 4 |
| G13 a G19 | Quanto o modelo erra e como os erros se distribuem | 4 |
| G23 | Como se reconstroem componentes de radiação a partir da POA | 3.1 |
| G24 e G25 | Como se comportam os cenários BIPV hipotéticos | 4.5 |

G01 e G23 ilustram 17/05/2024; G08 compara 17/05 e 04/05/2024. Curvas elétricas e esquemas representam relações calculadas. Os gráficos mensais abrangem abril, maio e junho; os de validação usam a máscara pareada, salvo indicação específica. A equipe seleciona as figuras do texto conforme sua função e o espaço disponível; diagnósticos extensos podem compor o material suplementar.

## Onde guardar cada material

| Material | Local principal | Organização |
| --- | --- | --- |
| PDFs dos 91 documentos | Drive, nas pastas por seção | Links e metadados no GitHub |
| Dados brutos e pacotes completos | GitHub, fonte oficial e Drive | Quatro CSVs e metadados; manifesto com URL, tamanho e SHA-256 |
| Código, notebooks e configuração | GitHub | Cadeia comum e cópias de notebooks executados |
| Tabelas numéricas | GitHub | CSVs com período, unidades e máscara temporal |
| Figuras para o capítulo | Pasta da seção correspondente no GitHub | Um ID e uma subseção por ilustração |
| 120 versões gráficas e documentos Word | GitHub e Drive | Temas claro/escuro e formatos PNG/PDF; documentos editáveis |
| Texto em elaboração | GitHub, em texto.md de cada seção | Uma fonte de edição e revisão por propostas de alteração |


O GitHub concentra o trabalho computacional e a redação. Cada seção desenvolve seu arquivo texto.md e abre propostas de alteração para revisão do grupo. Os documentos originais no Drive são fontes de consulta; a edição corrente do capítulo acontece no repositório.

Os PDFs bibliográficos estão organizados por seção e tipo: Artigos, Livros, Dissertacoes, Teses e Relatorios_e_Manuais. Os índices do GitHub identificam cada documento e sua cópia no Drive. As figuras e tabelas ficam nas pastas das respectivas seções, conforme o mapa editorial. Os dados brutos estão em data/raw, com URLs oficiais e hashes.

O repositório contém os quatro CSVs brutos, os documentos Word e as 120 exportações gráficas. O CSV elétrico possui 63.287.121 bytes e o Word dos gráficos, 14.465.317 bytes. Os PDFs de terceiros são acessados pelos índices bibliográficos; sua disponibilidade para leitura não implica autorização para redistribuição pública.

## Estrutura do repositório

O repositório reúne a cadeia computacional v1.2.2, dois notebooks de trabalho e suas cópias executadas, dados brutos e preparados, resultados, bibliografia, catálogo de 91 documentos, 30 ilustrações, documentos técnicos e modelos de tarefa e revisão. O ZIP contém todos os arquivos versionados; os PDFs de terceiros são acessados por links.

| Caminho | Uso pela equipe |
| --- | --- |
| README.md | Entrada única e orientações de uso |
| secoes/01_Recurso_Solar a 04_Desempenho_Perdas_Validacao | Roteiro, referências, figuras e tabelas de cada seção |
| notebooks e src | Uma cadeia computacional compartilhada |
| config | Instalação, período, modelos e hipóteses |
| references e bibliografia | Citações, inventário e seleção de referências |
| data/raw | Quatro CSVs brutos, metadados e manifesto das fontes |
| figuras e secoes | Catálogo e 120 arquivos PNG/PDF organizados por seção |
| docs | Plano, matriz das 19 subseções e auditoria dos arquivos |
| .github | Modelos para tarefas e revisões |

Repositório da equipe: [samuelasroma-byte/SPGER0046_Energias_Renovaveis](https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis). A disciplina é SPGER0046, PPGER/UFPB.

## Rotina de trabalho

1. A equipe usa PVDAQ 2107 e o período de abril a junho de 2024 como caso comum, registra as hipóteses e desenvolve a redação nos arquivos texto.md do GitHub.
2. Cada integrante abre a pasta de sua seção, seleciona referências prioritárias, lê os trechos necessários e registra página, equação e aplicação. Não usa apenas o resumo ou a indicação automática do catálogo.
3. A redação passa por subseções; cada tabela e figura selecionada recebe identificação, período, unidades, origem e vínculo com a versão do cálculo. Gráficos de cenários são identificados como cenários.
4. Mudanças em código, configuração ou cálculo são propostas em uma branch curta, com uma tarefa e revisão por outro integrante. Branch é uma versão de trabalho; pull request é um pedido de revisão para incorporar a mudança. A versão principal permanece comum às quatro seções.
5. Ao incorporar um cálculo, atualizar conjuntamente os resultados afetados, o catálogo das figuras, as legendas e as interpretações. Evitar que cada seção execute parâmetros ou períodos diferentes sem registro.
6. A revisão cruzada confere as interfaces 1→2→3→4, elimina repetição e verifica correspondência entre afirmação, equação, citação e resultado. O integrador consolida o texto; a pessoa deve ser definida pela equipe.

## Cronograma

| Prazo | Responsáveis | Entrega |
| --- | --- | --- |
| Até 22/10/2026 | Cada integrante | Roteiro de subseção, referências prioritárias e início do texto |
| 27/10/2026 | Equipe | Slides preliminares e uma subseção redigida por integrante |
| 05/11/2026 | Cada integrante | Segunda subseção atribuída redigida; divisão interna a confirmar |
| 19/11/2026 | Equipe | Capítulo completo integrado, introdução e considerações finais |
| 26/11 a 01/12/2026 | Revisão cruzada | Conferir ciência, referências, continuidade, figuras e formatação |
| 01/12/2026 | Equipe | Correções incorporadas, slides finais e entrega |


O marco de 15/10 corresponde à estrutura e ao cronograma. A equipe acompanha as entregas e define a distribuição interna das subseções, o integrador e os revisores.

## Critérios de conclusão

Cada subseção fica pronta quando possui argumento claro, equações definidas com unidades e fontes, referências lidas e verificadas, figuras/tabelas necessárias interpretadas e limites explícitos. No capítulo integrado, todos os autores devem usar as mesmas convenções de POA, potência, energia, PR e normalização dos erros.

A validação observacional disponível é da saída CA nessa instalação e nesse trimestre; ela não valida isoladamente a temperatura, as componentes de radiação, as strings reais ou os cenários BIPV. Não se deve transformar o trimestre em climatologia anual, nem atribuir todas as diferenças a uma perda física específica. A ausência da IEC impede alegações de conformidade com seus requisitos não examinados, mas não impede a redação fundamentada com as fontes disponíveis.

## Fontes para consulta

- [Proposta atual de estrutura e cronograma](https://docs.google.com/document/d/1v5h8IW7XLGd7LeXHOevwoKLSvLLsY9kI/edit).
- [Projeto PVDAQ e dados preservados](https://drive.google.com/drive/folders/1RyyZri_sGsB2MZ6Hygwwrkv8eqPWymJ3).
- [Notebook principal executado](https://drive.google.com/file/d/1EYHPdkAeotZTRryg73DTotHkOZH691Zk/view?usp=drivesdk).
- [Biblioteca de PDFs por seção](https://drive.google.com/drive/folders/1Ko7bngE2QGAChdqNUVib-Ls7j7d25kTe).
- [Catálogo de figuras](https://drive.google.com/file/d/1yWoU49d-e9Qlc9XWjwf6eXnGUIHyU1Cz/view?usp=drivesdk).
- [GitHub sobre tamanho dos arquivos](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-large-files-on-github).
- [GitHub sobre branches e revisão](https://docs.github.com/en/pull-requests/concepts/writing-code-for-a-project).

## Códigos do projeto

A identifica documentos do acervo; B, as 39 referências prioritárias; N, a norma complementar; R, as fontes metodológicas. Os códigos são identificadores, sem ranking de qualidade. A090 e A091 correspondem aos materiais parciais e outras edições fora do acervo ativo. A092 e A093 são relatórios de apoio.


## Ambiente de colaboração

O GitHub é o ambiente central escolhido para a equipe. Desenvolver a redação em texto.md de cada seção e revisar por propostas de alteração. A proposta original no Drive continua como registro de escopo, responsáveis e cronograma. Os arquivos do Drive são abertos pelos [índices de acesso](ACESSO_E_COLABORACAO.md).
