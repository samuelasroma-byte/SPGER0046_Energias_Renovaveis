# Arquitetura técnica do projeto

A proposta DOCX governa escopo, 19 subseções e cronograma. O notebook apresenta e coordena o cálculo; src implementa a física; config registra valores e hipóteses. As quatro seções consultam uma única cadeia compartilhada.

## Entradas e transformação

1. Preservar os cinco originais em data/raw e conferir seus hashes com fontes_pvdaq.json.
2. Consultar data/equipamentos para interpretar os canais e config para os modelos. A configuração CEC selecionada e a instalação real têm diferenças documentadas.
3. Selecionar abril a junho de 2024 no horário local, converter os índices para UTC e as unidades para °C, m/s e W, mantendo lacunas e flags.
4. Estimar temperatura operacional, MPP, potência CC e conversão CA. A medição CA é referência da validação; não entra como preditor.
5. Exportar dados preparados, séries simuladas, métricas e tabelas a partir do mesmo contexto. Registrar os hashes, versões e critérios em outputs/logs.
6. Inserir cada figura, gráfico, tabela e quadro apenas na subseção atribuída em [distribuicao_editorial.json](../config/distribuicao_editorial.json). Os índices, o notebook e o relatório HTML usam essa mesma atribuição. A inversão e o BIPV são explorações identificadas.

## Execução

Instalar requirements.txt em ambiente Python próprio. Para gerar dados e tabelas organizados:

```bash
python scripts/executar_projeto.py
```

Para incluir toda a coleção gráfica:

```bash
python scripts/executar_projeto.py --graficos
```

A primeira célula do notebook contém um pacote de apoio para execução no Colab. O pacote utiliza os mesmos arquivos de src e config do repositório; as quatro seções compartilham essa configuração.

`scripts/distribuir_materiais_editoriais.py` atualiza a navegação e os caminhos sem alterar bytes gráficos ou valores numéricos. `scripts/gerar_tabulares_por_secao.py` extrai tabelas e quadros editáveis para quatro Word com atribuição exclusiva. Consulte o [mapa de inserção única](Distribuicao_Editorial.md).

## Publicação e tamanho

O GitHub contém dez Word originais, 120 exportações finais de 30 ilustrações, tabelas completas do caso principal, relatórios, metadados, parâmetros e quatro CSVs brutos completos. Há seis PNG de prévia para consulta. PDFs bibliográficos de terceiros mantêm links individuais enquanto a redistribuição pública não estiver verificada. As famílias numéricas têm índices e unidades explícitos. Nenhuma chave de API é necessária para o caso físico local; a bibliografia usa chaves pessoais opcionais para outras bases, fora do repositório. Consulte a [auditoria final](AUDITORIA_FINAL_PUBLICACAO.md) e a [rotina de reprodução](REPRODUTIBILIDADE.md).
