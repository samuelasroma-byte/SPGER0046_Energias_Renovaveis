# Registro de decisões do projeto

## 16/10/2026 — Base inicial executada

1. Adotado o plano atual do capítulo, com subseções 1.1–4.5, preservando a distribuição dos sete integrantes.
2. Adotada a Farm Solar Array/PVDAQ 2107 como instalação real de referência. Período local de abril a junho de 2024, sem alterar os arquivos originais.
3. Mantida a POA local na validação elétrica principal. Acrescentado NASA POWER para percorrer GHI/DNI/DHI→POA→geração, com rótulo de estimativa em grade.
4. Mantido o medidor AC como referência primária. A soma dos inversores é uma comparação adicional; sua diferença não é apagada por ajuste automático.
5. Utilizados métodos publicados, disponíveis no pvlib 0.16.1, com parâmetros CEC/SAM congelados em JSON. Nenhum notebook de terceiros foi apresentado como trabalho do grupo.
6. Preservadas as divergências dos metadados e as lacunas de topologia/sensores. O limite AC de 30 kW por inversor é uma hipótese documentada pelo manual US; 27,6 kW aparece em sensibilidade.
7. Não foram preenchidas lacunas diurnas, selecionados atrasos pelo melhor ajuste ou removidos pontos pelo tamanho do erro. O modelo-base superestima o medidor em média 7,73% na amostra diurna pareada.
8. O ajuste empírico adicional usa somente abril. Maio e junho são relatados separadamente, sem substituir a avaliação principal sem ajuste.
9. BIPV é extensão simulada com os mesmos dados de entrada. Propriedades semitransparentes e térmicas são hipóteses; nenhuma fachada foi declarada validada.
10. Código, notebook e fontes textuais foram preparados para o repositório existente SPGER0046. A tentativa de gravação retornou 403: a conta está autenticada, mas nenhum repositório aparece autorizado para a integração. Nenhum commit foi publicado. O notebook funciona independentemente dessa publicação; dados volumosos e documentos técnicos ficam no pacote completo do projeto.

## Próximos pontos para discussão do grupo

Conferir com a professora o nível de detalhamento esperado; revisar a interpretação dos intervalos e as condições dos sensores; discutir o viés do modelo e a diferença entre medidor e inversores; redigir a análise de cada seção com as fontes citadas; manter uma pessoa responsável por integrar alterações do notebook. Esses pontos não impedem executar a base atual e não devem ser descritos como já resolvidos.


## 16/10/2026 — v1.1: medições locais como percurso principal

NASA POWER deixou de ser dependência da execução principal. Coordenadas e horários calculam a geometria SPA. Inversão POA→GHI/DNI/DHI foi incluída como etapa exploratória; não alimenta a validação elétrica e não cria referência independente. O BIPV passou a usar componentes reconstruídas e meteorologia local nas mesmas horas elegíveis, com escopo parcial explícito. Acrescentadas 26 fontes na seção 5, instalação/verificação de bibliotecas, nove figuras com inversão habilitada, relatório, ZIP e salvamento pelo Colab em nova pasta datada dentro de 03_Resultados. A autenticação remota do Colab será feita pelo usuário; a publicação GitHub permanece pendente.
