# 2.2 Albedo e ambiente radiativo da superfície

Responsável: **Vannessa e Thais**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Refletância do solo e contribuição da irradiância refletida, inclusive em aplicações bifaciais.

## Entradas, método e resultado esperado

**Entradas:** Albedo assumido e componentes estimadas da inversão.

O albedo expressa refletância do entorno. No exercício de transposição, varia-se 0,10/0,20/0,40 mantendo as componentes reconstruídas na referência 0,20. O arranjo real é monofacial; bifacialidade exige caracterização traseira adicional.

$$G_{\mathrm{solo}}=\rho_g\,GHI\,\frac{1-\cos\beta}{2}.$$

**Saídas:** Sensibilidade de albedo e quadro de hipóteses.

**Evidência:** Cenário de sensibilidade. **Limitação:** Expressão isotrópica para reflexão do solo. Não há albedo medido; a leitura POA principal não recebe uma segunda contribuição refletida.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B03](../../../../bibliografia/principal/README.md#b03) — Artigo | ANDREWS, R. W.; PEARCE, J. M. The effect of spectral albedo on amorphous silicon and crystalline silicon solar photovoltaic device performance. Solar Energy, [S. l.], v. 91, p. 233-241, 2013. DOI: https://doi.org/10.1016/j.solener.2013.01.030. Disponível em: https://doi.org/10.1016/j.solener.2013.01.030. Acesso em: 16 out. 2026. | [A072 — PDF](https://drive.google.com/file/d/1NkS35bxY9Yolo1t7sIg9dYe3CXvtTieM/view?usp=drivesdk) |
| [B11](../../../../bibliografia/principal/README.md#b11) — Artigo | DRIESSE, A.; JENSEN, A. R.; PEREZ, R. A continuous form of the Perez diffuse sky model for forward and reverse transposition. Solar Energy, [S. l.], v. 267, art. 112093, 2024. DOI: https://doi.org/10.1016/j.solener.2023.112093. Disponível em: https://doi.org/10.1016/j.solener.2023.112093. Acesso em: 16 out. 2026. | [A089 — PDF](https://drive.google.com/file/d/1woLwuNHB_hbHuY0GPOKyq_KvZ_heXRtb/view?usp=drivesdk) |
| [B12](../../../../bibliografia/principal/README.md#b12) — Livro | DUFFIE, J. A.; BECKMAN, W. A.; BLAIR, N. Solar Engineering of Thermal Processes, Photovoltaics and Wind. [S. l.]: Wiley, 2020. DOI: https://doi.org/10.1002/9781119540328. Disponível em: https://doi.org/10.1002/9781119540328. Acesso em: 16 out. 2026. | [A001 — PDF](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) |
| [B19](../../../../bibliografia/principal/README.md#b19) — Livro | KALOGIROU, S. A. Solar Energy Engineering: Processes and Systems. 2. ed. [S. l.]: Elsevier, 2014. DOI: https://doi.org/10.1016/c2011-0-07038-2. Disponível em: https://doi.org/10.1016/c2011-0-07038-2. Acesso em: 16 out. 2026. | PDF não localizado |
| [B25](../../../../bibliografia/principal/README.md#b25) — Artigo | PEREZ, R. et al. Modeling daylight availability and irradiance components from direct and global irradiance. Solar Energy, [S. l.], v. 44, n. 5, p. 271-289, 1990. DOI: https://doi.org/10.1016/0038-092x(90)90055-h. Disponível em: https://doi.org/10.1016/0038-092x(90)90055-h. Acesso em: 16 out. 2026. | [A083 — PDF](https://drive.google.com/file/d/1xd-WUiyIaAO8bse1xZNRd8zi7z48McF_/view?usp=drivesdk) |
| [B34](../../../../bibliografia/principal/README.md#b34) — Documento técnico | SANDIA NATIONAL LABORATORIES / PVPMC. Plane of Array (POA) Irradiance. [S. l.], [s.d.]. Disponível em: https://pvpmc.sandia.gov/modeling-guide/1-weather-design-inputs/plane-of-array-poa-irradiance/. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A001 | [Abrir Solar Engineering of Thermal Processes, Photovoltaics and Wind](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) | 5ª edição confirmada no PDF, com 919 páginas digitais e índice até a página impressa 905. Alternativa de trabalho adotada para B19, em conjunto com A003. Citar Duffie, Beckman e Blair (2020) ao usar este arquivo. |
| A072 | [Abrir The effect of spectral albedo on amorphous silicon and crystalline silicon solar photovoltaic device performance](https://drive.google.com/file/d/1NkS35bxY9Yolo1t7sIg9dYe3CXvtTieM/view?usp=drivesdk) | Manuscrito de autor completo; título, autoria, DOI e 9 páginas conferidos. |
| A083 | [Abrir Modeling daylight availability and irradiance components from direct and global irradiance](https://drive.google.com/file/d/1xd-WUiyIaAO8bse1xZNRd8zi7z48McF_/view?usp=drivesdk) | Versão publicada; páginas 271–289. |
| A089 | [Abrir A continuous form of the Perez diffuse sky model for forward and reverse transposition](https://drive.google.com/file/d/1woLwuNHB_hbHuY0GPOKyq_KvZ_heXRtb/view?usp=drivesdk) | Versão final da editora, completa, com 12 páginas e licença CC BY 4.0. Volume 267 (2024), artigo 112093; publicação online antecipada em 2/12/2023. Original recebido preservado. Cópias de consulta nas quatro seções. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Ilustrações de inserção exclusiva

Cada ID tem um único local de inserção no capítulo. As versões claro/escuro e PNG/PDF são alternativas do mesmo item; escolher apenas uma para a redação. Ao discutir um item de outra seção, fazer referência ao ID já inserido, sem reproduzi-lo.

| ID e título | Inserir em | PNG claro e escuro | PDF claro e escuro |
| --- | --- | --- | --- |
| G22_albedo — Sensibilidade ao albedo assumido | 2.2 | [Claro](../../graficos/claro/G22_albedo.png) / [Escuro](../../graficos/escuro/G22_albedo.png) | [Claro](../../graficos/claro/G22_albedo.pdf) / [Escuro](../../graficos/escuro/G22_albedo.pdf) |

**G22_albedo:** Transposição das mesmas componentes reconstruídas com albedo-base 0,20. A variação isola o parâmetro da transposição e não valida albedo. Apenas 1.037 horas elegíveis; não é trimestre integral. A POA medida da cadeia principal não recebe reflexão novamente. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R14; R15; R29.

## Tabelas e quadros de inserção exclusiva

| ID | Tabela ou quadro | Inserir em |
| --- | --- | --- |
| T14 | Albedo e geometrias com componentes estimadas | 2.2 |

[Baixar o Word com os materiais tabulares desta seção](../../tabelas/docx/Materiais_Tabulares_Secao_02.docx).

| Dados e tabelas em CSV | Inserir em |
| --- | --- |
| [environment_scenarios](../../../../outputs/tabelas/csv/environment_scenarios.csv) | 2.2 |

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)
