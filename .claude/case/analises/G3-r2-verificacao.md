# G3-r2 — VERIFICAÇÃO DE FONTES (anti-alucinação, modo DELTA)

> Verificador de fontes · 02/10/2026 · arquivo verificado: `analises/G3-r2.md` (485 linhas, lido inteiro).
> Base: `G3-r1-verificacao.md` (o que não mudou não foi refeito) e `G3-r1-critica.md` (19 itens).
> Método: toda URL nova e todo trecho novo em URL antiga foram reabertos com WebFetch, pedindo o trecho literal.
> Todas as contas do arquivo foram refeitas em Python (tolerância 0,5%). As tags [dado:] novas foram conferidas no `dados-case1.md`.
> Este arquivo **não opina sobre a análise**. Verifica só se a evidência existe, se diz o que o analista afirma e se as contas batem.

---

## RESUMO — problemas remanescentes (o que está errado → o que corrigir)

**Placar das fontes novas ou alteradas:** 9 URLs novas → 8 OK e 1 OK + FONTE FRACA (Mecânica Online, agora usada só para "31 mil km"). 8 trechos novos em URLs antigas → 7 OK e 1 OK-PARCIAL (EVIN). 0 NÃO ENCONTRADO, 0 INACESSÍVEL.
**Sentido:** nenhuma fonte nova foi usada com sentido trocado. energy.gov, DGABC, SEC 8-K, Electrek, TechCrunch, Localiza, Brazil Journal, EY 36% e Deloitte 67% dizem o que a análise afirma.
**Contas:** 34 linhas (~70 operações). Todas batem. A única fora da tolerância é o "~2,5 anos" da Hertz, que é frase da própria fonte (ver item 2).
**19 itens do crítico:** 19 SIM, 0 PARCIAL, 0 NÃO.
**Gravidade:** não há problema ALTO nem MÉDIO. Os 8 itens abaixo são de precisão e redação e não mudam veredito.

### Gravidade BAIXA
1. **Remissão errada: "Os BYD estão na oferta da Assinatura (fonte #30)" (l.200).** Na tabela de fontes da r2, a #30 é a PlugShare. A página da Assinatura BYD é a **#34** (a numeração #30 é da r1).
   → Trocar "fonte #30" por "fonte #34".
2. **Hertz: "~2,5 anos" (l.184 e IMPLICAÇÃO fase 4, l.384).** O trecho existe na Electrek ("Two and a half years later"), mas ela conta a partir do anúncio do hub da LAX em **out/2022**. Até jul/2025 são 33 meses (≈2,75 anos). Do anúncio citado pela análise (Auto Rental News, 27/09/2022) são 34 meses (≈2,8 anos).
   → Escrever "quase 3 anos (out/2022 → jul/2025)" ou "~2,5 anos, segundo a Electrek". O argumento não muda (o atraso é até maior).
3. **EVIN/IEA (l.79 e l.90).**
   - A l.90 cita "maintaining the ratio", mas a fonte diz **"maintained the ratio"** (frase completa: "This expansion matched the growth rate of the electric LDV fleet and maintained the ratio…"). O sentido (razão global estável em 2025) está correto.
   - A l.79 diz que a razão "é o indicador-síntese que a IEA publica para comparar países". A matéria mostra a razão por país/região (China, UE, EUA), mas não diz que é "indicador-síntese" nem que serve "para comparar países". É caracterização do analista.
   → Corrigir a citação para "maintained the ratio". Reescrever a l.79 como "a IEA publica a razão por país/região (China 10, UE 11, EUA 33)".
4. **EY (l.137–142 e Gráfico 5b): lista parcial e "+".**
   - No mesmo parágrafo da EY há ainda 28% (substituição de bateria), 28% (custo de compra inicial) e 21% (custo de reparo). Esses motivos não são de recarga e foram omitidos. Não há troca de sentido, mas o Gráfico 5b, com o título "Motivo", parece a lista completa.
   - "a infraestrutura (36% privada + 33% pública)": a pergunta é de múltipla resposta, então o "+" sugere uma soma que não vale.
   - "dado de mai/2026" é a data de publicação (14/05/2026). A EY chama a pesquisa de MCI, 6ª edição, 2025.
   → Acrescentar no Gráfico 5b a nota "lista parcial: só motivos ligados a recarga/autonomia; omitidos 28% bateria, 28% custo inicial, 21% reparo". Trocar "36% + 33%" por "36% e 33%". Escrever "publ. mai/2026".
5. **SEC 8-K (l.184): motivo incompleto.** O 8-K dá dois motivos: "eliminate a disproportionate number of lower margin rentals" **e** "reduce damage expense associated with EVs". Também diz que os ~20 mil EVs saem da **frota dos EUA** ("about one-third of the global EV fleet" está correto).
   → "para reduzir aluguéis de margem baixa e o custo de dano (8-K)".
6. **Log de correções diverge do texto (item 3 do quadro, l.14).** O log diz que a "CONCLUSÃO… passa a dizer 'até 20% (precedente 99)'". A CONCLUSÃO (l.257) não cita % nenhum: diz só "desconto em rede parceira a negociar". O texto está aceitável, porque tirar o % resolve o item. O erro é do log.
   → Ajustar o log ("a CONCLUSÃO deixou de citar %; Gráfico 6 e B7 dizem 'até 20% (precedente 99)'") ou inserir o "até 20% (precedente 99)" na CONCLUSÃO.
7. **Datas de página.**
   - energy.gov (l.96, Gráf. 2, fonte #8): a página tem data de **08/11/2024**, e a análise registra só "acesso em out/2026".
   - Localiza (l.198): a página **não tem data**. O "dado de fev/2026" vem do Brazil Journal (publicado em 12/02/2026). A tabela de fontes já diz isso; o corpo não.
   → energy.gov: "página de nov/2024". Localiza: "página sem data; acordo noticiado em fev/2026 (BJ)".
8. **Opcional (comparabilidade): SP ~20 (ago/25) no veredito e no Gráfico 2.** É uma razão de ago/25 com frota de definição não declarada, a mesma ressalva que a análise aplica ao Brasil 18 de ago/25 (Gráfico 2) e à Lacuna 2. A linha de SP no Gráfico 2 e a do veredito não repetem a ressalva. Não muda o veredito: SP e Brasil saem da mesma fonte e da mesma data.
   → Acrescentar "(frota com definição não declarada)" na linha de SP do Gráfico 2.

---

## TAREFA 1 — Fontes novas ou alteradas

Legenda: **OK** · **OK-PARCIAL** · **NÃO ENCONTRADO** · **INACESSÍVEL** · **FONTE FRACA** (cumulativo).

### 1a. URLs novas na r2

| # r2 | Fonte | Trechos/números verificados | Status | Sentido / observação |
|---|---|---|---|---|
| 8 | energy.gov, National EV Charging Network | "About 80 percent of charging happens at home." ✔ (seguido de "When you're on the go, you can use public charging…") | **OK** | Refere-se aos EUA ✔. A análise usa o dado só para explicar por que a razão de 33 é tolerada lá ✔. A página é de 08/11/2024 (item 7). |
| 11 | DGABC, "Volvo muda regras e passa a cobrar…" (05/06/2026, Vagner Aquino) | "R$ 2,90 por kWh nos carregadores rápidos (DC)" ✔ (AC R$ 2,00); "taxa de conectividade de R$ 2,50 por sessão de recarga" ✔; "75 eletropostos com mais de 140 conectores" ✔; "A partir de 15 de junho… passarão a pagar" ✔; não menciona "31 mil km" ✔ (como a análise diz) | **OK** | Substitui bem a Mecânica Online, com autor e data. "Encerrou a recarga gratuita em 15/06/2026" ✔. |
| 12 | Mecânica Online (já verificada na r1) | Agora usada só para "conecta mais de 31 mil km de rodovias" ✔ (r1) | **OK** + **FONTE FRACA** | Rotulada como fraca no corpo e na tabela ✔. Não reaberta (não mudou). |
| 21 | Electrek, bp pulse LAX (23/07/2025) | "Two and a half years later, bp pulse has officially cut the ribbon…" ✔; "first of several more hubs… in collaboration with Hertz" ✔ (sustenta "1º hub") | **OK** | A contagem dos "2,5 anos" começa em out/2022 (≈2,75 anos até jul/2025; item 2). A fonte diz que o hub "will soon formally open to the public": é corte de fita, mas "inaugurado" é aceitável. |
| 22 | SEC 8-K Hertz (11/01/2024) | "sell approximately 20,000 electric vehicles ("EVs") from its U.S. fleet" ✔; "about one-third of the global EV fleet" ✔; "reduce damage expense associated with EVs" ✔ | **OK** | Fonte primária. Há também o motivo "lower margin rentals", que foi omitido (item 5). Sentido preservado. |
| 23 | TechCrunch, Tim De Chant (12/01/2024) | "Include a map of compatible charging locations either on the company's website or app (preferably both)." ✔. O autor liga o fracasso à experiência de recarga (Supercharger incompatível, carregador do hotel quebrado, falta de carregador nível 1) ✔ | **OK** | Peça de análise/opinião, e a análise declara "(opinião do autor)" ✔. |
| 32 | Localiza, "Alugar um carro elétrico BYD" | "prevê a compra de 10 mil veículos híbridos e elétricos nos próximos dois anos" ✔; sem menção a recarga, eletroposto, wallbox ou mapa | **OK** (primária) | A página não tem data (item 7). "Acordo de compra… em 2 anos" ✔. O erro da r1 ("fechou a compra") foi corrigido. |
| 33 | Brazil Journal (12/02/2026) | "A Localiza fechou um acordo com a BYD para comprar 10 mil veículos híbridos e elétricos nos próximos dois anos." ✔ | **OK** | Não menciona assinatura nem recarga. A análise não afirma que menciona ✔. |
| 36 | CNN Brasil, "Dos 5.570 municípios…" (16/12/2020) | "Dos 5.570 municípios brasileiros, oito representam 25% do PIB nacional" ✔; fonte IBGE ✔ | **OK** (secundária do IBGE) | É a fonte que o verificador da r1 indicou. O IBGE deu 403. |

### 1b. Trechos novos em URLs que já estavam na r1

| # r2 | Fonte | Trecho novo | Status | Observação |
|---|---|---|---|---|
| 7 | EVIN (IEA GEVO 2026) | "ratio of electric LDVs to public chargepoints at approximately 11 vehicles per chargepoint" ✔ (dentro de "…and maintained the ratio of electric LDVs…") | **OK-PARCIAL** | "maintaining the ratio" (l.90) não é literal; o texto diz "maintained" (item 3). "Indicador-síntese… para comparar países" é caracterização do analista (item 3). |
| 9 | Deloitte, GACS 2026 | "Entre os brasileiros que desejam realizar a recarga residencial, 67% não possuem carregadores" ✔ (a página traz também "67% não têm acesso a um carregador privado"); "93%… esperam carregar seus veículos elétricos em locais privados" ✔; "No Brasil, o levantamento envolveu 1.000 pessoas" ✔ (n≈1.000 ✔); campo "entre outubro e novembro de 2025" ✔ | **OK** | Base dos 67% ("quem deseja recarga residencial") declarada corretamente no Gráfico 5a ✔. |
| 10 | EY, MCI (publ. 14/05/2026) | "Entre os consumidores que não pretendem adquirir um veículo elétrico, 36% apontam a falta de estrutura em casa ou no trabalho" ✔; 33%, 27% e 17% ✔ (r1); n = 1.000 no Brasil | **OK** | O 36% diz o que a análise afirma ✔ (1º motivo do grupo ✔). Lista parcial (28%, 28% e 21% omitidos) e "36% + 33%" (item 4). |
| 2 | ABVE mai/26 | Linhas da tabela regional ("Sudeste 9.380 11.079 18,1% 2.155 2.709 25,7%" etc.) ✔. As colunas da fonte são total fev, total mai, evolução, DC fev, DC mai, evolução DC. Valores de mai/26 usados no Gráf. 3 ✔. "contabilizados de 2022 a maio de 2026, totaliza 505.806" ✔ | **OK** | O "trecho" é uma linha de tabela reconstruída, com valores idênticos. Total fev na tabela = 21.060 (soma das linhas 21.061); diferença da própria fonte e irrelevante. |
| 3 | ABVE fev/26 | "total de veículos elétricos plug-in em circulação no Brasil até fevereiro (411.869)" ✔ | **OK** | Confirma a definição diferente (nota C) ✔. |
| 4 | ABVE fev/25 | "Atualmente, a frota de veículos elétricos plug-in no Brasil soma 208.344 unidades" ✔. Não diz desde quando conta ✔ ("origem não declarada") | **OK** | — |
| 20 | Auto Rental News | Publicada em 27/09/2022 ✔; trecho de clientes, motoristas de app e público ✔ | **OK** | — |
| 34 | Localiza Assinatura BYD | "BYD Song - Plus DM-I Turbo Híbrido" ✔ (r1) | **OK** | Já verificada na r1. |

**Fontes 403 declaradas pelo analista (IEA, bp.com, InsideEVs, Sixt, IBGE, Volvo, anl.gov):** não usadas como evidência ✔. O dado "IEA Brasil 17 → 24", visto em snippet, aparece só na lista de descartadas e na Lacuna 1 ✔.

---

## TAREFA 2 — Contas (todas refeitas; tolerância 0,5%)

| # | Onde | Fórmula | Analista | Verificador | Bate? |
|---|---|---|---|---|---|
| 1 | l.69, Gráf. 1 | 29.866 ÷ 4.300 | 6,9x (~7x) | 6,946 | ✔ |
| 2 | l.69 | dez/23 → ago/26 | 32 meses | 32 | ✔ |
| 3 | l.69 | 29.866 ÷ 16.880 | 1,77 (+77%) | 1,769 | ✔ |
| 4 | l.71 (fonte) | 11.397 ÷ 29.866 | 38,2% | 38,16% | ✔ |
| 5 | l.72 (fonte) | 11.397 ÷ 3.855 − 1 | 195,6% | 195,64% | ✔ |
| 6 | l.73 (fonte) | 2.792 ÷ 4.433 | 63,0% | 62,98% | ✔ |
| 7 | l.73 (nota nova) | 29.866 − 25.429 | 4.437 | 4.437 (DC: 2.796) | ✔ |
| 8 | l.74, Gráf. 1 | 2.430 ÷ 14.827 | 16,4% | 16,39% | ✔ (nota de safra presente) |
| 9 | l.88 | 21,4 ÷ 11 | 1,95 → 1,9x | 1,945 | ✔ |
| 10 | l.89 | 19,6 ÷ 11 | 1,78 → 1,8x | 1,782 | ✔ |
| 11 | l.83 (fonte) | 639.133 ÷ 29.866 | 21,4 | 21,40 | ✔ |
| 12 | l.101 (fonte) | 505.806 ÷ 25.429 | 19,9 | 19,89 | ✔ |
| 13 | l.101 | 639.133 ÷ 505.806 | 1,264 (+26,4%) | 1,2636 | ✔ |
| 14 | l.101 | 29.866 ÷ 25.429 | 1,174 (+17,4%) | 1,1745 | ✔ |
| 15 | l.103 | 313.140 ÷ 29.866 | 10,5 | 10,48 | ✔ |
| 16 | l.103/158 (fonte) | 313.140 ÷ 639.133 | 49% ("metade") | 48,99% | ✔ |
| 17 | l.104 | 302.225 ÷ 3.855 | 78,4 | 78,40 | ✔ |
| 18 | l.104 | 639.133 ÷ 11.397 | 56,1 | 56,08 | ✔ |
| 19 | Série (fonte) | 208.344/14.827; 302.225/16.880; 411.869/21.061 | 14; 18; 19,6 | 14,05; 17,90; 19,56 | ✔ (marcadas ⚠, sem ligar na série) |
| 20 | l.119, Gráf. 4 | 7.864 ÷ 29.866 | 26,3% | 26,33% | ✔ |
| 21 | l.119 | soma dos 5 estados; ÷ 29.866 | 17.427; 58,4% | 17.427; 58,35% | ✔ |
| 22 | l.123 | 1.156 ÷ 1.911 | 60,5% | 60,49% | ✔ |
| 23 | l.124, Gráf. 4 | 1.911 ÷ 5.570 | 34,3% | 34,31% | ✔ (corrigido em relação à r1) |
| 24 | l.175 | 40 ÷ 1.000 | US$ 0,04 | 0,04 | ✔ |
| 25 | l.176 | 53.000 × 4 × 0,04 | US$ 8.480 (~8,5 mil, teto) | 8.480 | ✔ (pelas faixas reais ≈ US$ 7.544; declarado como teto) |
| 26 | l.206 (fonte) | 44,9 × 2,50 | R$ 112,25 | 112,25 | ✔ |
| 27 | l.207, Gráf. 6 | 44,9 × 2,90 + 2,50 | R$ 132,71 / 132,7 | 132,71 | ✔ (nova) |
| 28 | l.208, Gráf. 6 | 112,25 × 0,10 / × 0,20 | 11,2 / 22,5 ("R$ 11–22") | 11,225 / 22,45 | ✔ |
| 29 | Gráf. 6 | 132,71 × 0,10 / × 0,20 | 13,3 / 26,5 | 13,27 / 26,54 | ✔ (nova) |
| 30 | l.209, CONCLUSÃO | 2 × 11,225 / 2 × 22,45 | R$ 22–45 | 22,45 / 44,90 | ✔ |
| 31 | Gráf. 1 | 3.855/16.880; 6.479/21.061; 8.601/25.429 | 22,8 / 30,8 / 33,8% | 22,84 / 30,76 / 33,82% | ✔ |
| 32 | Gráf. 3 | % da rede e % DC das 5 regiões; SE+S | 43,6/24,5; 24,0/37,2; 17,9/43,2; 11,2/41,8; 3,4/54,8; 67,6% | 43,57/24,45; 24,05/37,17; 17,86/43,20; 11,17/41,76; 3,38/54,83; 67,62% | ✔ (SE é a menor das 5 ✔) |
| 33 | Gráf. 4 | PR, RS, SC, MG, capital SP, BSB, RJ ÷ 29.866 | 8,4 / 8,1 / 7,8 / 7,7 / 10,4 / 4,1 / 3,6% | 8,41 / 8,11 / 7,81 / 7,68 / 10,38 / 4,10 / 3,59% | ✔ |
| 34 | l.184, l.384 | set/2022 (ou out/2022) → jul/2025 | "~2,5 anos" | 34 (33) meses ≈ 2,8 (2,75) anos | ✘ **fora da tolerância, mas é a frase da fonte** (Electrek). Item 2 |
| — | Recado (nota do crítico) | 0,801 × 70.000 | ≈56 mil | 56.070 | ✔ |
| — | Gráf. 3 (colunas de evolução da fonte) | 11.079/9.380 − 1 etc. | 18,1 / 23,4 / 20,5 / 23,7 / 30,7%; DC 25,7 / 35,8 / 33,7 / 36,3 / 51,0% | idem | ✔ (confere o trecho literal reconstruído) |

**Total:** 34 linhas, ~70 operações. Todas batem, exceto a #34, que é redação da fonte e não erro de conta do analista.

---

## TAREFA 3 — Rastreio dos números em VEREDITO / CONCLUSÃO / IMPLICAÇÃO

| Número ou afirmação | Onde aparece | Origem no arquivo | Status |
|---|---|---|---|
| 21,4 VEs/ponto (ago/26) | Veredito agregado | B, Gráf. 1/2, conta #11 | ✔ |
| Critério ≤ ~11 (IEA, fim/25) | Veredito agregado | B (EVIN), Gráf. 2 | ✔ |
| 1,8–1,9x | Veredito, Raciocínio | Contas #9 e #10 | ✔ |
| "é piso pelo viés de método" | Veredito | B (i)/(ii), nota do Gráf. 2 | ✔ (direção argumentada; magnitude declarada como lacuna) |
| EUA 33; ~80% doméstica | Veredito | B (EVIN; energy.gov) | ✔ |
| 19,9 → 21,4 | Veredito, Raciocínio, Gráf. 1 | B, contas #12–14 | ✔ (mesma definição de frota) |
| SP ~20 (ago/25) e Brasil 18 | Veredito SP | D, Gráf. 2 (Forbes) | ✔ (ressalva de definição de frota só na Lacuna 2; item 8, opcional) |
| "DC confirmado só em trechos (EPR 2026)" | Veredito corredores | E (O Tempo) | ✔ |
| ≈2x a média global | CONCLUSÃO | Contas #9 e #10 (1,8–1,9x) | ✔ |
| ~0 se a operadora bancar | CONCLUSÃO | C (l.210), Suposição 2 | ✔ declarado [suposição] |
| R$ 22–45 por assinante/mês | CONCLUSÃO, Fase 3 | Conta #30 + Suposição 5 | ✔ declarado [cálculo sobre suposição] |
| "até 20% (precedente 99)" | Suposição 3, B7, Fase 3, Gráf. 6 | Tabela G3.2.B (Mercado&Consumo, Olhar Digital) | ✔ (o log diz que está na CONCLUSÃO e não está; item 6) |
| até R$ 22 por carga | B7 | Conta #28 (22,45) | ✔ |
| teto ~US$ 8,5 mil/mês; 4 buscas/MAU | Suposição 4, Fase 2 | Conta #25, [suposição] | ✔ |
| CEP de casa/trabalho e "até 3 destinos" | Fase 1 | Parâmetro de desenho da proposta (não é dado) | ✔ (não exige fonte) |
| EZVolt 450+ | Fase 3 | Fonte #14 (release, rotulado) | ✔ |
| EZVolt parceira da 99 no RJ | Fase 3 | Fonte #17 | ✔ |
| Shell 600 DC, fev/2024, 3 anos | Fase 3 | Fonte #18 | ✔ |
| Volvo 75 eletropostos, 140+ conectores, cobra desde 15/06/2026 | Fase 3 | Fonte #11 (DGABC) | ✔ |
| Zletric, Rota Sul 2022 | Fase 3 | Fonte #24 | ✔ |
| 10 mil BYD em 2 anos | Fase 3 | Fontes #32 e #33 | ✔ |
| ~700 agências no Brasil e LatAm | Fase 4 | [dado: #localiza-co] | ✔ (idêntico ao dossiê) |
| Hertz: 1º hub em ~2,5 anos (jul/2025); recuo em EV em 2024 | Fase 4 | Fontes #21 e #22 | **OK-PARCIAL**: "~2,5 anos" é a frase da Electrek; a conta dá ≈2,8 anos (item 2) |
| 80% para ICE | KPIs | [dado: #conversao] | ✔ |
| 93% / 67% | Recado | Fonte #9 (bases declaradas) | ✔ |
| 1 das 5 | Recado | [dado: #gap-central] | ✔ (tag acrescentada) |
| "3 de 5" | Recado | [suposição] declarada | ✔ |
| 56 mil × 53k MAU | Recado | Nota do crítico; conta conferida | ✔ |
| "fonte #30" (Assinatura BYD) | G3.2.B, l.200 | Tabela de fontes: #30 = PlugShare | **INCONSISTENTE**: remissão deveria ser #34 (item 1) |

**Tags [dado:] novas ou alteradas (conferidas no dossiê):**
- #pdf-jornada 3 → 4 → 5 ✔ (dossiê: "3 Dúvidas sobre autonomia, recarga e custos → 4 Percebe risco na troca → 5 Adia ou abandona").
- #gap-central "1 das 5" ✔.
- #localiza-co "~700 agências no Brasil e LatAm" ✔.
- #app "53k MAU" e telemetria de bateria ✔.
- #conversao 80% ✔.
- #base-58 WhatsApp ✔.
- "Decisão acontece enquanto lead" passou a [inferência] ✔.

---

## TAREFA 4 — Checagem dos 19 itens do parecer r1

| # | Item | Atendido? | Evidência na r2 |
|---|---|---|---|
| 1 | EY 39%/11% com sentido trocado | **SIM** | Fora do texto e da Suposição 1. Automotive Business está em "descartadas" com o motivo (l.445). |
| 2 | "Piora" com bases misturadas | **SIM** | Apoiado só em mai→ago/26 (l.101); ⚠ e nota de quebra no Gráf. 1; "subiram de 14" saiu; ressalva simétrica (l.104, Lacuna 8). |
| 3 | 10–20% como "formato de mercado" | **SIM** | "Único precedente com % público: 99" (l.194); Raízen sem %; B7 = (b) SUPOSIÇÃO; Gráf. 6 com "precedente 99". A CONCLUSÃO tirou o % (o log diz outra coisa; item 6). |
| 4 | CONCLUSÃO com perna só de suposição | **SIM** | CONCLUSÃO condicional, com tags [suposição] e [cálculo sobre suposição]; a frase "nenhuma conclusão…" saiu (grep sem ocorrência no corpo). |
| 5 | "Maior alavanca" e "baixo esforço" | **SIM** | "Único item que alcança o ponto do vazamento [inferência]… efeito [suposição], A/B" (Fase 1); "baixo" = [suposição]; veredito "baixo investimento" = Não-comprovável. |
| 6 | Fontes fracas | **SIM** | 10 mil BYD: Localiza + BJ, "acordo de compra… 2 anos" ✔. Volvo: DGABC ✔ + taxa por sessão. Release e página comercial rotulados ✔. Tupi com "navegação via Waze/Google Maps" e #14/#16 ✔. |
| 7 | Tags do dossiê | **SIM** | 3 → 4 → 5; #gap-central; Brasil e LatAm; "app só alcança cliente" virou inferência; só 53k MAU. |
| 8 | EY sem base | **SIM** | Base declarada (l.137, Gráf. 5b, Lacuna 9); 36% incluído; 5a/5b separados; "só 17%" saiu. (Lista parcial, item 4) |
| 9 | Salto sobre o G2 | **SIM** | "Complemento" e "se resolve em casa" sem ocorrência; ficam só 93%/67% como fatos; divisão para G2/síntese. |
| 10 | Veredito G3.1 sem critério | **SIM** | Critério explícito (≤ ~11); EUA tratados com energy.gov; direção do viés; defasagem (1,8x); praças, corredores e agregado separados. |
| 11 | Veredito do galho troca a hipótese | **SIM** | "Hipótese original: Falsa / reformulada → veredito"; G3.2a = Verdadeira, G3.2b = Não-comprovável; tensão do mapa declarada (G3.2-E). |
| 12 | Municípios ~35% | **SIM** | 34,3% com 5.570 (CNN/IBGE); derivação pelo título abandonada. |
| 13 | Fase 3 sem tag | **SIM** | Volvo volume = [suposição]; Tupinambá saiu; Shell "previstos em fev/2024… não verificado". |
| 14 | Corredores | **SIM** | Dutra sem "primeira"/DC; Rota Sul plano; Motiva "poderão"; "Não-comprovável". |
| 15 | Casos únicos e Hertz | **SIM** | "A Sixt fez", "a Volvo encerrou"; desfecho da Hertz com 8-K, Electrek e TechCrunch; risco de pitch. ("~2,5 anos", item 2) |
| 16 | BEV 10,5 | **SIM** | Fora do ranking ("não comparável") e com ressalva no Raciocínio. |
| 17 | Fronteira G1 | **SIM** | Tarifa do B7 = a do G1; R$ 22–45 é custo do negócio; taxa Volvo registrada. |
| 18 | Fronteira G4 | **SIM** | Simulador marcado como interface G4; PHEV condicional à decisão do líder. |
| 19 | Sudeste/Sul e 16,4% | **SIM** | "Menor entre as regiões informadas" (ago/26) e "menor das 5" (mai/26); nota de safra no 16,4%. |

---

## TAREFA 5 — Sentido das fontes novas (o erro da r1 foi uso com sentido trocado)

| Fonte | O que a análise afirma | O que a fonte diz | Sentido |
|---|---|---|---|
| energy.gov | Nos EUA, ~80% da recarga é em casa; por isso a razão 33 é tolerada | "About 80 percent of charging happens at home" (EUA) | **Igual** |
| Deloitte 67% | Entre quem deseja recarga residencial, 67% não têm carregador | Idem, literal | **Igual** |
| EY 36% | 1º motivo de quem não pretende comprar VE: falta de estrutura em casa/trabalho | Idem, literal | **Igual** (lista parcial, item 4) |
| EVIN "maintained" | Razão global estável em 2025 | "matched the growth rate… and maintained the ratio" | **Igual** (citação não literal, item 3) |
| DGABC | Volvo encerrou a gratuidade; R$ 2,90/kWh DC + R$ 2,50/sessão | Idem | **Igual** |
| SEC 8-K | Hertz vende ~20 mil EVs (1/3 da frota global de EV) por custo de dano | Idem + "lower margin rentals"; frota dos EUA | **Igual** (motivo incompleto, item 5) |
| Electrek | 1º hub LAX só em jul/2025, ~2,5 anos depois | "Two and a half years later…"; "first of several more hubs" | **Igual** (conta, item 2) |
| TechCrunch | Liga parte do fracasso à recarga; recomenda mapa no site/app (opinião) | Relatos de falha de recarga; "Include a map of compatible charging locations…" | **Igual** |
| Localiza / Brazil Journal | Acordo de compra de 10 mil BYD em 2 anos (não "fechou a compra") | "prevê a compra… nos próximos dois anos" / "fechou um acordo… para comprar… nos próximos dois anos" | **Igual** |
| CNN 5.570 | Total de municípios (IBGE) | "Dos 5.570 municípios brasileiros" | **Igual** |

**Conclusão da tarefa 5:** nenhuma fonte nova foi usada com sentido trocado.
