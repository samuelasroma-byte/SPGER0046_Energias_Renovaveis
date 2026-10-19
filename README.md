# Recurso solar e modelagem da conversão fotovoltaica

Projeto da disciplina SPGER0046 Energias Renováveis, PPGER UFPB. Estrutura técnica organizada em 18/10/2026 com base no projeto computacional v1.2.2, na proposta oficial e no acervo disponível.

## Acesso aos arquivos e trabalho da equipe

O GitHub é o ambiente central de redação, revisão, código e organização deste projeto.

- [Abrir os 91 documentos bibliográficos](references/Indice_Documentos.md).
- [Abrir qualquer um dos 605 arquivos da pasta do projeto no Drive](docs/Acervo_Completo_Drive.md).
- [Baixar os quatro CSVs originais completos](data/raw/README.md).
- [Entender as contas, permissões e colaboração](docs/ACESSO_E_COLABORACAO.md).

Os links do Drive abrem as cópias dentro da pasta do projeto. A conferência individual de 19/10/2026 confirmou acesso por link nos 605 arquivos; a leitura dispensa login. Os CSVs originais possuem também links públicos oficiais. Para editar os arquivos do repositório, cada integrante precisa aceitar um convite na própria conta GitHub.

## Comece por sua seção

| Seção | Responsáveis | Conteúdo |
| --- | --- | --- |
| [1 Recurso solar](secoes/01_Recurso_Solar/README.md) | Samuel | 1.1 a 1.4 |
| [2 Condições ambientais](secoes/02_Condicoes_Ambientais/README.md) | Vannessa e Thais | 2.1 a 2.4 |
| [3 Modelagem fotovoltaica](secoes/03_Modelagem_Fotovoltaica/README.md) | Gabriela e Giulia | 3.1 a 3.6 |
| [4 Desempenho perdas e validação](secoes/04_Desempenho_Perdas_Validacao/README.md) | Júlia Ribeiro e Lucas Simão | 4.1 a 4.5 |

Cada seção contém roteiro, referências por tipo, índice de figuras e acesso às tabelas. Código, parâmetros e dados são comuns às quatro frentes.

## Documentos que orientam o trabalho

- [Proposta oficial e cronograma](docs/planejamento/README.md).
- [Matriz das 19 subseções](docs/Matriz_19_Subsecoes.md).
- [Arquitetura técnica e execução](docs/ARQUITETURA_TECNICA.md).
- [Dossiê técnico dos equipamentos e dados](docs/metodos/README.md).
- [Plano da equipe](docs/Plano_Equipe_SPGER0046.md).
- [Rotina de revisão](docs/Rotina_da_Equipe.md).

## Dados e resultados

O caso comum é Farm Solar Array, PVDAQ 2107, Arbuckle, Califórnia, de abril a junho de 2024. As entradas principais são POA, temperatura do ar e vento medidos junto à instalação. O modelo estima geração CA e a compara com o medidor local. NASA POWER fica fora da cadeia principal.

| Parte | Acesso |
| --- | --- |
| Originais e fontes | [data/raw](data/raw/README.md) |
| Equipamentos e 125 canais | [data/equipamentos](data/equipamentos/README.md) |
| Meteorologia irradiância e medições preparadas | [data/processed](data/processed/README.md) |
| Período e parâmetros | [config](config/README.md) |
| Séries métricas tabelas e gráficos | [outputs](outputs/README.md) |

Há 91 documentos bibliográficos distintos e 160 cópias nas pastas do Drive: 63 artigos, 9 livros, 3 dissertações, 3 teses, 12 relatórios/manuais e 1 TCC. Nenhuma norma técnica disponível. [Inventário](references/acervo_disponivel.csv) e [catálogo por seção](references/distribuicao_por_secao.csv). Os PDFs ficam no Drive; o acesso depende das permissões das pastas.

## Usar o projeto

Para consultar resultados e referências, abra os índices acima; não é necessário executar o código. Para calcular, instale requirements.txt em ambiente Python próprio. O leitor recupera os bytes oficiais descritos em data/raw/README.md e confere os hashes; os quatro CSVs também podem ser baixados individualmente pelos links daquela página.

```bash
python -m pip install -r requirements.txt
python scripts/executar_projeto.py
```

Para regenerar todas as figuras, acrescentar --graficos. O notebook principal fica em [notebooks/01_Projeto_FV_Quatro_Secoes.ipynb](notebooks/01_Projeto_FV_Quatro_Secoes.ipynb); o de literatura fica em [bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb](bibliografia/02_Fundamentacao_Teorica_por_Subsecao.ipynb). Os notebooks versionados estão sem saídas, enquanto os resultados numéricos pequenos já estão organizados em outputs. O [notebook executado no Drive](https://drive.google.com/file/d/1EYHPdkAeotZTRryg73DTotHkOZH691Zk/view) preserva a consulta anterior.

## Conferências e limites

O teste científico verifica integridade dos originais, STC, resposta térmica, conversão no inversor, definição de R², pareamento e conservação energética. A validação disponível é da saída CA da mesma instalação no trimestre. As componentes reconstruídas, temperatura operacional, strings equivalentes e fachada BIPV têm limitações documentadas.

```bash
python tests/verificar_ciencia.py
python tests/verificar_organizacao.py
```

O grupo redige nos arquivos texto.md de cada seção e revisa as alterações no GitHub. A proposta original no Drive continua sendo o registro de escopo e cronograma. Mudanças de cálculo devem passar por uma branch curta e revisão por outro integrante. Os PDFs bibliográficos e demais documentos do Drive estão ligados pelos índices de acesso deste repositório. Credenciais não devem ser incluídas nos arquivos. A norma IEC pendente não foi tratada como obtida nem substituída por um relatório.
