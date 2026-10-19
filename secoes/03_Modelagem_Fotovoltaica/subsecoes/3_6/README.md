# 3.6 Integração temporal e estimativa de energia

Responsável: **Gabriela e Giulia**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Integração da potência ao longo do tempo para estimar energia horária, diária, mensal ou anual.

## Entradas, método e resultado esperado

**Entradas:** Potência média em intervalos de 15 minutos e máscaras temporais.

Integre potência média por duração de cada intervalo. Compare séries e energias nas mesmas janelas. Apresente energia mensal e trimestral observada completa separadamente dos intervalos diurnos pareados.

$$E=\sum_i P_i\Delta t_i,\qquad \Delta t=0,25\ \mathrm{h}.$$

**Saídas:** Energia diária/mensal, cobertura e totais integrais separados.

**Evidência:** Integração calculada e geração observada. **Limitação:** O recorte é trimestral, não uma medição anual; energia pareada não equivale ao total integral do dia.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B12](../../../../bibliografia/principal/README.md#b12) — Livro | DUFFIE, J. A.; BECKMAN, W. A.; BLAIR, N. Solar Engineering of Thermal Processes, Photovoltaics and Wind. [S. l.]: Wiley, 2020. DOI: https://doi.org/10.1002/9781119540328. Disponível em: https://doi.org/10.1002/9781119540328. Acesso em: 16 out. 2026. | [A001 — PDF](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) |
| [B19](../../../../bibliografia/principal/README.md#b19) — Livro | KALOGIROU, S. A. Solar Energy Engineering: Processes and Systems. 2. ed. [S. l.]: Elsevier, 2014. DOI: https://doi.org/10.1016/c2011-0-07038-2. Disponível em: https://doi.org/10.1016/c2011-0-07038-2. Acesso em: 16 out. 2026. | PDF não localizado |
| [B20](../../../../bibliografia/principal/README.md#b20) — Livro | LUQUE, A.; HEGEDUS, S. (ed.). Handbook of Photovoltaic Science and Engineering. 2. ed. [S. l.]: Wiley, 2011. DOI: https://doi.org/10.1002/9780470974704. Disponível em: https://doi.org/10.1002/9780470974704. Acesso em: 16 out. 2026. | [A034 — outra edição](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) |
| [B22](../../../../bibliografia/principal/README.md#b22) — Trabalho em evento | MARION, B. et al. Performance parameters for grid-connected PV systems. In: IEEE PHOTOVOLTAIC SPECIALISTS CONFERENCE, 31., 2005, [S. l.]. Conference Record of the Thirty-first IEEE Photovoltaic Specialists Conference, 2005. [S. l.]: IEEE, 2005. p. 1601-1606. DOI: https://doi.org/10.1109/pvsc.2005.1488451. Disponível em: https://doi.org/10.1109/pvsc.2005.1488451. Acesso em: 16 out. 2026. | [A066 — PDF](https://drive.google.com/file/d/1MPTgWBkbLYYRfkAIcvqC7_JwsFr5VXYe/view?usp=drivesdk) |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A001 | [Abrir Solar Engineering of Thermal Processes, Photovoltaics and Wind](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) | 5ª edição confirmada no PDF, com 919 páginas digitais e índice até a página impressa 905. Alternativa de trabalho adotada para B19, em conjunto com A003. Citar Duffie, Beckman e Blair (2020) ao usar este arquivo. |
| A034 | [Abrir Handbook of Photovoltaic Science and Engineering](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) | 1ª edição. Apoio alternativo a B20; não satisfaz a edição de 2011 indicada. |
| A066 | [Abrir Performance Parameters for Grid-Connected PV Systems — NREL/CP-520-37358](https://drive.google.com/file/d/1MPTgWBkbLYYRfkAIcvqC7_JwsFr5VXYe/view?usp=drivesdk) | Versão de relatório/manuscrito do trabalho em evento; essa versão física deve ser indicada ao citar páginas. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Figuras, gráficos e fluxograma

| Identificador e título | Subseções | PNG claro / escuro | PDF claro / escuro |
| --- | --- | --- | --- |
| G08_series_potencia — Potência em dias de menor e maior variabilidade | 3.6; 4.4 | [Claro](../../graficos/claro/G08_series_potencia.png) / [Escuro](../../graficos/escuro/G08_series_potencia.png) | [Claro](../../graficos/claro/G08_series_potencia.pdf) / [Escuro](../../graficos/escuro/G08_series_potencia.pdf) |
| G09_energia_diaria — Energia diária em intervalos pareados | 3.6; 4.4 | [Claro](../../graficos/claro/G09_energia_diaria.png) / [Escuro](../../graficos/escuro/G09_energia_diaria.png) | [Claro](../../graficos/claro/G09_energia_diaria.pdf) / [Escuro](../../graficos/escuro/G09_energia_diaria.pdf) |
| G10_energia_mensal — Energia mensal na janela de comparação | 3.6 | [Claro](../../graficos/claro/G10_energia_mensal.png) / [Escuro](../../graficos/escuro/G10_energia_mensal.png) | [Claro](../../graficos/claro/G10_energia_mensal.pdf) / [Escuro](../../graficos/escuro/G10_energia_mensal.pdf) |

**G08_series_potencia:** Dias 2024-05-17 e 2024-05-04. Seleção pelo passo absoluto médio da POA dividido por sua média, com cobertura ≥99%; sem seleção pelo erro do modelo. Mesmos intervalos medidos/simulados. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R01; R08; R11.

**G09_energia_diaria:** Soma de potência média × 0,25 h sobre intervalos com os mesmos dados disponíveis. Não é a energia observada do dia inteiro. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R12.

**G10_energia_mensal:** Energia simulada e observada calculadas sobre a mesma máscara diurna pareada. Totais integrais medidos do mês são fornecidos separadamente nas tabelas. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R12.

## Tabelas e quadros

| Tabela CSV | Subseções |
| --- | --- |
| [energia_diaria_pareada](../../../../outputs/tabelas/csv/energia_diaria_pareada.csv) | 3.6; 4.4 |
| [energia_e_indicadores_mensais](../../../../outputs/tabelas/csv/energia_e_indicadores_mensais.csv) | 3.6; 4.2; 4.3 |
| [series_15min_local_e_modelo](../../../../outputs/tabelas/csv/series_15min_local_e_modelo.csv) | 3.6 |

[Tabelas originais em Word](../../../../outputs/tabelas/docx/Tabelas_do_Projeto.docx) · [Quadros originais em Word](../../../../outputs/quadros/docx/Quadros_do_Projeto.docx)

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Word completo dos gráficos](../../../../outputs/graficos/docx/Graficos_do_Projeto.docx) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)
