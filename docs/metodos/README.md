# Dossiê técnico e natureza das informações

O estudo principal usa PVDAQ 2107, Farm Solar Array, Arbuckle, Califórnia, de abril a junho de 2024. Há 2.880 módulos, 24 inversores e 125 canais observacionais no conjunto original.

- [Guia técnico resumido em Word](Guia_Tecnico_Resumido_PVDAQ_2107.docx): origem, período, equipamentos, entradas, referência observacional e uso nas quatro seções.
- [Dossiê técnico completo em Word](Dossie_Tecnico_por_Secao.docx).
- [Transcrição integral para consulta](Dossie_Tecnico_Leitura.txt).
- [Inventários e dicionário de canais](../../data/equipamentos/README.md).
- [Procedência dos parâmetros](../../config/proveniencia_parametros.csv).
- [Métodos e fontes](../Metodos_e_Fontes_Conferidos.md).

POA, temperatura do ar, vento e potência CA são observações locais. Temperatura operacional, curvas I–V/P–V, potência prevista e perdas por estágio são resultados calculados. As propriedades de fachada BIPV são hipóteses.

O limite CA efetivamente configurado, a topologia de strings/MPPTs, a altura do anemômetro, albedo e histórico de limpeza não foram comprovados nos dados. O equivalente 20×6 não é um diagrama verificado da instalação. O banco CEC diverge do cadastro na classificação da tecnologia do módulo; a variante de tensão do inversor também requer conferência. Consultar o dossiê antes de citar valores como especificações de campo.

A saída CA observada serve à validação da previsão. Não entra como variável explicativa no modelo físico. A inversão de POA e os cenários BIPV não têm medições independentes para validar suas etapas.

## Quantidades dos grupos de módulos

O JSON original e o CSV de grupos registram 19 grupos de 120 módulos, um de 160, um de 200 e três de 80, totalizando 2.880 módulos. A expressão “24 grupos de 120 módulos” no dossiê original é uma simplificação que não descreve a distribuição cadastrada. O guia resumido usa as quantidades conferidas no JSON e no CSV. O exemplo 20 em série × 6 strings em paralelo permanece apenas didático.
