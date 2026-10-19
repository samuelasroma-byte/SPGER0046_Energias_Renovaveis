# Dados preparados para o cálculo

As quatro famílias abaixo provêm da mesma execução e compartilham índices de 15 minutos em UTC. Cada arquivo contém 8.736 intervalos do trimestre, inclusive registros sem par e valores ausentes. O filtro de comparação é explicitado nas colunas booleanas; não se apagam as lacunas.

| Família | Arquivo | Papel |
| --- | --- | --- |
| Meteorologia | [meteorologia_15min.csv](meteorologia/meteorologia_15min.csv) | Temperatura °C, vento m/s e direção em graus. |
| Irradiância | [poa_15min.csv](irradiancia/poa_15min.csv) | POA em W/m² e flag das três amostras originais de 5 min. |
| Elétrica observada | [potencias_15min.csv](eletrica_observada/potencias_15min.csv) | Medidor e soma dos inversores em W; V×I é derivado, não um canal de potência CC independente. |
| Base do modelo | [entradas_e_mascaras_15min.csv](base_modelagem/entradas_e_mascaras_15min.csv) | Entradas físicas e máscaras; a geração observada fica na família elétrica. |

Usar paired_daylight para a comparação observacional. Há 4.401 pares entre 4.421 intervalos diurnos elegíveis. As observações elétricas referenciam a validação; não são usadas na previsão física. Informações do trimestre e da execução estão em [ultima_execucao.json](../../outputs/logs/ultima_execucao.json).
