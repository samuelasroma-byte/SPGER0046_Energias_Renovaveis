# Matriz de cobertura do capítulo

Versão 1.2.2. As 19 subseções estão mapeadas. Cobertura teórica ou execução de um cenário não equivale à validação independente da etapa.

## 1.1 Geometria solar e irradiância extraterrestre

**Responsável:** Samuel

**Entradas:** Latitude, longitude, altitude e horário dos intervalos.

**Método:** Calcular a posição solar com SPA e a irradiância extraterrestre com Spencer. O azimute é contado a partir do norte no sentido horário.

**Saídas:** Geometria solar e quadro de convenções.

**Evidência:** Cálculo físico com coordenadas documentadas

**Limite:** Não há observação independente de ângulo solar; a geometria pode ser calculada.

**Figuras disponíveis:** G01_recurso_geometria; F01_plano_angulos

**Situação de execução:** calculado e exportado

**Referências:** R03, R04, R05.

## 1.2 Grandezas radiométricas e componentes da radiação

**Responsável:** Samuel

**Entradas:** POA local medida; componentes reconstruídas quando a inversão estiver ativa.

**Método:** Irradiância é potência por área; irradiação é sua integral no tempo. GHI é horizontal, DNI é normal aos raios solares e DHI é difusa horizontal. POA se refere ao plano do arranjo.

**Saídas:** Quadro das grandezas e componentes estimadas.

**Evidência:** Medição POA e estimativa exploratória das componentes

**Limite:** Sem GHI/DNI/DHI locais medidos; reconstrução não equivale a observação.

**Figuras disponíveis:** F02_componentes_POA; G23_componentes_estimadas

**Situação de execução:** calculado e exportado

**Referências:** R01, R14, R18, R29.

## 1.3 Modulação atmosférica e variabilidade espaço-temporal

**Responsável:** Samuel

**Entradas:** Série de POA, intervalo de integração e critérios de cobertura.

**Método:** Nuvens, aerossóis e vapor d’água modificam o recurso solar. A série permite descrever a variabilidade intradiária e entre dias; a seleção dos dias ilustrativos usa apenas POA e cobertura.

**Saídas:** Critério dos dias ilustrativos e irradiação pareada.

**Evidência:** Descrição observacional de variabilidade

**Limite:** Não se atribuem causas atmosféricas isoladas nem climatologia anual a um trimestre.

**Figuras disponíveis:** G02_variabilidade_recurso

**Situação de execução:** calculado e exportado

**Referências:** R01, R25.

## 1.4 Medição e estimativa do recurso solar

**Responsável:** Samuel

**Entradas:** Arquivos PVDAQ, metadados, canais medidos e resoluções de 5/15 minutos.

**Método:** Inspecionar integridade, unidades, lacunas, simultaneidade e limites físicos. Medições de superfície, satélites, reanálises e atlas têm representatividades diferentes; os produtos em grade são contextualizados, sem uso na cadeia principal.

**Saídas:** Situação dos dados, proveniência e cobertura.

**Evidência:** Auditoria de disponibilidade e documentação

**Limite:** Disponibilidade elevada não certifica sensores. Altura do anemômetro e alguns metadados permanecem incompletos.

**Figuras disponíveis:** FL01_fluxo_projeto; G19_consistencia_medicoes

**Situação de execução:** calculado e exportado

**Referências:** R01, R02, R21, R22, R23, R25, R26.

## 2.1 Condições térmicas

**Responsável:** Vannessa e Thais

**Entradas:** Temperatura do ar e vento locais; POA medida.

**Método:** Temperatura ambiente, vento e trocas de calor condicionam a operação do módulo. As distribuições observadas e o cenário de menor ventilação ilustram a passagem do ambiente à modelagem térmica da seção 3.2.

**Saídas:** Estatística ambiental e sensibilidade de ventilação.

**Evidência:** Medições ambientais e temperatura estimada

**Limite:** U₀ e U₁ genéricos; T operacional é aproximação de célula, sem validação térmica independente.

**Figuras disponíveis:** G03_condicoes_ambientais; G04_temperatura_estimada

**Situação de execução:** calculado e exportado

**Referências:** R07.

## 2.2 Albedo e ambiente radiativo da superfície

**Responsável:** Vannessa e Thais

**Entradas:** Albedo assumido e componentes estimadas da inversão.

**Método:** O albedo expressa refletância do entorno. No exercício de transposição, varia-se 0,10/0,20/0,40 mantendo as componentes reconstruídas na referência 0,20. O arranjo real é monofacial; bifacialidade exige caracterização traseira adicional.

**Saídas:** Sensibilidade de albedo e quadro de hipóteses.

**Evidência:** Cenário de sensibilidade

**Limite:** Expressão isotrópica para reflexão do solo. Não há albedo medido; a leitura POA principal não recebe uma segunda contribuição refletida.

**Figuras disponíveis:** G22_albedo; F02_componentes_POA

**Situação de execução:** calculado e exportado

**Referências:** R06, R14, R29.

## 2.3 Sombreamento, sujidade e obstruções locais

**Responsável:** Vannessa e Thais

**Entradas:** Cenários de atenuação adicional de 0%, 2% e 5%; alertas operacionais.

**Método:** A sujeira pode atenuar a luz incidente e diferir entre módulos e sensor POA. Os cenários são hipóteses de atenuação adicional à leitura. Sombreamento parcial pode envolver mismatch e diodos de bypass, que um redutor uniforme não reproduz.

**Saídas:** Sensibilidade e alertas sem atribuição causal automática.

**Evidência:** Sensibilidade hipotética e fundamentos

**Limite:** Sem histórico de limpeza e mapa de sombras; o resíduo não identifica a perda real de sujidade ou sombra.

**Figuras disponíveis:** G20_sujidade_ventilacao

**Situação de execução:** calculado e exportado

**Referências:** R28, R25.

## 2.4 Geometria de instalação e exposição do arranjo fotovoltaico

**Responsável:** Vannessa e Thais

**Entradas:** Inclinação de 25° e azimute de 180° documentados; fachadas hipotéticas.

**Método:** A instalação define exposição e incidência. A inclinação é medida em relação à horizontal. Espaçamento entre fileiras e exposição traseira precisam de geometria adicional; em um exemplo de sombra coplanar, uma altura h gera projeção horizontal h/tan(altura solar).

**Saídas:** Convenções geométricas e limite de dados de espaçamento.

**Evidência:** Geometria documentada e extensão didática

**Limite:** A expressão de projeção é um exemplo plano sem dimensão de fileira real; não calcula o sombreamento específico da usina.

**Figuras disponíveis:** F01_plano_angulos; F04_geometrias_BIPV

**Situação de execução:** calculado e exportado

**Referências:** R03, R09, R29.

## 3.1 Transposição para o plano do arranjo

**Responsável:** Gabriela e Giulia

**Entradas:** Componentes reconstruídas, posição solar e geometria.

**Método:** A cadeia usual transpõe GHI/DNI/DHI para POA. Como a instalação já mede POA, o modelo principal começa dessa observação. A inversão opcional usa Driesse 2024, Erbs–Driesse e Perez–Driesse para exercícios de orientação/albedo.

**Saídas:** Diagnóstico horário da inversão e critérios de exclusão.

**Evidência:** Medição direta e inversão exploratória

**Limite:** Há possibilidade de soluções não únicas; o fechamento de POA é teste numérico, sem validação independente das componentes.

**Figuras disponíveis:** G23_componentes_estimadas

**Situação de execução:** calculado e exportado

**Referências:** R06, R14, R15, R16, R18.

## 3.2 Modelagem da temperatura operacional

**Responsável:** Gabriela e Giulia

**Entradas:** POA, temperatura do ar, vento e coeficientes Faiman.

**Método:** A temperatura estimada entra no modelo elétrico. U₀=25 W/(m² K) e U₁=6,84 W s/(m³ K) são parâmetros genéricos de referência; a sensibilidade de ventilação usa 15 e 3, respectivamente.

**Saídas:** Temperatura estimada e registro dos coeficientes.

**Evidência:** Modelo térmico

**Limite:** Ausência de temperatura de módulo/célula e altura de vento suficientemente documentada.

**Figuras disponíveis:** G04_temperatura_estimada

**Situação de execução:** calculado e exportado

**Referências:** R07.

## 3.3 Modelagem elétrica do módulo fotovoltaico

**Responsável:** Gabriela e Giulia

**Entradas:** Parâmetros CEC, irradiância efetiva e temperatura estimada.

**Método:** O modelo de diodo único fornece curvas I–V, P–V e o ponto de máxima potência. Compare irradiâncias a 25 °C e temperaturas a 1.000 W/m². Registre divergências de classificação e parâmetros entre CEC e metadados.

**Saídas:** Curvas calculadas e identificação de MPP.

**Evidência:** Modelo elétrico e curvas calculadas

**Limite:** Sem varreduras I–V experimentais da instalação; as curvas não constituem validação do módulo.

**Figuras disponíveis:** G05_curvas_irradiancia; G06_curvas_temperatura

**Situação de execução:** calculado e exportado

**Referências:** R08, R09, R10.

## 3.4 Modelagem do arranjo fotovoltaico em corrente contínua (CC)

**Responsável:** Gabriela e Giulia

**Entradas:** MPP do módulo, 2.880 módulos, 24 grupos/inversores e perdas DC assumidas.

**Método:** Em uma associação ideal, as tensões somam em série e as correntes em paralelo. O exemplo 20 módulos × 6 strings por grupo corresponde a 120 módulos, mas não confirma o cabeamento real ou a ligação aos MPPTs.

**Saídas:** Tensão, corrente e potência do equivalente em CSV.

**Evidência:** Modelo agregado e equivalente didático

**Limite:** Strings/MPPTs reais incompletos; V×I disponível não foi adotado como potência DC observada certificada.

**Figuras disponíveis:** F03_arranjo_eletrico

**Situação de execução:** calculado e exportado

**Referências:** R08, R10, R13.

## 3.5 Conversão de CC para corrente alternada (CA) e modelagem do inversor

**Responsável:** Gabriela e Giulia

**Entradas:** Potência DC calculada, eficiência e limites assumidos do inversor.

**Método:** A curva PVWatts estima conversão e clipping. O limite de referência é 30 kW por inversor; 27,6 kW permanece como sensibilidade documentada. Verificar a faixa real de MPPT exige topologia e configuração de campo adicionais.

**Saídas:** Curva de eficiência, clipping calculado e sensibilidade AC.

**Evidência:** Modelo de conversão e sensibilidade

**Limite:** A simulação agregada não verifica todas as restrições reais de tensão/MPPT nem confirma o limite instalado.

**Figuras disponíveis:** G07_inversor

**Situação de execução:** calculado e exportado

**Referências:** R11, R13.

## 3.6 Integração temporal e estimativa de energia

**Responsável:** Gabriela e Giulia

**Entradas:** Potência média em intervalos de 15 minutos e máscaras temporais.

**Método:** Integre potência média por duração de cada intervalo. Compare séries e energias nas mesmas janelas. Apresente energia mensal e trimestral observada completa separadamente dos intervalos diurnos pareados.

**Saídas:** Energia diária/mensal, cobertura e totais integrais separados.

**Evidência:** Integração calculada e geração observada

**Limite:** O recorte é trimestral, não uma medição anual; energia pareada não equivale ao total integral do dia.

**Figuras disponíveis:** G08_series_potencia; G09_energia_diaria; G10_energia_mensal

**Situação de execução:** calculado e exportado

**Referências:** R12.

## 4.1 Balanço energético e cadeia de perdas

**Responsável:** Júlia Ribeiro

**Entradas:** Estágios do modelo e alertas de potência sob irradiância elevada.

**Método:** Integre a cadeia óptica, térmica, elétrica DC, conversão e limite AC. A diferença entre estágios pertence ao modelo; um desvio do medidor pode envolver fenômenos e incertezas não identificados.

**Saídas:** Energia por estágio e alertas operacionais.

**Evidência:** Decomposição calculada

**Limite:** Não se identificam perdas ópticas/operacionais reais isoladas sem medições adicionais; ganhos sob frio podem ocorrer.

**Figuras disponíveis:** G11_cadeia_energetica

**Situação de execução:** calculado e exportado

**Referências:** R08, R11, R12, R25.

## 4.2 Produtividades de referência, do arranjo e final

**Responsável:** Lucas Simão

**Entradas:** Irradiação POA, energia DC/AC e potência declarada de 893 kWp.

**Método:** Yr é o recurso em horas equivalentes; Ya representa a energia DC por capacidade; Yf representa energia AC por capacidade. HSP/PSH corresponde ao mesmo conceito de recurso quando plano e janela são os mesmos.

**Saídas:** Yr, Ya, Yf e HSP na janela definida.

**Evidência:** Indicadores sobre observações e modelo

**Limite:** Ya é modelada; HSP da janela pareada não é duração de brilho solar nem total integral diário.

**Figuras disponíveis:** G12_produtividades_PR; G21_HSP_POA_pareada

**Situação de execução:** calculado e exportado

**Referências:** R12, R30.

## 4.3 Razão de desempenho (Performance Ratio

**Responsável:** Lucas Simão

**Entradas:** Produtividades calculadas na mesma máscara temporal.

**Método:** Compare PR observado e modelado com irradiação e energia da mesma janela. Lc e Ls decompõem o modelo em perdas de captura e sistema. Informe a normalização e o papel da potência declarada.

**Saídas:** PR, Lc, Ls e janela de integração.

**Evidência:** PR observado pareado e perdas calculadas

**Limite:** Não combinar energia integral do trimestre com POA parcial; perdas calculadas não são identificação experimental de cada causa.

**Figuras disponíveis:** G12_produtividades_PR

**Situação de execução:** calculado e exportado

**Referências:** R12, R30.

## 4.4 Validação de modelos de geração fotovoltaica

**Responsável:** Lucas Simão

**Entradas:** Mesmos pares de potência AC medida e simulada.

**Método:** Avalie viés, magnitude do erro, correlação e determinação. Erro=simulado−observado. MBE, MAE e RMSE são em kW; nMBE/nRMSE são divididos pela média observada dos respectivos pares. O modelo físico é separado do fator empírico ajustado somente em abril.

**Saídas:** Métricas gerais, por mês/hora/POA, resíduos e consistência de medidores.

**Evidência:** Comparação observacional da saída AC

**Limite:** Junho é teste temporal separado, não instalação independente. Correlação elevada não prova exatidão; nenhum limiar universal de aceitação foi adotado.

**Figuras disponíveis:** G13_validacao; G14_residuos_temporais; G15_residuos_potencia; G16_distribuicao_residuos; G17_metricas_mensais; G18_vies_horario; G19_consistencia_medicoes

**Situação de execução:** calculado e exportado

**Referências:** R27, R25.

## 4.5 Avaliação de desempenho de sistemas fotovoltaicos integrados à edificação (BIPV)

**Responsável:** Júlia Ribeiro

**Entradas:** Componentes reconstruídas, meteorologia local e coeficientes BIPV assumidos.

**Método:** Explore fachadas sul/leste/oeste e menor ventilação. O exemplo separado de 100 m² semitransparentes usa transmissão solar 0,25, reflexão 0,12, absorção 0,63 e transmissão visível 0,35. As propriedades não caracterizam o módulo real.

**Saídas:** Produtividade/PR de cenários e conservação da partição solar.

**Evidência:** Cenário geométrico e balanço hipotético

**Limite:** Somente horas elegíveis da inversão; sem fachada medida, SHGC certificado, cálculo de lux ou balanço térmico completo do edifício.

**Figuras disponíveis:** G24_BIPV_orientacoes; G25_BIPV_balanco; F04_geometrias_BIPV

**Situação de execução:** calculado e exportado

**Referências:** R14, R19, R20.

