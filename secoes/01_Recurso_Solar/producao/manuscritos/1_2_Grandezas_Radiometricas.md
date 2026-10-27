# 1.2 Grandezas radiométricas e componentes da radiação

## 1.2.1 Irradiância e irradiação

A descrição do recurso solar exige identificar a grandeza física, o plano de referência e o intervalo temporal a que cada valor se refere. A irradiância corresponde à potência radiante incidente por unidade de área, expressa em watt por metro quadrado (W/m²). A irradiação representa a energia radiante recebida por unidade de área durante um intervalo definido, expressa no Sistema Internacional em joule por metro quadrado (J/m²). O uso de Wh/m² ou kWh/m² é conveniente em aplicações energéticas, desde que o intervalo de integração seja explicitado. Assim, irradiância e irradiação descrevem aspectos relacionados do recurso, mas não podem ser substituídas uma pela outra em equações ou eixos gráficos (DUFFIE; BECKMAN; BLAIR, 2020, p. 10).

Se $G(t)$ representa a irradiância no plano considerado, a irradiação entre os instantes $t_1$ e $t_2$ é

$$H_{[t_1,t_2]}=\int_{t_1}^{t_2}G(t)\,\mathrm{d}t.\tag{E1.03}$$

Com $G$ em W/m² e o tempo em segundos, $H$ é obtida em J/m². Quando o tempo é expresso em horas, a integração fornece Wh/m². A equivalência $1\,\mathrm{Wh/m^2}=3600\,\mathrm{J/m^2}$ decorre da definição de watt e da conversão entre hora e segundo. Para registros que representam médias de intervalos, a forma discreta é

$$H=\sum_{i\in\mathcal{V}}\overline{G}_i\,\Delta t_i,\tag{E1.04}$$

em que $\overline{G}_i$ é a irradiância média do intervalo, $\Delta t_i$ é sua duração e $\mathcal{V}$ é o conjunto de intervalos válidos. Essa soma representa a energia dos intervalos efetivamente incluídos; não reconstitui a energia dos intervalos ausentes. Se o registro for uma amostra instantânea, a integração por soma ou por outra quadratura constitui uma aproximação adicional. Portanto, a resolução nominal de um arquivo não informa, por si só, se seus valores são instantâneos, médios ou acumulados. A interpretação deve ser obtida nos metadados de aquisição e processamento (DUFFIE; BECKMAN; BLAIR, 2020, p. 10; SENGUPTA et al., 2024, cap. 6, p. 24–25).

## 1.2.2 Componentes direta, difusa e global horizontal

A interação da radiação solar com a atmosfera produz um campo radiativo com contribuições direcionais distintas. A irradiância direta normal, DNI, é referida a uma superfície perpendicular à direção solar e à radiação proveniente de uma pequena região angular centrada no Sol. A irradiância difusa horizontal, DHI, é a contribuição do céu recebida por uma superfície horizontal, excluída a região angular atribuída à componente direta. A irradiância global horizontal, GHI, representa a irradiância descendente total recebida no plano horizontal. As três grandezas são expressas em W/m²; suas diferenças decorrem da direção de recepção e do campo angular integrado, e não da unidade (SENGUPTA et al., 2024, cap. 2, p. 9–10).

Para o Sol acima do horizonte e para definições radiométricas compatíveis, o balanço geométrico ideal é

$$\mathrm{GHI}=\mathrm{DNI}\cos\theta_z+\mathrm{DHI}.\tag{E1.05}$$

O produto $\mathrm{DNI}\cos\theta_z$ é a componente direta projetada na horizontal. A equação deve utilizar um ângulo solar coerente com a aplicação, distinguindo a geometria da refração quando necessário. No fechamento de medidas reais, também importam o campo de visão do pireliômetro, o sombreamento aplicado ao sensor de DHI, a resposta angular dos sensores e sua sincronização. Por isso, um resíduo entre os termos medidos não pode ser atribuído automaticamente a uma falha atmosférica ou a um único instrumento (SENGUPTA et al., 2024, cap. 2, p. 10; cap. 3, p. 5–7).

A equação de fechamento é uma restrição física útil, mas não transforma uma medição isolada de GHI em três observações independentes. A estimação de DNI e DHI a partir de GHI requer modelos de decomposição, cuja validade depende de condições e escalas temporais. Próximo ao horizonte, estimar DNI pela divisão da componente direta horizontal por $\cos\theta_z$ amplifica a sensibilidade a pequenos erros, pois o denominador tende a zero. A caracterização das componentes deve, portanto, manter explícita a distinção entre valores medidos e estimados (SENGUPTA et al., 2024, cap. 2, p. 10–11).

## 1.2.3 Referência extraterrestre e irradiância no plano do arranjo

A irradiância extraterrestre normal $G_{0n}$ e sua projeção horizontal $G_{0h}$, definidas em 1.1, constituem referências anteriores à interação com a atmosfera. A presença do mesmo plano horizontal em $G_{0h}$ e GHI não as torna equivalentes: a primeira representa a projeção extraterrestre, enquanto a segunda descreve o campo radiativo disponível na superfície. Também não se deve impor que toda observação de curta duração seja necessariamente inferior a essa projeção, pois a redistribuição por nuvens pode produzir episódios de intensificação local da irradiância global (DUFFIE; BECKMAN; BLAIR, 2020, p. 9–10; SENGUPTA et al., 2024, cap. 6, p. 2).

A irradiância no plano do arranjo, POA, é referida à superfície dos módulos, que pode ser inclinada ou rastreada. Sua descrição separa a contribuição direta projetada nesse plano, a difusa proveniente do céu e a refletida pelo entorno. Essa separação conceitual identifica a natureza das parcelas sem impor um modelo de distribuição angular da radiação difusa. O cálculo de transposição e suas hipóteses pertencem à subseção 3.1; o albedo e a instalação são desenvolvidos nas subseções 2.2 e 2.4. A Seção 1 estabelece as grandezas necessárias a essas etapas, sem antecipar seus resultados (SENGUPTA et al., 2024, cap. 2, p. 1 e 9–11).

| Grandeza | Definição e plano | Unidade |
|:--|:--|:--|
| $G_{0n}$ | Irradiância extraterrestre normal ao feixe | W/m² |
| $G_{0h}$ | Projeção extraterrestre na horizontal | W/m² |
| DNI | Componente direta referida à normal solar | W/m² |
| DHI | Componente difusa recebida na horizontal | W/m² |
| GHI | Irradiância global recebida na horizontal | W/m² |
| POA | Irradiância recebida no plano do arranjo | W/m² |
| $H$ | Irradiação no plano e intervalo declarados | J/m², Wh/m² ou kWh/m² |

Fonte: elaboração de Samuel Constantino Teixeira a partir de Duffie, Beckman e Blair (2020, p. 9–15) e Sengupta et al. (2024, cap. 2, p. 9–11).

## 1.2.4 Aplicação ao PVDAQ 2107 e continuidade

No conjunto utilizado pelo capítulo, a POA observada constitui a entrada radiométrica local da cadeia principal. O arquivo preparado preserva o início de cada intervalo em UTC e um indicador da presença das três amostras previstas na agregação de 15 minutos. A posição solar é calculada no ponto médio, enquanto a POA conserva a natureza de média do intervalo. A Figura G01, discutida em 1.1, apresenta essas informações com suas diferentes origens explicitadas. Esse procedimento permite relacionar geometria e observação sem transformar o sensor POA em um sensor horizontal.

As componentes GHI, DNI e DHI eventualmente reconstruídas a partir da POA permanecem estimativas dependentes de modelos e hipóteses. A reprodução da POA de entrada por uma transposição inversa seguida da transposição direta não constitui validação independente dessas componentes. Essa conclusão resulta da dependência entre entradas e saídas do procedimento, e não de uma comparação realizada com sensores locais adicionais. A verificação das componentes exigiria referências observacionais ou estimativas externas com incerteza e independência documentadas.

A distinção entre potência radiativa, energia integrada e planos de recepção prepara a análise da modulação atmosférica em 1.3. Ela também define o requisito de comparabilidade para 1.4: duas séries somente podem ser confrontadas após compatibilizar a grandeza, o plano, o tempo de integração e o domínio de observação.
