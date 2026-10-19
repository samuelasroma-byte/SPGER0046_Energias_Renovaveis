# 1.3 Modulação atmosférica e variabilidade espaço-temporal

Responsável: **Samuel**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Nuvens, aerossóis, vapor d’água e variações horárias, sazonais e espaciais.

## Entradas, método e resultado esperado

**Entradas:** Série de POA, intervalo de integração e critérios de cobertura.

Nuvens, aerossóis e vapor d’água modificam o recurso solar. A série permite descrever a variabilidade intradiária e entre dias; a seleção dos dias ilustrativos usa apenas POA e cobertura.

$$V_{\Delta G}=\frac{\operatorname{média}(|G_i-G_{i-1}|)}{\operatorname{média}(G_i)}.$$

**Saídas:** Critério dos dias ilustrativos e irradiação pareada.

**Evidência:** Descrição observacional de variabilidade. **Limitação:** Não se atribuem causas atmosféricas isoladas nem climatologia anual a um trimestre.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B12](../../../../bibliografia/principal/README.md#b12) — Livro | DUFFIE, J. A.; BECKMAN, W. A.; BLAIR, N. Solar Engineering of Thermal Processes, Photovoltaics and Wind. [S. l.]: Wiley, 2020. DOI: https://doi.org/10.1002/9781119540328. Disponível em: https://doi.org/10.1002/9781119540328. Acesso em: 16 out. 2026. | [A001 — PDF](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) |
| [B19](../../../../bibliografia/principal/README.md#b19) — Livro | KALOGIROU, S. A. Solar Energy Engineering: Processes and Systems. 2. ed. [S. l.]: Elsevier, 2014. DOI: https://doi.org/10.1016/c2011-0-07038-2. Disponível em: https://doi.org/10.1016/c2011-0-07038-2. Acesso em: 16 out. 2026. | PDF não localizado |
| [B24](../../../../bibliografia/principal/README.md#b24) — Documento técnico | OEDI / PVDAQ. PVDAQ public photovoltaic performance data — OEDI. [S. l.], [s.d.]. DOI: https://doi.org/10.25984/1846021. Disponível em: https://doi.org/10.25984/1846021. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |
| [B26](../../../../bibliografia/principal/README.md#b26) — Documento técnico | PV ANALYTICS WEBINAR. Solar Data Tools demo — Farm Solar Array. [S. l.], 2024. Disponível em: https://pv-tutorials.github.io/2024_Analytics_Webinar/solar-data-tools-demo.html. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |
| [B36](../../../../bibliografia/principal/README.md#b36) — Relatório técnico | SENGUPTA, M. et al. Best Practices Handbook for the Collection and Use of Solar Resource Data for Solar Energy Applications: Third Edition. [S. l.]: Office of Scientific and Technical Information (OSTI), 2021. DOI: https://doi.org/10.2172/1778700. Disponível em: https://doi.org/10.2172/1778700. Acesso em: 16 out. 2026. | [A088 — PDF](https://drive.google.com/file/d/1dty_mkSk-clgscx1BxxMdMcliI42ewjd/view?usp=drivesdk) |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A001 | [Abrir Solar Engineering of Thermal Processes, Photovoltaics and Wind](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) | 5ª edição confirmada no PDF, com 919 páginas digitais e índice até a página impressa 905. Alternativa de trabalho adotada para B19, em conjunto com A003. Citar Duffie, Beckman e Blair (2020) ao usar este arquivo. |
| A088 | [Abrir Best practices handbook for the collection and use of solar resource data for solar energy applications: third edition (formato IEA PVPS)](https://drive.google.com/file/d/1dty_mkSk-clgscx1BxxMdMcliI42ewjd/view?usp=drivesdk) | Terceira edição obtida no formato IEA-PVPS T16-04:2021, 331 páginas, ISBN 978-3-907281-19-2. A página oficial informa dois formatos da mesma edição (NREL e IEA PVPS). O DOI 10.2172/1778700 identifica o formato NREL, não este arquivo IEA PVPS. Citar o formato efetivamente consultado; a 4ª edição de 2024 A045 permanece disponível. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Ilustrações de inserção exclusiva

A coluna de subseção indica o local de cada material no capítulo. Claro/escuro e PNG/PDF são opções do mesmo item. Referências em outras seções usam o ID correspondente.

| ID e título | Inserir em | PNG claro e escuro | PDF claro e escuro |
| --- | --- | --- | --- |
| G02_variabilidade_recurso — Variabilidade diária do recurso solar | 1.3 | [Claro](../../graficos/claro/G02_variabilidade_recurso.png) / [Escuro](../../graficos/escuro/G02_variabilidade_recurso.png) | [Claro](../../graficos/claro/G02_variabilidade_recurso.pdf) / [Escuro](../../graficos/escuro/G02_variabilidade_recurso.pdf) |

**G02_variabilidade_recurso:** Integração somente nos intervalos diurnos pareados. Oscilações não identificam isoladamente nuvens, aerossóis ou vapor d’água. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R01; R12.

## Tabelas e quadros de inserção exclusiva

Não há tabela ou quadro Word atribuído a esta subseção.

| Dados e tabelas em CSV | Inserir em |
| --- | --- |
| [criterio_dias_ilustrativos](../../../../outputs/tabelas/csv/criterio_dias_ilustrativos.csv) | 1.3 |

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)

## Inventário de equações

[Quadro de equações da seção em PDF e Word](../../equacoes/README.md): 1 relações do núcleo e 0 de apoio nesta subseção. IDs: E1.05.
