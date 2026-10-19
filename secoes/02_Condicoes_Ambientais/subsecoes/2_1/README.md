# 2.1 Condições térmicas

Responsável: **Vannessa e Thais**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Temperatura ambiente, vento, trocas de calor e temperatura operacional do módulo.

## Entradas, método e resultado esperado

**Entradas:** Temperatura do ar e vento locais; POA medida.

Temperatura ambiente, vento e trocas de calor condicionam a operação do módulo. As distribuições observadas e o cenário de menor ventilação ilustram a passagem do ambiente à modelagem térmica da seção 3.2.

$$T_{\mathrm{op}}=T_a+\frac{G_{\mathrm{ef}}}{U_0+U_1v}.$$

**Saídas:** Estatística ambiental e sensibilidade de ventilação.

**Evidência:** Medições ambientais e temperatura estimada. **Limitação:** U₀ e U₁ genéricos; T operacional é aproximação de célula, sem validação térmica independente.

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

## Ilustrações de inserção exclusiva

Cada ID tem um único local de inserção no capítulo. As versões claro/escuro e PNG/PDF são alternativas do mesmo item; escolher apenas uma para a redação. Ao discutir um item de outra seção, fazer referência ao ID já inserido, sem reproduzi-lo.

| ID e título | Inserir em | PNG claro e escuro | PDF claro e escuro |
| --- | --- | --- | --- |
| G03_condicoes_ambientais — Distribuições das condições ambientais | 2.1 | [Claro](../../graficos/claro/G03_condicoes_ambientais.png) / [Escuro](../../graficos/escuro/G03_condicoes_ambientais.png) | [Claro](../../graficos/claro/G03_condicoes_ambientais.pdf) / [Escuro](../../graficos/escuro/G03_condicoes_ambientais.pdf) |

**G03_condicoes_ambientais:** Temperatura do ar e vento medidos; mesma janela diurna pareada da avaliação elétrica. Sem interpolação. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R01; R07.

## Tabelas e quadros de inserção exclusiva

| ID | Tabela ou quadro | Inserir em |
| --- | --- | --- |
| T01 | Estatística descritiva de posição e dispersão | 2.1 |
| T02 | Extremos e quartis dos mesmos pares | 2.1 |

[Baixar o Word com os materiais tabulares desta seção](../../tabelas/docx/Materiais_Tabulares_Secao_02.docx).

| Dados e tabelas em CSV | Inserir em |
| --- | --- |
| [estatistica_descritiva](../../../../outputs/tabelas/csv/estatistica_descritiva.csv) | 2.1 |

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)

## Inventário de equações

[Quadro de equações da seção](../../equacoes/Quadro_Equacoes_Secao_02.docx): 0 relações do núcleo e 3 de apoio nesta subseção. IDs: E2.01, E2.02, E2.03.

Para o modelo térmico de Faiman, citar E3.03 em 3.2 sem repetir sua inserção.
