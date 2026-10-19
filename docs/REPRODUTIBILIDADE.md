# Executar e reproduzir o projeto

O caso principal é PVDAQ 2107, Farm Solar Array, Arbuckle, Califórnia, de 01/04/2024 a 30/06/2024 em America/Los_Angeles. As tabelas comuns usam UTC e intervalos de 15 minutos. NASA POWER e os dados IFES permanecem fora da cadeia principal.

Na raiz de uma cópia completa do repositório:

```bash
python -m pip install -r requirements.txt
python scripts/baixar_dados_originais.py
python tests/verificar_organizacao.py
python tests/verificar_ciencia.py
python tests/verificar_refinamento.py
```

As verificações usam os dados e resultados existentes. Para recalcular a cadeia física, execute `python scripts/executar_projeto.py`. Esse comando escreve saídas; use uma cópia de trabalho. Os quatro CSVs brutos e os metadados estão incluídos no repositório, com os SHA-256 registrados em `data/raw/fontes_pvdaq.json`. A rotina de download recupera as fontes oficiais quando necessário.

O notebook principal está em [notebooks](../notebooks/01_Projeto_FV_Quatro_Secoes.ipynb), e o bibliográfico em [bibliografia](../bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb). Os originais executados do Drive foram preservados em [originais fotovoltaicos](../notebooks/originais_executados/01_Projeto_FV_Quatro_Secoes.ipynb) e [originais bibliográficos](../bibliografia/originais_executados/02_Fundamentacao_Teorica_por_Subsecao.ipynb), sem alterar suas células ou saídas. Suas rotinas opcionais de exportação ao Drive dependem de autenticação própria do usuário.

O notebook e o script existente encontram a raiz pelos arquivos do projeto. Os caminhos computacionais `src`, `config`, `data`, `outputs` e `bibliografia` foram preservados. A nova navegação em `secoes` usa os arquivos originais com links relativos; não exige mudar as equações nem os caminhos do cálculo.

O parâmetro `--graficos` regenera ilustrações apenas quando solicitado. As 120 exportações finais publicadas foram recuperadas do Drive e não foram regeneradas nesta integração. O modelo principal permanece separado do ajuste empírico treinado em abril. POA, temperatura do ar, vento e potência AC observada são medições; temperatura de célula, curvas elétricas, perdas e cenários BIPV são calculados ou assumidos conforme o dossiê.
