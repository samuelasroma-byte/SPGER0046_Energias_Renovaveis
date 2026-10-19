# Executar e reproduzir o projeto

O caso principal é PVDAQ 2107, Farm Solar Array, Arbuckle, Califórnia, de 01/04/2024 a 30/06/2024 em America/Los_Angeles. As tabelas comuns usam UTC e intervalos de 15 minutos. NASA POWER e os dados IFES permanecem fora da cadeia principal.

Na raiz de uma cópia completa do repositório:

```bash
python -m pip install -r requirements.txt
python scripts/baixar_dados_originais.py
python tests/verificar_organizacao.py
python tests/verificar_ciencia.py
python tests/verificar_refinamento.py
python tests/verificar_distribuicao_editorial.py
python tests/verificar_inventario_equacoes.py
```

As verificações usam os dados e resultados existentes. Para recalcular a cadeia física, execute `python scripts/executar_projeto.py`. Esse comando escreve saídas; use uma cópia de trabalho. Os quatro CSVs brutos e os metadados estão incluídos no repositório, com os SHA-256 registrados em `data/raw/fontes_pvdaq.json`. A rotina de download recupera as fontes oficiais quando necessário.

O [notebook principal](../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb) apresenta o estudo fotovoltaico; o [notebook bibliográfico](../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb), o levantamento das fontes. Há cópias executadas para consulta em [estudo fotovoltaico](../notebooks/originais_executados/01_Projeto_FV_Quatro_Secoes.ipynb) e [bibliografia](../bibliografia/originais_executados/02_Fundamentacao_Teorica_por_Subsecao.ipynb). A exportação opcional ao Drive requer autenticação pessoal.

O notebook e o script existente encontram a raiz pelos arquivos do projeto. Os dados e tabelas numéricas mantêm seus caminhos computacionais. Os gráficos finais ficam exclusivamente na seção atribuída pelo [mapa editorial](Distribuicao_Editorial.md); `src/editorial_fv.py` aplica essa regra à exportação, ao notebook e ao relatório. O pacote ZIP de resultados inclui `outputs`, `secoes` e a política editorial. A exportação pessoal opcional ao Drive inclui esse ZIP completo.

Para atualizar os índices e os quatro Word tabulares, sem recalcular os dados:

```bash
python scripts/distribuir_materiais_editoriais.py
python scripts/gerar_tabulares_por_secao.py
python build_notebook_v1_2.py
```

As cópias executadas e os [relatórios](../outputs/relatorios/originais/README.md) documentam o cálculo. A [distribuição editorial](Distribuicao_Editorial.md) define o local de cada material no capítulo.

O [inventário de equações](equacoes/README.md) possui 37 relações do núcleo do notebook e 24 de apoio extraídas do código. Para recriar seus cinco Word com equações nativas editáveis, usar `python scripts/gerar_inventario_equacoes.py` em ambiente com `python-docx`, `lxml` e o executável Pandoc disponível. Essa rotina atualiza a documentação e os índices sem recalcular os resultados físicos.

Cada PDF corresponde ao Word indicado em `docs/auditoria/Publicacao_Drive_Equacoes.json`, com hashes de ambos os arquivos. Após editar um Word, exportar o PDF correspondente. O comando `python tests/verificar_acesso_equacoes.py` confere os documentos, os IDs por seção e os atalhos das 19 subseções; requer PyMuPDF.

O parâmetro `--graficos` regenera as ilustrações. O modelo principal é separado do ajuste empírico treinado em abril. POA, temperatura do ar, vento e potência CA observada são medições; temperatura de célula, curvas elétricas, perdas e cenários BIPV são calculados ou assumidos conforme o dossiê.
