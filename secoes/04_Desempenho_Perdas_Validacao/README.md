# 4 Avaliação de desempenho, perdas e validação da modelagem

Responsáveis: **Júlia Ribeiro e Lucas Simão**.

Como o desempenho de um sistema fotovoltaico é quantificado, como suas perdas são decompostas e quão bem o modelo reproduz o comportamento observado?

| Subseção oficial | Responsável | Referências prioritárias |
| --- | --- | --- |
| [4.1 Balanço energético e cadeia de perdas](subsecoes/4_1/README.md) | Júlia Ribeiro | [B08](../../bibliografia/principal/README.md#b08), [B17](../../bibliografia/principal/README.md#b17), [B20](../../bibliografia/principal/README.md#b20), [B21](../../bibliografia/principal/README.md#b21), [B22](../../bibliografia/principal/README.md#b22), [B26](../../bibliografia/principal/README.md#b26) |
| [4.2 Produtividades de referência, do arranjo e final](subsecoes/4_2/README.md) | Lucas Simão | [B12](../../bibliografia/principal/README.md#b12), [B20](../../bibliografia/principal/README.md#b20), [B22](../../bibliografia/principal/README.md#b22), [B33](../../bibliografia/principal/README.md#b33) |
| [4.3 Razão de desempenho (Performance Ratio](subsecoes/4_3/README.md) | Lucas Simão | [B09](../../bibliografia/principal/README.md#b09), [B12](../../bibliografia/principal/README.md#b12), [B20](../../bibliografia/principal/README.md#b20), [B22](../../bibliografia/principal/README.md#b22), [B33](../../bibliografia/principal/README.md#b33) |
| [4.4 Validação de modelos de geração fotovoltaica](subsecoes/4_4/README.md) | Lucas Simão | [B07](../../bibliografia/principal/README.md#b07), [B26](../../bibliografia/principal/README.md#b26), [B39](../../bibliografia/principal/README.md#b39) |
| [4.5 Avaliação de desempenho de sistemas fotovoltaicos integrados à edificação (BIPV)](subsecoes/4_5/README.md) | Júlia Ribeiro | [B02](../../bibliografia/principal/README.md#b02), [B05](../../bibliografia/principal/README.md#b05), [B11](../../bibliografia/principal/README.md#b11), [B16](../../bibliografia/principal/README.md#b16), [B18](../../bibliografia/principal/README.md#b18), [B20](../../bibliografia/principal/README.md#b20) |

## Materiais da seção

| Coleção | Acesso |
| --- | --- |
| figuras | [Abrir figuras](figuras/README.md) |
| graficos | [Abrir graficos](graficos/README.md) |
| tabelas | [Abrir tabelas](tabelas/README.md) |
| quadros | [Abrir quadros](quadros/README.md) |
| documentos | [Abrir documentos](documentos/README.md) |
| referencias | [Abrir referencias](referencias/README.md) |

## Ilustrações pertinentes

| Identificador e título | Subseções | PNG claro / escuro | PDF claro / escuro |
| --- | --- | --- | --- |
| G08_series_potencia — Potência em dias de menor e maior variabilidade | 3.6; 4.4 | [Claro](../03_Modelagem_Fotovoltaica/graficos/claro/G08_series_potencia.png) / [Escuro](../03_Modelagem_Fotovoltaica/graficos/escuro/G08_series_potencia.png) | [Claro](../03_Modelagem_Fotovoltaica/graficos/claro/G08_series_potencia.pdf) / [Escuro](../03_Modelagem_Fotovoltaica/graficos/escuro/G08_series_potencia.pdf) |
| G09_energia_diaria — Energia diária em intervalos pareados | 3.6; 4.4 | [Claro](../03_Modelagem_Fotovoltaica/graficos/claro/G09_energia_diaria.png) / [Escuro](../03_Modelagem_Fotovoltaica/graficos/escuro/G09_energia_diaria.png) | [Claro](../03_Modelagem_Fotovoltaica/graficos/claro/G09_energia_diaria.pdf) / [Escuro](../03_Modelagem_Fotovoltaica/graficos/escuro/G09_energia_diaria.pdf) |
| G11_cadeia_energetica — Cadeia de energia calculada | 4.1 | [Claro](graficos/claro/G11_cadeia_energetica.png) / [Escuro](graficos/escuro/G11_cadeia_energetica.png) | [Claro](graficos/claro/G11_cadeia_energetica.pdf) / [Escuro](graficos/escuro/G11_cadeia_energetica.pdf) |
| G12_produtividades_PR — Produtividades e razão de desempenho | 4.2; 4.3 | [Claro](graficos/claro/G12_produtividades_PR.png) / [Escuro](graficos/escuro/G12_produtividades_PR.png) | [Claro](graficos/claro/G12_produtividades_PR.pdf) / [Escuro](graficos/escuro/G12_produtividades_PR.pdf) |
| G13_validacao — Comparação entre potência simulada e medida | 4.4 | [Claro](graficos/claro/G13_validacao.png) / [Escuro](graficos/escuro/G13_validacao.png) | [Claro](graficos/claro/G13_validacao.pdf) / [Escuro](graficos/escuro/G13_validacao.pdf) |
| G14_residuos_temporais — Resíduos ao longo do trimestre | 4.4 | [Claro](graficos/claro/G14_residuos_temporais.png) / [Escuro](graficos/escuro/G14_residuos_temporais.png) | [Claro](graficos/claro/G14_residuos_temporais.pdf) / [Escuro](graficos/escuro/G14_residuos_temporais.pdf) |
| G15_residuos_potencia — Resíduos em função da potência observada | 4.4 | [Claro](graficos/claro/G15_residuos_potencia.png) / [Escuro](graficos/escuro/G15_residuos_potencia.png) | [Claro](graficos/claro/G15_residuos_potencia.pdf) / [Escuro](graficos/escuro/G15_residuos_potencia.pdf) |
| G16_distribuicao_residuos — Distribuição dos resíduos | 4.4 | [Claro](graficos/claro/G16_distribuicao_residuos.png) / [Escuro](graficos/escuro/G16_distribuicao_residuos.png) | [Claro](graficos/claro/G16_distribuicao_residuos.pdf) / [Escuro](graficos/escuro/G16_distribuicao_residuos.pdf) |
| G17_metricas_mensais — Erros mensais do modelo físico | 4.4 | [Claro](graficos/claro/G17_metricas_mensais.png) / [Escuro](graficos/escuro/G17_metricas_mensais.png) | [Claro](graficos/claro/G17_metricas_mensais.pdf) / [Escuro](graficos/escuro/G17_metricas_mensais.pdf) |
| G18_vies_horario — Viés por hora local e tamanho da amostra | 4.4 | [Claro](graficos/claro/G18_vies_horario.png) / [Escuro](graficos/escuro/G18_vies_horario.png) | [Claro](graficos/claro/G18_vies_horario.pdf) / [Escuro](graficos/escuro/G18_vies_horario.pdf) |
| G19_consistencia_medicoes — Consistência entre referências elétricas | 1.4; 4.4 | [Claro](../01_Recurso_Solar/graficos/claro/G19_consistencia_medicoes.png) / [Escuro](../01_Recurso_Solar/graficos/escuro/G19_consistencia_medicoes.png) | [Claro](../01_Recurso_Solar/graficos/claro/G19_consistencia_medicoes.pdf) / [Escuro](../01_Recurso_Solar/graficos/escuro/G19_consistencia_medicoes.pdf) |
| G21_HSP_POA_pareada — Horas equivalentes de sol na janela pareada | 4.2 | [Claro](graficos/claro/G21_HSP_POA_pareada.png) / [Escuro](graficos/escuro/G21_HSP_POA_pareada.png) | [Claro](graficos/claro/G21_HSP_POA_pareada.pdf) / [Escuro](graficos/escuro/G21_HSP_POA_pareada.pdf) |
| G24_BIPV_orientacoes — Cenários de orientação e integração | 2.4; 4.5 | [Claro](../02_Condicoes_Ambientais/graficos/claro/G24_BIPV_orientacoes.png) / [Escuro](../02_Condicoes_Ambientais/graficos/escuro/G24_BIPV_orientacoes.png) | [Claro](../02_Condicoes_Ambientais/graficos/claro/G24_BIPV_orientacoes.pdf) / [Escuro](../02_Condicoes_Ambientais/graficos/escuro/G24_BIPV_orientacoes.pdf) |
| G25_BIPV_balanco — Partição solar do exemplo semitransparente | 4.5 | [Claro](graficos/claro/G25_BIPV_balanco.png) / [Escuro](graficos/escuro/G25_BIPV_balanco.png) | [Claro](graficos/claro/G25_BIPV_balanco.pdf) / [Escuro](graficos/escuro/G25_BIPV_balanco.pdf) |
| FL01_fluxo_projeto — Fluxo do estudo com medições locais | 1.4; 3.1; 4.4; 4.5 | [Claro](../01_Recurso_Solar/figuras/fluxogramas/claro/FL01_fluxo_projeto.png) / [Escuro](../01_Recurso_Solar/figuras/fluxogramas/escuro/FL01_fluxo_projeto.png) | [Claro](../01_Recurso_Solar/figuras/fluxogramas/claro/FL01_fluxo_projeto.pdf) / [Escuro](../01_Recurso_Solar/figuras/fluxogramas/escuro/FL01_fluxo_projeto.pdf) |
| F04_geometrias_BIPV — Arranjo inclinado e extensão de fachada | 2.4; 4.5 | [Claro](../02_Condicoes_Ambientais/figuras/claro/F04_geometrias_BIPV.png) / [Escuro](../02_Condicoes_Ambientais/figuras/escuro/F04_geometrias_BIPV.png) | [Claro](../02_Condicoes_Ambientais/figuras/claro/F04_geometrias_BIPV.pdf) / [Escuro](../02_Condicoes_Ambientais/figuras/escuro/F04_geometrias_BIPV.pdf) |

[Início](../../README.md) · [Proposta oficial em Word](../../docs/planejamento/Proposta_do_Capitulo_Recurso_Solar_FV.docx)
