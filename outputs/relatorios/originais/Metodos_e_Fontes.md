# Métodos, fontes e parâmetros

Versão do projeto: 1.2.0, preparada em 16/10/2026. Implementação científica: pvlib 0.16.1. Os valores em `config/projeto.json` são a referência executável; este texto explica sua procedência.

## Métodos na ordem do capítulo

| Etapa | Método | Fonte primária | Implementação |
|---|---|---|---|
| Posição solar | SPA | Reda e Andreas, NREL/TP-560-34302, revisão 2008 | `Location.get_solarposition`, método SPA do pvlib |
| Extraterrestre | Correção Terra–Sol de Spencer | Documentação e implementação pvlib | `get_extra_radiation(method='spencer')` |
| Entradas principais | POA, temperatura e vento locais | PVDAQ/OEDI | CSVs originais, sem consulta NASA |
| Componentes exploratórias | Inversão Driesse + decomposição Erbs-Driesse | Driesse et al. (2024), DOI 10.1016/j.solener.2023.112093 | ghi_from_poa_driesse_2024; sem validação independente das componentes |
| POA | Perez e reflexão isotrópica do solo | Perez et al. (1990), DOI 10.1016/0038-092X(90)90055-H | `get_total_irradiance(model='perez')` |
| Temperatura | Faiman | Faiman (2008), DOI 10.1002/pip.813 | `temperature.faiman` |
| Módulo | Diodo único, parâmetros CEC, derivados da formulação De Soto | De Soto et al. (2006), DOI 10.1016/j.solener.2005.06.010; documentação CEC/pvlib | `calcparams_cec`, `singlediode`, Lambert W |
| Inversor | PVWatts | Dobos (2014), NREL/TP-6A20-62641 | Curva idêntica a `inverter.pvwatts`, com estágios de eficiência/clipping separados |
| Desempenho | Yr, Ya, Yf, PR, Lc e Ls | Marion et al. (2005), NREL/CP-520-37358 | Integração nos mesmos intervalos |
| BIPV | Mesma cadeia de radiação/conversão + balanço solar simplificado | Conceitos de integração FV e ganho solar da DOE | Cenário próprio explicitamente hipotético |

Os manuais SPA, PVWatts, parâmetros de desempenho e ABB foram baixados de fontes oficiais e estão no pacote completo. URLs, tamanhos e hashes estão em `fontes_metodos.json`. As páginas pvlib cuja cópia HTML não pôde ser obtida permanecem indicadas por URL; a implementação é disponibilizada pela instalação da versão fixada do software.

## Referências e documentos oficiais

- [Registro PVDAQ/OEDI](https://data.openei.org/submissions/4568), DOI 10.25984/1846021, CC BY 4.0.
- [Repositório oficial de acesso ao PVDAQ](https://github.com/NatLabRockies/pvdaq_access).
- [Documentação openEDI/PVDAQ](https://github.com/openEDI/documentation/blob/main/pvdaq.md).
- [SPA, PDF oficial](https://docs.nlr.gov/docs/fy08osti/34302.pdf).
- [PVWatts v5, PDF oficial](https://docs.nlr.gov/docs/fy14osti/62641.pdf).
- [Performance Parameters, PDF oficial](https://docs.nlr.gov/docs/fy05osti/37358.pdf).
- [Manual ABB TRIO US, PDF oficial](https://library.e.abb.com/public/9ddffa465aa146bfa43bd0854abbcc81/TRIO-20.0-27.6-TL-US_Product_Manual.pdf).
- [NASA POWER: API horária](https://power.larc.nasa.gov/docs/services/api/temporal/hourly/).
- [NASA POWER: SYN1deg](https://power.larc.nasa.gov/docs/methodology/energy-fluxes/syn1deg/).
- [pvlib: CEC](https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.pvsystem.calcparams_cec.html).
- [pvlib: Faiman](https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.temperature.faiman.html).
- [pvlib: Perez](https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.irradiance.perez.html).
- [pvlib: inversor PVWatts](https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.inverter.pvwatts.html).
- [DOE: BIPV](https://www.energy.gov/cmei/systems/articles/expanding-solar-energy-opportunities-rooftops-building-integration).
- [DOE: definição de ganho solar em janelas](https://www.energy.gov/energysaver/energy-performance-ratings-windows-doors-and-skylights).

## Convenções temporais e auditoria

O trimestre começa em 01/04/2024 00:00 e termina, de forma exclusiva, em 01/07/2024 00:00 no fuso `America/Los_Angeles`. Os índices internos e os CSVs de saída usam UTC. Seleciona-se o trimestre antes de localizar os carimbos locais do PVDAQ, evitando os horários ambíguos das transições anuais de verão.

Adota-se o rótulo como início do intervalo; a SPA é calculada em seu ponto médio. NASA POWER não é consultado na versão atual; a consulta UTC da versão 1.0 permanece preservada como histórico. Essa interpretação de intervalo é uma hipótese documentada, sem otimizar a defasagem contra a geração. A cobertura reproduz o critério anterior: elevação NOAA de pelo menos 10°. A seleção diurna não usa a própria potência elétrica.

Para POA e inversores com frequência original de 5 minutos, só se usa a média de 15 minutos se as três observações existirem. Temperatura, vento e medidor têm cadência de 15 minutos. Não se preenchem lacunas. Os limites físicos amplos e as máscaras ficam na série de saída. A disponibilidade conjunta inclui os 24 inversores; a referência principal continua sendo o medidor.

## Parâmetros e suas incertezas

| Item | Valor-base | Procedência e limite |
|---|---|---|
| Local | 38,996306°; −122,134111°; 10 m | Metadados PVDAQ |
| Geometria | Inclinação 25°; azimute 180° | Metadados; norte=0°, sul=180° |
| Módulos | 2.880 HiS-M310TI | Metadados; parâmetros CEC preservados em JSON |
| Referência P0 | 893 kW | Potência declarada usada em produtividades/PR |
| STC do modelo | 309,6 W/módulo; 891,648 kW no total | Banco CEC/SAM, diferente dos 310 W nominais |
| Térmica | U0=25; U1=6,84 | Valores genéricos Faiman; temperatura operacional usada como aproximação da célula |
| Albedo | 0,20 | Não medido; sensibilidade 0,10/0,20/0,40 |
| Sujidade | 0% | Não medida; cenários adicionais 2% e 5% |
| Perdas CC | Fios 2%; mismatch 2%; conexões 0,5% | Hipóteses genéricas, combinadas multiplicativamente |
| Inversores | 24 unidades | Metadados |
| Limite AC-base | 30 kW por inversor | Possibilidade da configuração US padrão documentada pelo fabricante, configuração local não comprovada |
| Limite alternativo | 27,6 kW por inversor | Designação nominal/banco CEC; ambos os cenários são apresentados |
| Eficiência | ηnom=0,98; ηref=0,9637 | Hipótese nominal + referência da curva PVWatts |
| Vento principal | Medição local convertida de mph | Altura do anemômetro não suficientemente documentada |

O JSON PVDAQ classifica o módulo como mono-Si, enquanto o banco CEC o classifica como multicristalino. Mantém-se o arquivo original e usam-se os parâmetros do modelo CEC identificado. A corrente de curto-circuito do ajuste CEC não coincide exatamente com a corrente tabulada. Nenhum desses campos foi corrigido para melhorar a comparação com o medidor.

Os campos de topologia e associação módulo–inversor não permitem reconstruir comprovadamente as strings. A potência principal é agregada a partir do MPP do módulo. O exemplo 20×6 demonstra regras de série/paralelo, sem validar tensões e MPPTs da instalação real.

## Validação e separação temporal

Erro = predição − observação. O nRMSE divide o RMSE pela média observada, não pela potência nominal. R² usa 1−SSE/SST e não o quadrado da correlação. As estatísticas são pareadas sem exclusão de pontos por apresentarem erro alto.

O modelo sem escala empírica é o resultado principal. O fator adicional k=0,9266727368 foi obtido por mínimos quadrados sem intercepto **somente com abril**. Maio é apresentado separadamente e junho não entra no ajuste. A escala não identifica uma perda física nem comprova a qualidade do sensor. O modelo-base mantém um viés positivo de 7,73% contra o medidor.

O PR com POA local é restrito aos 4.401 intervalos pareados. A energia observada integral de 454,285 MWh usa todos os 8.736 intervalos do trimestre. Não se misturam esses dois escopos no mesmo indicador.

## Extensão BIPV e conservação de energia

O caso de fachada reutiliza o local e a meteorologia medida, com componentes estimadas da POA por inversão. São usadas somente as horas diurnas elegíveis; a energia não é o total integral do trimestre. A comparação por 1 kWp mantém o modelo CEC, perdas e relação CC/CA do caso de referência; a energia é normalizada pela potência declarada de 893 kW. Assim se examina geometria/ventilação sem substituir silenciosamente o módulo ou o inversor. O cenário semitransparente é um produto hipotético distinto de 100 m²: eficiência de referência 10%, refletância solar 0,12, transmitância solar 0,25, transmitância visível 0,35 e fração de calor para dentro 0,50. A transmitância visível não é inferida da transmitância solar.

Com α=1−ρ−τs, a radiação incidente GA é dividida em reflexão ρGA, transmissão τsGA, eletricidade ηGA e calor (α−η)GA. O calor se divide entre interior e exterior. A soma dessas parcelas é conferida em cada hora. O ganho solar interno é τsGA+fin(α−η)GA e o SHGC equivalente simplificado é essa parcela dividida por GA.

Esse balanço não é certificação de SHGC, não produz iluminância em lux e não substitui um modelo térmico completo da edificação. Nenhuma observação de fachada foi inventada. Uma aplicação futura precisa de propriedades ópticas/térmicas do produto e, para validação, medições da envoltória real.


## Atualização v1.1 — inversão e referências

A inversão usa médias horárias completas, zenital e incidência de até 80°, albedo 0,20 e tolerância numérica de 0,01 W/m². A convergência e o fechamento verificam a solução do modelo adotado; não demonstram precisão física nem unicidade e não validam GHI, DNI ou DHI sem observações independentes. A POA original medida continua na comparação elétrica principal.

Inventário completo de 30 fontes: `references/Referencias_do_Projeto.md`, `referencias_projeto.json` e `referencias_projeto.bib`; seção 5 do notebook. NASA é preservado apenas como histórico.


## Refinamento v1.2

Os métodos físicos foram mantidos; acrescentaram-se estatística descritiva com DP amostral e quartis, erros por estrato, resíduos, gráficos de validação e PSH da janela pareada. nMBE e nRMSE normalizam pela média observada dos respectivos pares; estratos mensais/horários/faixas de POA identificam sua amostra e cobertura. R27 complementa os indicadores de erro, R28 a sujidade, R29 a POA e R30 as produtividades/PR.

Saídas: outputs/tabelas, quadros, graficos, fluxogramas, figuras e relatorios. Há cinco DOCX, 30 figuras em 120 arquivos PDF/PNG e matriz das 19 subseções. Os PNG têm 600 dpi; os PDF são gerados diretamente com elementos vetoriais. Os temas conservam dados, textos e limites dos eixos. As tabelas têm três traços horizontais e os quadros têm grade completa, conforme preferência do usuário. Fonte 12 e espessura dos traços são especificações do projeto, sem alegação de universalidade normativa.

O notebook usa descrições separadas em details HTML. O relatório HTML tem recolhimento nativo e botão de tema; não se presume renderização idêntica entre interfaces Jupyter/Colab. A autenticação Google é pessoal e a exportação do Colab é opcional.
