# Referências e fontes do projeto — v1.2

Fontes científicas e técnicas dos dados, modelos e planejamento do capítulo. Os códigos R identificam os métodos e as hipóteses usados nos resultados. A seleção orienta a leitura e não constitui revisão sistemática. As fontes NASA documentam consultas complementares e não alimentam a validação elétrica do PVDAQ.

## R01 — Photovoltaic Data Acquisition (PVDAQ) Public Datasets

DELINE, Chris; PERRY, Kirsten; DECEGLIE, Michael; MULLER, Matthew; SEKULIC, William; JORDAN, Dirk. Photovoltaic Data Acquisition (PVDAQ) Public Datasets. [S. l.]: NREL, 2021. Conjunto de dados. Open Energy Data Initiative (OEDI). DOI: https://doi.org/10.25984/1846021. Disponível em: https://data.openei.org/submissions/4568. Acesso em: 19 out. 2026.

Seções: 0; 1.4; 4.4. Uso: Dados medidos e documentação da instalação; licença CC BY 4.0.

Fonte: https://data.openei.org/submissions/4568

DOI: 10.25984/1846021. Cópia local: data/raw/fontes_pvdaq.json. Consulta: 2026-10-19.

## R02 — PVDAQ access tools and openEDI documentation

PVDAQ / openEDI. PVDAQ access tools and openEDI documentation. s.d..

Seções: 0; 1.4. Uso: Documentação de acesso, formatos e proveniência.

Fonte: https://github.com/NatLabRockies/pvdaq_access

DOI: não informado. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R03 — Solar Position Algorithm for Solar Radiation Applications — NREL/TP-560-34302

Reda, I. and Andreas, A.. Solar Position Algorithm for Solar Radiation Applications — NREL/TP-560-34302. 2008.

Seções: 1.1; 3.1. Uso: Posição solar e cálculo do ângulo zenital; revisão do relatório.

Fonte: https://docs.nlr.gov/docs/fy08osti/34302.pdf

DOI: não informado. Cópia local: methods/SPA_Reda_Andreas_2008.pdf. Consulta: 2026-10-16.

## R04 — General Solar Position Calculations

NOAA Global Monitoring Laboratory. General Solar Position Calculations. s.d..

Seções: 0; 1.1. Uso: Aproximação usada somente para reproduzir o critério de disponibilidade diurna.

Fonte: https://gml.noaa.gov/grad/solcalc/solareqns.PDF

DOI: não informado. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R05 — get_extra_radiation — Spencer method; pvlib 0.16.1

pvlib contributors. get_extra_radiation — Spencer method; pvlib 0.16.1. 2026.

Seções: 1.1. Uso: Irradiância extraterrestre; constante de referência 1366,1 W/m² do software.

Fonte: https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.irradiance.get_extra_radiation.html

DOI: não informado. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R06 — Modeling daylight availability and irradiance components from direct and global irradiance

Perez, R. and Ineichen, P. and Seals, R. and Michalsky, J. and Stewart, R.. Modeling daylight availability and irradiance components from direct and global irradiance. 1990.

Seções: 2.2; 3.1. Uso: Modelo de transposição difusa; fonte original.

Fonte: https://doi.org/10.1016/0038-092X(90)90055-H

DOI: 10.1016/0038-092X(90)90055-H. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R07 — Assessing the outdoor operating temperature of photovoltaic modules

Faiman, D.. Assessing the outdoor operating temperature of photovoltaic modules. 2008.

Seções: 2.1; 3.2. Uso: Modelo térmico e interpretação de seus coeficientes.

Fonte: https://doi.org/10.1002/pip.813

DOI: 10.1002/pip.813. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R08 — Improvement and validation of a model for photovoltaic array performance

De Soto, W. and Klein, S. A. and Beckman, W. A.. Improvement and validation of a model for photovoltaic array performance. 2006.

Seções: 3.3; 3.4. Uso: Base física da parametrização do diodo único; implementação CEC identificada separadamente.

Fonte: https://doi.org/10.1016/j.solener.2005.06.010

DOI: 10.1016/j.solener.2005.06.010. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R09 — pvlib python: a python package for modeling solar energy systems

Holmgren, W. F. and Hansen, C. W. and Mikofski, M. A.. pvlib python: a python package for modeling solar energy systems. 2018.

Seções: 1–4. Uso: Referência do software; versão efetivamente usada 0.16.1.

Fonte: https://joss.theoj.org/papers/10.21105/joss.00884

DOI: 10.21105/joss.00884. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R10 — calcparams_cec and retrieve_sam — pvlib 0.16.1

pvlib contributors. calcparams_cec and retrieve_sam — pvlib 0.16.1. 2026.

Seções: 3.3; 3.5. Uso: Implementação CEC e origem dos parâmetros SAM preservados em JSON.

Fonte: https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.pvsystem.calcparams_cec.html

DOI: não informado. Cópia local: config/modulo_cec.json; config/inversor_cec.json. Consulta: 2026-10-16.

## R11 — PVWatts Version 5 Manual — NREL/TP-6A20-62641

Dobos, A. P.. PVWatts Version 5 Manual — NREL/TP-6A20-62641. 2014.

Seções: 3.3; 3.5. Uso: Conversão CC–CA e comparação CC por coeficiente térmico.

Fonte: https://docs.nlr.gov/docs/fy14osti/62641.pdf

DOI: não informado. Cópia local: methods/PVWatts_v5_Dobos_2014.pdf. Consulta: 2026-10-16.

## R12 — Performance Parameters for Grid-Connected PV Systems — NREL/CP-520-37358

Marion, B. and others. Performance Parameters for Grid-Connected PV Systems — NREL/CP-520-37358. 2005.

Seções: 4.1; 4.2; 4.3. Uso: Produtividades, PR e perdas normalizadas.

Fonte: https://docs.nlr.gov/docs/fy05osti/37358.pdf

DOI: não informado. Cópia local: methods/Performance_Parameters_Marion_2005.pdf. Consulta: 2026-10-16.

## R13 — TRIO-20.0/27.6-TL-US — Product Manual

ABB. TRIO-20.0/27.6-TL-US — Product Manual. s.d..

Seções: 3.5. Uso: Limites e configurações do inversor; configuração efetiva da usina não comprovada.

Fonte: https://library.e.abb.com/public/9ddffa465aa146bfa43bd0854abbcc81/TRIO-20.0-27.6-TL-US_Product_Manual.pdf

DOI: não informado. Cópia local: methods/ABB_TRIO_20_27_US_Manual.pdf. Consulta: 2026-10-16.

## R14 — A continuous form of the Perez diffuse sky model for forward and reverse transposition

Driesse, A. and Jensen, A. R. and Perez, R.. A continuous form of the Perez diffuse sky model for forward and reverse transposition. 2024.

Seções: 1.2; 3.1; 4.5. Uso: Transposição inversa exploratória; Erbs-Driesse e Perez-Driesse.

Fonte: https://doi.org/10.1016/j.solener.2023.112093

DOI: 10.1016/j.solener.2023.112093. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R15 — ghi_from_poa_driesse_2024 — pvlib 0.16.1

pvlib contributors. ghi_from_poa_driesse_2024 — pvlib 0.16.1. 2026.

Seções: 3.1. Uso: Implementação e critérios numéricos da inversão POA→GHI.

Fonte: https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.irradiance.ghi_from_poa_driesse_2024.html

DOI: não informado. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R16 — Reverse transposition limitations — pvlib 0.16.1

Driesse, A.. Reverse transposition limitations — pvlib 0.16.1. 2026.

Seções: 1.4; 3.1; 4.4. Uso: Demonstra a possibilidade de soluções não únicas; fechamento não é validação independente.

Fonte: https://pvlib-python.readthedocs.io/en/v0.16.1/gallery/irradiance-transposition/plot_rtranpose_limitations.html

DOI: não informado. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R17 — A model for deriving the direct normal and diffuse horizontal irradiance from the global tilted irradiance

Marion, B.. A model for deriving the direct normal and diffuse horizontal irradiance from the global tilted irradiance. 2015.

Seções: 3.1. Uso: Método alternativo GTI-DIRINT, citado para comparação; não executado nesta versão.

Fonte: https://doi.org/10.1016/j.solener.2015.10.024

DOI: 10.1016/j.solener.2015.10.024. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R18 — erbs_driesse — pvlib 0.16.1

pvlib contributors. erbs_driesse — pvlib 0.16.1. 2026.

Seções: 1.2; 3.1. Uso: Decomposição estimada de GHI em DNI e DHI, baseada em relação empírica.

Fonte: https://pvlib-python.readthedocs.io/en/v0.16.1/reference/generated/pvlib.irradiance.erbs_driesse.html

DOI: não informado. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R19 — Expanding Solar Energy Opportunities: From Rooftops to Building Integration

U.S. Department of Energy. Expanding Solar Energy Opportunities: From Rooftops to Building Integration. s.d..

Seções: 4.5. Uso: Contexto introdutório de BIPV; não fornece validação da fachada hipotética.

Fonte: https://www.energy.gov/cmei/systems/articles/expanding-solar-energy-opportunities-rooftops-building-integration

DOI: não informado. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R20 — Energy Performance Ratings for Windows, Doors, and Skylights

U.S. Department of Energy. Energy Performance Ratings for Windows, Doors, and Skylights. s.d..

Seções: 4.5. Uso: Definição de SHGC e transmissão visível; o SHGC do cenário não é certificado.

Fonte: https://www.energy.gov/energysaver/energy-performance-ratings-windows-doors-and-skylights

DOI: não informado. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R21 — POWER Hourly API

NASA POWER. POWER Hourly API. s.d..

Seções: Histórico v1.0; 1.4. Uso: Fonte complementar da versão anterior; não utilizada no percurso principal v1.1.

Fonte: https://power.larc.nasa.gov/docs/services/api/temporal/hourly/

DOI: não informado. Cópia local: methods/NASA_POWER_Hourly_API.html. Consulta: 2026-10-16.

## R22 — CERES SYN1deg hourly GHI, DNI and DHI methodology

NASA POWER. CERES SYN1deg hourly GHI, DNI and DHI methodology. s.d..

Seções: Histórico v1.0; 1.4. Uso: Produto solar em grade da versão anterior; não utilizado no percurso principal v1.1.

Fonte: https://power.larc.nasa.gov/docs/methodology/energy-fluxes/syn1deg/

DOI: não informado. Cópia local: methods/NASA_POWER_SYN1deg.html. Consulta: 2026-10-16.

## R23 — Meteorological Data Overview — MERRA-2

NASA POWER. Meteorological Data Overview — MERRA-2. s.d..

Seções: Histórico v1.0; 1.4. Uso: Meteorologia em grade da versão anterior; não utilizada no percurso principal v1.1.

Fonte: https://power.larc.nasa.gov/docs/methodology/meteorology/

DOI: não informado. Cópia local: data/raw/fonte_nasa.json. Consulta: 2026-10-16.

## R24 — Proposta de estrutura do capítulo: Recurso solar e modelagem da conversão fotovoltaica

Equipe SPGER0046 / UFPB. Proposta de estrutura do capítulo: Recurso solar e modelagem da conversão fotovoltaica. 2026.

Seções: Planejamento. Uso: Documento interno que define as quatro seções; não é referência científica de um modelo.

Fonte: ACERVO_RESTRITO_DA_EQUIPE

DOI: não informado. Cópia local: docs/Plano_do_Capitulo_Fonte_Drive_20261016.txt. Consulta: 2026-10-16.

## R25 — Solar Data Tools demo — Farm Solar Array

PV Analytics Webinar. Solar Data Tools demo — Farm Solar Array. 2024.

Seções: 0; 1.4; 4.4. Uso: Contexto complementar de qualidade e operação; não usado para remover erros altos.

Fonte: https://pv-tutorials.github.io/2024_Analytics_Webinar/solar-data-tools-demo.html

DOI: não informado. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R26 — openEDI PVDAQ dataset documentation

openEDI. openEDI PVDAQ dataset documentation. s.d..

Seções: 0; 1.4. Uso: Estrutura e documentação geral dos dados abertos.

Fonte: https://github.com/openEDI/documentation/blob/main/pvdaq.md

DOI: não informado. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R27 — Root mean square error (RMSE) or mean absolute error (MAE)? Arguments against avoiding RMSE in the literature

Chai, T. and Draxler, R. R.. Root mean square error (RMSE) or mean absolute error (MAE)? Arguments against avoiding RMSE in the literature. 2014.

Seções: 4.4. Uso: Métricas complementares para avaliação, com definição explícita de sinal e normalização neste projeto.

Fonte: https://gmd.copernicus.org/articles/7/1247/2014/

DOI: 10.5194/gmd-7-1247-2014. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R28 — Soiling Losses

Sandia National Laboratories / PVPMC. Soiling Losses. s.d..

Seções: 2.3. Uso: Mecanismo de atenuação por sujidade e interpretação de hipóteses.

Fonte: https://pvpmc.sandia.gov/modeling-guide/1-weather-design-inputs/shading-soiling-and-reflection-losses/soiling-losses/

DOI: não informado. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R29 — Plane of Array (POA) Irradiance

Sandia National Laboratories / PVPMC. Plane of Array (POA) Irradiance. s.d..

Seções: 1.2; 2.2; 2.4; 3.1. Uso: Componentes da POA e cuidado com correções já incorporadas à medição.

Fonte: https://pvpmc.sandia.gov/modeling-guide/1-weather-design-inputs/plane-of-array-poa-irradiance/

DOI: não informado. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

## R30 — Performance Ratio

Sandia National Laboratories / PVPMC. Performance Ratio. s.d..

Seções: 4.2; 4.3. Uso: Definição de Yr e PR; especificação da referência de irradiância.

Fonte: https://pvpmc.sandia.gov/modeling-guide/5-ac-system-output/pv-performance-metrics/performance-ratio/

DOI: não informado. Cópia local: Consulta por URL/DOI; PDF não incluído. Consulta: 2026-10-16.

