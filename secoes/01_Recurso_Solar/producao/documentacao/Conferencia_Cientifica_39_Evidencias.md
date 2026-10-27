# Conferência científica da Seção 1

Samuel Constantino Teixeira — PPGER/UFPB — 27 de outubro de 2026

As 39 afirmações da matriz foram confrontadas com as páginas indicadas, as equações, as convenções e os limites de uso. O confronto sustenta a redação com as qualificações registradas: 16 relações diretas, 18 relações diretas com restrições, uma com derivação matemática e quatro com inferência explicitada. A leitura foi assistida por IA; não corresponde a revisão por pares, leitura integral dos livros ou aplicação integral do ProKnow-C.

## Correções físicas e bibliográficas

A convenção azimutal do capítulo parte do norte e cresce no sentido horário. O livro de Duffie, Beckman e Blair parte do sul; a conversão foi explicitada como Aₛ = (γₛ + 180°) mod 360°. O símbolo Aₛ identifica o azimute nos diagramas. No zênite a projeção horizontal se anula e o azimute é indefinido.

A aproximação secante para massa de ar recebeu o domínio indicado no livro: nível do mar e zenitais de até aproximadamente 70°. O critério NOAA de 90,833° para nascer e pôr do Sol inclui refração e tamanho angular do disco; não substitui o recorte geométrico da projeção extraterrestre.

O coeficiente de cos(2B) é 0,000719 no pvlib 0.16.1 executado, enquanto o exemplar do livro imprime 0,00719 na p. 9. A implementação mantém o coeficiente do software e o denominador 365, inclusive no ano bissexto, com a divergência registrada. O SPA calcula posição; Spencer calcula irradiância extraterrestre.

A reprodução da Tabela A5.1 do SPA foi conferida contra o arredondamento a cinco casas decimais, com tolerância de 0,000005°. Essa tolerância é numérica e não expressa a incerteza do sensor ou a exatidão das entradas PVDAQ.

GHI, DNI e DHI foram delimitadas ao campo solar de ondas curtas e a planos, bandas e intervalos compatíveis. A soma discreta de médias para obter irradiação foi identificada como derivação da integral. Reconstituir componentes e reproduzir a POA de entrada não as valida como observações independentes. Driesse, Jensen e Perez (2024, pp. 9–11) distinguem testes da solução inversa com alvos modelados e comparação com observações.

Inferências sobre umidade superficial e água precipitável, resolução de pixel e exatidão, e interpolação temporal foram separadas das definições diretamente documentadas. Uma montagem fixa não oferece todas as componentes independentes; sistemas de sombra rotativa alternam medidas e calculam DNI. A POA isolada restringe certos testes de qualidade, mas não impede controles de cadência, lacunas e disponibilidade.

## Decisões sobre as fontes

B11 passou por leitura das pp. 1 e 9–11. O README oficial B27 foi lido. A autoria e o DOI de B24 foram confirmados na p. 25 de material institucional DOE/NREL de 2024, mantendo a indicação de que o destino DOI não estava acessível. O arquivo B36/2021 foi inspecionado e excluído como prova devido a defeitos de representação; a quarta edição A045 foi lida e registrada separadamente. B19 e B20 permanecem no catálogo histórico, sem uso como prova nesta versão.

## Rastreabilidade e arquivos editáveis

Confronto_Cientifico_39_Evidencias.csv e a aba Confronto_Cientifico da planilha contêm afirmação, página, classificação, justificativa, consequência editorial e hashes. O notebook executa verificações de integridade e relações físicas e exporta os DOCX editáveis. Reexecutar o código não simula uma nova leitura intelectual das referências. PDFs integrais de terceiros permanecem no acervo autorizado.

Os manuscritos estão em Times New Roman, com equações nativas do Word. Os PDFs de texto são exportados por LibreOffice. Os slides são compilados em Beamer com XeLaTeX; PDF e PPTX compartilham o conteúdo declarado, sem sincronização bidirecional. Diagramas, equações e gráficos dos seis quadros usam fundo preto opaco, textos brancos e destaques amarelos/cianos. O PPTX inclui vetores e imagens PNG válidas para compatibilidade.
