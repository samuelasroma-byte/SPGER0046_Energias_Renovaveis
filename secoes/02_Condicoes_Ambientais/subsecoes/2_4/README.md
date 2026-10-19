# 2.4 Geometria de instalação e exposição do arranjo fotovoltaico

Responsável: **Vannessa e Thais**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Inclinação, azimute, espaçamento entre fileiras e exposição frontal e, quando aplicável, traseira dos módulos.

## Entradas, método e resultado esperado

**Entradas:** Inclinação de 25° e azimute de 180° documentados; fachadas hipotéticas.

A instalação define exposição e incidência. A inclinação é medida em relação à horizontal. Espaçamento entre fileiras e exposição traseira precisam de geometria adicional; em um exemplo de sombra coplanar, uma altura h gera projeção horizontal h/tan(altura solar).

$$\cos\theta_i=\cos\theta_z\cos\beta+\sin\theta_z\sin\beta\cos(\gamma_s-\gamma_a),\quad \ell=h/\tan\alpha_s.$$

**Saídas:** Convenções geométricas e limite de dados de espaçamento.

**Evidência:** Geometria documentada e extensão didática. **Limitação:** A expressão de projeção é um exemplo plano sem dimensão de fileira real; não calcula o sombreamento específico da usina.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B12](../../../../bibliografia/principal/README.md#b12) — Livro | DUFFIE, J. A.; BECKMAN, W. A.; BLAIR, N. Solar Engineering of Thermal Processes, Photovoltaics and Wind. [S. l.]: Wiley, 2020. DOI: https://doi.org/10.1002/9781119540328. Disponível em: https://doi.org/10.1002/9781119540328. Acesso em: 16 out. 2026. | [A001 — PDF](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) |
| [B14](../../../../bibliografia/principal/README.md#b14) — Artigo | HOLMGREN, W. F.; HANSEN, C. W.; MIKOFSKI, M. A. pvlib python: a python package for modeling solar energy systems. Journal of Open Source Software, [S. l.], v. 3, n. 29, art. 884, 2018. DOI: https://doi.org/10.21105/joss.00884. Disponível em: https://doi.org/10.21105/joss.00884. Acesso em: 16 out. 2026. | [A018 — PDF](https://drive.google.com/file/d/1FBMDvA4xpAW7-8zq2Tre5AGUt_kr56TL/view?usp=drivesdk) |
| [B15](../../../../bibliografia/principal/README.md#b15) — Artigo | JACOBSON, M. Z.; JADHAV, V. World estimates of PV optimal tilt angles and ratios of sunlight incident upon tilted and tracked PV panels relative to horizontal panels. Solar Energy, [S. l.], v. 169, p. 55-66, 2018. DOI: https://doi.org/10.1016/j.solener.2018.04.030. Disponível em: https://doi.org/10.1016/j.solener.2018.04.030. Acesso em: 16 out. 2026. | [A077 — PDF](https://drive.google.com/file/d/1zCaoOVTMtTmiJd0klVpiMZVWaqIaBdJl/view?usp=drivesdk) |
| [B19](../../../../bibliografia/principal/README.md#b19) — Livro | KALOGIROU, S. A. Solar Energy Engineering: Processes and Systems. 2. ed. [S. l.]: Elsevier, 2014. DOI: https://doi.org/10.1016/c2011-0-07038-2. Disponível em: https://doi.org/10.1016/c2011-0-07038-2. Acesso em: 16 out. 2026. | PDF não localizado |
| [B32](../../../../bibliografia/principal/README.md#b32) — Documento técnico | REDA, I.; ANDREAS, A. Solar Position Algorithm for Solar Radiation Applications — NREL/TP-560-34302. [S. l.], 2008. Disponível em: https://docs.nlr.gov/docs/fy08osti/34302.pdf. Acesso em: 16 out. 2026. | [A065 — PDF](https://drive.google.com/file/d/1uUE7A-W7yY-HZRcw0FFs3g0nF_Yh5i4F/view?usp=drivesdk) |
| [B34](../../../../bibliografia/principal/README.md#b34) — Documento técnico | SANDIA NATIONAL LABORATORIES / PVPMC. Plane of Array (POA) Irradiance. [S. l.], [s.d.]. Disponível em: https://pvpmc.sandia.gov/modeling-guide/1-weather-design-inputs/plane-of-array-poa-irradiance/. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A001 | [Abrir Solar Engineering of Thermal Processes, Photovoltaics and Wind](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) | 5ª edição confirmada no PDF, com 919 páginas digitais e índice até a página impressa 905. Alternativa de trabalho adotada para B19, em conjunto com A003. Citar Duffie, Beckman e Blair (2020) ao usar este arquivo. |
| A018 | [Abrir pvlib python: a python package for modeling solar energy systems](https://drive.google.com/file/d/1FBMDvA4xpAW7-8zq2Tre5AGUt_kr56TL/view?usp=drivesdk) |  |
| A065 | [Abrir Solar Position Algorithm for Solar Radiation Applications — NREL/TP-560-34302](https://drive.google.com/file/d/1uUE7A-W7yY-HZRcw0FFs3g0nF_Yh5i4F/view?usp=drivesdk) | Relatório revisado em 2008; distinto do artigo de 2004, B31. |
| A077 | [Abrir World estimates of PV optimal tilt angles and ratios of sunlight incident upon tilted and tracked PV panels relative to horizontal panels](https://drive.google.com/file/d/1zCaoOVTMtTmiJd0klVpiMZVWaqIaBdJl/view?usp=drivesdk) | Versão publicada; páginas 55–66. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Ilustrações de inserção exclusiva

A coluna de subseção indica o local de cada material no capítulo. Claro/escuro e PNG/PDF são opções do mesmo item. Referências em outras seções usam o ID correspondente.

| ID e título | Inserir em | PNG claro e escuro | PDF claro e escuro |
| --- | --- | --- | --- |
| F01_plano_angulos — Plano do arranjo e convenções angulares | 2.4 | [Claro](../../figuras/claro/F01_plano_angulos.png) / [Escuro](../../figuras/escuro/F01_plano_angulos.png) | [Claro](../../figuras/claro/F01_plano_angulos.pdf) / [Escuro](../../figuras/escuro/F01_plano_angulos.pdf) |

**F01_plano_angulos:** Corte coplanar didático: β=25° documentado; θz=55° e θi=30° são valores ilustrativos coerentes nesse corte. Abaixo, azimute medido a partir do norte no sentido horário; arranjo orientado ao sul. Não é um levantamento tridimensional da usina. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R03; R09.

## Tabelas e quadros de inserção exclusiva

| ID | Tabela ou quadro | Inserir em |
| --- | --- | --- |
| Q04 | Ambiente e instalação | 2.4 |

[Baixar o Word com os materiais tabulares desta seção](../../tabelas/docx/Materiais_Tabulares_Secao_02.docx).

Não há CSV de tabela atribuído a esta subseção.

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)

## Inventário de equações

[Quadro de equações da seção em PDF e Word](../../equacoes/README.md): 2 relações do núcleo e 0 de apoio nesta subseção. IDs: E2.06, E2.07.
