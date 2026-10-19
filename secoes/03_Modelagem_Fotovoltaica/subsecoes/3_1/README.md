# 3.1 Transposição para o plano do arranjo

Responsável: **Gabriela e Giulia**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Conversão de GHI, DNI e DHI em irradiância no plano do arranjo (plane of array — POA).

## Entradas, método e resultado esperado

**Entradas:** Componentes reconstruídas, posição solar e geometria.

A cadeia usual transpõe GHI/DNI/DHI para POA. Como a instalação já mede POA, o modelo principal começa dessa observação. A inversão opcional usa Driesse 2024, Erbs–Driesse e Perez–Driesse para exercícios de orientação/albedo.

$$G_{\mathrm{POA}}=DNI\max(\cos\theta_i,0)+G_{\mathrm{céu}}+G_{\mathrm{solo}}.$$

**Saídas:** Diagnóstico horário da inversão e critérios de exclusão.

**Evidência:** Medição direta e inversão exploratória. **Limitação:** Há possibilidade de soluções não únicas; o fechamento de POA é teste numérico, sem validação independente das componentes.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B11](../../../../bibliografia/principal/README.md#b11) — Artigo | DRIESSE, A.; JENSEN, A. R.; PEREZ, R. A continuous form of the Perez diffuse sky model for forward and reverse transposition. Solar Energy, [S. l.], v. 267, art. 112093, 2024. DOI: https://doi.org/10.1016/j.solener.2023.112093. Disponível em: https://doi.org/10.1016/j.solener.2023.112093. Acesso em: 16 out. 2026. | [A089 — PDF](https://drive.google.com/file/d/1woLwuNHB_hbHuY0GPOKyq_KvZ_heXRtb/view?usp=drivesdk) |
| [B12](../../../../bibliografia/principal/README.md#b12) — Livro | DUFFIE, J. A.; BECKMAN, W. A.; BLAIR, N. Solar Engineering of Thermal Processes, Photovoltaics and Wind. [S. l.]: Wiley, 2020. DOI: https://doi.org/10.1002/9781119540328. Disponível em: https://doi.org/10.1002/9781119540328. Acesso em: 16 out. 2026. | [A001 — PDF](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) |
| [B19](../../../../bibliografia/principal/README.md#b19) — Livro | KALOGIROU, S. A. Solar Energy Engineering: Processes and Systems. 2. ed. [S. l.]: Elsevier, 2014. DOI: https://doi.org/10.1016/c2011-0-07038-2. Disponível em: https://doi.org/10.1016/c2011-0-07038-2. Acesso em: 16 out. 2026. | PDF não localizado |
| [B25](../../../../bibliografia/principal/README.md#b25) — Artigo | PEREZ, R. et al. Modeling daylight availability and irradiance components from direct and global irradiance. Solar Energy, [S. l.], v. 44, n. 5, p. 271-289, 1990. DOI: https://doi.org/10.1016/0038-092x(90)90055-h. Disponível em: https://doi.org/10.1016/0038-092x(90)90055-h. Acesso em: 16 out. 2026. | [A083 — PDF](https://drive.google.com/file/d/1xd-WUiyIaAO8bse1xZNRd8zi7z48McF_/view?usp=drivesdk) |
| [B30](../../../../bibliografia/principal/README.md#b30) — Documento técnico | PVLIB CONTRIBUTORS. ghi_from_poa_driesse_2024 — pvlib 0.16.1. [S. l.], 2026. Disponível em: https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.irradiance.ghi_from_poa_driesse_2024.html. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |
| [B36](../../../../bibliografia/principal/README.md#b36) — Relatório técnico | SENGUPTA, M. et al. Best Practices Handbook for the Collection and Use of Solar Resource Data for Solar Energy Applications: Third Edition. [S. l.]: Office of Scientific and Technical Information (OSTI), 2021. DOI: https://doi.org/10.2172/1778700. Disponível em: https://doi.org/10.2172/1778700. Acesso em: 16 out. 2026. | [A088 — PDF](https://drive.google.com/file/d/1dty_mkSk-clgscx1BxxMdMcliI42ewjd/view?usp=drivesdk) |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A001 | [Abrir Solar Engineering of Thermal Processes, Photovoltaics and Wind](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) | 5ª edição confirmada no PDF, com 919 páginas digitais e índice até a página impressa 905. Alternativa de trabalho adotada para B19, em conjunto com A003. Citar Duffie, Beckman e Blair (2020) ao usar este arquivo. |
| A083 | [Abrir Modeling daylight availability and irradiance components from direct and global irradiance](https://drive.google.com/file/d/1xd-WUiyIaAO8bse1xZNRd8zi7z48McF_/view?usp=drivesdk) | Versão publicada; páginas 271–289. |
| A088 | [Abrir Best practices handbook for the collection and use of solar resource data for solar energy applications: third edition (formato IEA PVPS)](https://drive.google.com/file/d/1dty_mkSk-clgscx1BxxMdMcliI42ewjd/view?usp=drivesdk) | Terceira edição obtida no formato IEA-PVPS T16-04:2021, 331 páginas, ISBN 978-3-907281-19-2. A página oficial informa dois formatos da mesma edição (NREL e IEA PVPS). O DOI 10.2172/1778700 identifica o formato NREL, não este arquivo IEA PVPS. Citar o formato efetivamente consultado; a 4ª edição de 2024 A045 permanece disponível. |
| A089 | [Abrir A continuous form of the Perez diffuse sky model for forward and reverse transposition](https://drive.google.com/file/d/1woLwuNHB_hbHuY0GPOKyq_KvZ_heXRtb/view?usp=drivesdk) | Versão final da editora, completa, com 12 páginas e licença CC BY 4.0. Volume 267 (2024), artigo 112093; publicação online antecipada em 2/12/2023. Original recebido preservado. Cópias de consulta nas quatro seções. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Ilustrações de inserção exclusiva

Cada ID tem um único local de inserção no capítulo. As versões claro/escuro e PNG/PDF são alternativas do mesmo item; escolher apenas uma para a redação. Ao discutir um item de outra seção, fazer referência ao ID já inserido, sem reproduzi-lo.

| ID e título | Inserir em | PNG claro e escuro | PDF claro e escuro |
| --- | --- | --- | --- |
| G23_componentes_estimadas — Componentes reconstruídas da POA | 3.1 | [Claro](../../graficos/claro/G23_componentes_estimadas.png) / [Escuro](../../graficos/escuro/G23_componentes_estimadas.png) | [Claro](../../graficos/claro/G23_componentes_estimadas.pdf) / [Escuro](../../graficos/escuro/G23_componentes_estimadas.pdf) |

**G23_componentes_estimadas:** Exemplo de 2024-05-17, em horas elegíveis. Driesse 2024 e Erbs–Driesse; não são três sensores independentes. O fechamento pelo modelo não prova exatidão das componentes. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R14; R15; R16; R18.

## Tabelas e quadros de inserção exclusiva

Não há tabela ou quadro Word atribuído a esta subseção.

| Dados e tabelas em CSV | Inserir em |
| --- | --- |
| [componentes_estimadas_da_POA_horario](../../../../outputs/tabelas/csv/componentes_estimadas_da_POA_horario.csv) | 3.1 |

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)

## Inventário de equações

[Quadro de equações da seção](../../equacoes/Quadro_Equacoes_Secao_03.docx): 1 relações do núcleo e 1 de apoio nesta subseção. IDs: E3.01, E3.02.
