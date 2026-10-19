# 3.5 Conversão de CC para corrente alternada (CA) e modelagem do inversor

Responsável: **Gabriela e Giulia**. [Voltar à seção](../../README.md) · [Início do projeto](../../../../README.md)

## Objetivo oficial

Eficiência, faixa de operação, relação de potência CC/CA, limitação de potência e clipping.

## Entradas, método e resultado esperado

**Entradas:** Potência DC calculada, eficiência e limites assumidos do inversor.

A curva PVWatts estima conversão e clipping. O limite de referência é 30 kW por inversor; 27,6 kW permanece como sensibilidade documentada. Verificar a faixa real de MPPT exige topologia e configuração de campo adicionais.

$$P_{\mathrm{AC}}=\min[\eta(P_{\mathrm{DC}})P_{\mathrm{DC}},P_{\mathrm{AC,max}}],\quad P_{\mathrm{dc0,inv}}=P_{\mathrm{AC,max}}/\eta_{\mathrm{nom}}.$$

**Saídas:** Curva de eficiência, clipping calculado e sensibilidade AC.

**Evidência:** Modelo de conversão e sensibilidade. **Limitação:** A simulação agregada não verifica todas as restrições reais de tensão/MPPT nem confirma o limite instalado.

## Bibliografia principal B

| Código e tipo | Referência ABNT | Texto integral / disponibilidade |
| --- | --- | --- |
| [B01](../../../../bibliografia/principal/README.md#b01) — Documento técnico | ABB. TRIO-20.0/27.6-TL-US — Product Manual. [S. l.], [s.d.]. Disponível em: https://library.e.abb.com/public/9ddffa465aa146bfa43bd0854abbcc81/TRIO-20.0-27.6-TL-US_Product_Manual.pdf. Acesso em: 16 out. 2026. | [A068 — PDF](https://drive.google.com/file/d/1wZ672wUUn4pjxEQO_L4469NZvf4RO2Eq/view?usp=drivesdk) |
| [B06](../../../../bibliografia/principal/README.md#b06) — Relatório técnico | BOYSON, W. et al. Performance model for grid-connected photovoltaic inverters. [S. l.]: Office of Scientific and Technical Information (OSTI), 2007. DOI: https://doi.org/10.2172/920449. Disponível em: https://doi.org/10.2172/920449. Acesso em: 16 out. 2026. | [A086 — PDF](https://drive.google.com/file/d/1jB5u6-hVizTlQj0xKA0PKYAP1Oll6eOf/view?usp=drivesdk) |
| [B10](../../../../bibliografia/principal/README.md#b10) — Documento técnico | DOBOS, A. P. PVWatts Version 5 Manual — NREL/TP-6A20-62641. [S. l.], 2014. Disponível em: https://docs.nlr.gov/docs/fy14osti/62641.pdf. Acesso em: 16 out. 2026. | [A067 — PDF](https://drive.google.com/file/d/1ATm6277jw9kBI7Tl6FOruDMQvbzBCXTY/view?usp=drivesdk) |
| [B12](../../../../bibliografia/principal/README.md#b12) — Livro | DUFFIE, J. A.; BECKMAN, W. A.; BLAIR, N. Solar Engineering of Thermal Processes, Photovoltaics and Wind. [S. l.]: Wiley, 2020. DOI: https://doi.org/10.1002/9781119540328. Disponível em: https://doi.org/10.1002/9781119540328. Acesso em: 16 out. 2026. | [A001 — PDF](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) |
| [B20](../../../../bibliografia/principal/README.md#b20) — Livro | LUQUE, A.; HEGEDUS, S. (ed.). Handbook of Photovoltaic Science and Engineering. 2. ed. [S. l.]: Wiley, 2011. DOI: https://doi.org/10.1002/9780470974704. Disponível em: https://doi.org/10.1002/9780470974704. Acesso em: 16 out. 2026. | [A034 — outra edição](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) |

## PDFs A de apoio e acervo complementar

| Código | PDF e edição | Observação |
| --- | --- | --- |
| A001 | [Abrir Solar Engineering of Thermal Processes, Photovoltaics and Wind](https://drive.google.com/file/d/1FRN89M_tXpON-3OFe5K06p9xt3nqfl7u/view?usp=drivesdk) | 5ª edição confirmada no PDF, com 919 páginas digitais e índice até a página impressa 905. Alternativa de trabalho adotada para B19, em conjunto com A003. Citar Duffie, Beckman e Blair (2020) ao usar este arquivo. |
| A034 | [Abrir Handbook of Photovoltaic Science and Engineering](https://drive.google.com/file/d/1gHLYXkymfLiRuyNfYDDRuJ0KsKJByVdh/view?usp=drivesdk) | 1ª edição. Apoio alternativo a B20; não satisfaz a edição de 2011 indicada. |
| A067 | [Abrir PVWatts Version 5 Manual — NREL/TP-6A20-62641](https://drive.google.com/file/d/1ATm6277jw9kBI7Tl6FOruDMQvbzBCXTY/view?usp=drivesdk) |  |
| A068 | [Abrir TRIO-20.0/27.6-TL-US — Product Manual](https://drive.google.com/file/d/1wZ672wUUn4pjxEQO_L4469NZvf4RO2Eq/view?usp=drivesdk) |  |
| A086 | [Abrir Performance model for grid-connected photovoltaic inverters](https://drive.google.com/file/d/1jB5u6-hVizTlQj0xKA0PKYAP1Oll6eOf/view?usp=drivesdk) | Relatório oficial completo, 47 páginas. Autores: King, Gonzalez, Galbraith e Boyson. |

[Outros documentos A da seção, com pertinência específica ainda a conferir](../../referencias/README.md)

## Ilustrações de inserção exclusiva

A coluna de subseção indica o local de cada material no capítulo. Claro/escuro e PNG/PDF são opções do mesmo item. Referências em outras seções usam o ID correspondente.

| ID e título | Inserir em | PNG claro e escuro | PDF claro e escuro |
| --- | --- | --- | --- |
| G07_inversor — Eficiência e limitação de potência do inversor | 3.5 | [Claro](../../graficos/claro/G07_inversor.png) / [Escuro](../../graficos/escuro/G07_inversor.png) | [Claro](../../graficos/claro/G07_inversor.pdf) / [Escuro](../../graficos/escuro/G07_inversor.pdf) |

**G07_inversor:** Curva PVWatts com limite assumido de 30 kW por inversor e η nominal de 98%. O valor de pdc0 do inversor é Paco/ηnom; não é a potência STC do arranjo. Configuração real do limite AC ainda não comprovada. Fonte: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026). Métodos: R11; R13.

## Tabelas e quadros de inserção exclusiva

| ID | Tabela ou quadro | Inserir em |
| --- | --- | --- |
| T13 | Sensibilidade do limite AC por inversor | 3.5 |
| Q05 | Modelagem da conversão | 3.5 |

[Baixar o Word com os materiais tabulares desta seção](../../tabelas/docx/Materiais_Tabulares_Secao_03.docx).

| Dados e tabelas em CSV | Inserir em |
| --- | --- |
| [capacity_sensitivity](../../../../outputs/tabelas/csv/capacity_sensitivity.csv) | 3.5 |
| [curva_inversor_modelada](../../../../outputs/tabelas/csv/curva_inversor_modelada.csv) | 3.5 |

## Documentos, dados e execução

[Dossiê técnico original — dados e equipamentos](../../../../docs/metodos/Dossie_Tecnico_por_Secao.docx) · [Métodos e fontes](../../../../docs/Metodos_e_Fontes_Conferidos.md) · [Notebook fotovoltaico](../../../../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) · [Notebook bibliográfico](../../../../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb) · [Todos os documentos Word](../../../../docs/README.md)

[Dados preparados e máscaras](../../../../data/processed/README.md) · [Quatro CSVs originais completos](../../../../data/raw/README.md) · [Módulos, inversores e 125 canais](../../../../data/equipamentos/README.md)

## Inventário de equações

[Quadro de equações da seção em PDF e Word](../../equacoes/README.md): 2 relações do núcleo e 5 de apoio nesta subseção. IDs: E3.11, E3.12, E3.13, E3.14, E3.15, E3.16, E3.17.
