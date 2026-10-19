# 3.4 Modelagem do arranjo fotovoltaico em corrente contínua (CC)

Responsável: **Gabriela e Giulia**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Associação dos módulos em série e em paralelo e determinação da tensão, da corrente e da potência do arranjo.

## Entradas, método e resultado esperado

**Entradas:** MPP do módulo, 2.880 módulos, 24 grupos/inversores e perdas DC assumidas.

Em uma associação ideal, as tensões somam em série e as correntes em paralelo. O exemplo 20 módulos × 6 strings por grupo corresponde a 120 módulos, mas não confirma o cabeamento real ou a ligação aos MPPTs.

$$V_a=N_sV_m,\quad I_a=N_pI_m,\quad P_a=N_sN_pP_m,\quad P_{\mathrm{DC}}=P_a\prod_j(1-\ell_j).$$

**Saídas:** Tensão, corrente e potência do equivalente em CSV.

**Evidência:** Modelo agregado e equivalente didático. **Limitação:** Strings/MPPTs reais incompletos; V×I disponível não foi adotado como potência DC observada certificada.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B04](../../../../bibliografia/principal/README.md#b04) — Artigo | BISHOP, J. W. Computer simulation of the effects of electrical mismatches in photovoltaic cell interconnection circuits. Solar Cells, [S. l.], v. 25, n. 1, p. 73-89, 1988. DOI: https://doi.org/10.1016/0379-6787(88)90059-2. Disponível em: https://doi.org/10.1016/0379-6787(88)90059-2. Acesso em: 16 out. 2026. | [A073 — PDF](https://drive.google.com/file/d/1naylazsLo6-XnxIAo2WGf7BB22ATIava/view?usp=drivesdk) |
| [B08](../../../../bibliografia/principal/README.md#b08) — Artigo | DE SOTO, W.; KLEIN, S. A.; BECKMAN, W. A. Improvement and validation of a model for photovoltaic array performance. Solar Energy, [S. l.], v. 80, n. 1, p. 78-88, 2006. DOI: https://doi.org/10.1016/j.solener.2005.06.010. Disponível em: https://doi.org/10.1016/j.solener.2005.06.010. Acesso em: 16 out. 2026. | [A076 — PDF](https://drive.google.com/file/d/14zVR8JRkL9ixP6pmdyhsCWg58ymL3M6v/view?usp=drivesdk) |
| [B12](../../../../bibliografia/principal/README.md#b12) — Livro | DUFFIE, J. A.; BECKMAN, W. A.; BLAIR, N. Solar Engineering of Thermal Processes, Photovoltaics and Wind. [S. l.]: Wiley, 2020. DOI: https://doi.org/10.1002/9781119540328. Disponível em: https://doi.org/10.1002/9781119540328. Acesso em: 16 out. 2026. | [A001 — PDF](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) |
| [B20](../../../../bibliografia/principal/README.md#b20) — Livro | LUQUE, A.; HEGEDUS, S. (ed.). Handbook of Photovoltaic Science and Engineering. 2. ed. [S. l.]: Wiley, 2011. DOI: https://doi.org/10.1002/9780470974704. Disponível em: https://doi.org/10.1002/9780470974704. Acesso em: 16 out. 2026. | [A034 — outra edição](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) |
| [B28](../../../../bibliografia/principal/README.md#b28) — Documento técnico | PVLIB CONTRIBUTORS. calcparams_cec and retrieve_sam — pvlib 0.16.1. [S. l.], 2026. Disponível em: https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.pvsystem.calcparams_cec.html. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |
| [B38](../../../../bibliografia/principal/README.md#b38) — Artigo | VILLALVA, M. G.; GAZOLI, J. R.; FILHO, E. R. Comprehensive Approach to Modeling and Simulation of Photovoltaic Arrays. IEEE Transactions on Power Electronics, [S. l.], v. 24, n. 5, p. 1198-1208, 2009. DOI: https://doi.org/10.1109/tpel.2009.2013862. Disponível em: https://doi.org/10.1109/tpel.2009.2013862. Acesso em: 16 out. 2026. | [A085 — PDF](https://drive.google.com/file/d/1Ct3ezT5aQQ0gVbWTB2zBDGn2VEg0hZ4b/view?usp=drivesdk) |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A001 | [Abrir Solar Engineering of Thermal Processes, Photovoltaics and Wind](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) | 5ª edição confirmada no PDF, com 919 páginas digitais e índice até a página impressa 905. Alternativa de trabalho adotada para B19, em conjunto com A003. Citar Duffie, Beckman e Blair (2020) ao usar este arquivo. |
| A034 | [Abrir Handbook of Photovoltaic Science and Engineering](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) | 1ª edição. Apoio alternativo a B20; não satisfaz a edição de 2011 indicada. |
| A073 | [Abrir Computer simulation of the effects of electrical mismatches in photovoltaic cell interconnection circuits](https://drive.google.com/file/d/1naylazsLo6-XnxIAo2WGf7BB22ATIava/view?usp=drivesdk) | Artigo completo; páginas 73–89. |
| A076 | [Abrir Improvement and validation of a model for photovoltaic array performance](https://drive.google.com/file/d/14zVR8JRkL9ixP6pmdyhsCWg58ymL3M6v/view?usp=drivesdk) | Versão publicada; páginas 78–88. |
| A085 | [Abrir Comprehensive approach to modeling and simulation of photovoltaic arrays](https://drive.google.com/file/d/1Ct3ezT5aQQ0gVbWTB2zBDGn2VEg0hZ4b/view?usp=drivesdk) | Versão publicada; páginas 1198–1208. Sobrenome do terceiro autor corrigido para RUPPERT FILHO. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Ilustrações de inserção exclusiva

Cada ID tem um único local de inserção no capítulo. As versões claro/escuro e PNG/PDF são alternativas do mesmo item; escolher apenas uma para a redação. Ao discutir um item de outra seção, fazer referência ao ID já inserido, sem reproduzi-lo.

| ID e título | Inserir em | PNG claro e escuro | PDF claro e escuro |
| --- | --- | --- | --- |
| F03_arranjo_eletrico — Organização elétrica do sistema de referência | 3.4 | [Claro](../../figuras/claro/F03_arranjo_eletrico.png) / [Escuro](../../figuras/escuro/F03_arranjo_eletrico.png) | [Claro](../../figuras/claro/F03_arranjo_eletrico.pdf) / [Escuro](../../figuras/escuro/F03_arranjo_eletrico.pdf) |

**F03_arranjo_eletrico:** Número de módulos, inversores e módulos por grupo documentados. Associação 20 em série por 6 strings é um equivalente didático de 120 módulos, não confirmação da fiação/MPPT real. Tensões e correntes desse equivalente são calculadas em CSV. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R01; R10; R13.

## Tabelas e quadros de inserção exclusiva

Não há tabela ou quadro Word atribuído a esta subseção.

| Dados e tabelas em CSV | Inserir em |
| --- | --- |
| [arranjo_equivalente_diurno](../../../../outputs/tabelas/csv/arranjo_equivalente_diurno.csv) | 3.4 |

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)

## Inventário de equações

[Quadro de equações da seção](../../equacoes/Quadro_Equacoes_Secao_03.docx): 4 relações do núcleo e 0 de apoio nesta subseção. IDs: E3.07, E3.08, E3.09, E3.10.
