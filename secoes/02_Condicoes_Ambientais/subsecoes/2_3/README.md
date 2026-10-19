# 2.3 Sombreamento, sujidade e obstruções locais

Responsável: **Vannessa e Thais**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Fatores que reduzem a irradiância efetivamente recebida.

## Entradas, método e resultado esperado

**Entradas:** Cenários de atenuação adicional de 0%, 2% e 5%; alertas operacionais.

A sujeira pode atenuar a luz incidente e diferir entre módulos e sensor POA. Os cenários são hipóteses de atenuação adicional à leitura. Sombreamento parcial pode envolver mismatch e diodos de bypass, que um redutor uniforme não reproduz.

$$G_{\mathrm{ef}}=(1-s)G_{\mathrm{POA}}.$$

**Saídas:** Sensibilidade e alertas sem atribuição causal automática.

**Evidência:** Sensibilidade hipotética e fundamentos. **Limitação:** Sem histórico de limpeza e mapa de sombras; o resíduo não identifica a perda real de sujidade ou sombra.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B04](../../../../bibliografia/principal/README.md#b04) — Artigo | BISHOP, J. W. Computer simulation of the effects of electrical mismatches in photovoltaic cell interconnection circuits. Solar Cells, [S. l.], v. 25, n. 1, p. 73-89, 1988. DOI: https://doi.org/10.1016/0379-6787(88)90059-2. Disponível em: https://doi.org/10.1016/0379-6787(88)90059-2. Acesso em: 16 out. 2026. | [A073 — PDF](https://drive.google.com/file/d/1naylazsLo6-XnxIAo2WGf7BB22ATIava/view?usp=drivesdk) |
| [B12](../../../../bibliografia/principal/README.md#b12) — Livro | DUFFIE, J. A.; BECKMAN, W. A.; BLAIR, N. Solar Engineering of Thermal Processes, Photovoltaics and Wind. [S. l.]: Wiley, 2020. DOI: https://doi.org/10.1002/9781119540328. Disponível em: https://doi.org/10.1002/9781119540328. Acesso em: 16 out. 2026. | [A001 — PDF](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) |
| [B20](../../../../bibliografia/principal/README.md#b20) — Livro | LUQUE, A.; HEGEDUS, S. (ed.). Handbook of Photovoltaic Science and Engineering. 2. ed. [S. l.]: Wiley, 2011. DOI: https://doi.org/10.1002/9780470974704. Disponível em: https://doi.org/10.1002/9780470974704. Acesso em: 16 out. 2026. | [A034 — outra edição](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) |
| [B21](../../../../bibliografia/principal/README.md#b21) — Artigo | MANI, M.; PILLAI, R. Impact of dust on solar photovoltaic (PV) performance: Research status, challenges and recommendations. Renewable and Sustainable Energy Reviews, [S. l.], v. 14, n. 9, p. 3124-3131, 2010. DOI: https://doi.org/10.1016/j.rser.2010.07.065. Disponível em: https://doi.org/10.1016/j.rser.2010.07.065. Acesso em: 16 out. 2026. | [A081 — PDF](https://drive.google.com/file/d/1DDy6MPhAxwJqT25dWSO_LaSSCIM9Hbrc/view?usp=drivesdk) |
| [B26](../../../../bibliografia/principal/README.md#b26) — Documento técnico | PV ANALYTICS WEBINAR. Solar Data Tools demo — Farm Solar Array. [S. l.], 2024. Disponível em: https://pv-tutorials.github.io/2024_Analytics_Webinar/solar-data-tools-demo.html. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |
| [B35](../../../../bibliografia/principal/README.md#b35) — Documento técnico | SANDIA NATIONAL LABORATORIES / PVPMC. Soiling Losses. [S. l.], [s.d.]. Disponível em: https://pvpmc.sandia.gov/modeling-guide/1-weather-design-inputs/shading-soiling-and-reflection-losses/soiling-losses/. Acesso em: 16 out. 2026. | Fonte online / sem PDF catalogado |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A001 | [Abrir Solar Engineering of Thermal Processes, Photovoltaics and Wind](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) | 5ª edição confirmada no PDF, com 919 páginas digitais e índice até a página impressa 905. Alternativa de trabalho adotada para B19, em conjunto com A003. Citar Duffie, Beckman e Blair (2020) ao usar este arquivo. |
| A034 | [Abrir Handbook of Photovoltaic Science and Engineering](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) | 1ª edição. Apoio alternativo a B20; não satisfaz a edição de 2011 indicada. |
| A073 | [Abrir Computer simulation of the effects of electrical mismatches in photovoltaic cell interconnection circuits](https://drive.google.com/file/d/1naylazsLo6-XnxIAo2WGf7BB22ATIava/view?usp=drivesdk) | Artigo completo; páginas 73–89. |
| A081 | [Abrir Impact of dust on solar photovoltaic (PV) performance: research status, challenges and recommendations](https://drive.google.com/file/d/1DDy6MPhAxwJqT25dWSO_LaSSCIM9Hbrc/view?usp=drivesdk) | Versão publicada; páginas 3124–3131. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Ilustrações de inserção exclusiva

A coluna de subseção indica o local de cada material no capítulo. Claro/escuro e PNG/PDF são opções do mesmo item. Referências em outras seções usam o ID correspondente.

| ID e título | Inserir em | PNG claro e escuro | PDF claro e escuro |
| --- | --- | --- | --- |
| G20_sujidade_ventilacao — Sensibilidade à sujidade e à ventilação | 2.3 | [Claro](../../graficos/claro/G20_sujidade_ventilacao.png) / [Escuro](../../graficos/escuro/G20_sujidade_ventilacao.png) | [Claro](../../graficos/claro/G20_sujidade_ventilacao.pdf) / [Escuro](../../graficos/escuro/G20_sujidade_ventilacao.pdf) |

**G20_sujidade_ventilacao:** Cenários, não perdas medidas. Sujidade representa atenuação adicional do módulo em relação à leitura POA; considerar a condição do sensor evita dupla contagem. Ventilação reduzida usa U₀=15 e U₁=3. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R07; R28.

## Tabelas e quadros de inserção exclusiva

| ID | Tabela ou quadro | Inserir em |
| --- | --- | --- |
| T12 | Sensibilidade de sujidade e ventilação | 2.3 |

[Baixar o Word com os materiais tabulares desta seção](../../tabelas/docx/Materiais_Tabulares_Secao_02.docx).

| Dados e tabelas em CSV | Inserir em |
| --- | --- |
| [environment_sensitivity](../../../../outputs/tabelas/csv/environment_sensitivity.csv) | 2.3 |

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)

## Inventário de equações

[Quadro de equações da seção em PDF e Word](../../equacoes/README.md): 1 relações do núcleo e 0 de apoio nesta subseção. IDs: E2.05.
