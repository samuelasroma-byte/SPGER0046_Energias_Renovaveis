# 3 Modelagem da conversão fotovoltaica

Responsáveis: **Gabriela e Giulia**.

Como essas entradas são incorporadas aos modelos para estimar a potência e a energia produzidas pelo sistema fotovoltaico?

| Subseção oficial | Responsável | Referências prioritárias |
| --- | --- | --- |
| [3.1 Transposição para o plano do arranjo](subsecoes/3_1/README.md) | Gabriela e Giulia | [B11](../../bibliografia/principal/README.md#b11), [B12](../../bibliografia/principal/README.md#b12), [B19](../../bibliografia/principal/README.md#b19), [B25](../../bibliografia/principal/README.md#b25), [B30](../../bibliografia/principal/README.md#b30), [B36](../../bibliografia/principal/README.md#b36) |
| [3.2 Modelagem da temperatura operacional](subsecoes/3_2/README.md) | Gabriela e Giulia | [B12](../../bibliografia/principal/README.md#b12), [B13](../../bibliografia/principal/README.md#b13), [B19](../../bibliografia/principal/README.md#b19), [B20](../../bibliografia/principal/README.md#b20), [B37](../../bibliografia/principal/README.md#b37) |
| [3.3 Modelagem elétrica do módulo fotovoltaico](subsecoes/3_3/README.md) | Gabriela e Giulia | [B08](../../bibliografia/principal/README.md#b08), [B12](../../bibliografia/principal/README.md#b12), [B14](../../bibliografia/principal/README.md#b14), [B20](../../bibliografia/principal/README.md#b20), [B28](../../bibliografia/principal/README.md#b28), [B38](../../bibliografia/principal/README.md#b38) |
| [3.4 Modelagem do arranjo fotovoltaico em corrente contínua (CC)](subsecoes/3_4/README.md) | Gabriela e Giulia | [B04](../../bibliografia/principal/README.md#b04), [B08](../../bibliografia/principal/README.md#b08), [B12](../../bibliografia/principal/README.md#b12), [B20](../../bibliografia/principal/README.md#b20), [B28](../../bibliografia/principal/README.md#b28), [B38](../../bibliografia/principal/README.md#b38) |
| [3.5 Conversão de CC para corrente alternada (CA) e modelagem do inversor](subsecoes/3_5/README.md) | Gabriela e Giulia | [B01](../../bibliografia/principal/README.md#b01), [B06](../../bibliografia/principal/README.md#b06), [B10](../../bibliografia/principal/README.md#b10), [B12](../../bibliografia/principal/README.md#b12), [B20](../../bibliografia/principal/README.md#b20) |
| [3.6 Integração temporal e estimativa de energia](subsecoes/3_6/README.md) | Gabriela e Giulia | [B12](../../bibliografia/principal/README.md#b12), [B19](../../bibliografia/principal/README.md#b19), [B20](../../bibliografia/principal/README.md#b20), [B22](../../bibliografia/principal/README.md#b22) |

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
| G04_temperatura_estimada — Resposta térmica estimada pelo modelo | 2.1; 3.2 | [Claro](../02_Condicoes_Ambientais/graficos/claro/G04_temperatura_estimada.png) / [Escuro](../02_Condicoes_Ambientais/graficos/escuro/G04_temperatura_estimada.png) | [Claro](../02_Condicoes_Ambientais/graficos/claro/G04_temperatura_estimada.pdf) / [Escuro](../02_Condicoes_Ambientais/graficos/escuro/G04_temperatura_estimada.pdf) |
| G05_curvas_irradiancia — Curvas elétricas para diferentes irradiâncias | 3.3 | [Claro](graficos/claro/G05_curvas_irradiancia.png) / [Escuro](graficos/escuro/G05_curvas_irradiancia.png) | [Claro](graficos/claro/G05_curvas_irradiancia.pdf) / [Escuro](graficos/escuro/G05_curvas_irradiancia.pdf) |
| G06_curvas_temperatura — Curvas elétricas para diferentes temperaturas | 3.3 | [Claro](graficos/claro/G06_curvas_temperatura.png) / [Escuro](graficos/escuro/G06_curvas_temperatura.png) | [Claro](graficos/claro/G06_curvas_temperatura.pdf) / [Escuro](graficos/escuro/G06_curvas_temperatura.pdf) |
| G07_inversor — Eficiência e limitação de potência do inversor | 3.5 | [Claro](graficos/claro/G07_inversor.png) / [Escuro](graficos/escuro/G07_inversor.png) | [Claro](graficos/claro/G07_inversor.pdf) / [Escuro](graficos/escuro/G07_inversor.pdf) |
| G08_series_potencia — Potência em dias de menor e maior variabilidade | 3.6; 4.4 | [Claro](graficos/claro/G08_series_potencia.png) / [Escuro](graficos/escuro/G08_series_potencia.png) | [Claro](graficos/claro/G08_series_potencia.pdf) / [Escuro](graficos/escuro/G08_series_potencia.pdf) |
| G09_energia_diaria — Energia diária em intervalos pareados | 3.6; 4.4 | [Claro](graficos/claro/G09_energia_diaria.png) / [Escuro](graficos/escuro/G09_energia_diaria.png) | [Claro](graficos/claro/G09_energia_diaria.pdf) / [Escuro](graficos/escuro/G09_energia_diaria.pdf) |
| G10_energia_mensal — Energia mensal na janela de comparação | 3.6 | [Claro](graficos/claro/G10_energia_mensal.png) / [Escuro](graficos/escuro/G10_energia_mensal.png) | [Claro](graficos/claro/G10_energia_mensal.pdf) / [Escuro](graficos/escuro/G10_energia_mensal.pdf) |
| G22_albedo — Sensibilidade ao albedo assumido | 2.2; 3.1 | [Claro](../02_Condicoes_Ambientais/graficos/claro/G22_albedo.png) / [Escuro](../02_Condicoes_Ambientais/graficos/escuro/G22_albedo.png) | [Claro](../02_Condicoes_Ambientais/graficos/claro/G22_albedo.pdf) / [Escuro](../02_Condicoes_Ambientais/graficos/escuro/G22_albedo.pdf) |
| G23_componentes_estimadas — Componentes reconstruídas da POA | 1.2; 3.1 | [Claro](../01_Recurso_Solar/graficos/claro/G23_componentes_estimadas.png) / [Escuro](../01_Recurso_Solar/graficos/escuro/G23_componentes_estimadas.png) | [Claro](../01_Recurso_Solar/graficos/claro/G23_componentes_estimadas.pdf) / [Escuro](../01_Recurso_Solar/graficos/escuro/G23_componentes_estimadas.pdf) |
| FL01_fluxo_projeto — Fluxo do estudo com medições locais | 1.4; 3.1; 4.4; 4.5 | [Claro](../01_Recurso_Solar/figuras/fluxogramas/claro/FL01_fluxo_projeto.png) / [Escuro](../01_Recurso_Solar/figuras/fluxogramas/escuro/FL01_fluxo_projeto.png) | [Claro](../01_Recurso_Solar/figuras/fluxogramas/claro/FL01_fluxo_projeto.pdf) / [Escuro](../01_Recurso_Solar/figuras/fluxogramas/escuro/FL01_fluxo_projeto.pdf) |
| F01_plano_angulos — Plano do arranjo e convenções angulares | 1.1; 2.4; 3.1 | [Claro](../01_Recurso_Solar/figuras/claro/F01_plano_angulos.png) / [Escuro](../01_Recurso_Solar/figuras/escuro/F01_plano_angulos.png) | [Claro](../01_Recurso_Solar/figuras/claro/F01_plano_angulos.pdf) / [Escuro](../01_Recurso_Solar/figuras/escuro/F01_plano_angulos.pdf) |
| F02_componentes_POA — Componentes incidentes no plano do módulo | 1.2; 2.2; 3.1 | [Claro](../01_Recurso_Solar/figuras/claro/F02_componentes_POA.png) / [Escuro](../01_Recurso_Solar/figuras/escuro/F02_componentes_POA.png) | [Claro](../01_Recurso_Solar/figuras/claro/F02_componentes_POA.pdf) / [Escuro](../01_Recurso_Solar/figuras/escuro/F02_componentes_POA.pdf) |
| F03_arranjo_eletrico — Organização elétrica do sistema de referência | 3.3; 3.4; 3.5 | [Claro](figuras/claro/F03_arranjo_eletrico.png) / [Escuro](figuras/escuro/F03_arranjo_eletrico.png) | [Claro](figuras/claro/F03_arranjo_eletrico.pdf) / [Escuro](figuras/escuro/F03_arranjo_eletrico.pdf) |

[Início](../../README.md) · [Proposta oficial em Word](../../docs/planejamento/Proposta_do_Capitulo_Recurso_Solar_FV.docx)
