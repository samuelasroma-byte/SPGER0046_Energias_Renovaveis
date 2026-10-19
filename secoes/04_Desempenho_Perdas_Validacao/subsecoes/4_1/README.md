# 4.1 Balanço energético e cadeia de perdas

Responsável: **Júlia Ribeiro**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Perdas ópticas, térmicas e elétricas em CC, no inversor e em CA; indisponibilidade operacional em sistemas monitorados. (Julia)

## Entradas, método e resultado esperado

**Entradas:** Estágios do modelo e alertas de potência sob irradiância elevada.

Integre a cadeia óptica, térmica, elétrica DC, conversão e limite AC. A diferença entre estágios pertence ao modelo; um desvio do medidor pode envolver fenômenos e incertezas não identificados.

$$\Delta E_j=E_j-E_{j+1},\qquad \sum_j\Delta E_j=E_1-E_{\mathrm{final}}.$$

**Saídas:** Energia por estágio e alertas operacionais.

**Evidência:** Decomposição calculada. **Limitação:** Não se identificam perdas ópticas/operacionais reais isoladas sem medições adicionais; ganhos sob frio podem ocorrer.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B08](../../../../bibliografia/principal/README.md#b08) — Artigo | DE SOTO, W.; KLEIN, S. A.; BECKMAN, W. A. Improvement and validation of a model for photovoltaic array performance. Solar Energy, [S. l.], v. 80, n. 1, p. 78-88, 2006. DOI: https://doi.org/10.1016/j.solener.2005.06.010. Disponível em: https://doi.org/10.1016/j.solener.2005.06.010. Acesso em: 16 out. 2026. | [A076 — PDF](https://drive.google.com/file/d/14zVR8JRkL9ixP6pmdyhsCWg58ymL3M6v/view?usp=drivesdk) |
| [B17](../../../../bibliografia/principal/README.md#b17) — Artigo | JORDAN, D. C.; KURTZ, S. R. Photovoltaic Degradation Rates—an Analytical Review. Progress in Photovoltaics: Research and Applications, [S. l.], v. 21, n. 1, p. 12-29, 2013. DOI: https://doi.org/10.1002/pip.1182. Disponível em: https://doi.org/10.1002/pip.1182. Acesso em: 16 out. 2026. | [A079 — PDF](https://drive.google.com/file/d/1l516rsEeUdlDEVSNYoThD0_WJeQbd22_/view?usp=drivesdk) |
| [B20](../../../../bibliografia/principal/README.md#b20) — Livro | LUQUE, A.; HEGEDUS, S. (ed.). Handbook of Photovoltaic Science and Engineering. 2. ed. [S. l.]: Wiley, 2011. DOI: https://doi.org/10.1002/9780470974704. Disponível em: https://doi.org/10.1002/9780470974704. Acesso em: 16 out. 2026. | [A034 — outra edição](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) |
| [B21](../../../../bibliografia/principal/README.md#b21) — Artigo | MANI, M.; PILLAI, R. Impact of dust on solar photovoltaic (PV) performance: Research status, challenges and recommendations. Renewable and Sustainable Energy Reviews, [S. l.], v. 14, n. 9, p. 3124-3131, 2010. DOI: https://doi.org/10.1016/j.rser.2010.07.065. Disponível em: https://doi.org/10.1016/j.rser.2010.07.065. Acesso em: 16 out. 2026. | [A081 — PDF](https://drive.google.com/file/d/1DDy6MPhAxwJqT25dWSO_LaSSCIM9Hbrc/view?usp=drivesdk) |
| [B22](../../../../bibliografia/principal/README.md#b22) — Trabalho em evento | MARION, B. et al. Performance parameters for grid-connected PV systems. In: IEEE PHOTOVOLTAIC SPECIALISTS CONFERENCE, 31., 2005, [S. l.]. Conference Record of the Thirty-first IEEE Photovoltaic Specialists Conference, 2005. [S. l.]: IEEE, 2005. p. 1601-1606. DOI: https://doi.org/10.1109/pvsc.2005.1488451. Disponível em: https://doi.org/10.1109/pvsc.2005.1488451. Acesso em: 16 out. 2026. | [A066 — PDF](https://drive.google.com/file/d/1MPTgWBkbLYYRfkAIcvqC7_JwsFr5VXYe/view?usp=drivesdk) |
| [B26](../../../../bibliografia/principal/README.md#b26) — Documento técnico | PV ANALYTICS WEBINAR. Solar Data Tools demo — Farm Solar Array. [S. l.], 2024. Disponível em: https://pv-tutorials.github.io/2024_Analytics_Webinar/solar-data-tools-demo.html. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A034 | [Abrir Handbook of Photovoltaic Science and Engineering](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) | 1ª edição. Apoio alternativo a B20; não satisfaz a edição de 2011 indicada. |
| A066 | [Abrir Performance Parameters for Grid-Connected PV Systems — NREL/CP-520-37358](https://drive.google.com/file/d/1MPTgWBkbLYYRfkAIcvqC7_JwsFr5VXYe/view?usp=drivesdk) | Versão de relatório/manuscrito do trabalho em evento; essa versão física deve ser indicada ao citar páginas. |
| A076 | [Abrir Improvement and validation of a model for photovoltaic array performance](https://drive.google.com/file/d/14zVR8JRkL9ixP6pmdyhsCWg58ymL3M6v/view?usp=drivesdk) | Versão publicada; páginas 78–88. |
| A079 | [Abrir Photovoltaic degradation rates: an analytical review](https://drive.google.com/file/d/1l516rsEeUdlDEVSNYoThD0_WJeQbd22_/view?usp=drivesdk) | Nome recebido indica 2011 (publicação online); adotado 2013, ano do volume 21, páginas 12–29. |
| A081 | [Abrir Impact of dust on solar photovoltaic (PV) performance: research status, challenges and recommendations](https://drive.google.com/file/d/1DDy6MPhAxwJqT25dWSO_LaSSCIM9Hbrc/view?usp=drivesdk) | Versão publicada; páginas 3124–3131. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Ilustrações de inserção exclusiva

Cada ID tem um único local de inserção no capítulo. As versões claro/escuro e PNG/PDF são alternativas do mesmo item; escolher apenas uma para a redação. Ao discutir um item de outra seção, fazer referência ao ID já inserido, sem reproduzi-lo.

| ID e título | Inserir em | PNG claro e escuro | PDF claro e escuro |
| --- | --- | --- | --- |
| G11_cadeia_energetica — Cadeia de energia calculada | 4.1 | [Claro](../../graficos/claro/G11_cadeia_energetica.png) / [Escuro](../../graficos/escuro/G11_cadeia_energetica.png) | [Claro](../../graficos/claro/G11_cadeia_energetica.pdf) / [Escuro](../../graficos/escuro/G11_cadeia_energetica.pdf) |

**G11_cadeia_energetica:** Estágios integrados na mesma janela. Diferenças são decomposição do modelo, não identificação independente das perdas reais. Ganhos relativos sob frio não são forçados a perdas positivas. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R08; R11; R12.

## Tabelas e quadros de inserção exclusiva

| ID | Tabela ou quadro | Inserir em |
| --- | --- | --- |
| T11 | Energia por estágio do modelo | 4.1 |

[Baixar o Word com os materiais tabulares desta seção](../../tabelas/docx/Materiais_Tabulares_Secao_04.docx).

| Dados e tabelas em CSV | Inserir em |
| --- | --- |
| [energy_stages](../../../../outputs/tabelas/csv/energy_stages.csv) | 4.1 |
| [operational_flags](../../../../outputs/tabelas/csv/operational_flags.csv) | 4.1 |

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)

## Inventário de equações

[Quadro de equações da seção](../../equacoes/Quadro_Equacoes_Secao_04.docx): 2 relações do núcleo e 1 de apoio nesta subseção. IDs: E4.01, E4.02, E4.03.
