# Registro de decisões da versão 1.2

1. A cadeia física usa POA e meteorologia locais; a geração medida é a referência de avaliação.
2. Os diagnósticos abrangem resíduos, erros por mês/hora/faixa de POA, estatísticas com quartis e cobertura, energia por período e PSH da janela pareada.
3. nMBE/nRMSE usam a média observada dos respectivos pares/estratos. R² é 1−SSE/SST; não r².
4. Albedo usa componentes reconstruídas com referência 0,20 e variação isolada do parâmetro de transposição. Não é identificação de albedo real.
5. A sujidade é atenuação adicional do módulo relativamente à leitura POA. A condição do sensor não foi reconstruída; não inferir sujeira real pelo resíduo.
6. BIPV mantém o recorte exploratório e hipóteses explícitas. A comparação de geometrias combina orientação e condição de ventilação; o balanço semitransparente é um exemplo separado de 100 m².
7. As tabelas usam três linhas horizontais; os quadros, grade completa. O texto e os títulos usam fonte 12. A espessura das linhas é uma convenção gráfica do projeto.
8. Fluxogramas e ilustrações são produzidos em Matplotlib, em PDF vetorial e PNG. Os temas claro e escuro usam os mesmos dados e escalas.
9. O controle de qualidade não exclui dados por erro alto do modelo. O teste temporal de junho não é instalação independente.
10. O relatório HTML oferece descrições recolhíveis e alternância de tema. O comportamento dos blocos no notebook depende do visualizador.
11. A exportação opcional do Colab ao Drive utiliza autenticação pessoal e mantém a hierarquia de subpastas.
