# 3.2 Modelagem da temperatura operacional

Responsável: **Gabriela e Giulia**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Estimativa da temperatura da célula ou do módulo a partir da irradiância, temperatura ambiente e vento.

## Entradas, método e resultado esperado

**Entradas:** POA, temperatura do ar, vento e coeficientes Faiman.

A temperatura estimada entra no modelo elétrico. U₀=25 W/(m² K) e U₁=6,84 W s/(m³ K) são parâmetros genéricos de referência; a sensibilidade de ventilação usa 15 e 3, respectivamente.

$$T_{\mathrm{op}}=T_a+G_{\mathrm{ef}}/(U_0+U_1v).$$

**Saídas:** Temperatura estimada e registro dos coeficientes.

**Evidência:** Modelo térmico. **Limitação:** Ausência de temperatura de módulo/célula e altura de vento suficientemente documentada.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B12](../../../../bibliografia/principal/README.md#b12) — Livro | DUFFIE, J. A.; BECKMAN, W. A.; BLAIR, N. Solar Engineering of Thermal Processes, Photovoltaics and Wind. [S. l.]: Wiley, 2020. DOI: https://doi.org/10.1002/9781119540328. Disponível em: https://doi.org/10.1002/9781119540328. Acesso em: 16 out. 2026. | [A001 — PDF](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) |
| [B13](../../../../bibliografia/principal/README.md#b13) — Artigo | FAIMAN, D. Assessing the outdoor operating temperature of photovoltaic modules. Progress in Photovoltaics: Research and Applications, [S. l.], v. 16, n. 4, p. 307-315, 2008. DOI: https://doi.org/10.1002/pip.813. Disponível em: https://doi.org/10.1002/pip.813. Acesso em: 16 out. 2026. | [A030 — PDF](https://drive.google.com/file/d/1a5bAatpefvDnnLc4ffZoFQJizKzCsnHV/view?usp=drivesdk) |
| [B19](../../../../bibliografia/principal/README.md#b19) — Livro | KALOGIROU, S. A. Solar Energy Engineering: Processes and Systems. 2. ed. [S. l.]: Elsevier, 2014. DOI: https://doi.org/10.1016/c2011-0-07038-2. Disponível em: https://doi.org/10.1016/c2011-0-07038-2. Acesso em: 16 out. 2026. | PDF não localizado |
| [B20](../../../../bibliografia/principal/README.md#b20) — Livro | LUQUE, A.; HEGEDUS, S. (ed.). Handbook of Photovoltaic Science and Engineering. 2. ed. [S. l.]: Wiley, 2011. DOI: https://doi.org/10.1002/9780470974704. Disponível em: https://doi.org/10.1002/9780470974704. Acesso em: 16 out. 2026. | [A034 — outra edição](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) |
| [B37](../../../../bibliografia/principal/README.md#b37) — Artigo | SKOPLAKI, E.; PALYVOS, J. A. On the temperature dependence of photovoltaic module electrical performance: A review of efficiency/power correlations. Solar Energy, [S. l.], v. 83, n. 5, p. 614-624, 2009. DOI: https://doi.org/10.1016/j.solener.2008.10.008. Disponível em: https://doi.org/10.1016/j.solener.2008.10.008. Acesso em: 16 out. 2026. | [A024 — PDF](https://drive.google.com/file/d/1F1kNAs41Buzt_p_R7WcxxQ_2iq6HxDvu/view?usp=drivesdk) |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A001 | [Abrir Solar Engineering of Thermal Processes, Photovoltaics and Wind](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) | 5ª edição confirmada no PDF, com 919 páginas digitais e índice até a página impressa 905. Alternativa de trabalho adotada para B19, em conjunto com A003. Citar Duffie, Beckman e Blair (2020) ao usar este arquivo. |
| A024 | [Abrir On the temperature dependence of photovoltaic module electrical performance: A review of efficiency/power correlations](https://drive.google.com/file/d/1F1kNAs41Buzt_p_R7WcxxQ_2iq6HxDvu/view?usp=drivesdk) |  |
| A030 | [Abrir Assessing the outdoor operating temperature of photovoltaic modules](https://drive.google.com/file/d/1a5bAatpefvDnnLc4ffZoFQJizKzCsnHV/view?usp=drivesdk) |  |
| A034 | [Abrir Handbook of Photovoltaic Science and Engineering](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) | 1ª edição. Apoio alternativo a B20; não satisfaz a edição de 2011 indicada. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Figuras, gráficos e fluxograma

| Identificador e título | Subseções | PNG claro / escuro | PDF claro / escuro |
| --- | --- | --- | --- |
| G04_temperatura_estimada — Resposta térmica estimada pelo modelo | 2.1; 3.2 | [Claro](../../../02_Condicoes_Ambientais/graficos/claro/G04_temperatura_estimada.png) / [Escuro](../../../02_Condicoes_Ambientais/graficos/escuro/G04_temperatura_estimada.png) | [Claro](../../../02_Condicoes_Ambientais/graficos/claro/G04_temperatura_estimada.pdf) / [Escuro](../../../02_Condicoes_Ambientais/graficos/escuro/G04_temperatura_estimada.pdf) |

**G04_temperatura_estimada:** Elevação térmica por Faiman com U₀=25 W/(m² K) e U₁=6,84 W s/(m³ K). Temperatura operacional usada como aproximação da célula; sem medição térmica independente. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R07.

## Tabelas e quadros

| Tabela CSV | Subseções |
| --- | --- |
| [environment_sensitivity](../../../../outputs/tabelas/csv/environment_sensitivity.csv) | 2.1; 2.3; 3.2 |
| [estatistica_descritiva](../../../../outputs/tabelas/csv/estatistica_descritiva.csv) | 2.1; 3.2 |

[Tabelas originais em Word](../../../../outputs/tabelas/docx/Tabelas_do_Projeto.docx) · [Quadros originais em Word](../../../../outputs/quadros/docx/Quadros_do_Projeto.docx)

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Word completo dos gráficos](../../../../outputs/graficos/docx/Graficos_do_Projeto.docx) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)
