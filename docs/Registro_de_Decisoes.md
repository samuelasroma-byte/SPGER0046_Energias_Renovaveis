# Premissas do estudo fotovoltaico

1. O capítulo possui quatro seções e 19 subseções, com responsáveis definidos na proposta oficial.
2. O estudo usa Farm Solar Array, PVDAQ 2107, de abril a junho de 2024, em hora local America/Los_Angeles.
3. POA, temperatura do ar e vento locais alimentam o modelo físico. NASA POWER é fonte complementar, fora da cadeia principal.
4. O medidor CA é a referência primária. A soma dos inversores oferece uma comparação adicional, com diferenças observacionais próprias.
5. Os métodos estão implementados no pvlib 0.16.1. Os parâmetros CEC/SAM são registrados em JSON, com as fontes metodológicas identificadas.
6. As divergências dos metadados e as lacunas de topologia e sensores constam do dossiê. O limite de 30 kW por inversor é uma hipótese; 27,6 kW é avaliado como sensibilidade.
7. O controle de qualidade mantém lacunas, não seleciona atrasos pelo melhor ajuste e não exclui pontos pelo erro do modelo. O viés médio do modelo físico é +7,73% na amostra diurna pareada.
8. O ajuste empírico utiliza abril. Maio e junho são avaliados separadamente; o modelo físico sem escala é a referência principal.
9. BIPV é um cenário hipotético. As propriedades semitransparentes e térmicas não representam uma fachada medida.
10. O GitHub reúne código, notebooks, dados, resultados e documentos. A equipe utiliza uma cadeia computacional comum às quatro seções.

## Geometria e análises exploratórias

A geometria solar utiliza coordenadas, horários e SPA. A inversão POA→GHI/DNI/DHI é exploratória e não produz uma referência independente de validação. O BIPV usa componentes reconstruídas e meteorologia local nas mesmas horas elegíveis, com cobertura parcial identificada.

O notebook inclui verificação de dependências, fontes metodológicas, exportações gráficas, relatório e ZIP de resultados. A exportação opcional do Colab ao Drive requer autenticação pessoal e usa uma pasta datada em 03_Resultados.

## Orientação para a discussão científica

A equipe deve examinar o detalhamento do capítulo, a interpretação temporal, as condições dos sensores, o viés do modelo e a diferença entre medidor e inversores. Cada seção relaciona suas conclusões às fontes e aos limites da evidência. A integração do notebook e do texto cabe aos responsáveis definidos pelo grupo.
