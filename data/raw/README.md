# Dados observacionais originais

Os quatro CSVs completos podem ser baixados individualmente na fonte pública oficial OEDI/PVDAQ. Não exigem conta Google. As cópias no Drive pertencem ao acervo da equipe e também estão liberadas por link.

| Arquivo original | Bytes | Download público | Cópia da equipe |
| --- | --- | --- | --- |
| 2107_system_metadata.json | 64652 | [Baixar na fonte oficial](https://oedi-data-lake.s3.amazonaws.com/pvdaq/2023-solar-data-prize/2107_OEDI/metadata/2107_system_metadata.json) | [Abrir no Drive](https://drive.google.com/file/d/1utWa8jDZr6hPA_j05-uF_aOk0JaBfz9-/view?usp=drivesdk) [Também neste repositório](2107_system_metadata.json) |
| 2107_environment_data_2024.csv | 1179362 | [Baixar na fonte oficial](https://oedi-data-lake.s3.amazonaws.com/pvdaq/2023-solar-data-prize/2107_OEDI/data/2107_environment_data_2024.csv) | [Abrir no Drive](https://drive.google.com/file/d/1ZK-ktg1OepO39B1Xi0Qd2igeuGo3EW43/view?usp=drivesdk)  |
| 2107_irradiance_data_2024.csv | 1933523 | [Baixar na fonte oficial](https://oedi-data-lake.s3.amazonaws.com/pvdaq/2023-solar-data-prize/2107_OEDI/data/2107_irradiance_data_2024.csv) | [Abrir no Drive](https://drive.google.com/file/d/1905okZsOhvmqaiRXWUlSDM2h3TUlTsBZ/view?usp=drivesdk)  |
| 2107_meter_15m_data_2024.csv | 849109 | [Baixar na fonte oficial](https://oedi-data-lake.s3.amazonaws.com/pvdaq/2023-solar-data-prize/2107_OEDI/data/2107_meter_15m_data_2024.csv) | [Abrir no Drive](https://drive.google.com/file/d/1Eut35Zci56dAvcmVvl7wq_0GnMpkxZV-/view?usp=drivesdk)  |
| 2107_electrical_data_2024.csv | 63287121 | [Baixar na fonte oficial](https://oedi-data-lake.s3.amazonaws.com/pvdaq/2023-solar-data-prize/2107_OEDI/data/2107_electrical_data_2024.csv) | [Abrir no Drive](https://drive.google.com/file/d/13O36LA_0VErwSRtb-4Yf8LT8_uHUQz8N/view?usp=drivesdk)  |

Os links públicos foram conferidos por HTTP em 19/10/2026, com resposta 200 e tamanhos correspondentes ao manifesto. O arquivo elétrico tem 63.287.121 bytes; baixe o CSV para consultar a série completa.

Para executar, o leitor do projeto já recupera os arquivos das URLs oficiais e confere os hashes em [fontes_pvdaq.json](fontes_pvdaq.json). Também é possível usar o ZIP original no Drive, sem mudar seus nomes internos. As cópias individuais acima permitem acesso sem depender do ZIP.

O período do estudo é 01/04/2024 a 30/06/2024 em America/Los_Angeles, com saídas em UTC. Os arquivos originais têm períodos maiores. Temperatura em °F, vento em mph e potências em kW são preservados nos originais; as conversões ocorrem nos dados preparados, sem preenchimento de lacunas. NASA POWER não entra na cadeia principal.
