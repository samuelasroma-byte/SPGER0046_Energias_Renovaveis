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

O notebook principal está em [notebooks](../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb), e o bibliográfico em [bibliografia](../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb). Os originais executados do Drive foram preservados em [originais fotovoltaicos](../notebooks/originais_executados/01_Projeto_FV_Quatro_Secoes.ipynb) e [originais bibliográficos](../bibliografia/originais_executados/02_Fundamentacao_Teorica_por_Subsecao.ipynb), sem alterar suas células ou saídas. Suas rotinas opcionais de exportação ao Drive dependem de autenticação própria do usuário.

O notebook e o script existente encontram a raiz pelos arquivos do projeto. Os dados e tabelas numéricas mantêm seus caminhos computacionais. Os gráficos finais ficam exclusivamente na seção atribuída pelo [mapa editorial](Distribuicao_Editorial.md); `src/editorial_fv.py` aplica essa regra à exportação, ao notebook e ao relatório. O pacote ZIP de resultados inclui `outputs`, `secoes` e a política editorial. A exportação pessoal opcional ao Drive inclui esse ZIP completo.

Para atualizar os índices e os quatro Word tabulares, sem recalcular os dados:

```bash
python scripts/distribuir_materiais_editoriais.py
python scripts/gerar_tabulares_por_secao.py
python build_notebook_v1_2.py
```

Os originais executados e os [relatórios históricos](../outputs/relatorios/originais/README.md) preservam as associações temáticas anteriores. Para a redação atual, cada material tem uma única subseção responsável; referências em outros trechos devem citar seu ID sem repeti-lo.

O [inventário de equações](equacoes/README.md) possui 37 relações do núcleo do notebook e 24 de apoio extraídas do código. Para recriar seus cinco Word com equações nativas editáveis, usar `python scripts/gerar_inventario_equacoes.py` em ambiente com `python-docx`, `lxml` e o executável Pandoc disponível. Essa rotina atualiza a documentação e os índices sem recalcular os resultados físicos.

As cinco versões PDF de leitura foram exportadas dos Word da revisão 2026-10-19.2 e preservam suas 51 páginas. A publicação registra o SHA-256 de cada PDF e do Word que lhe deu origem em `docs/auditoria/Publicacao_Drive_Equacoes.json`. Se um Word for atualizado, reexportar e revisar seu PDF antes de atualizar os vínculos de leitura. `python tests/verificar_acesso_equacoes.py` confere as cópias, os IDs por seção, a preservação dos Word e os atalhos das 19 subseções; requer PyMuPDF.

O parâmetro `--graficos` regenera ilustrações apenas quando solicitado. As 120 exportações finais publicadas foram recuperadas do Drive e não foram regeneradas nesta integração. O modelo principal permanece separado do ajuste empírico treinado em abril. POA, temperatura do ar, vento e potência AC observada são medições; temperatura de célula, curvas elétricas, perdas e cenários BIPV são calculados ou assumidos conforme o dossiê.
