# 3.3 Modelagem elétrica do módulo fotovoltaico

Responsável: **Gabriela e Giulia**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Curvas corrente–tensão (I–V) e potência–tensão (P–V), ponto de máxima potência (maximum power point — MPP) e resposta do módulo à irradiância e à temperatura.

## Entradas, método e resultado esperado

**Entradas:** Parâmetros CEC, irradiância efetiva e temperatura estimada.

O modelo de diodo único fornece curvas I–V, P–V e o ponto de máxima potência. Compare irradiâncias a 25 °C e temperaturas a 1.000 W/m². Registre divergências de classificação e parâmetros entre CEC e metadados.

$$I=I_L-I_0[\exp((V+IR_s)/a)-1]-(V+IR_s)/R_{sh},\quad P=VI.$$

**Saídas:** Curvas calculadas e identificação de MPP.

**Evidência:** Modelo elétrico e curvas calculadas. **Limitação:** Sem varreduras I–V experimentais da instalação; as curvas não constituem validação do módulo.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B08](../../../../bibliografia/principal/README.md#b08) — Artigo | DE SOTO, W.; KLEIN, S. A.; BECKMAN, W. A. Improvement and validation of a model for photovoltaic array performance. Solar Energy, [S. l.], v. 80, n. 1, p. 78-88, 2006. DOI: https://doi.org/10.1016/j.solener.2005.06.010. Disponível em: https://doi.org/10.1016/j.solener.2005.06.010. Acesso em: 16 out. 2026. | [A076 — PDF](https://drive.google.com/file/d/14zVR8JRkL9ixP6pmdyhsCWg58ymL3M6v/view?usp=drivesdk) |
| [B12](../../../../bibliografia/principal/README.md#b12) — Livro | DUFFIE, J. A.; BECKMAN, W. A.; BLAIR, N. Solar Engineering of Thermal Processes, Photovoltaics and Wind. [S. l.]: Wiley, 2020. DOI: https://doi.org/10.1002/9781119540328. Disponível em: https://doi.org/10.1002/9781119540328. Acesso em: 16 out. 2026. | [A001 — PDF](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) |
| [B14](../../../../bibliografia/principal/README.md#b14) — Artigo | HOLMGREN, W. F.; HANSEN, C. W.; MIKOFSKI, M. A. pvlib python: a python package for modeling solar energy systems. Journal of Open Source Software, [S. l.], v. 3, n. 29, art. 884, 2018. DOI: https://doi.org/10.21105/joss.00884. Disponível em: https://doi.org/10.21105/joss.00884. Acesso em: 16 out. 2026. | [A018 — PDF](https://drive.google.com/file/d/1FBMDvA4xpAW7-8zq2Tre5AGUt_kr56TL/view?usp=drivesdk) |
| [B20](../../../../bibliografia/principal/README.md#b20) — Livro | LUQUE, A.; HEGEDUS, S. (ed.). Handbook of Photovoltaic Science and Engineering. 2. ed. [S. l.]: Wiley, 2011. DOI: https://doi.org/10.1002/9780470974704. Disponível em: https://doi.org/10.1002/9780470974704. Acesso em: 16 out. 2026. | [A034 — outra edição](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) |
| [B28](../../../../bibliografia/principal/README.md#b28) — Documento técnico | PVLIB CONTRIBUTORS. calcparams_cec and retrieve_sam — pvlib 0.16.1. [S. l.], 2026. Disponível em: https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.pvsystem.calcparams_cec.html. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |
| [B38](../../../../bibliografia/principal/README.md#b38) — Artigo | VILLALVA, M. G.; GAZOLI, J. R.; FILHO, E. R. Comprehensive Approach to Modeling and Simulation of Photovoltaic Arrays. IEEE Transactions on Power Electronics, [S. l.], v. 24, n. 5, p. 1198-1208, 2009. DOI: https://doi.org/10.1109/tpel.2009.2013862. Disponível em: https://doi.org/10.1109/tpel.2009.2013862. Acesso em: 16 out. 2026. | [A085 — PDF](https://drive.google.com/file/d/1Ct3ezT5aQQ0gVbWTB2zBDGn2VEg0hZ4b/view?usp=drivesdk) |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A001 | [Abrir Solar Engineering of Thermal Processes, Photovoltaics and Wind](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) | 5ª edição confirmada no PDF, com 919 páginas digitais e índice até a página impressa 905. Alternativa de trabalho adotada para B19, em conjunto com A003. Citar Duffie, Beckman e Blair (2020) ao usar este arquivo. |
| A018 | [Abrir pvlib python: a python package for modeling solar energy systems](https://drive.google.com/file/d/1FBMDvA4xpAW7-8zq2Tre5AGUt_kr56TL/view?usp=drivesdk) |  |
| A034 | [Abrir Handbook of Photovoltaic Science and Engineering](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) | 1ª edição. Apoio alternativo a B20; não satisfaz a edição de 2011 indicada. |
| A076 | [Abrir Improvement and validation of a model for photovoltaic array performance](https://drive.google.com/file/d/14zVR8JRkL9ixP6pmdyhsCWg58ymL3M6v/view?usp=drivesdk) | Versão publicada; páginas 78–88. |
| A085 | [Abrir Comprehensive approach to modeling and simulation of photovoltaic arrays](https://drive.google.com/file/d/1Ct3ezT5aQQ0gVbWTB2zBDGn2VEg0hZ4b/view?usp=drivesdk) | Versão publicada; páginas 1198–1208. Sobrenome do terceiro autor corrigido para RUPPERT FILHO. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Ilustrações de inserção exclusiva

Cada ID tem um único local de inserção no capítulo. As versões claro/escuro e PNG/PDF são alternativas do mesmo item; escolher apenas uma para a redação. Ao discutir um item de outra seção, fazer referência ao ID já inserido, sem reproduzi-lo.

| ID e título | Inserir em | PNG claro e escuro | PDF claro e escuro |
| --- | --- | --- | --- |
| G05_curvas_irradiancia — Curvas elétricas para diferentes irradiâncias | 3.3 | [Claro](../../graficos/claro/G05_curvas_irradiancia.png) / [Escuro](../../graficos/escuro/G05_curvas_irradiancia.png) | [Claro](../../graficos/claro/G05_curvas_irradiancia.pdf) / [Escuro](../../graficos/escuro/G05_curvas_irradiancia.pdf) |
| G06_curvas_temperatura — Curvas elétricas para diferentes temperaturas | 3.3 | [Claro](../../graficos/claro/G06_curvas_temperatura.png) / [Escuro](../../graficos/escuro/G06_curvas_temperatura.png) | [Claro](../../graficos/claro/G06_curvas_temperatura.pdf) / [Escuro](../../graficos/escuro/G06_curvas_temperatura.pdf) |

**G05_curvas_irradiancia:** Temperatura fixa de 25 °C; modelo de diodo único com parâmetros CEC do módulo. Círculos indicam MPP. Curvas calculadas, não ensaios I–V da instalação. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R08; R10.

**G06_curvas_temperatura:** Irradiância fixa de 1.000 W/m²; modelo de diodo único com parâmetros CEC do módulo. Círculos indicam MPP. Curvas calculadas, não ensaios I–V da instalação. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R08; R10.

## Tabelas e quadros de inserção exclusiva

Não há tabela ou quadro Word atribuído a esta subseção.

Não há CSV de tabela atribuído a esta subseção.

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)

## Inventário de equações

[Quadro de equações da seção em PDF e Word](../../equacoes/README.md): 2 relações do núcleo e 1 de apoio nesta subseção. IDs: E3.04, E3.05, E3.06.
