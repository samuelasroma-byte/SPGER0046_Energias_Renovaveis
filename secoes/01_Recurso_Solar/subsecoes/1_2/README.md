# 1.2 Grandezas radiométricas e componentes da radiação

Responsável: **Samuel**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Irradiância, irradiação, irradiância global horizontal (GHI), irradiância direta normal (DNI) e irradiância difusa horizontal (DHI).

## Entradas, método e resultado esperado

**Entradas:** POA local medida; componentes reconstruídas quando a inversão estiver ativa.

Irradiância é potência por área; irradiação é sua integral no tempo. GHI é horizontal, DNI é normal aos raios solares e DHI é difusa horizontal. POA se refere ao plano do arranjo.

$$GHI=DNI\max(\cos\theta_z,0)+DHI,\qquad H=\sum_i G_i\Delta t_i.$$

**Saídas:** Quadro das grandezas e componentes estimadas.

**Evidência:** Medição POA e estimativa exploratória das componentes. **Limitação:** Sem GHI/DNI/DHI locais medidos; reconstrução não equivale a observação.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B11](../../../../bibliografia/principal/README.md#b11) — Artigo | DRIESSE, A.; JENSEN, A. R.; PEREZ, R. A continuous form of the Perez diffuse sky model for forward and reverse transposition. Solar Energy, [S. l.], v. 267, art. 112093, 2024. DOI: https://doi.org/10.1016/j.solener.2023.112093. Disponível em: https://doi.org/10.1016/j.solener.2023.112093. Acesso em: 16 out. 2026. | [A089 — PDF](https://drive.google.com/file/d/1woLwuNHB_hbHuY0GPOKyq_KvZ_heXRtb/view?usp=drivesdk) |
| [B12](../../../../bibliografia/principal/README.md#b12) — Livro | DUFFIE, J. A.; BECKMAN, W. A.; BLAIR, N. Solar Engineering of Thermal Processes, Photovoltaics and Wind. [S. l.]: Wiley, 2020. DOI: https://doi.org/10.1002/9781119540328. Disponível em: https://doi.org/10.1002/9781119540328. Acesso em: 16 out. 2026. | [A001 — PDF](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) |
| [B19](../../../../bibliografia/principal/README.md#b19) — Livro | KALOGIROU, S. A. Solar Energy Engineering: Processes and Systems. 2. ed. [S. l.]: Elsevier, 2014. DOI: https://doi.org/10.1016/c2011-0-07038-2. Disponível em: https://doi.org/10.1016/c2011-0-07038-2. Acesso em: 16 out. 2026. | PDF não localizado |
| [B20](../../../../bibliografia/principal/README.md#b20) — Livro | LUQUE, A.; HEGEDUS, S. (ed.). Handbook of Photovoltaic Science and Engineering. 2. ed. [S. l.]: Wiley, 2011. DOI: https://doi.org/10.1002/9780470974704. Disponível em: https://doi.org/10.1002/9780470974704. Acesso em: 16 out. 2026. | [A034 — outra edição](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) |
| [B24](../../../../bibliografia/principal/README.md#b24) — Documento técnico | OEDI / PVDAQ. PVDAQ public photovoltaic performance data — OEDI. [S. l.], [s.d.]. DOI: https://doi.org/10.25984/1846021. Disponível em: https://doi.org/10.25984/1846021. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |
| [B36](../../../../bibliografia/principal/README.md#b36) — Relatório técnico | SENGUPTA, M. et al. Best Practices Handbook for the Collection and Use of Solar Resource Data for Solar Energy Applications: Third Edition. [S. l.]: Office of Scientific and Technical Information (OSTI), 2021. DOI: https://doi.org/10.2172/1778700. Disponível em: https://doi.org/10.2172/1778700. Acesso em: 16 out. 2026. | [A088 — PDF](https://drive.google.com/file/d/1dty_mkSk-clgscx1BxxMdMcliI42ewjd/view?usp=drivesdk) |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A001 | [Abrir Solar Engineering of Thermal Processes, Photovoltaics and Wind](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) | 5ª edição confirmada no PDF, com 919 páginas digitais e índice até a página impressa 905. Alternativa de trabalho adotada para B19, em conjunto com A003. Citar Duffie, Beckman e Blair (2020) ao usar este arquivo. |
| A034 | [Abrir Handbook of Photovoltaic Science and Engineering](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) | 1ª edição. Apoio alternativo a B20; não satisfaz a edição de 2011 indicada. |
| A088 | [Abrir Best practices handbook for the collection and use of solar resource data for solar energy applications: third edition (formato IEA PVPS)](https://drive.google.com/file/d/1dty_mkSk-clgscx1BxxMdMcliI42ewjd/view?usp=drivesdk) | Terceira edição obtida no formato IEA-PVPS T16-04:2021, 331 páginas, ISBN 978-3-907281-19-2. A página oficial informa dois formatos da mesma edição (NREL e IEA PVPS). O DOI 10.2172/1778700 identifica o formato NREL, não este arquivo IEA PVPS. Citar o formato efetivamente consultado; a 4ª edição de 2024 A045 permanece disponível. |
| A089 | [Abrir A continuous form of the Perez diffuse sky model for forward and reverse transposition](https://drive.google.com/file/d/1woLwuNHB_hbHuY0GPOKyq_KvZ_heXRtb/view?usp=drivesdk) | Versão final da editora, 12 páginas, licença CC BY 4.0. Volume 267 (2024), artigo 112093; publicação online em 2/12/2023. Cópias nas quatro seções. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Ilustrações de inserção exclusiva

A coluna de subseção indica o local de cada material no capítulo. Claro/escuro e PNG/PDF são opções do mesmo item. Referências em outras seções usam o ID correspondente.

| ID e título | Inserir em | PNG claro e escuro | PDF claro e escuro |
| --- | --- | --- | --- |
| F02_componentes_POA — Componentes incidentes no plano do módulo | 1.2 | [Claro](../../figuras/claro/F02_componentes_POA.png) / [Escuro](../../figuras/escuro/F02_componentes_POA.png) | [Claro](../../figuras/claro/F02_componentes_POA.pdf) / [Escuro](../../figuras/escuro/F02_componentes_POA.pdf) |

**F02_componentes_POA:** Representação esquemática das contribuições à POA. Não atribui medições locais de GHI/DNI/DHI nem albedo. O sensor POA da cadeia principal já recebe a contribuição refletida do entorno. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R06; R29.

## Tabelas e quadros de inserção exclusiva

Não há tabela ou quadro Word atribuído a esta subseção.

Não há CSV de tabela atribuído a esta subseção.

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)

## Inventário de equações

[Quadro de equações da seção em PDF e Word](../../equacoes/README.md): 2 relações do núcleo e 0 de apoio nesta subseção. IDs: E1.03, E1.04.
