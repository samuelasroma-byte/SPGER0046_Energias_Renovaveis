# Projeto em ZIP

**[Baixar o projeto em ZIP](https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis/releases/latest/download/SPGER0046_Projeto_Completo.zip)** · [Arquivos da entrega](https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis/releases/latest) · [Download alternativo](https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis/archive/refs/heads/main.zip)

O ZIP contém dados originais e preparados, notebooks, resultados, figuras, tabelas, documentos técnicos, bibliografia e equações em Word e PDF. Os quadros de equações apresentam símbolos, unidades, função e aplicação no notebook. Os PDFs de terceiros são acessados pelos índices bibliográficos.

## Identificação dos arquivos

Os arquivos da entrega incluem o ZIP, seu código de verificação em `.sha256` e o relatório `Verificacao_Pacote.json`. Dentro do ZIP, a pasta `SPGER0046_Energias_Renovaveis/` contém:

| Arquivo | Função |
| --- | --- |
| `ENTREGA.json` | Identifica a revisão do projeto, a data e a quantidade de arquivos |
| `MANIFESTO_SHA256.csv` | Lista caminho, tamanho e códigos de verificação de cada arquivo do projeto |
| `README.md` | Entrada para as quatro seções, 19 subseções, dados, referências e documentos |

O processo reabre todos os arquivos do ZIP e compara cada conteúdo com seu SHA-256 antes de publicá-lo. Para conferir o download em Linux, salve o ZIP e o arquivo `.sha256` na mesma pasta e execute `sha256sum -c SPGER0046_Projeto_Completo.zip.sha256`. No PowerShell, use `Get-FileHash SPGER0046_Projeto_Completo.zip -Algorithm SHA256` e compare com o valor publicado.

## Geração do pacote

O pacote é gerado a partir da versão principal do projeto. A [rotina de publicação](../.github/workflows/publicar-entrega.yml) verifica os arquivos, referências e equações antes de disponibilizar o ZIP.

O ZIP é gerado a partir dos objetos Git. Arquivos temporários e alterações locais ainda não publicadas não entram no pacote. Para reproduzir a geração, usar Python 3.11 ou superior:

```bash
python scripts/empacotar_entrega.py --ref HEAD --output ../entrega
```

O pacote não é incluído dentro do próprio repositório. Ele é distribuído como arquivo da versão, evitando duplicação e crescimento recursivo do ZIP.
