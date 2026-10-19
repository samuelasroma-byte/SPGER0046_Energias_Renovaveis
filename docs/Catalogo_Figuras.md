# Catálogo explicado das figuras

Observações principais: abril a junho de 2024. Exemplos diários e curvas calculadas têm seu escopo na legenda. Fonte padrão: elaboração da equipe a partir de dados do PVDAQ, sistema 2107 (2026); 2026 é o ano da elaboração.

## G01_recurso_geometria

**Recurso solar medido e geometria calculada**

Subseções: 1.1; 1.2. Natureza: medição e modelo identificados.

Dia 2024-05-17, selecionado pela menor variação relativa da POA entre dias com cobertura ≥99%. Ângulos calculados no meio dos intervalos; POA medida.

## G02_variabilidade_recurso

**Variabilidade diária do recurso solar**

Subseções: 1.3. Natureza: medição e modelo identificados.

Integração somente nos intervalos diurnos pareados. Oscilações não identificam isoladamente nuvens, aerossóis ou vapor d’água.

## G03_condicoes_ambientais

**Distribuições das condições ambientais**

Subseções: 2.1. Natureza: medição e modelo identificados.

Temperatura do ar e vento medidos; mesma janela diurna pareada da avaliação elétrica. Sem interpolação.

## G04_temperatura_estimada

**Resposta térmica estimada pelo modelo**

Subseções: 2.1; 3.2. Natureza: medição e modelo identificados.

Elevação térmica por Faiman com U₀=25 W/(m² K) e U₁=6,84 W s/(m³ K). Temperatura operacional usada como aproximação da célula; sem medição térmica independente.

## G05_curvas_irradiancia

**Curvas elétricas para diferentes irradiâncias**

Subseções: 3.3. Natureza: curvas calculadas.

Temperatura fixa de 25 °C; modelo de diodo único com parâmetros CEC do módulo. Círculos indicam MPP. Curvas calculadas, não ensaios I–V da instalação.

## G06_curvas_temperatura

**Curvas elétricas para diferentes temperaturas**

Subseções: 3.3. Natureza: curvas calculadas.

Irradiância fixa de 1.000 W/m²; modelo de diodo único com parâmetros CEC do módulo. Círculos indicam MPP. Curvas calculadas, não ensaios I–V da instalação.

## G07_inversor

**Eficiência e limitação de potência do inversor**

Subseções: 3.5. Natureza: modelo de inversor e limite assumido.

Curva PVWatts com limite assumido de 30 kW por inversor e η nominal de 98%. O valor de pdc0 do inversor é Paco/ηnom; não é a potência STC do arranjo. Configuração real do limite AC ainda não comprovada.

## G08_series_potencia

**Potência em dias de menor e maior variabilidade**

Subseções: 3.6; 4.4. Natureza: medição e modelo identificados.

Dias 2024-05-17 e 2024-05-04. Seleção pelo passo absoluto médio da POA dividido por sua média, com cobertura ≥99%; sem seleção pelo erro do modelo. Mesmos intervalos medidos/simulados.

## G09_energia_diaria

**Energia diária em intervalos pareados**

Subseções: 3.6; 4.4. Natureza: medição e modelo identificados.

Soma de potência média × 0,25 h sobre intervalos com os mesmos dados disponíveis. Não é a energia observada do dia inteiro.

## G10_energia_mensal

**Energia mensal na janela de comparação**

Subseções: 3.6. Natureza: medição e modelo identificados.

Energia simulada e observada calculadas sobre a mesma máscara diurna pareada. Totais integrais medidos do mês são fornecidos separadamente nas tabelas.

## G11_cadeia_energetica

**Cadeia de energia calculada**

Subseções: 4.1. Natureza: medição e modelo identificados.

Estágios integrados na mesma janela. Diferenças são decomposição do modelo, não identificação independente das perdas reais. Ganhos relativos sob frio não são forçados a perdas positivas.

## G12_produtividades_PR

**Produtividades e razão de desempenho**

Subseções: 4.2; 4.3. Natureza: medição e modelo identificados.

Normalização por 893 kWp declarados. Yr, Ya e Yf estão na mesma janela pareada; Ya é modelada. Numericamente, kWh/kWp corresponde a horas equivalentes. PR observado não representa automaticamente todo o trimestre.

## G13_validacao

**Comparação entre potência simulada e medida**

Subseções: 4.4. Natureza: medição e modelo identificados.

Modelo físico original, sem ajuste empírico; 4.401 pares diurnos. R²=1−SSE/SST e r calculado separadamente. nRMSE normalizado pela média observada dos pares.

## G14_residuos_temporais

**Resíduos ao longo do trimestre**

Subseções: 4.4. Natureza: medição e modelo identificados.

Resíduo = potência simulada − medida, sobre os pares diurnos. Valores positivos representam superestimação. Nenhum ponto foi removido pelo tamanho do erro.

## G15_residuos_potencia

**Resíduos em função da potência observada**

Subseções: 4.4. Natureza: medição e modelo identificados.

Diagnóstico de dependência do erro com o nível de potência; não identifica isoladamente causas operacionais, ópticas ou térmicas.

## G16_distribuicao_residuos

**Distribuição dos resíduos**

Subseções: 4.4. Natureza: medição e modelo identificados.

Histograma dos mesmos 4.401 resíduos. MBE mantém o sinal; MAE e RMSE resumem magnitudes diferentes do erro e são apresentados em tabela.

## G17_metricas_mensais

**Erros mensais do modelo físico**

Subseções: 4.4. Natureza: medição e modelo identificados.

Mesma definição de erro; normalização pela média observada de cada mês. n e cobertura estão nas tabelas. Modelos com ajuste empírico são relatados separadamente.

## G18_vies_horario

**Viés por hora local e tamanho da amostra**

Subseções: 4.4. Natureza: medição e modelo identificados.

Médias condicionadas à janela diurna selecionada; cada faixa tem n e cobertura próprios. O padrão horário não prova uma causa única.

## G19_consistencia_medicoes

**Consistência entre referências elétricas**

Subseções: 1.4; 4.4. Natureza: medição e modelo identificados.

Comparação entre dois registros observacionais locais; não é previsão do modelo. Divergências entre medidor e inversores integram os limites da referência.

## G20_sujidade_ventilacao

**Sensibilidade à sujidade e à ventilação**

Subseções: 2.1; 2.3. Natureza: cenários hipotéticos.

Cenários, não perdas medidas. Sujidade representa atenuação adicional do módulo em relação à leitura POA; considerar a condição do sensor evita dupla contagem. Ventilação reduzida usa U₀=15 e U₁=3.

## G21_HSP_POA_pareada

**Horas equivalentes de sol na janela pareada**

Subseções: 4.2. Natureza: medição e modelo identificados.

HSP/PSH=H_POA/(1 kW/m²), correspondente a Yr na janela. Não é duração medida de brilho solar nem HSP integral do dia. A cobertura diária está no CSV.

## G22_albedo

**Sensibilidade ao albedo assumido**

Subseções: 2.2; 3.1. Natureza: componentes estimadas e hipótese de albedo.

Transposição das mesmas componentes reconstruídas com albedo-base 0,20. A variação isola o parâmetro da transposição e não valida albedo. Apenas 1.037 horas elegíveis; não é trimestre integral. A POA medida da cadeia principal não recebe reflexão novamente.

## G23_componentes_estimadas

**Componentes reconstruídas da POA**

Subseções: 1.2; 3.1. Natureza: estimativa exploratória.

Exemplo de 2024-05-17, em horas elegíveis. Driesse 2024 e Erbs–Driesse; não são três sensores independentes. O fechamento pelo modelo não prova exatidão das componentes.

## G24_BIPV_orientacoes

**Cenários de orientação e integração**

Subseções: 2.4; 4.5. Natureza: cenários BIPV, 1.037 horas elegíveis.

Mesmo recorte de componentes estimadas, meteorologia e capacidade de normalização. Cenários verticais incluem menor ventilação; portanto a comparação combina orientação e condição térmica. Sem medições de fachada.

## G25_BIPV_balanco

**Partição solar do exemplo semitransparente**

Subseções: 4.5. Natureza: balanço solar hipotético.

Área hipotética de 100 m²; ρsolar=0,12, τsolar=0,25, α=0,63, eficiência de referência=0,10. Soma das cinco parcelas igual à energia incidente. SHGC equivalente simplificado, sem certificação.

## FL01_fluxo_projeto

**Fluxo do estudo com medições locais**

Subseções: 1.4; 3.1; 4.4; 4.5. Natureza: esquema do método.

As observações AC são referência para comparação, não entrada da previsão física. Controle de qualidade e pareamento precedem a análise. Setas tracejadas identificam a extensão exploratória.

## F01_plano_angulos

**Plano do arranjo e convenções angulares**

Subseções: 1.1; 2.4; 3.1. Natureza: geometria documentada e exemplo solar hipotético.

Corte coplanar didático: β=25° documentado; θz=55° e θi=30° são valores ilustrativos coerentes nesse corte. Abaixo, azimute medido a partir do norte no sentido horário; arranjo orientado ao sul. Não é um levantamento tridimensional da usina.

## F02_componentes_POA

**Componentes incidentes no plano do módulo**

Subseções: 1.2; 2.2; 3.1. Natureza: esquema radiativo.

Representação esquemática das contribuições à POA. Não atribui medições locais de GHI/DNI/DHI nem albedo. O sensor POA da cadeia principal já recebe a contribuição refletida do entorno.

## F03_arranjo_eletrico

**Organização elétrica do sistema de referência**

Subseções: 3.3; 3.4; 3.5. Natureza: metadados e associação equivalente hipotética.

Número de módulos, inversores e módulos por grupo documentados. Associação 20 em série por 6 strings é um equivalente didático de 120 módulos, não confirmação da fiação/MPPT real. Tensões e correntes desse equivalente são calculadas em CSV.

## F04_geometrias_BIPV

**Arranjo inclinado e extensão de fachada**

Subseções: 2.4; 4.5. Natureza: esquema BIPV hipotético.

Comparação geométrica didática. A fachada e suas propriedades semitransparentes são hipotéticas. O painel inclinado corresponde à referência geométrica; não existe fachada BIPV monitorada nos dados.

