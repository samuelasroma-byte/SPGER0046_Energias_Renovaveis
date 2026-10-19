# Dados observacionais originais — PVDAQ 2107

Os quatro CSVs completos estão neste repositório, sem alteração de bytes, incluindo o CSV elétrico de 63.287.121 bytes. Também têm download individual na fonte oficial e cópias autorizadas no Drive.

| Arquivo | Bytes | GitHub | Fonte oficial | Cópia da equipe |
| --- | --- | --- | --- | --- |
| 2107_system_metadata.json | 64652 | [Baixar](2107_system_metadata.json) | [Download oficial](https://oedi-data-lake.s3.amazonaws.com/pvdaq/2023-solar-data-prize/2107_OEDI/metadata/2107_system_metadata.json) | [Drive](https://drive.google.com/file/d/1utWa8jDZr6hPA_j05-uF_aOk0JaBfz9-/view?usp=drivesdk) |
| 2107_environment_data_2024.csv | 1179362 | [Baixar](2107_environment_data_2024.csv) | [Download oficial](https://oedi-data-lake.s3.amazonaws.com/pvdaq/2023-solar-data-prize/2107_OEDI/data/2107_environment_data_2024.csv) | [Drive](https://drive.google.com/file/d/1ZK-ktg1OepO39B1Xi0Qd2igeuGo3EW43/view?usp=drivesdk) |
| 2107_irradiance_data_2024.csv | 1933523 | [Baixar](2107_irradiance_data_2024.csv) | [Download oficial](https://oedi-data-lake.s3.amazonaws.com/pvdaq/2023-solar-data-prize/2107_OEDI/data/2107_irradiance_data_2024.csv) | [Drive](https://drive.google.com/file/d/1905okZsOhvmqaiRXWUlSDM2h3TUlTsBZ/view?usp=drivesdk) |
| 2107_meter_15m_data_2024.csv | 849109 | [Baixar](2107_meter_15m_data_2024.csv) | [Download oficial](https://oedi-data-lake.s3.amazonaws.com/pvdaq/2023-solar-data-prize/2107_OEDI/data/2107_meter_15m_data_2024.csv) | [Drive](https://drive.google.com/file/d/1Eut35Zci56dAvcmVvl7wq_0GnMpkxZV-/view?usp=drivesdk) |
| 2107_electrical_data_2024.csv | 63287121 | [Baixar](2107_electrical_data_2024.csv) | [Download oficial](https://oedi-data-lake.s3.amazonaws.com/pvdaq/2023-solar-data-prize/2107_OEDI/data/2107_electrical_data_2024.csv) | [Drive](https://drive.google.com/file/d/13O36LA_0VErwSRtb-4Yf8LT8_uHUQz8N/view?usp=drivesdk) |

Os SHA-256 completos constam do [manifesto original](fontes_pvdaq.json). O carregador verifica os hashes antes do cálculo. Não é necessário Git LFS para os arquivos publicados.

O conjunto público está identificado por DOI [10.25984/1846021](https://doi.org/10.25984/1846021). A licença CC BY 4.0 foi conferida em 19/10/2026 no [registro oficial do Data.gov](https://catalog.data.gov/dataset/photovoltaic-data-acquisition-pvdaq-public-datasets) e no [OEDI](https://data.openei.org/submissions/4568). Atribuição: DELINE, Chris et al. Photovoltaic Data Acquisition (PVDAQ) Public Datasets. NREL, 2021.

Os arquivos brutos cobrem períodos maiores que o trimestre. Temperatura em °F, vento em mph e potência em kW permanecem nas unidades de origem. Conversões e máscaras ocorrem nas tabelas preparadas; não há interpolação das lacunas.
