# Registro de decisões da versão 1.2

1. A linha física original foi preservada. POA e meteorologia são locais; geração medida serve como referência de avaliação.
2. Acrescentados diagnósticos de resíduos, erros por mês/hora/faixa de POA, descritivas com quartis e cobertura, energia por período e PSH da janela pareada.
3. nMBE/nRMSE usam a média observada dos respectivos pares/estratos. R² é 1−SSE/SST; não r².
4. Albedo usa componentes reconstruídas com referência 0,20 e variação isolada do parâmetro de transposição. Não é identificação de albedo real.
5. A sujidade é atenuação adicional do módulo relativamente à leitura POA. A condição do sensor não foi reconstruída; não inferir sujeira real pelo resíduo.
6. BIPV mantém o recorte exploratório e hipóteses explícitas. A comparação de geometrias combina orientação e condição de ventilação; o balanço semitransparente é um exemplo separado de 100 m².
7. Os cinco DOCX respeitam o padrão solicitado. Três traços grossos, negrito e fonte 12 são especificações do usuário, sem alegação de universalidade normativa.
8. Fluxogramas e ilustrações são científicos e vetoriais, gerados em Matplotlib. Temas claro/escuro usam dados e escalas iguais. Não foi gerado TIFF.
9. O controle de qualidade não exclui dados por erro alto do modelo. O teste temporal de junho não é instalação independente.
10. Detalhes HTML recolhíveis são dependentes do visualizador do notebook. O relatório HTML é entregue com detalhes fechados e tema alternável; não se afirma teste de interface/autenticação Colab.
11. Salvamento no Drive usa integração autorizada e conferência de metadados. O upload pessoal do Colab é opcional e preserva hierarquia real de subpastas, corrigindo o comportamento anterior que criava nomes contendo barras.
