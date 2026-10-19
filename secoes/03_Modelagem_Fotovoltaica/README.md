# 3 Modelagem da conversão fotovoltaica

[Guia técnico comum do estudo de caso em Word](../../docs/metodos/Guia_Tecnico_Resumido_PVDAQ_2107.docx): origem dos dados, período, equipamentos, entradas e hipóteses para as quatro seções.

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

## Materiais exclusivos desta seção

Cada ID tem um único local de inserção no capítulo. As versões claro/escuro e PNG/PDF são alternativas do mesmo item; escolher apenas uma para a redação. Ao discutir um item de outra seção, fazer referência ao ID já inserido, sem reproduzi-lo.

| ID e título | Inserir em | PNG claro e escuro | PDF claro e escuro |
| --- | --- | --- | --- |
| G04_temperatura_estimada — Resposta térmica estimada pelo modelo | 3.2 | [Claro](graficos/claro/G04_temperatura_estimada.png) / [Escuro](graficos/escuro/G04_temperatura_estimada.png) | [Claro](graficos/claro/G04_temperatura_estimada.pdf) / [Escuro](graficos/escuro/G04_temperatura_estimada.pdf) |
| G05_curvas_irradiancia — Curvas elétricas para diferentes irradiâncias | 3.3 | [Claro](graficos/claro/G05_curvas_irradiancia.png) / [Escuro](graficos/escuro/G05_curvas_irradiancia.png) | [Claro](graficos/claro/G05_curvas_irradiancia.pdf) / [Escuro](graficos/escuro/G05_curvas_irradiancia.pdf) |
| G06_curvas_temperatura — Curvas elétricas para diferentes temperaturas | 3.3 | [Claro](graficos/claro/G06_curvas_temperatura.png) / [Escuro](graficos/escuro/G06_curvas_temperatura.png) | [Claro](graficos/claro/G06_curvas_temperatura.pdf) / [Escuro](graficos/escuro/G06_curvas_temperatura.pdf) |
| G07_inversor — Eficiência e limitação de potência do inversor | 3.5 | [Claro](graficos/claro/G07_inversor.png) / [Escuro](graficos/escuro/G07_inversor.png) | [Claro](graficos/claro/G07_inversor.pdf) / [Escuro](graficos/escuro/G07_inversor.pdf) |
| G08_series_potencia — Potência em dias de menor e maior variabilidade | 3.6 | [Claro](graficos/claro/G08_series_potencia.png) / [Escuro](graficos/escuro/G08_series_potencia.png) | [Claro](graficos/claro/G08_series_potencia.pdf) / [Escuro](graficos/escuro/G08_series_potencia.pdf) |
| G09_energia_diaria — Energia diária em intervalos pareados | 3.6 | [Claro](graficos/claro/G09_energia_diaria.png) / [Escuro](graficos/escuro/G09_energia_diaria.png) | [Claro](graficos/claro/G09_energia_diaria.pdf) / [Escuro](graficos/escuro/G09_energia_diaria.pdf) |
| G10_energia_mensal — Energia mensal na janela de comparação | 3.6 | [Claro](graficos/claro/G10_energia_mensal.png) / [Escuro](graficos/escuro/G10_energia_mensal.png) | [Claro](graficos/claro/G10_energia_mensal.pdf) / [Escuro](graficos/escuro/G10_energia_mensal.pdf) |
| G23_componentes_estimadas — Componentes reconstruídas da POA | 3.1 | [Claro](graficos/claro/G23_componentes_estimadas.png) / [Escuro](graficos/escuro/G23_componentes_estimadas.png) | [Claro](graficos/claro/G23_componentes_estimadas.pdf) / [Escuro](graficos/escuro/G23_componentes_estimadas.pdf) |
| F03_arranjo_eletrico — Organização elétrica do sistema de referência | 3.4 | [Claro](figuras/claro/F03_arranjo_eletrico.png) / [Escuro](figuras/escuro/F03_arranjo_eletrico.png) | [Claro](figuras/claro/F03_arranjo_eletrico.pdf) / [Escuro](figuras/escuro/F03_arranjo_eletrico.pdf) |

[Tabelas e séries da seção](tabelas/README.md) · [Quadros da seção](quadros/README.md) · [Word exclusivo desta seção](tabelas/docx/Materiais_Tabulares_Secao_03.docx)

[Mapa geral e regra de inserção única](../../docs/Distribuicao_Editorial.md)
