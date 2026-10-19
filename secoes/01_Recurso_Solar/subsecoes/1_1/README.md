# 1.1 Geometria solar e irradiância extraterrestre

Responsável: **Samuel**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Posição Sol–Terra, ângulos solares e referência física da radiação.

## Entradas, método e resultado esperado

**Entradas:** Latitude, longitude, altitude e horário dos intervalos.

Calcular a posição solar com SPA e a irradiância extraterrestre com Spencer. O azimute é contado a partir do norte no sentido horário.

$$\cos\theta_z=\sin\varphi\sin\delta+\cos\varphi\cos\delta\cos\omega,\qquad G_{0h}=G_{0n}\max(\cos\theta_z,0).$$

**Saídas:** Geometria solar e quadro de convenções.

**Evidência:** Cálculo físico com coordenadas documentadas. **Limitação:** Não há observação independente de ângulo solar; a geometria pode ser calculada.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B12](../../../../bibliografia/principal/README.md#b12) — Livro | DUFFIE, J. A.; BECKMAN, W. A.; BLAIR, N. Solar Engineering of Thermal Processes, Photovoltaics and Wind. [S. l.]: Wiley, 2020. DOI: https://doi.org/10.1002/9781119540328. Disponível em: https://doi.org/10.1002/9781119540328. Acesso em: 16 out. 2026. | [A001 — PDF](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) |
| [B19](../../../../bibliografia/principal/README.md#b19) — Livro | KALOGIROU, S. A. Solar Energy Engineering: Processes and Systems. 2. ed. [S. l.]: Elsevier, 2014. DOI: https://doi.org/10.1016/c2011-0-07038-2. Disponível em: https://doi.org/10.1016/c2011-0-07038-2. Acesso em: 16 out. 2026. | PDF não localizado |
| [B23](../../../../bibliografia/principal/README.md#b23) — Documento técnico | NOAA GLOBAL MONITORING LABORATORY. General Solar Position Calculations. [S. l.], [s.d.]. Disponível em: https://gml.noaa.gov/grad/solcalc/solareqns.PDF. Acesso em: 16 out. 2026. | [A082 — PDF](https://drive.google.com/file/d/1L8p-uBexCRZ1N9b-JCVqyiaygdKQH7Ot/view?usp=drivesdk) |
| [B29](../../../../bibliografia/principal/README.md#b29) — Documento técnico | PVLIB CONTRIBUTORS. get_extra_radiation — Spencer method; pvlib 0.16.1. [S. l.], 2026. Disponível em: https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.irradiance.get_extra_radiation.html. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |
| [B31](../../../../bibliografia/principal/README.md#b31) — Artigo | REDA, I.; ANDREAS, A. Solar position algorithm for solar radiation applications. Solar Energy, [S. l.], v. 76, n. 5, p. 577-589, 2004. DOI: https://doi.org/10.1016/j.solener.2003.12.003. Disponível em: https://doi.org/10.1016/j.solener.2003.12.003. Acesso em: 16 out. 2026. | [A084 — PDF](https://drive.google.com/file/d/1Al8R_ZriNBDixLTfsBcDVRxxAm38sPto/view?usp=drivesdk) |
| [B32](../../../../bibliografia/principal/README.md#b32) — Documento técnico | REDA, I.; ANDREAS, A. Solar Position Algorithm for Solar Radiation Applications — NREL/TP-560-34302. [S. l.], 2008. Disponível em: https://docs.nlr.gov/docs/fy08osti/34302.pdf. Acesso em: 16 out. 2026. | [A065 — PDF](https://drive.google.com/file/d/1uUE7A-W7yY-HZRcw0FFs3g0nF_Yh5i4F/view?usp=drivesdk) |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A001 | [Abrir Solar Engineering of Thermal Processes, Photovoltaics and Wind](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) | 5ª edição confirmada no PDF, com 919 páginas digitais e índice até a página impressa 905. Alternativa de trabalho adotada para B19, em conjunto com A003. Citar Duffie, Beckman e Blair (2020) ao usar este arquivo. |
| A065 | [Abrir Solar Position Algorithm for Solar Radiation Applications — NREL/TP-560-34302](https://drive.google.com/file/d/1uUE7A-W7yY-HZRcw0FFs3g0nF_Yh5i4F/view?usp=drivesdk) | Relatório revisado em 2008; distinto do artigo de 2004, B31. |
| A082 | [Abrir General Solar Position Calculations](https://drive.google.com/file/d/1L8p-uBexCRZ1N9b-JCVqyiaygdKQH7Ot/view?usp=drivesdk) | Documento técnico completo de 2 páginas; sem data e sem DOI identificado. Não é norma. |
| A084 | [Abrir Solar position algorithm for solar radiation applications](https://drive.google.com/file/d/1Al8R_ZriNBDixLTfsBcDVRxxAm38sPto/view?usp=drivesdk) | Artigo de 2004, páginas 577–589; distinto do relatório revisado em 2008 já presente como A065/B32. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Figuras, gráficos e fluxograma

| Identificador e título | Subseções | PNG claro / escuro | PDF claro / escuro |
| --- | --- | --- | --- |
| G01_recurso_geometria — Recurso solar medido e geometria calculada | 1.1; 1.2 | [Claro](../../graficos/claro/G01_recurso_geometria.png) / [Escuro](../../graficos/escuro/G01_recurso_geometria.png) | [Claro](../../graficos/claro/G01_recurso_geometria.pdf) / [Escuro](../../graficos/escuro/G01_recurso_geometria.pdf) |
| F01_plano_angulos — Plano do arranjo e convenções angulares | 1.1; 2.4; 3.1 | [Claro](../../figuras/claro/F01_plano_angulos.png) / [Escuro](../../figuras/escuro/F01_plano_angulos.png) | [Claro](../../figuras/claro/F01_plano_angulos.pdf) / [Escuro](../../figuras/escuro/F01_plano_angulos.pdf) |

**G01_recurso_geometria:** Dia 2024-05-17, selecionado pela menor variação relativa da POA entre dias com cobertura ≥99%. Ângulos calculados no meio dos intervalos; POA medida. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R01; R03; R05.

**F01_plano_angulos:** Corte coplanar didático: β=25° documentado; θz=55° e θi=30° são valores ilustrativos coerentes nesse corte. Abaixo, azimute medido a partir do norte no sentido horário; arranjo orientado ao sul. Não é um levantamento tridimensional da usina. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R03; R09.

## Tabelas e quadros

| Tabela CSV | Subseções |
| --- | --- |
| [criterio_dias_ilustrativos](../../../../outputs/tabelas/csv/criterio_dias_ilustrativos.csv) | 1.1; 1.3 |

[Tabelas originais em Word](../../../../outputs/tabelas/docx/Tabelas_do_Projeto.docx) · [Quadros originais em Word](../../../../outputs/quadros/docx/Quadros_do_Projeto.docx)

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Word completo dos gráficos](../../../../outputs/graficos/docx/Graficos_do_Projeto.docx) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)
