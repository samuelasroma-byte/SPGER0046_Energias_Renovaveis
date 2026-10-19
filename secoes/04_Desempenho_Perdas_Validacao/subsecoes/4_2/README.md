# 4.2 Produtividades de referência, do arranjo e final

Responsável: **Lucas Simão**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Produtividade de referência (Yr), produtividade do arranjo (Ya) e produtividade final (Yf); produtividade específica em quilowatt-hora por quilowatt-pico (kWh/kWp). (Lucas)

## Entradas, método e resultado esperado

**Entradas:** Irradiação POA, energia DC/AC e potência declarada de 893 kWp.

Yr é o recurso em horas equivalentes; Ya representa a energia DC por capacidade; Yf representa energia AC por capacidade. HSP/PSH corresponde ao mesmo conceito de recurso quando plano e janela são os mesmos.

$$Y_r=H_{\mathrm{POA}}/G_{\mathrm{ref}},\quad Y_a=E_{\mathrm{DC}}/P_0,\quad Y_f=E_{\mathrm{AC}}/P_0,\quad G_{\mathrm{ref}}=1\ \mathrm{kW/m^2}.$$

**Saídas:** Yr, Ya, Yf e HSP na janela definida.

**Evidência:** Indicadores sobre observações e modelo. **Limitação:** Ya é modelada; HSP da janela pareada não é duração de brilho solar nem total integral diário.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B12](../../../../bibliografia/principal/README.md#b12) — Livro | DUFFIE, J. A.; BECKMAN, W. A.; BLAIR, N. Solar Engineering of Thermal Processes, Photovoltaics and Wind. [S. l.]: Wiley, 2020. DOI: https://doi.org/10.1002/9781119540328. Disponível em: https://doi.org/10.1002/9781119540328. Acesso em: 16 out. 2026. | [A001 — PDF](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) |
| [B20](../../../../bibliografia/principal/README.md#b20) — Livro | LUQUE, A.; HEGEDUS, S. (ed.). Handbook of Photovoltaic Science and Engineering. 2. ed. [S. l.]: Wiley, 2011. DOI: https://doi.org/10.1002/9780470974704. Disponível em: https://doi.org/10.1002/9780470974704. Acesso em: 16 out. 2026. | [A034 — outra edição](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) |
| [B22](../../../../bibliografia/principal/README.md#b22) — Trabalho em evento | MARION, B. et al. Performance parameters for grid-connected PV systems. In: IEEE PHOTOVOLTAIC SPECIALISTS CONFERENCE, 31., 2005, [S. l.]. Conference Record of the Thirty-first IEEE Photovoltaic Specialists Conference, 2005. [S. l.]: IEEE, 2005. p. 1601-1606. DOI: https://doi.org/10.1109/pvsc.2005.1488451. Disponível em: https://doi.org/10.1109/pvsc.2005.1488451. Acesso em: 16 out. 2026. | [A066 — PDF](https://drive.google.com/file/d/1MPTgWBkbLYYRfkAIcvqC7_JwsFr5VXYe/view?usp=drivesdk) |
| [B33](../../../../bibliografia/principal/README.md#b33) — Documento técnico | SANDIA NATIONAL LABORATORIES / PVPMC. Performance Ratio. [S. l.], [s.d.]. Disponível em: https://pvpmc.sandia.gov/modeling-guide/5-ac-system-output/pv-performance-metrics/performance-ratio/. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |

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
| G12_produtividades_PR — Produtividades e razão de desempenho | 4.2; 4.3 | [Claro](../../graficos/claro/G12_produtividades_PR.png) / [Escuro](../../graficos/escuro/G12_produtividades_PR.png) | [Claro](../../graficos/claro/G12_produtividades_PR.pdf) / [Escuro](../../graficos/escuro/G12_produtividades_PR.pdf) |
| G21_HSP_POA_pareada — Horas equivalentes de sol na janela pareada | 4.2 | [Claro](../../graficos/claro/G21_HSP_POA_pareada.png) / [Escuro](../../graficos/escuro/G21_HSP_POA_pareada.png) | [Claro](../../graficos/claro/G21_HSP_POA_pareada.pdf) / [Escuro](../../graficos/escuro/G21_HSP_POA_pareada.pdf) |

**G12_produtividades_PR:** Normalização por 893 kWp declarados. Yr, Ya e Yf estão na mesma janela pareada; Ya é modelada. Numericamente, kWh/kWp corresponde a horas equivalentes. PR observado não representa automaticamente todo o trimestre. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R12; R30.

**G21_HSP_POA_pareada:** HSP/PSH=H_POA/(1 kW/m²), correspondente a Yr na janela. Não é duração medida de brilho solar nem HSP integral do dia. A cobertura diária está no CSV. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R12; R30.

## Tabelas e quadros

| Tabela CSV | Subseções |
| --- | --- |
| [energia_e_HSP_diurna_pareada](../../../../outputs/tabelas/csv/energia_e_HSP_diurna_pareada.csv) | 1.3; 4.2 |
| [energia_e_indicadores_mensais](../../../../outputs/tabelas/csv/energia_e_indicadores_mensais.csv) | 3.6; 4.2; 4.3 |
| [yields](../../../../outputs/tabelas/csv/yields.csv) | 4.2; 4.3 |

[Tabelas originais em Word](../../../../outputs/tabelas/docx/Tabelas_do_Projeto.docx) · [Quadros originais em Word](../../../../outputs/quadros/docx/Quadros_do_Projeto.docx)

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Word completo dos gráficos](../../../../outputs/graficos/docx/Graficos_do_Projeto.docx) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)
