# Configuração executável

- [projeto.json](projeto.json): local, trimestre, capacidade e hipóteses.
- [modulo_cec.json](modulo_cec.json): registro CEC do módulo usado no diodo único.
- [inversor_cec.json](inversor_cec.json): registro de referência do inversor; o modelo principal de conversão é PVWatts.
- [proveniencia_parametros.csv](proveniencia_parametros.csv): natureza e origem dos parâmetros.
- [ambiente_executado.json](ambiente_executado.json): ambiente da execução anterior registrada.

A execução atual registra suas versões em outputs/logs/ultima_execucao.json. Alterações no período ou nos parâmetros devem ser comuns às quatro seções, revisadas e acompanhadas por nova exportação dos resultados. Ausências e divergências continuam no dossiê, sem preenchimento como se fossem fatos medidos.
