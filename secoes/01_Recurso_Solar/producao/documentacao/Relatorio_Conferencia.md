# RELATÓRIO DE CONFERÊNCIA CIENTÍFICA E VISUAL — SEÇÃO 1

**Samuel Constantino Teixeira — SPGER0046/PPGER/UFPB — 27/10/2026.** Conferência e elaboração assistidas por IA, com cálculos efetivamente executados e cotejo das páginas indicadas na matriz.

## Escopo realizado

O planejamento oficial, o manuscrito de 1.1, os dois notebooks, o PPTX coletivo, as figuras e a configuração computacional foram inspecionados antes da edição. O manuscrito 1.1 foi revisto de forma localizada, preservando sua argumentação, suas equações nativas e o histórico. Os arquivos de 1.2 a 1.4 continham estruturas sem redação; receberam fundamentação, equações quando pertinentes, limites e referências. A seção foi integrada em DOCX, com versões PDF para leitura.

Os seis quadros de 1.1 foram corrigidos no mesmo PPTX compartilhado, nos slides físicos 5–10, com numeração 4–9. Os outros 12 slides permanecem idênticos em XML e pixels. O arquivo remoto foi recuperado imediatamente antes da gravação e baixado após a atualização para conferir seu SHA-256. As nove figuras mantêm SVG e PNG válidos e opacos em alto contraste. A confirmação está em `Conferencia_PPTX_Publicado.json`. O PowerPoint individual contém somente os seis quadros de Samuel, sem partes ocultas dos colegas.

## Conferência científica

| Item | Resultado e implicação |
|---|---|
| Posição solar | SPA, implementação `nrel_numpy` do pvlib 0.16.1; zenital geométrico distinguido do aparente. |
| Convenções | Azimute desde o norte, sentido horário; longitude leste positiva; ângulos em graus, convertidos para radianos nas operações trigonométricas. |
| Irradiância extraterrestre | Spencer separado do SPA; Gsc = 1366,1 W/m²; projeção horizontal com zenital geométrico e recorte noturno. |
| Cotejo de Spencer | O coeficiente 0,000719 do código foi conferido. A página 9 de Duffie et al. (2020) imprime 0,00719; a divergência foi registrada, sem alegar investigação de errata editorial. |
| Teste publicado do SPA | Exemplo da Tabela A5.1 de Reda e Andreas (2008): zenital aparente 50,111622° e azimute 194,340241°, compatíveis com os valores publicados arredondados, tolerância 0,000005°. |
| Configuração PVDAQ | 38,996306° N; 122,134111° O; altitude 10 m; inclinação 25°; azimute do arranjo 180°. |
| Tempo | 01/04–30/06/2024, 91 dias e 8.736 intervalos; início do intervalo em UTC, cálculo 7 min 30 s depois e apresentação em America/Los_Angeles. Em 17/05, UTC−7. |
| G01 de 17/05 | 96 posições, 94 médias POA disponíveis e 68 intervalos com três amostras; lacunas preservadas, sem interpolação. |
| Entradas de refração | Pressão estimada da altitude; temperatura padrão 12 °C e ΔT padrão 67 s mantidos para reproduzir o projeto. Não são medições locais nem uma atualização temporal específica. |
| Limites observacionais | POA observada; ângulos calculados. Sem atribuição causal de nuvens e sem tratar componentes reconstruídas como medições independentes. |

Também foram conferidas a cadência, a ausência de duplicatas temporais, a expressão independente de Spencer, o complemento elevação–zenital, a convenção de azimute e o recorte noturno. Esses controles verificam a implementação e a coerência das entradas; não validam a calibração do sensor POA. Os resultados completos e seus hashes estão em `resultados/Conferencia_Calculos.json`.

## Conferência bibliográfica

O recorte herdado contém 12 códigos B e 23 associações. As 39 afirmações de cinco PDFs receberam confronto analítico: 16 diretas, 18 diretas com restrições, uma com derivação e quatro com inferência. Oito PDFs estão inventariados: cinco sustentam a matriz original, B11 foi lida como complemento, B36 foi inspecionada e excluída devido a defeitos do arquivo, e A003 não foi utilizada. Somente o documento NOAA de duas páginas foi lido integralmente. Afirmações da mesma obra não são estudos independentes. A matriz e `Conferencia_Cientifica_39_Evidencias.docx` registram páginas, hashes, justificativas e aplicação editorial.

A bibliometria anterior foi recuperada, sem nova busca: o catálogo consolidado contém 829 registros; o arquivo de prioridades coletivo contém 102 associações a 39 obras distintas. Esses números descrevem arquivos anteriores e não atualizam, por equivalência, o inventário histórico de 91 documentos do acervo coletivo. A seleção efetiva da Seção 1 é documentada separadamente. A conferência do recorte não identificou DOI repetido nem duplicata binária nos seis PDFs locais; o título comum de Reda/Andreas foi mantido em dois registros por corresponder a versões distintas. As 23 fichas associativas B foram atualizadas e receberam quatro associações A045: 27 fichas, distintas das 39 evidências por afirmação.

O material introdutório ao ProKnow-C foi lido; sua página 2 contém a ementa, sem protocolo operacional completo. Não se declara aplicação integral, cobertura exaustiva de bases ou revisão por pares. B11 foi conferida nas pp. 1 e 9–11; o README B27 foi lido; a citação DOI de B24 foi confirmada em material institucional DOE/NREL de 2024, p. 25. O destino DOI não estava acessível. B19/B20 não foram utilizadas como prova porque suas edições exatas não estavam no recorte. A045/2024 foi lida separadamente de B36/2021. As decisões de seleção e exclusão delimitam a versão efetivamente fundamentada.

## Conferência editorial e acessibilidade

Os seis slides e todas as figuras utilizam fundo preto opaco, texto branco e destaques amarelos/cianos. Equações foram compostas em LaTeX, com SVG e PNG reais de compatibilidade. A cópia temporária sem SVG foi renderizada para conferir PNG. Os gráficos possuem fontes, eixos e unidades. PDF/Beamer e PPTX representam o mesmo conteúdo, sem sincronização automática.

Os DOCX usam A4, margens de 3 cm à esquerda e acima e 2 cm à direita e abaixo, corpo 14, hierarquia de títulos, equações nativas, páginas numeradas e referências com recuo suspenso. A formatação é compatível com a organização acadêmica solicitada; a adequação final ao modelo específico do capítulo deve ser conferida na revisão coletiva. Times New Roman é solicitada nos arquivos editáveis; os PDFs foram renderizados com Nimbus Roman, sua substituta métrica disponível. O painel HTML oferece estudo em fundo escuro e fonte 26 px.

Foram renderizados os DOCX e PDFs, com inspeção de páginas e slides para verificar fórmulas, quebras, legendas, proporções e sobreposições. Uma legenda duplicada na integração e a composição de uma equação em duas linhas foram corrigidas. A validação do PPTX foi feita pela estrutura OOXML e por renderização LibreOffice; não se afirma inspeção nativa no PowerPoint. A matriz XLSX inclui a aba Confronto_Cientifico com os 39 pareceres. As áreas de visão geral, confronto e seleção foram renderizadas e conferidas. As tabelas dos DOCX repetem cabeçalhos e não dividem uma linha entre páginas.

## Continuidade científica

O notebook executou dez células sem erros por IPython em processo local. O ambiente restringiu os sockets de um kernel externo; as mesmas células foram executadas e suas saídas registradas. A célula editorial exporta sete DOCX editáveis e os PDFs de texto: python-docx preserva e revisa a 1.1; Pandoc insere equações e converte as demais subseções; LibreOffice exporta PDFs. Beamer/XeLaTeX compila os slides. Seis verificações adicionais de relações físicas foram executadas, com exemplos construídos identificados como didáticos, sem tratá-los como resultados PVDAQ. Não foram repetidas buscas bibliométricas ou a cadeia térmica/elétrica dos colegas. A revisão cruzada e o ensaio oral seguem o cronograma oficial.
