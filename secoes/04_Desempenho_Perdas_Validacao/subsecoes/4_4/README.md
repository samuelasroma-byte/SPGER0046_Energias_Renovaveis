# 4.4 Validação de modelos de geração fotovoltaica

Responsável: **Lucas Simão**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Comparação modelo–observação por erro médio de viés (MBE), erro absoluto médio (MAE), raiz do erro quadrático médio (RMSE), raiz do erro quadrático médio normalizada (nRMSE), coeficiente de correlação de Pearson (r) e coeficiente de determinação (R²). (Lucas)

## Entradas, método e resultado esperado

**Entradas:** Mesmos pares de potência AC medida e simulada.

Avalie viés, magnitude do erro, correlação e determinação. Erro=simulado−observado. MBE, MAE e RMSE são em kW; nMBE/nRMSE são divididos pela média observada dos respectivos pares. O modelo físico é separado do fator empírico ajustado somente em abril.

$$MBE=\bar e,\quad MAE=\overline{|e|},\quad RMSE=\sqrt{\overline{e^2}},\quad R^2=1-\frac{\sum e_i^2}{\sum(y_i-\bar y)^2}.$$

**Saídas:** Métricas gerais, por mês/hora/POA, resíduos e consistência de medidores.

**Evidência:** Comparação observacional da saída AC. **Limitação:** Junho é teste temporal separado, não instalação independente. Correlação elevada não prova exatidão; nenhum limiar universal de aceitação foi adotado.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B07](../../../../bibliografia/principal/README.md#b07) — Artigo | CHAI, T.; DRAXLER, R. R. Root mean square error (RMSE) or mean absolute error (MAE)? – Arguments against avoiding RMSE in the literature. Geoscientific Model Development, [S. l.], v. 7, n. 3, p. 1247-1250, 2014. DOI: https://doi.org/10.5194/gmd-7-1247-2014. Disponível em: https://doi.org/10.5194/gmd-7-1247-2014. Acesso em: 16 out. 2026. | [A075 — PDF](https://drive.google.com/file/d/1sa701Mfu5c9f0dEdcvRChFAhaUbMA0YC/view?usp=drivesdk) |
| [B26](../../../../bibliografia/principal/README.md#b26) — Documento técnico | PV ANALYTICS WEBINAR. Solar Data Tools demo — Farm Solar Array. [S. l.], 2024. Disponível em: https://pv-tutorials.github.io/2024_Analytics_Webinar/solar-data-tools-demo.html. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |
| [B39](../../../../bibliografia/principal/README.md#b39) — Artigo | WILLMOTT, C. J.; MATSUURA, K. Advantages of the mean absolute error (MAE) over the root mean square error (RMSE) in assessing average model performance. Climate Research, [S. l.], v. 30, p. 79-82, 2005. DOI: https://doi.org/10.3354/cr030079. Disponível em: https://doi.org/10.3354/cr030079. Acesso em: 16 out. 2026. | [A035 — PDF](https://drive.google.com/file/d/10RiMS80gPltkfyN5SPcGonRpFIiqhdGv/view?usp=drivesdk) |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A035 | [Abrir Advantages of the mean absolute error (MAE) over the root mean square error (RMSE) in assessing average model performance](https://drive.google.com/file/d/10RiMS80gPltkfyN5SPcGonRpFIiqhdGv/view?usp=drivesdk) |  |
| A075 | [Abrir Root mean square error (RMSE) or mean absolute error (MAE)? Arguments against avoiding RMSE in the literature](https://drive.google.com/file/d/1sa701Mfu5c9f0dEdcvRChFAhaUbMA0YC/view?usp=drivesdk) | Versão publicada; páginas 1247–1250. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Figuras, gráficos e fluxograma

| Identificador e título | Subseções | PNG claro / escuro | PDF claro / escuro |
| --- | --- | --- | --- |
| G08_series_potencia — Potência em dias de menor e maior variabilidade | 3.6; 4.4 | [Claro](../../../03_Modelagem_Fotovoltaica/graficos/claro/G08_series_potencia.png) / [Escuro](../../../03_Modelagem_Fotovoltaica/graficos/escuro/G08_series_potencia.png) | [Claro](../../../03_Modelagem_Fotovoltaica/graficos/claro/G08_series_potencia.pdf) / [Escuro](../../../03_Modelagem_Fotovoltaica/graficos/escuro/G08_series_potencia.pdf) |
| G09_energia_diaria — Energia diária em intervalos pareados | 3.6; 4.4 | [Claro](../../../03_Modelagem_Fotovoltaica/graficos/claro/G09_energia_diaria.png) / [Escuro](../../../03_Modelagem_Fotovoltaica/graficos/escuro/G09_energia_diaria.png) | [Claro](../../../03_Modelagem_Fotovoltaica/graficos/claro/G09_energia_diaria.pdf) / [Escuro](../../../03_Modelagem_Fotovoltaica/graficos/escuro/G09_energia_diaria.pdf) |
| G13_validacao — Comparação entre potência simulada e medida | 4.4 | [Claro](../../graficos/claro/G13_validacao.png) / [Escuro](../../graficos/escuro/G13_validacao.png) | [Claro](../../graficos/claro/G13_validacao.pdf) / [Escuro](../../graficos/escuro/G13_validacao.pdf) |
| G14_residuos_temporais — Resíduos ao longo do trimestre | 4.4 | [Claro](../../graficos/claro/G14_residuos_temporais.png) / [Escuro](../../graficos/escuro/G14_residuos_temporais.png) | [Claro](../../graficos/claro/G14_residuos_temporais.pdf) / [Escuro](../../graficos/escuro/G14_residuos_temporais.pdf) |
| G15_residuos_potencia — Resíduos em função da potência observada | 4.4 | [Claro](../../graficos/claro/G15_residuos_potencia.png) / [Escuro](../../graficos/escuro/G15_residuos_potencia.png) | [Claro](../../graficos/claro/G15_residuos_potencia.pdf) / [Escuro](../../graficos/escuro/G15_residuos_potencia.pdf) |
| G16_distribuicao_residuos — Distribuição dos resíduos | 4.4 | [Claro](../../graficos/claro/G16_distribuicao_residuos.png) / [Escuro](../../graficos/escuro/G16_distribuicao_residuos.png) | [Claro](../../graficos/claro/G16_distribuicao_residuos.pdf) / [Escuro](../../graficos/escuro/G16_distribuicao_residuos.pdf) |
| G17_metricas_mensais — Erros mensais do modelo físico | 4.4 | [Claro](../../graficos/claro/G17_metricas_mensais.png) / [Escuro](../../graficos/escuro/G17_metricas_mensais.png) | [Claro](../../graficos/claro/G17_metricas_mensais.pdf) / [Escuro](../../graficos/escuro/G17_metricas_mensais.pdf) |
| G18_vies_horario — Viés por hora local e tamanho da amostra | 4.4 | [Claro](../../graficos/claro/G18_vies_horario.png) / [Escuro](../../graficos/escuro/G18_vies_horario.png) | [Claro](../../graficos/claro/G18_vies_horario.pdf) / [Escuro](../../graficos/escuro/G18_vies_horario.pdf) |
| G19_consistencia_medicoes — Consistência entre referências elétricas | 1.4; 4.4 | [Claro](../../../01_Recurso_Solar/graficos/claro/G19_consistencia_medicoes.png) / [Escuro](../../../01_Recurso_Solar/graficos/escuro/G19_consistencia_medicoes.png) | [Claro](../../../01_Recurso_Solar/graficos/claro/G19_consistencia_medicoes.pdf) / [Escuro](../../../01_Recurso_Solar/graficos/escuro/G19_consistencia_medicoes.pdf) |
| FL01_fluxo_projeto — Fluxo do estudo com medições locais | 1.4; 3.1; 4.4; 4.5 | [Claro](../../../01_Recurso_Solar/figuras/fluxogramas/claro/FL01_fluxo_projeto.png) / [Escuro](../../../01_Recurso_Solar/figuras/fluxogramas/escuro/FL01_fluxo_projeto.png) | [Claro](../../../01_Recurso_Solar/figuras/fluxogramas/claro/FL01_fluxo_projeto.pdf) / [Escuro](../../../01_Recurso_Solar/figuras/fluxogramas/escuro/FL01_fluxo_projeto.pdf) |

**G08_series_potencia:** Dias 2024-05-17 e 2024-05-04. Seleção pelo passo absoluto médio da POA dividido por sua média, com cobertura ≥99%; sem seleção pelo erro do modelo. Mesmos intervalos medidos/simulados. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R01; R08; R11.

**G09_energia_diaria:** Soma de potência média × 0,25 h sobre intervalos com os mesmos dados disponíveis. Não é a energia observada do dia inteiro. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R12.

**G13_validacao:** Modelo físico original, sem ajuste empírico; 4.401 pares diurnos. R²=1−SSE/SST e r calculado separadamente. nRMSE normalizado pela média observada dos pares. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R27.

**G14_residuos_temporais:** Resíduo = potência simulada − medida, sobre os pares diurnos. Valores positivos representam superestimação. Nenhum ponto foi removido pelo tamanho do erro. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R27.

**G15_residuos_potencia:** Diagnóstico de dependência do erro com o nível de potência; não identifica isoladamente causas operacionais, ópticas ou térmicas. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R27.

**G16_distribuicao_residuos:** Histograma dos mesmos 4.401 resíduos. MBE mantém o sinal; MAE e RMSE resumem magnitudes diferentes do erro e são apresentados em tabela. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R27.

**G17_metricas_mensais:** Mesma definição de erro; normalização pela média observada de cada mês. n e cobertura estão nas tabelas. Modelos com ajuste empírico são relatados separadamente. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R27.

**G18_vies_horario:** Médias condicionadas à janela diurna selecionada; cada faixa tem n e cobertura próprios. O padrão horário não prova uma causa única. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R27.

**G19_consistencia_medicoes:** Comparação entre dois registros observacionais locais; não é previsão do modelo. Divergências entre medidor e inversores integram os limites da referência. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R01; R25.

**FL01_fluxo_projeto:** As observações AC são referência para comparação, não entrada da previsão física. Controle de qualidade e pareamento precedem a análise. Setas tracejadas identificam a extensão exploratória. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R01; R09; R14.

## Tabelas e quadros

| Tabela CSV | Subseções |
| --- | --- |
| [consistencia_medidor_inversores](../../../../outputs/tabelas/csv/consistencia_medidor_inversores.csv) | 1.4; 4.4 |
| [energia_diaria_pareada](../../../../outputs/tabelas/csv/energia_diaria_pareada.csv) | 3.6; 4.4 |
| [metricas_por_faixa_POA](../../../../outputs/tabelas/csv/metricas_por_faixa_POA.csv) | 4.4 |
| [metricas_por_hora](../../../../outputs/tabelas/csv/metricas_por_hora.csv) | 4.4 |
| [metricas_por_mes](../../../../outputs/tabelas/csv/metricas_por_mes.csv) | 4.4 |
| [metrics](../../../../outputs/tabelas/csv/metrics.csv) | 4.4 |

[Tabelas originais em Word](../../../../outputs/tabelas/docx/Tabelas_do_Projeto.docx) · [Quadros originais em Word](../../../../outputs/quadros/docx/Quadros_do_Projeto.docx)

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Word completo dos gráficos](../../../../outputs/graficos/docx/Graficos_do_Projeto.docx) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)
