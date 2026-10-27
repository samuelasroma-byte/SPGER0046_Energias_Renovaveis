# ROTEIRO ORAL DA SUBSEÇÃO 1.1

Samuel Constantino Teixeira — apresentação preliminar de 29/10/2026

Os seis quadros correspondem aos slides físicos 5 a 10 do arquivo coletivo, com numeração visível 4 a 9. O tempo individual não foi fixado no planejamento; este roteiro organiza a fala sem presumir uma duração autorizada.

## QUADRO 1 — 1.1 · GEOMETRIA SOLAR

Definir a direção solar sem confundir direção com fluxo medido. O esquema é didático e não representa uma observação. θz é contado da vertical e αs da horizontal. A vista em planta define o azimute horário desde o norte. O livro Duffie usa outra origem azimutal; a convenção adotada aqui é a do SPA, também descrita no handbook. No zênite o azimute é indefinido. Fontes verificadas: B12 p. 13/PDF31; A045 cap. 2-8/PDF37.

Fontes: Duffie, Beckman e Blair (2020), p. 13; Sengupta et al. (2024), cap. 2, p. 8.

## QUADRO 2 — 1.1 · RELAÇÃO DO ÂNGULO ZENITAL

A equação relaciona latitude, declinação e ângulo horário e expressa a trigonometria esférica. ω=0 no meio-dia solar, que não coincide necessariamente com 12h civis. A notação t_sol está em horas de tempo solar verdadeiro; ω=15°(t_sol/1h−12). Não misturar graus e radianos em sin/cos. Esta equação elementar não inclui refração; no SPA zenith e apparent_zenith são saídas distintas. Fontes: B12 pp.13–15/PDF31–33; B32 pp.10–11/PDF16–17.

Fontes: Duffie, Beckman e Blair (2020), p. 13–15; Reda e Andreas (2008), p. 10–11.

## QUADRO 3 — 1.1 · IRRADIÂNCIA EXTRATERRESTRE

O inverso do quadrado relaciona a irradiância normal à distância Terra–Sol. Spencer aproxima o fator orbital E0; não calcula nuvens, absorção nem radiação difusa. Aqui Gsc=1366,1 W/m² é uma constante de compatibilidade da implementação, não uma nova determinação metrológica da constante solar. O coeficiente de cos(2B) é 0,000719 conforme código conferido do pvlib 0.16.1; o exemplar B12 apresenta 0,00719 na equação 1.4.1b, divergência registrada na conferência. A projeção usa o zenital geométrico e é anulada com o Sol abaixo do horizonte. O ano 2024 é bissexto, mas o denominador 365 é mantido para reproduzir o método do projeto.

Fontes: Duffie, Beckman e Blair (2020), p. 9; pvlib 0.16.1, get_extra_radiation.

## QUADRO 4 — 1.1 · IMPLEMENTAÇÃO COMPUTACIONAL

Mostrar as duas ramificações: localização e instante alimentam o SPA; o dia do ano alimenta Spencer; zenital e G0n entram na projeção. Não há dependência conceitual de Spencer em relação ao SPA. POA representa médias de 15 minutos, rotuladas pelo início; os ângulos são calculados 7min30s depois. A pressão é estimada da altitude de 10 m; temperatura de refração 12°C e ΔT=67s são padrões de compatibilidade mantidos do projeto. São parâmetros do cálculo, não medições atmosféricas. A comparação com o exemplo publicado do SPA verifica a implementação, e não valida os sensores do PVDAQ.

Fontes: configuração do projeto PVDAQ 2107; Reda e Andreas (2008); pvlib 0.16.1.

## QUADRO 5 — 1.1 · PVDAQ 2107 EM 17/05/2024

A POA é observacional; os ângulos são calculados. A janela do gráfico é 05h–21h locais; o CSV preserva as 96 posições do dia. Há 94 médias POA não ausentes e 68 intervalos com três amostras originais. Não preencher lacunas. A incidência utiliza zenital aparente e orientação 25°/180°, conforme a configuração coletiva, enquanto a projeção extraterrestre usa zenital geométrico. Não interpretar o máximo próximo do meio-dia como validação independente do SPA nem declarar céu claro apenas pela forma da curva. Os dados são um exemplo diário de abril–junho/2024; não estabelecem climatologia ou efeito atmosférico causal. GHI/DNI/DHI locais independentes não estão disponíveis nesta seleção. Fontes: CSV observado preparado, configuração vigente, B32.

G01 — Fonte: POA/PVDAQ 2107 e cálculos SPA da equipe. Curvas no ponto médio; sem interpolação.

## QUADRO 6 — 1.1 · SÍNTESE E LIMITES

Retomar a distinção entre referência geométrica e irradiância efetiva. A geometria fornece o referencial; a atmosfera modifica o campo radiativo. Os sensores permitem confrontar grandezas compatíveis, mas um sensor POA não constitui uma medição independente de cada componente horizontal. Massa de ar relativa é uma ligação com a atmosfera: secante do zenital apenas em domínio moderado, sem validade no horizonte; parametrizações devem distinguir pressão e refração. A próxima subseção formaliza irradiância, irradiação e componentes. Não antecipar modelos térmicos, elétricos nem de desempenho dos colegas.

Fontes: Duffie, Beckman e Blair (2020), p. 9–15; Sengupta et al. (2024), cap. 2, p. 5–10.

## QUESTÕES PARA ESTUDO

Por que o meio-dia solar difere de 12 h no relógio? Porque longitude, equação do tempo e convenção civil deslocam a correspondência entre posição solar e hora registrada.

Por que SPA não fornece a GHI medida? Porque o algoritmo de posição solar não representa, por si só, a transferência radiativa na atmosfera.

Por que a POA não é uma medição de GHI? Porque o sensor está em outro plano e integra contribuições com distribuição angular distinta.

O valor 1366,1 W/m² é uma nova medida da constante solar? Não. É o parâmetro de referência mantido para reproduzir o método Spencer do projeto.

O que demonstra a conferência com a Tabela A5.1? A consistência da implementação com um exemplo publicado, sem validação independente do conjunto de sensores do estudo.

É possível identificar nuvens apenas pela G01? A forma da curva não discrimina de modo único os mecanismos atmosféricos e de medição.

# Referências

DUFFIE, John A.; BECKMAN, William A.; BLAIR, Nathan. **Solar engineering of thermal processes, photovoltaics and wind**. 5. ed. Hoboken: Wiley, 2020. ISBN 9781119540311. DOI: https://doi.org/10.1002/9781119540328.

NOAA GLOBAL MONITORING LABORATORY. **General solar position calculations**. [S. l.]: NOAA, [s. d.]. 2 p. Disponível em: https://gml.noaa.gov/grad/solcalc/solareqns.PDF. Acesso em: 27 out. 2026.

PVLIB CONTRIBUTORS. **pvlib python: get_extra_radiation e spa_python**. Versão 0.16.1. 2026. Disponível em: https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.irradiance.get_extra_radiation.html. Acesso em: 27 out. 2026.

REDA, Ibrahim; ANDREAS, Afshin. Solar position algorithm for solar radiation applications. **Solar Energy**, v. 76, n. 5, p. 577–589, 2004. DOI: https://doi.org/10.1016/j.solener.2003.12.003.

REDA, Ibrahim; ANDREAS, Afshin. **Solar position algorithm for solar radiation applications**. Revised January 2008. Golden: National Renewable Energy Laboratory, 2008. Relatório NREL/TP-560-34302. DOI: https://doi.org/10.2172/15003974.

SENGUPTA, Manajit et al. (ed.). **Best practices handbook for the collection and use of solar resource data for solar energy applications**. 4. ed. Golden: National Renewable Energy Laboratory, 2024. Relatório NREL/TP-5D00-88300. Disponível em: https://docs.nrel.gov/docs/fy24osti/88300.pdf. Acesso em: 27 out. 2026.

TEIXEIRA, Samuel Constantino et al. **SPGER0046 Energias Renováveis: configuração e dados preparados do estudo PVDAQ 2107**. 2026. Repositório de trabalho. Dados utilizados: abril a junho de 2024. Disponível em: https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis. Acesso em: 27 out. 2026.
