# Protocolo da revisão estruturada da Seção 1

**Responsável:** Samuel Constantino Teixeira. **Registro:** 27/10/2026. **Método:** revisão bibliográfica estruturada inspirada no ProKnow-C, complementada por síntese crítica integrativa. A declaração não corresponde à execução integral do ProKnow-C.

## Continuidade e unidade de análise

O ponto de partida é o portfólio existente, os notebooks 00 e 02, os arquivos de protocolo e os catálogos produzidos anteriormente. As buscas bibliométricas não foram repetidas. A seleção da Seção 1 herdou 12 códigos B e 23 associações entre referência e subseção. A045, quarta edição do handbook de 2024, é um complemento identificado por código próprio; não substitui silenciosamente B36, a terceira edição de 2021. A003, obra de Jäger e colaboradores, não resolve a ausência das edições de Kalogirou ou de Luque/Hegedus.

Uma obra pode atender a mais de uma subseção sem ser contada novamente como documento distinto. Uma associação bibliográfica também pode originar várias evidências, porque conceitos, equações e limitações diferentes precisam de localização própria. As contagens de documentos, associações, páginas extraídas e evidências conferidas permanecem separadas.

## Perguntas e eixos

| Subseção | Pergunta específica | Eixos e descritores para busca complementar, somente quando houver lacuna |
|:--|:--|:--|
| 1.1 | Quais relações e convenções permitem calcular a direção solar e a referência extraterrestre sem confundi-las com irradiância de superfície? | geometria solar; solar geometry; solar position; zenith; azimuth; SPA; extraterrestrial irradiance; Earth–Sun distance; Spencer |
| 1.2 | Como definir e relacionar irradiância, irradiação e componentes em planos distintos? | irradiance; irradiation; radiant exposure; GHI; DNI; DHI; global tilted irradiance; plane of array; closure equation |
| 1.3 | Como atmosfera e escalas de análise condicionam a variabilidade do recurso e a interpretação de uma série local? | clouds; aerosols; aerosol optical depth; precipitable water; air mass; irradiance variability; temporal aggregation; spatial representativeness |
| 1.4 | Como medições e estimativas caracterizam o recurso com suporte, qualidade e incertezas explícitos? | pyranometer; pyrheliometer; solar resource assessment; satellite irradiance; reanalysis; solar atlas; quality control; uncertainty; temporal support |

Os descritores incluem português e inglês para não restringir a recuperação textual ao idioma da redação. Busca semântica ou TF–IDF serve à localização de candidatos; sua pontuação não significa qualidade metodológica, leitura concluída ou aprovação científica.

## Critérios de inclusão e exclusão

São incluídas como evidência direta fontes cuja identidade e edição sejam verificáveis e cujo conteúdo tenha sido efetivamente conferido para uma afirmação do manuscrito. Para algoritmos e implementação, priorizam-se o artigo/relatório metodológico e a documentação ou código da versão executada. Livros e handbooks sustentam definições, sínteses físicas e limitações. A atualidade é avaliada em relação ao uso: uma publicação clássica pode permanecer fundamental, enquanto versões de software e bases precisam ser identificadas precisamente.

São excluídos do conjunto de provas diretas os registros sem conteúdo conferido, edições diferentes usadas como se fossem a mesma obra, duplicatas do mesmo arquivo e materiais sem aderência à pergunta. Fontes pertinentes ainda não lidas são mantidas como pendentes, sem exclusão definitiva. Estudos de transposição, temperatura, conversão elétrica e desempenho ficam como complementos quando sua discussão detalhada pertence às demais seções.

As duplicatas documentais são identificadas por SHA-256 e, para registros bibliográficos, por DOI normalizado ou, na ausência deste, por título, autoria, ano e edição. Edições diferentes e artigo/relatório revisado não são fundidos automaticamente. Em particular, Reda e Andreas (2004) e o relatório revisado de 2008 permanecem registros distintos.

## Avaliação crítica

As sete lentes do protocolo anterior são preservadas: fundamentos e definições; equações, hipóteses e domínio; unidades e convenções; método e reprodutibilidade; convergências e divergências; limites observacionais; pertinência ao PVDAQ e ao capítulo. Cada evidência identifica a afirmação parafraseada, a página do arquivo, a página impressa, o hash da fonte, o destino e seus limites.

A avaliação não atribui um escore de qualidade aparente a uma fonte não lida. Para fontes de posição solar, confrontam-se convenções, entradas e resultados de referência. Para descrições radiométricas, confrontam-se plano, unidade e suporte temporal. Para estudos atmosféricos e bases em grade, examinam-se escala, representatividade e possibilidade de atribuição. Inferências do pesquisador e resultados computacionais recebem identificação própria, sem serem apresentados como conclusões literais de uma referência.

Uma divergência foi registrada no fator orbital: o exemplar de Duffie, Beckman e Blair (2020, p. 9) apresenta 0,00719 no coeficiente de cos(2B), enquanto o código executado de pvlib 0.16.1 utiliza 0,000719. O projeto reproduz a implementação do software. A observação é um cotejo de conteúdo, sem alegar consulta a uma errata editorial.

## Afunilamento documentado

O acervo coletivo e os resultados bibliométricos anteriores são o universo herdado, sem reconstrução retroativa de etapas não documentadas. O recorte B da Seção 1 contém 12 referências e 23 associações. A seleção crítica acrescenta explicitamente A045 como fonte de evidências e mantém A003 como disponível, mas não lida. A matriz de 39 evidências bibliográficas resulta de conferência localizada de cinco PDFs; somente o documento NOAA de duas páginas foi lido integralmente. O código do pvlib e os dados/configuração do projeto constituem evidências digitais separadas dessa contagem de PDFs.

Não foram produzidos números novos de citações, índices de reconhecimento científico ou percentuais acumulados de relevância. O material introdutório de ProKnow-C é uma ementa de formação, não um registro de execução das etapas da revisão. A implementação integral exigiria explicitar e executar todas as escolhas e filtros correspondentes, incluindo a avaliação e atualização do portfólio com o protocolo completo.

## Pendências e limites

| Registro | Estado e consequência |
|:--|:--|
| B19 — Kalogirou, edição de 2014 | Edição exata não localizada; sem uso como evidência direta |
| B20 — Luque/Hegedus, edição de 2011 | Edição exata não localizada; sem citações de páginas presumidas |
| B11 — Driesse/Jensen/Perez, 2024 | PDF disponível; leitura pendente; aprofundamento de transposição pertence a 3.1 |
| B36 — handbook de 2021 | PDF disponível nas pastas 1.2–1.4; não declarar leitura da terceira edição a partir da quarta |
| B27 — documentação de acesso | Catalogada; leitura técnica detalhada pendente |
| B24 — registro do conjunto de dados | Metadados herdados do projeto; recuperação web do DOI falhou; dados preparados e configuração foram conferidos |
| Revisão humana cruzada | A conferência assistida por IA e os testes computacionais não substituem a revisão acadêmica da autoria e da equipe |

As pendências de leitura não invalidam automaticamente as definições já fundamentadas em fontes conferidas. Elas delimitam o alcance do portfólio atual e orientam complementações reais, sem declarar concluída uma revisão bibliográfica apenas pela existência de fichas, códigos ou modelos de documentos.


## Registro anterior preservado

# Perguntas de estudo e lentes de curadoria — Seção 1

**Planejamento, não resultado de leitura.**

## 1.1 — Geometria solar e irradiância extraterrestre
- Quais grandezas definem a geometria solar e qual convenção angular?
- Como calcular irradiância extraterrestre e quais aproximações têm domínio limitado?

## 1.2 — Grandezas radiométricas e componentes da radiação
- Como distinguir irradiância e irradiação e as componentes GHI DNI DHI?
- Como interpretar POA medida sem fingir disponibilidade de componentes horizontais locais?

## 1.3 — Modulação atmosférica e variabilidade espaço-temporal
- Como atmosfera e nuvens modulam o recurso solar?
- Que variabilidade pode ser inferida de 91 dias sem fazer climatologia ou atribuição causal não identificada?

## 1.4 — Medição e estimativa do recurso solar
- Quais sensores e metodologias quantificam o recurso e suas incertezas?
- Como distinguir observações de satélites, reanálises e dados de superfície e auditar PVDAQ?

## Lentes de avaliação
- **L01 — Fundamentos e definições:** As grandezas, conceitos e hipóteses são explicitamente definidos pelo autor?
- **L02 — Equações, símbolos e unidades:** As equações são verificáveis e fisicamente/dimensionalmente coerentes, com convenções indicadas?
- **L03 — Métodos e proveniência:** Que instrumentos, modelos, métodos ou fontes de dados sustentam a afirmação?
- **L04 — Confronto e convergências:** O que está de acordo ou conflita entre diferentes autores, normas e gerações de modelos?
- **L05 — Limites e incerteza:** Qual escala espacial/temporal, hipótese, domínio de validade e incerteza são explicitados?
- **L06 — Aplicação PVDAQ 2107:** O resultado é aplicável a POA observada entre abril e junho de 2024 sem inventar GHI/DNI/DHI medidos?
- **L07 — Rastreabilidade e coerência editorial:** Página digital/impressa, arquivo/edição e interpretação estão confirmados e cabem no escopo da subseção?
