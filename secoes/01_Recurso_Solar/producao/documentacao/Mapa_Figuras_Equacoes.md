# FIGURAS, EQUAÇÕES E FONTES

Os arquivos PDF e SVG de `figuras/` são vetoriais. PNG é uma alternativa para aplicativos sem suporte a SVG; não substitui o vetor como matriz de produção.

| Identificação | Arquivo-base | Uso e fonte conferida |
|---|---|---|
| D01 | `D01_geometria` | Corte vertical e azimute; Duffie et al. (2020), p. 13; Sengupta et al. (2024), cap. 2-8. Esquema próprio, fora de escala. |
| E1.01 | `EQ_zenital` | Relação esférica do zenital; Duffie et al., p. 15. |
| Complemento angular | `EQ_elevacao` | Elevação = 90° − zenital; Duffie et al., p. 13. |
| Ângulo horário | `EQ_horario` | Tempo solar verdadeiro; NOAA, p. 1. |
| Relação orbital | `EQ_distancia` | Inverso do quadrado; Duffie et al., p. 9; handbook 2024, cap. 2-5. |
| Spencer | `EQ_spencer` | Implementação conferida do pvlib 0.16.1, coeficiente 0,000719. |
| E1.02 | `EQ_projecao` | Projeção horizontal extraterrestre, com recorte geométrico noturno. |
| D02 | `D02_fluxo_geometria` | Diagrama próprio: entradas → SPA e Spencer em ramos distintos → projeção. |
| G01 | `G01_recurso_geometria_escuro` e `_claro` | POA medida e geometria calculada em 17/05/2024; dados preparados PVDAQ 2107 e SPA. CSV e parâmetros em `resultados/`. |
| E1.03 | `EQ_integracao` | Integração de irradiância; Duffie et al., p. 10. |
| E1.04 | Equação nativa do DOCX | Soma de médias sobre intervalos válidos, com duração declarada; consequência da definição de integral. |
| E1.05 | `EQ_fechamento` | GHI = DNI cos(zenital) + DHI; Sengupta et al., cap. 2-10. |

As matrizes bibliográficas indicam páginas PDF e impressas. Dados, hipóteses de processamento e inferências lógicas estão registrados separadamente de evidências documentais. A G01 não representa uma simulação de céu claro nem uma reconstrução de componentes independentes.
