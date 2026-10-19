# Dados observacionais originais

Os quatro CSVs e o JSON de metadados estão preservados no ZIP original, mantido fora do histórico Git. O JSON cadastral também está disponível neste repositório. A lista completa, com origem, tamanho e SHA-256, está em [fontes_pvdaq.json](fontes_pvdaq.json).

| Arquivo original | Uso |
| --- | --- |
| 2107_environment_data_2024.csv | Temperatura do ar, velocidade e direção do vento. |
| 2107_irradiance_data_2024.csv | POA medida no plano dos módulos. |
| 2107_electrical_data_2024.csv | Correntes, tensões e potências dos 24 inversores. |
| 2107_meter_15m_data_2024.csv | Potência CA medida para comparação. |
| 2107_system_metadata.json | Cadastro integral do sistema e dos equipamentos. |

Para executar, obter o ZIP original no Drive (consulta no acervo da equipe) e salvá-lo nesta pasta com o nome pvdaq_2107_2024_originais.zip. Não alterar o conteúdo nem os nomes internos. Se o ZIP estiver ausente, o leitor também tenta obter os mesmos bytes das fontes oficiais do manifesto e confere os hashes antes de calcular.

Os CSVs abrangem períodos maiores e diferentes entre si. A configuração seleciona 01/04/2024 a 30/06/2024 no fuso America/Los_Angeles; saídas são em UTC. A temperatura original está em °F, o vento em mph e potências em kW. Conversões para °C, m/s e W ocorrem apenas nos produtos derivados. Não há preenchimento de lacunas.

NASA POWER não entra na cadeia principal; sua documentação remanescente é histórica. Os PDFs bibliográficos e o acesso ao Drive dependem das permissões já existentes para cada arquivo.
