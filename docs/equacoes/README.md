# Inventário de equações por seção e subseção

O levantamento contém **61 relações numeradas**: **37 do núcleo do notebook** e **24 de apoio verificadas no código**. Cada ID tem uma única subseção de inserção. A equação de Faiman aparece uma vez em 3.2; em 2.1 há remissão a E3.03.

Uma linha representa uma relação numerada. Constantes e parâmetros não são novas equações. Os itens N formam o núcleo de inserção; os itens C documentam o método e sua inclusão depende do espaço e da discussão. O documento geral serve ao controle da equipe e os quatro documentos individuais à redação da respectiva seção.

[Baixar inventário geral em Word](Inventario_Geral_Equacoes_SPGER0046.docx) · [Dados do inventário em CSV](Inventario_Equacoes.csv) · [Fonte estruturada em JSON](Inventario_Equacoes.json)

[Abrir a pasta dos cinco Word no Google Drive](https://drive.google.com/drive/folders/1yfwwArqBTVwPt7EYer9DlHL1vmeO5V7B). Os arquivos DOCX foram preservados no formato Word.

| Seção | Núcleo N | Apoio C | Total | Documento exclusivo |
| --- | --- | --- | --- | --- |
| 1 Fundamentos e caracterização do recurso solar | 6 | 0 | 6 | [Word da seção 1](../../secoes/01_Recurso_Solar/equacoes/Quadro_Equacoes_Secao_01.docx) |
| 2 Condições ambientais e de entorno da conversão fotovoltaica | 4 | 3 | 7 | [Word da seção 2](../../secoes/02_Condicoes_Ambientais/equacoes/Quadro_Equacoes_Secao_02.docx) |
| 3 Modelagem da conversão fotovoltaica | 11 | 7 | 18 | [Word da seção 3](../../secoes/03_Modelagem_Fotovoltaica/equacoes/Quadro_Equacoes_Secao_03.docx) |
| 4 Avaliação de desempenho perdas e validação da modelagem | 16 | 14 | 30 | [Word da seção 4](../../secoes/04_Desempenho_Perdas_Validacao/equacoes/Quadro_Equacoes_Secao_04.docx) |
| Total | 37 | 24 | 61 | |

## Fontes e convenções

O núcleo foi conferido no notebook e na matriz da revisão `17ffe0eeb7d70876eabf222ec30fb828ee28d3c8`. As fórmulas são nativas e editáveis nos Word. As potências devem usar unidades coerentes; para integrar W em kWh, multiplicar pela duração em horas e dividir por 1000. A análise usa intervalos de 15 minutos e o período abril a junho de 2024 do PVDAQ 2107.

N corresponde a relações já escritas nas células de método. C expõe relações utilizadas pelo código, inclusive métricas normalizadas, correlação, curva do inversor, ajuste empírico e balanço BIPV. As expressões internas de bibliotecas e os critérios computacionais não são expandidos como equações de redação.

## Subseção 1.1

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E1.01 | **Ângulo zenital**. Relacionar a posição do Sol à latitude e ao tempo solar. | N | [geometry](../../src/projeto_fv.py) |
| E1.02 | **Irradiância extraterrestre horizontal**. Projetar a irradiância extraterrestre normal na horizontal. | N | [geometry](../../src/projeto_fv.py) |

**E1.01**

$$\cos\theta_z=\sin\varphi\sin\delta+\cos\varphi\cos\delta\cos\omega$$

φ latitude; δ declinação; ω ângulo horário; θz zênite. Relação geométrica de fundamentação; o cálculo utiliza SPA e o meio de cada intervalo.

**E1.02**

$$G_{0h}=G_{0n}\max(\cos\theta_z,0)$$

G0n e G0h em W/m².

## Subseção 1.2

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E1.03 | **Componentes na horizontal**. Distinguir irradiâncias global horizontal direta normal e difusa horizontal. | N | [1.2](../../docs/secoes_capitulo.json) |
| E1.04 | **Irradiação acumulada**. Integrar irradiância média no plano e período definidos. | N | [analytics](../../src/refinamento_fv.py) |

**E1.03**

$$GHI=DNI\max(\cos\theta_z,0)+DHI$$

GHI DNI e DHI em W/m². Identidade de fundamentação; GHI DNI e DHI locais são estimativas na exploração inversa.

**E1.04**

$$H=\sum_i G_i\Delta t_i$$

G em W/m²; Δt em h; H em Wh/m²; dividir por 1000 para kWh/m².

## Subseção 1.3

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E1.05 | **Variabilidade relativa da irradiância**. Ordenar os dias pelo passo absoluto médio da POA relativo à sua média. | N | [analytics](../../src/refinamento_fv.py) |

**E1.05**

$$V_{\Delta G}=\frac{\operatorname{média}(|G_i-G_{i-1}|)}{\operatorname{média}(G_i)}$$

Gi POA dos pares válidos ordenados do dia; resultado adimensional. O código aplica diff aos pares disponíveis do dia; intervalos entre pares podem conter lacunas.

## Subseção 1.4

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E1.06 | **Cobertura dos dados**. Informar a proporção de intervalos válidos frente aos esperados. | N | [analytics](../../src/refinamento_fv.py) |

**E1.06**

$$C=100\,N_{\mathrm{pares}}/N_{\mathrm{esperados}}$$

Npares e Nesperados na mesma janela; C em %.

## Subseção 2.1

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E2.01 | **Média amostral**. Resumir a posição das distribuições ambientais e das variáveis tabuladas. | C | [analytics](../../src/refinamento_fv.py) |
| E2.02 | **Desvio padrão amostral**. Quantificar a dispersão com a convenção amostral usada no projeto. | C | [analytics](../../src/refinamento_fv.py) |
| E2.03 | **Amplitude interquartil**. Resumir a dispersão central entre os percentis 25 e 75. | C | [analytics](../../src/refinamento_fv.py) |

**E2.01**

$$\bar{x}=\frac{1}{n}\sum_{i=1}^{n}x_i$$

xi variável analisada; n pares; média na unidade de x.

**E2.02**

$$s_x=\sqrt{\frac{\sum_{i=1}^{n}(x_i-\bar{x})^2}{n-1}}$$

n maior que 1; sx na unidade de x. O código usa std com ddof igual a 1. A equação de Faiman fica em E3.03 e deve ser apenas citada em 2.1.

**E2.03**

$$IQR=Q_3-Q_1$$

Q1 e Q3 quartis da mesma variável e janela.

## Subseção 2.2

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E2.04 | **Reflexão isotrópica do solo**. Estimar a parcela refletida pelo solo que incide no plano inclinado. | N | [transpose](../../src/projeto_fv.py) |

**E2.04**

$$G_{\mathrm{solo}}=\rho_g\,GHI\,\frac{1-\cos\beta}{2}$$

ρg albedo; β inclinação; irradiâncias em W/m². Aplicada aos cenários de transposição; não somar novamente à POA medida da cadeia principal.

## Subseção 2.3

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E2.05 | **Irradiância efetiva**. Aplicar a hipótese de atenuação adicional à leitura POA. | N | [simulate](../../src/projeto_fv.py) |

**E2.05**

$$G_{\mathrm{ef}}=(1-s)G_{\mathrm{POA}}$$

s fração assumida entre 0 e 1; Gef e GPOA em W/m². A atenuação uniforme não representa sombreamento parcial com mismatch ou diodos de bypass.

## Subseção 2.4

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E2.06 | **Ângulo de incidência**. Relacionar a geometria do Sol à orientação do plano. | N | [geometry](../../src/projeto_fv.py) |
| E2.07 | **Projeção geométrica de sombra**. Ilustrar a projeção horizontal de uma altura sob o Sol. | N | [2.4](../../docs/secoes_capitulo.json) |

**E2.06**

$$\cos\theta_i=\cos\theta_z\cos\beta+\sin\theta_z\sin\beta\cos(\gamma_s-\gamma_a)$$

β inclinação; γs e γa azimutes solar e do arranjo; θi incidência.

**E2.07**

$$\ell=h/\tan\alpha_s$$

h altura; αs altura solar positiva; ℓ comprimento na unidade de h. Exemplo plano didático; não calcula o sombreamento real das fileiras sem suas dimensões.

## Subseção 3.1

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E3.01 | **Transposição para o plano do arranjo**. Combinar radiação direta difusa do céu e refletida pelo solo. | N | [transpose](../../src/projeto_fv.py) |
| E3.02 | **Resíduo de fechamento da POA**. Verificar o fechamento numérico da transposição inversa. | C | [reverse_components](../../src/projeto_fv.py) |

**E3.01**

$$G_{\mathrm{POA}}=DNI\max(\cos\theta_i,0)+G_{\mathrm{céu}}+G_{\mathrm{solo}}$$

Gcéu e Gsolo no plano; todos os termos em W/m². Cenários usam Perez–Driesse; a cadeia principal recebe POA medida diretamente.

**E3.02**

$$\varepsilon_{\mathrm{POA}}=G_{\mathrm{POA,recon}}-G_{\mathrm{POA,med}}$$

POA reconstruída e medida no mesmo intervalo; resíduo em W/m². O fechamento não constitui validação independente das componentes reconstruídas.

## Subseção 3.2

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E3.03 | **Temperatura operacional de Faiman**. Estimar a temperatura operacional a partir da irradiância e da meteorologia. | N | [simulate](../../src/projeto_fv.py) |

**E3.03**

$$T_{\mathrm{op}}=T_a+\frac{G_{\mathrm{ef}}}{U_0+U_1v}$$

Ta em °C; v em m/s; U0 e U1 coeficientes térmicos. Temperatura operacional usada como aproximação da célula; sem medição térmica independente.

## Subseção 3.3

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E3.04 | **Modelo de diodo único**. Relacionar corrente e tensão do módulo nas condições operacionais. | N | [module_mpp](../../src/projeto_fv.py) |
| E3.05 | **Potência elétrica**. Obter potência e construir curvas P–V e o ponto de máxima potência. | N | [module_curves](../../src/projeto_fv.py) |
| E3.06 | **Comparação CC com PVWatts**. Registrar a aproximação linear CC exportada como comparação auxiliar. | C | [simulate](../../src/projeto_fv.py) |

**E3.04**

$$I=I_L-I_0\left[\exp\left(\frac{V+IR_s}{a}\right)-1\right]-\frac{V+IR_s}{R_{sh}}$$

IL e I0 correntes; Rs e Rsh resistências; a fator em volts. Parâmetros corrigidos pelo modelo CEC; curvas calculadas não são varreduras experimentais.

**E3.05**

$$P=VI$$

V em V; I em A; P em W.

**E3.06**

$$P_{\mathrm{DC,PVW}}=P_{\mathrm{STC}}\frac{G_{\mathrm{ef}}}{1000}\left[1+\gamma(T_{\mathrm{op}}-25)\right]\prod_j(1-\ell_j)$$

Gef em W/m²; γ em °C⁻¹; PSTC potência total dos módulos em W. Comparação auxiliar; a previsão principal usa o modelo CEC de diodo único.

## Subseção 3.4

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E3.07 | **Tensão em série**. Calcular a tensão do equivalente de módulos em série. | N | [analytics](../../src/refinamento_fv.py) |
| E3.08 | **Corrente em paralelo**. Calcular a corrente do equivalente de strings em paralelo. | N | [analytics](../../src/refinamento_fv.py) |
| E3.09 | **Potência do arranjo ideal**. Escalar a potência do módulo para a associação ideal. | N | [analytics](../../src/refinamento_fv.py) |
| E3.10 | **Perdas CC multiplicativas**. Aplicar perdas assumidas de cabos mismatch e conexões. | N | [simulate](../../src/projeto_fv.py) |

**E3.07**

$$V_a=N_sV_m$$

Ns número em série; Vm tensão do módulo.

**E3.08**

$$I_a=N_pI_m$$

Np strings em paralelo; Im corrente do módulo.

**E3.09**

$$P_a=N_sN_pP_m$$

Pm potência do módulo; Pa em W. O exemplo 20 em série e 6 em paralelo não comprova o cabeamento real; a simulação total usa 2880 módulos.

**E3.10**

$$P_{\mathrm{DC}}=P_a\prod_j(1-\ell_j)$$

ℓj frações de perda; Pa potência bruta; PDC potência líquida.

## Subseção 3.5

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E3.11 | **Potência CA limitada**. Limitar a conversão pela capacidade CA assumida. | N | [inverter_pvwatts_stages](../../src/projeto_fv.py) |
| E3.12 | **Referência CC do inversor**. Converter a capacidade CA em potência CC de referência da curva. | N | [inverter_pvwatts_stages](../../src/projeto_fv.py) |
| E3.13 | **Carregamento relativo**. Definir a variável independente da curva de eficiência. | C | [inverter_pvwatts_stages](../../src/projeto_fv.py) |
| E3.14 | **Eficiência PVWatts**. Calcular a eficiência em função do carregamento do inversor. | C | [inverter_pvwatts_stages](../../src/projeto_fv.py) |
| E3.15 | **Potência antes do clipping**. Impor o piso físico não negativo antes da limitação superior. | C | [inverter_pvwatts_stages](../../src/projeto_fv.py) |
| E3.16 | **Potência suprimida pelo clipping**. Quantificar a parcela limitada pela capacidade do inversor. | C | [inverter_pvwatts_stages](../../src/projeto_fv.py) |
| E3.17 | **Potência CA final**. Aplicar a perda CA assumida após a conversão e o clipping. | C | [simulate](../../src/projeto_fv.py) |

**E3.11**

$$P_{\mathrm{AC}}=\min[\eta(P_{\mathrm{DC}})P_{\mathrm{DC}},P_{\mathrm{AC,max}}]$$

η eficiência; PACmax limite; potências em W. No código o piso zero é aplicado antes do limite superior; usar também E3.15.

**E3.12**

$$P_{\mathrm{dc0,inv}}=P_{\mathrm{AC,max}}/\eta_{\mathrm{nom}}$$

ηnom eficiência nominal; Pdc0 não é a potência STC dos módulos.

**E3.13**

$$\zeta=\frac{P_{\mathrm{DC}}}{P_{\mathrm{dc0,inv}}}$$

ζ adimensional; mesma unidade nas duas potências.

**E3.14**

$$\eta=\frac{\eta_{\mathrm{nom}}}{\eta_{\mathrm{ref}}}\left(-0.0162\zeta-\frac{0.0059}{\zeta}+0.9858\right)$$

ζ positivo; ηnom igual a 0,98; ηref igual a 0,9637. Em potência CC nula o código define saída CA nula sem avaliar a divisão por ζ.

**E3.15**

$$P_{\mathrm{pre}}=\max(\eta P_{\mathrm{DC}},0)$$

Ppre em W; PDC igual a zero produz Ppre igual a zero.

**E3.16**

$$P_{\mathrm{clip}}=P_{\mathrm{pre}}-P_{\mathrm{AC}}$$

Pclip em W; não confundir com energia perdida.

**E3.17**

$$P_{\mathrm{AC,final}}=(1-\ell_{\mathrm{AC}})P_{\mathrm{AC}}$$

ℓAC fração de perda; PACfinal em W.

## Subseção 3.6

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E3.18 | **Energia elétrica**. Integrar a potência média nos intervalos selecionados. | N | [daily_paired_energy](../../src/projeto_fv.py) |

**E3.18**

$$E=\sum_i P_i\Delta t_i$$

P em kW; Δt igual a 0,25 h; E em kWh. Se P estiver em W dividir por 1000. Energia pareada e energia integral do mês são totais diferentes e devem ser identificados.

## Subseção 4.1

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E4.01 | **Variação de energia entre estágios**. Quantificar a diferença calculada entre dois estágios consecutivos. | N | [performance](../../src/projeto_fv.py) |
| E4.02 | **Fechamento da cadeia de energia**. Conferir que a soma das variações recupera a diferença total. | N | [performance](../../src/projeto_fv.py) |
| E4.03 | **Potência linear de referência**. Definir a referência linear STC que inicia a cadeia energética. | C | [simulate](../../src/projeto_fv.py) |

**E4.01**

$$\Delta E_j=E_j-E_{j+1}$$

Ej energias na mesma máscara temporal em kWh.

**E4.02**

$$\sum_j\Delta E_j=E_1-E_{\mathrm{final}}$$

Mesmos estágios e intervalos; podem ocorrer ganhos sob frio. Decomposição do modelo não identifica automaticamente perdas reais ou suas causas.

**E4.03**

$$P_{\mathrm{lin}}=P_0\frac{G_{\mathrm{POA}}}{G_{\mathrm{ref}}}$$

P0 capacidade declarada; Gref igual a 1000 W/m²; potências na mesma unidade. Na cadeia principal P0 declarada é 893 kWp; não substituir pela soma CEC sem identificar a mudança.

## Subseção 4.2

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E4.04 | **Produtividade de referência**. Expressar o recurso como horas equivalentes no plano e período definidos. | N | [performance](../../src/projeto_fv.py) |
| E4.05 | **Produtividade do arranjo**. Normalizar a energia CC pela capacidade declarada. | N | [performance](../../src/projeto_fv.py) |
| E4.06 | **Produtividade final**. Normalizar a energia CA observada ou modelada pela capacidade. | N | [performance](../../src/projeto_fv.py) |

**E4.04**

$$Y_r=H_{\mathrm{POA}}/G_{\mathrm{ref}}$$

HPOA em kWh/m²; Gref igual a 1 kW/m²; Yr em h. HSP e PSH designam o mesmo conceito nesta janela; não são duração de brilho solar.

**E4.05**

$$Y_a=E_{\mathrm{DC}}/P_0$$

EDC em kWh; P0 em kWp; Ya em kWh/kWp ou horas equivalentes. A energia CC e Ya são modeladas neste estudo.

**E4.06**

$$Y_f=E_{\mathrm{AC}}/P_0$$

EAC em kWh; P0 em kWp; Yf em kWh/kWp.

## Subseção 4.3

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E4.07 | **Razão de desempenho**. Relacionar a produtividade final ao recurso da mesma janela. | N | [performance](../../src/projeto_fv.py) |
| E4.08 | **Perda de captura normalizada**. Comparar o recurso e a produtividade CC do modelo. | N | [performance](../../src/projeto_fv.py) |
| E4.09 | **Perda de sistema normalizada**. Comparar as produtividades CC e CA do modelo. | N | [performance](../../src/projeto_fv.py) |

**E4.07**

$$PR=Y_f/Y_r$$

PR adimensional; multiplicar por 100 quando apresentado em %.

**E4.08**

$$L_c=Y_r-Y_a$$

Lc em horas equivalentes.

**E4.09**

$$L_s=Y_a-Y_f$$

Ls em horas equivalentes.

## Subseção 4.4

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E4.10 | **Resíduo de potência**. Fixar o sinal do erro usado nas tabelas e gráficos. | C | [metrics](../../src/projeto_fv.py) |
| E4.11 | **Erro médio de viés**. Quantificar a tendência média de superestimação ou subestimação. | N | [metrics](../../src/projeto_fv.py) |
| E4.12 | **Erro absoluto médio**. Quantificar a magnitude média do erro sem cancelamento de sinais. | N | [metrics](../../src/projeto_fv.py) |
| E4.13 | **Raiz do erro quadrático médio**. Resumir a magnitude quadrática dos mesmos resíduos. | N | [metrics](../../src/projeto_fv.py) |
| E4.14 | **Viés normalizado**. Expressar o viés em relação à média observada dos pares. | C | [metrics](../../src/projeto_fv.py) |
| E4.15 | **Erro quadrático normalizado**. Expressar o RMSE em relação à média observada dos pares. | C | [metrics](../../src/projeto_fv.py) |
| E4.16 | **Correlação de Pearson**. Quantificar a associação linear entre observações e simulações. | C | [metrics](../../src/projeto_fv.py) |
| E4.17 | **Coeficiente de determinação**. Comparar o erro quadrático à dispersão das observações. | N | [metrics](../../src/projeto_fv.py) |
| E4.18 | **Fator empírico de abril**. Ajustar um fator multiplicativo secundário apenas com os pares de abril. | C | [run_models](../../src/projeto_fv.py) |
| E4.19 | **Potência com ajuste empírico**. Aplicar o fator de abril e reportar os resultados separadamente do modelo físico. | C | [run_models](../../src/projeto_fv.py) |

**E4.10**

$$e_i=p_i-y_i$$

pi potência simulada; yi observada; ambas em kW. Valores positivos indicam superestimação.

**E4.11**

$$MBE=\frac{1}{n}\sum_{i=1}^{n}e_i$$

n pares válidos; MBE em kW.

**E4.12**

$$MAE=\frac{1}{n}\sum_{i=1}^{n}|e_i|$$

MAE em kW.

**E4.13**

$$RMSE=\sqrt{\frac{1}{n}\sum_{i=1}^{n}e_i^2}$$

RMSE em kW.

**E4.14**

$$nMBE=100\frac{MBE}{\bar y}$$

nMBE em %; média observada não nula.

**E4.15**

$$nRMSE=100\frac{RMSE}{\bar y}$$

nRMSE em %; não usar potência nominal como denominador neste projeto.

**E4.16**

$$r=\frac{\sum_i(y_i-\bar y)(p_i-\bar p)}{\sqrt{\sum_i(y_i-\bar y)^2\sum_i(p_i-\bar p)^2}}$$

r adimensional; requer variância positiva nas duas séries. Correlação elevada não prova exatidão.

**E4.17**

$$R^2=1-\frac{\sum e_i^2}{\sum(y_i-\bar y)^2}$$

R² adimensional; denominador positivo. O projeto calcula 1 menos SSE/SST; não substitui R² pelo quadrado de r.

**E4.18**

$$k=\frac{\sum_{i\in\mathrm{abril}}p_i y_i}{\sum_{i\in\mathrm{abril}}p_i^2}$$

k adimensional; pi e yi na mesma unidade. Ajuste sem intercepto; maio é verificação e junho avaliação temporal separada.

**E4.19**

$$p_i^{\mathrm{emp}}=k p_i$$

Potências na mesma unidade; k fixado no mês de ajuste.

## Subseção 4.5

| ID | Equação e função | Origem | Local verificável |
| --- | --- | --- | --- |
| E4.20 | **Absortância solar**. Fechar a partição óptica do exemplo semitransparente. | C | [bipv_scenario](../../src/projeto_fv.py) |
| E4.21 | **Potência solar incidente**. Converter a irradiância do plano em potência incidente na área. | C | [bipv_scenario](../../src/projeto_fv.py) |
| E4.22 | **Potência solar refletida**. Quantificar a fração refletida da potência incidente. | C | [bipv_scenario](../../src/projeto_fv.py) |
| E4.23 | **Potência solar transmitida**. Quantificar a parcela solar que atravessa o elemento. | C | [bipv_scenario](../../src/projeto_fv.py) |
| E4.24 | **Eficiência elétrica do exemplo BIPV**. Corrigir a eficiência assumida pela temperatura e limitar a conversão à absorção. | C | [bipv_scenario](../../src/projeto_fv.py) |
| E4.25 | **Potência elétrica do elemento BIPV**. Separar a parcela convertida em eletricidade no balanço solar. | N | [bipv_scenario](../../src/projeto_fv.py) |
| E4.26 | **Calor absorvido após conversão elétrica**. Calcular a parcela absorvida que permanece térmica. | N | [bipv_scenario](../../src/projeto_fv.py) |
| E4.27 | **Calor absorvido dirigido ao exterior**. Separar a fração do calor absorvido dirigida ao exterior. | C | [bipv_scenario](../../src/projeto_fv.py) |
| E4.28 | **Ganho solar para o interior**. Somar transmissão solar e fração térmica dirigida ao interior. | N | [bipv_scenario](../../src/projeto_fv.py) |
| E4.29 | **SHGC equivalente simplificado**. Normalizar o ganho solar interior pela potência incidente. | N | [bipv_scenario](../../src/projeto_fv.py) |
| E4.30 | **Conservação do balanço solar**. Conferir a conservação das parcelas ópticas elétricas e térmicas. | C | [bipv_scenario](../../src/projeto_fv.py) |

**E4.20**

$$\alpha=1-\rho_s-\tau_s$$

α absortância; ρs refletância; τs transmitância solar; frações. As propriedades são hipóteses do exemplo de 100 m² e não do módulo real.

**E4.21**

$$P_{\mathrm{inc}}=GA$$

G em W/m²; A em m²; Pinc em W.

**E4.22**

$$P_{\mathrm{ref}}=\rho_s GA$$

Pref em W.

**E4.23**

$$P_{\mathrm{trans}}=\tau_s GA$$

Ptrans em W; τs solar difere da transmitância visível.

**E4.24**

$$\eta=\min\{\max[\eta_{\mathrm{ref}}(1+\gamma(T_{\mathrm{op}}-25)),0],\alpha\}$$

ηref eficiência a 25 °C; γ em °C⁻¹. Esta aproximação pertence ao balanço semitransparente; os cenários de produtividade usam a cadeia CEC.

**E4.25**

$$P_e=\eta GA$$

η eficiência instantânea; Pe em W.

**E4.26**

$$Q_{\mathrm{abs}}=(\alpha-\eta)GA$$

Qabs representa potência térmica em W apesar do símbolo Q.

**E4.27**

$$Q_{\mathrm{out}}=(1-f_{\mathrm{in}})Q_{\mathrm{abs}}$$

fin fração dirigida ao interior entre 0 e 1; Qout em W.

**E4.28**

$$Q_{\mathrm{in}}=\tau_sGA+f_{\mathrm{in}}Q_{\mathrm{abs}}$$

Qin é potência em W; fin fração térmica interior. Balanço solar simplificado; não inclui todas as trocas térmicas do edifício.

**E4.29**

$$SHGC_{\mathrm{eq}}=\tau_s+f_{\mathrm{in}}(\alpha-\eta)$$

SHGCeq adimensional; não equivale a certificação de produto.

**E4.30**

$$P_{\mathrm{inc}}=P_{\mathrm{ref}}+P_{\mathrm{trans}}+P_e+f_{\mathrm{in}}Q_{\mathrm{abs}}+Q_{\mathrm{out}}$$

Todos os termos em W; o código testa o resíduo de fechamento.

## Referências metodológicas

[Fontes R do projeto](../../references/Referencias_do_Projeto.md). O código e o notebook permitem localizar cada relação; as fontes metodológicas devem ser citadas na redação final.
