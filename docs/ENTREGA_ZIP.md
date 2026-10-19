# Entrega completa em ZIP

**[Baixar a entrega mais recente](https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis/releases/latest/download/SPGER0046_Projeto_Completo.zip)** · [Ver versões e arquivos de verificação](https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis/releases/latest) · [Baixar o estado atual da main](https://github.com/samuelasroma-byte/SPGER0046_Energias_Renovaveis/archive/refs/heads/main.zip)

O ZIP da entrega contém todos os arquivos versionados da revisão indicada: dados originais e preparados, notebooks, resultados, figuras, tabelas, documentos técnicos, bibliografia atualizada e os cinco documentos de equações em Word e PDF. As equações mantêm as descrições dos símbolos, unidades e aplicação no notebook. Os PDFs de terceiros mantidos no Drive continuam acessíveis pelos links dos índices bibliográficos.

## Identificar e conferir a versão

Cada entrega tem uma página de versão com o commit completo, um ZIP, seu arquivo `.sha256` e `Verificacao_Pacote.json`. Dentro do ZIP, a pasta `SPGER0046_Energias_Renovaveis/` contém:

| Arquivo | Função |
| --- | --- |
| `ENTREGA.json` | Identifica o commit, a árvore Git, a data da revisão e as contagens de arquivos |
| `MANIFESTO_SHA256.csv` | Lista caminho, tamanho, SHA-256 e objeto Git de cada arquivo do projeto |
| `README.md` | Entrada para as quatro seções, 19 subseções, dados, referências e documentos |

O processo reabre todos os arquivos do ZIP e compara cada conteúdo com seu SHA-256 antes de publicá-lo. Para conferir o download em Linux, salve o ZIP e o arquivo `.sha256` na mesma pasta e execute `sha256sum -c SPGER0046_Projeto_Completo.zip.sha256`. No PowerShell, use `Get-FileHash SPGER0046_Projeto_Completo.zip -Algorithm SHA256` e compare com o valor publicado.

## Atualizações futuras

Após cada atualização da `main`, o [workflow de publicação](../.github/workflows/publicar-entrega.yml) verifica os originais, referências, equações e empacotamento. Em seguida gera um ZIP daquele commit e publica uma nova versão. O botão no início do projeto aponta para a entrega mais recente concluída. Enquanto uma execução estiver em andamento, ele conserva a entrega anterior; o link alternativo da `main` já contém os arquivos recém-integrados.

O ZIP é gerado a partir dos objetos Git. Arquivos temporários e alterações locais ainda não publicadas não entram no pacote. Para reproduzir a geração, usar Python 3.11 ou superior:

```bash
python scripts/empacotar_entrega.py --ref HEAD --output ../entrega
```

O pacote não é incluído dentro do próprio repositório. Ele é distribuído como arquivo da versão, evitando duplicação e crescimento recursivo do ZIP.
