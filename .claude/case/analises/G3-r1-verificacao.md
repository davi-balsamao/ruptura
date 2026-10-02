# G3-r1 — VERIFICAÇÃO DE FONTES (anti-alucinação)

> Verificador de fontes · 02/10/2026 · arquivo verificado: `analises/G3-r1.md` (364 linhas, lido inteiro).
> Método: as 31 URLs da TABELA DE FONTES (que cobrem todas as URLs do corpo) foram reabertas com WebFetch, pedindo os trechos literais.
> Todas as contas marcadas [cálculo] foram refeitas em Python. Todas as tags [dado:] foram conferidas no `dados-case1.md`.
> Este arquivo **não opina sobre a análise**: verifica só se as evidências existem e se dizem o que o analista afirma.

---

## RESUMO — lista objetiva de problemas (o que está errado → o que corrigir)

**Placar:** 31 URLs → 25 OK · 6 OK-PARCIAL · 0 NÃO ENCONTRADO · 0 INACESSÍVEL. Dessas, 4 são FONTE FRACA (somam-se aos status acima).
**Contas:** 41 linhas de conta (~57 operações) refeitas. Todas batem, exceto 1 fora da tolerância (municípios, ~35% → 34,3%).
**Tags [dado:]:** 11 conferidas → 9 OK e 2 OK-PARCIAL.
**Nenhum número foi inventado.** Todos os números citados existem nas fontes. Os problemas são de sentido, de base e de comparabilidade.

### Gravidade ALTA (muda argumento ou veredito)
1. **EY 39%/11% atribuídos à recarga, mas o motivo é geopolítico** (l.102–104 e Suposição 1, l.181). A EY e a Automotive Business dizem que os 39% adiam por "gargalos logísticos e tarifas" ligados a instabilidade geopolítica. Não é por recarga.
   → Retirar o 39%/11% como prova de que "o efeito da barreira é real" e tirá-lo da Suposição 1. Se quiser manter um dado da mesma matéria, use a frase da Automotive Business de que a infraestrutura pública e residencial é "o principal entrave". Ou use os 36%/33% da EY, com a base explicitada (ver item 4).
2. **A série "a relação piora" (14 → 18 → 19,6 → 19,9 → 21,4) mistura definições de frota.** A definição muda ao longo da série:
   - fev/25: "frota… soma 208.344"
   - fev/26: "em circulação no Brasil até fevereiro (411.869)"
   - mai/26 e ago/26: "contabilizados de 2022 a [mês]" (505.806 e 639.133)

   A frota sobe +94 mil em 3 meses (fev→mai/26), contra +110 mil nos 6 meses anteriores, justamente quando a definição muda. Isso é indício de possível quebra metodológica. A Lacuna 13 ressalva só a conta de DC por veículo, não a série nem o veredito. A frase "a relação piora" sustenta o VEREDITO G3.1 e a mensagem do Gráfico 1.
   → Apoiar o "piora" no par com a mesma definição: **mai/26 19,9 → ago/26 21,4**, que continua mostrando piora. Ressalvar a série longa no texto, no Gráfico 1 e na linha do veredito.
3. **"Desconto de 10–20% é o formato de mercado (99, BYD+Raízen)"** (l.143, B7, CONCLUSÃO, IMPLICAÇÃO fase 3). O BYD+Raízen fala só em "preços menores" e "bonificações", **sem percentual**. Os 10–20% da 99 valem para o RJ com EzVolt, para "motoristas parceiros elegíveis". Na matéria de 2025 a 99 dá "até 20%… dependendo do fornecedor e do horário".
   → Reescrever assim: "único precedente com % público: 99Recarga (até 20%; 10–20% no RJ/EzVolt). BYD+Raízen: preço menor sem % divulgado". B7 "(a) CONFIRMADA por benchmark" passa a "confirmada no formato (desconto em rede parceira); a faixa de 10–20% vem de 1 caso".

### Gravidade MÉDIA (base ou trecho distorcido, não muda o veredito)
4. **EY 27% / 33% / 17%: a base é "consumidores que não pretendem adquirir um veículo elétrico"**, um subconjunto. O texto (l.91–93, l.100) e o Gráfico 5 apresentam esses números como "% dos consumidores" e os colocam lado a lado com a Deloitte, cuja base é o total do Brasil (n≈1.000). Além disso, no mesmo parágrafo da EY, o 1º motivo é **36% "falta de estrutura em casa ou no trabalho"**, que foi omitido.
   → Explicitar a base ("entre quem não pretende comprar VE") e separar EY de Deloitte no Gráfico 5. Vale considerar citar os 36% (reforçam a fronteira com G2).
5. **Gráfico 2 coloca "Brasil, só BEV 10,5" ranqueado entre China 10, UE 11 e global 11**, que contam BEV+PHEV. O texto (l.62) admite que não há comparável global só de BEV. Mesmo assim, o gráfico e o Raciocínio G3.1 (l.108, "Os BEV têm ~10,5 por ponto") sugerem paridade com a referência.
   → Tirar a linha BEV do ranking ou anotá-la como "não comparável (só BEV)".
6. **Linha Tupi da tabela G3.2.A.**
   - "rota": a página da Tupi só diz para dirigir até a estação usando Waze ou Google Maps. Não há roteirizador.
   - "99 e BYD Recharge" e "hub OCPI": não aparecem na página da Tupi. Estão corretos, mas em outras fontes: a Cenário Energia diz que a Tupi desenvolveu a integração OCPI e o app BYD Recharge, e a Mercado&Consumo traz a parceria 99+Tupi.
   → Trocar "rota" por "navegação via Waze/Google Maps" e acrescentar as tags #14 e #16 na linha.
7. **Municípios "~35%" (l.78) fica fora da tolerância.** O IBGE conta 5.570 municípios: 1.911 ÷ 5.570 = **34,3%**. Os "25%" da ABVE para 1.363 municípios estão **só no título** da matéria; a conta exata dá 24,5%.
   → Corrigir para "~34%". Fonte aberta: CNN Brasil (16/12/2020), "Dos 5.570 municípios brasileiros…", porque a página do IBGE deu 403 de novo.
8. **"~700 agências Localiza" (IMPLICAÇÃO, fase 4).** O dossiê diz "~700 agências **no Brasil e LatAm**" (#localiza-co).
   → Escrever "~700 agências (Brasil + LatAm)".
9. **Dutra: "a primeira rede é de 2018" (l.82).** A AutoPapo não diz "primeira" nem diz que os carregadores são DC (só informa 25 min para 80% de uma bateria de 22 kWh).
   → Tirar "primeira". Se quiser chamar de DC, achar outra fonte.
10. **Fontes fracas, mantidas mas sinalizadas:**
   - acendebrasil.com.br: clipping da **Exame**. Citar a Exame.
   - mecanicaonline.com.br: "Redação", sem autor. Preferir o comunicado da Volvo.
   - cenarioenergia.com.br: press release das partes interessadas (BYD/EZVolt/Tupi).
   - tupimob.com: página comercial do fornecedor ("+2.800 estações listadas", "+1500 conectadas" são números de marketing).

### Gravidade BAIXA (precisão e redação)
11. **Brasil (ago/26) × IEA (fim/25): datas diferentes, sem ressalva.** Com o dado brasileiro mais próximo, fev/26 = 19,6, a razão é 1,8x. O "~2x" se mantém. → Citar a defasagem na nota de método.
12. **"Sudeste tem a menor fatia de DC" (l.66).** A matéria de ago/26 dá o % DC de N, NE, CO e SE, mas **não o do Sul**. A afirmação é inferência; o Sul tinha 37,2% em mai/26. → "a menor entre as regiões informadas".
13. **Matéria ABVE de ago/26: "4.433 pontos acrescentados entre junho e setembro".** O dado de referência é ago/26 e a conta mai→ago dá 4.437 (DC: 2.796, contra 2.792). É inconsistência da própria fonte; o analista citou corretamente. → Nenhuma correção obrigatória. Opcional: notar a discrepância.
14. **% DC de fev/25 (16,4%) mistura safras.** O numerador (2.430) é retroativo, da matéria de fev/26. O denominador (14.827) vem da matéria de fev/25. → Notar.
15. **#pdf-jornada (l.26): "o passo 3 leva ao passo 5"** omite o passo 4, "Percebe risco na troca". → "passo 3 → 4 → 5".
16. **"Placar de 1 de 5" (l.296) sem tag.** → Acrescentar [dado: dados-case1.md#gap-central].
17. **"A BYD descreve a fragmentação…" (l.90).** O texto é da Agência Cenário Energia, num release; a frase não é atribuída à BYD. → "o release de lançamento do BYD Recharge descreve…".
18. **Dossiê #app: 80,1% × ~70 mil = 56 mil, mas o mesmo item diz 53k MAU.** É inconsistência interna do dossiê, não do analista. → Citar só "53k MAU", ou avisar o orquestrador.
19. **Detalhes que não exigem correção:**
   - A Volvo também cobra R$ 2,50 de taxa por sessão, então o R$ 2,90/kWh subestima o preço efetivo.
   - Os carregadores da Motiva na Dutra servem sobretudo à frota da concessionária e só "poderão" atender usuários. O analista citou corretamente.

---

## TAREFA 1 — URLs e trechos

Legenda: **OK** · **OK-PARCIAL** · **NÃO ENCONTRADO** · **INACESSÍVEL** · **FONTE FRACA** (cumulativo).

| # | Fonte | Números/trechos verificados | Status | Observação |
|---|---|---|---|---|
| 1 | ABVE, "DC quase triplica…" (publ. 28/09/2026, dado ago/26; ABVE+Tupi) | 29.866 ✔; "38,2% (11.397)… DC" ✔; "195,6%… de 3.855 para 11.397" ✔; "4.433… entre junho e setembro, 2.792… 63,0%" ✔; "21,4 veículos elétricos plug-in por ponto" ✔; "contabilizada de 2022 a agosto de 2026, totaliza 639.133" ✔; "49% (313.140)… BEV… dependem totalmente" ✔; "Sudeste… 42,4%… 27,9%" ✔; SP 7.864, PR 2.513, RS 2.422, SC 2.333, MG 2.295 ✔; capital SP 3.101, Brasília 1.225, Rio 1.071 ✔; 1.911 municípios ✔ ("contagem provisória"); 1.156 com DC ✔ | **OK** | Não traz o % DC do Sul (ver item 12). A fonte cita "junho e setembro" para dado de ago/26 (item 13). Não há tabela regional completa em ago/26, então a escolha de mai/26 para o Gráfico 3 está correta. |
| 2 | ABVE, "DC cresce 33% em três meses" (publ. 22/06/2026, dado mai/26) | 25.429 ✔; "19,9 veículos elétricos plug-in por eletroposto" ✔ (frota 505.806, "contabilizados de 2022 a maio de 2026"); DC "Maio de 2026: 8.601" ✔; "nascendo 'rápidas'… corredores logísticos e rodoviários" ✔; tabela regional (SE 11.079/2.709; S 6.115/2.273; NE 4.542/1.962; CO 2.840/1.186; N 859/471) ✔ | **OK** | A soma das linhas (25.435 ≠ 25.429) é da própria fonte, e o analista registrou. |
| 3 | ABVE, "Recarga pública rápida cresce 167%…" (publ. 04/03/2026, dado fev/26) | "21.061 pontos públicos e semipúblicos" ✔; "Eram 2.430 em fevereiro de 2025 e chegaram a 6.479" ✔; "chegou a 19,6/1" ✔ (frota 411.869 "em circulação… até fevereiro"); "meta ideal de 10/1, que exigiria o dobro de pontos" ✔ | **OK** | A definição da frota difere da de mai/26 e ago/26 (item 2 do resumo). |
| 4 | ABVE, "…já está em 25% dos municípios" (publ. 18/02/2025, dado fev/25) | "14.827 eletropostos públicos e semi-públicos" ✔; "índice de 14 veículos por eletroposto" ✔ (frota 208.344); "1.363 municípios… contam com eletropostos" ✔; "25% dos municípios" **só no título** | **OK-PARCIAL** | O 25% vem do título e é arredondado (1.363/5.570 = 24,5%). |
| 5 | Forbes Brasil, "Pontos de recarga… cresce 59%" (publ. 13/09/2025; Redação c/ Reuters; dados ABVE/Tupi) | "em agosto de 2024… 10.622… saltou para os atuais 16.880" ✔; "frota de 302.225 veículos eletrificados plug-in" ✔; "expansão de 59%, para 3.855 eletropostos" ✔ (é **DC**; lentos 13.025; 3.855+13.025 = 16.880) ✔; "um eletroposto para cada 18 veículos" ✔ (302.225/16.880 = 17,9); SP "cerca de 20 veículos por eletroposto" ✔; "Estado somava 4.678 pontos" ✔ | **OK** | — |
| 6 | CNN Brasil, "Brasil… chega a 10 mil pontos" (publ. 20/10/2024; dados ABVE/Tupi) | "Dezembro/2023: 4.300" ✔; "Março/2024: 7.758" ✔; "Julho/2024: 8.800" ✔; "Agosto/2024: 10.622" ✔; "carregadores em estradas torna-se escassa" ✔ (fora das principais rodovias do SE e S, como o analista leu); "manutenção precária de carregadores de uso público" ✔ | **OK** | — |
| 7 | EV Infrastructure News, IEA GEVO 2026 (publ. 21/05/2026; dado fim/2025) | "approximately 11 vehicles per chargepoint" ✔; "ten electric LDVs per public chargepoint in China" ✔; "The EU averaged 11 EVs per public chargepoint" ✔; "the US had 33 electric LDVs per public chargepoint" ✔ | **OK** (fonte secundária da IEA) | Não cita Brasil nem Coreia. Usa estoque de LDVs elétricos (BEV+PHEV). |
| 8 | Deloitte, Global Automotive Consumer Study 2026 (campo out–nov/2025; n BR≈1.000) | "93%… e 86%… esperam carregar… em locais privados, como residências ou ambientes de trabalho" ✔; "infraestrutura de recarga preocupa 37%… e 67% não têm acesso a um carregador privado" ✔; "autonomia (31% e 37%…) e tempo de carregamento (31% e 39%)" ✔ (BR × global) | **OK** | — |
| 9 | EY, Mobility Consumer Index (publ. 14/05/2026) | "27% indagam sobre a qualidade e interoperabilidade" ✔; "33% mencionam a ausência de estações públicas" ✔; "17% citam a autonomia e incertezas sobre custos" ✔ | **OK-PARCIAL** | Os três números valem "entre os consumidores que **não pretendem adquirir** um VE", base não informada pelo analista. O 1º motivo desse grupo (36%, casa/trabalho) foi omitido (item 4). |
| 10 | Automotive Business, pesquisa EY (publ. 15/05/2026) | "39%… adiando ou reconsiderando a compra" ✔; "11%… desistiram de comprar um EV" ✔ | **OK-PARCIAL — SENTIDO DIFERENTE** | O motivo declarado é **"gargalos logísticos e tarifas associadas a instabilidades geopolíticas"**, não recarga. O analista usa como efeito da barreira de recarga (item 1). |
| 11 | Mecânica Online, Volvo encerra gratuidade (publ. 07/06/2026; Redação) | "R$ 2,90/kWh em carregadores rápidos (DC)" ✔ (AC R$ 2,00; taxa R$ 2,50 por sessão); "a partir de 15 de junho… passarão a pagar" ✔; "conecta mais de 31 mil km de rodovias" ✔ | **OK** + **FONTE FRACA** | Redação sem autor. Preferir o release da Volvo. |
| 12 | Vrum, "A guerra dos eletropostos" (publ. 07/08/2026; Lucas Maia Gomes) | "O valor por kWh pode variar entre R$ 2 e R$ 2,80." ✔ (refere-se a recarga rápida pública) | **OK** | — |
| 13 | Vrum, "Quanto custa carregar em casa vs postos" (publ. 07/08/2026) | "valor médio de R$ 2,50… Dolphin custaria R$ 112,25" ✔; bateria de 44,9 kWh ✔ | **OK** | — |
| 14 | Cenário Energia, BYD Recharge + EZVolt + Tupi (publ. 19/05/2025) | "a fragmentação das plataformas de recarga" ✔; "sem a necessidade de utilizar aplicativos distintos" ✔; "protocolo OCPI (Open Charge Point Interface)" ✔; "acesso direto a mais de 450 eletropostos da EZVolt" ✔; a Tupi desenvolveu a integração e o app BYD Recharge ✔ | **OK-PARCIAL** + **FONTE FRACA** | É press release ("Agência Cenário Energia"). A frase da "fragmentação" não é atribuída à BYD (item 17). Não menciona desconto. |
| 15 | Tupi, app de recarga (página comercial) | "Os pontos azuis são carregadores que usam o software de gestão da Tupi" ✔; "com informações de disponibilidade em tempo real" ✔; "+2.800 estações listadas" ✔; "+1500 estações conectadas" ✔; pagamento no app ✔ | **OK-PARCIAL** + **FONTE FRACA** | Não há "rota" (só "dirija… com Waze ou Google Maps"). Não menciona 99, BYD nem OCPI (item 6). É página de vendedor. |
| 16 | Mercado&Consumo, 99 lança app de recarga (publ. 05/09/2025) | "fruto de uma parceria entre a 99 e a Tupi Mobilidade" ✔; "descontos exclusivos de até 20%… dependendo do fornecedor" ✔ (continua: "e do horário da recarga") | **OK** | Quem banca o desconto não é informado (o analista registrou como lacuna). |
| 17 | Olhar Digital, 99 no RJ (publ. 21/09/2026) | "mais de 1,5 mil estações, soma 34 mil recargas e três mil usuários" ✔; "descontos de 10% a 20% para motoristas parceiros elegíveis" ✔ | **OK** | Os 10–20% valem para o lançamento no RJ com EzVolt. Quem banca não é informado. |
| 18 | CNN Brasil, Raízen + BYD (publ. 02/02/2024) | "terão benefícios ao utilizar a rede Shell Recharge, pagando preços menores" ✔ (+ "bonificações"); "600 pontos de recarga rápida… Shell Recharge" ✔ ("nos próximos três anos") | **OK** | **Não informa %** de desconto, então não sustenta "10–20%" (item 3). |
| 19 | electrive, Sixt charge + Elli (publ. 27/02/2024) | "first major provider in the industry to offer its customers a charging solution" ✔; "almost 400,000 charging points in Elli's public charging network" ✔; "accessible without a charging card" ✔ | **OK** | — |
| 20 | Auto Rental News, Hertz + bp pulse (publ. 27/09/2022) | "Hertz customers, including taxi and ride sharing drivers, as well as the general public" ✔; hubs de recarga rápida em locais da Hertz ✔ | **OK** | Precedente de 2022: anúncio, não resultado. |
| 21 | Tecnologística, Rota Sul (publ. 13/09/2022) | "Movida, Nissan, a Rede de Postos SIM e a Zletric lançaram a Rota Sul" ✔; "carregadores rápidos para a cada 200 km" ✔ | **OK** | A fonte diz "lançaram"; o analista diz "co-criou". Equivalente aceitável. |
| 22 | O Tempo, EPR Triângulo (publ. 26/08/2026) | "um equipamento a cada 45 quilômetros (km) nos trechos contemplados" ✔; "seis carregadores rápidos de 60… kW" ✔ | **OK** | — |
| 23 | Agência iNFRA, ANTT/Motiva Dutra (publ. 29/09/2026) | "também poderão atender usuários da rodovia" ✔ | **OK** | O foco principal é a frota da concessionária (R$ 84 mi, 253 veículos); o analista citou com "poderão". |
| 24 | AutoPapo, rede na Dutra (publ. 19/07/2018; BMW + EDP) | "distância máxima de 122 quilômetros entre si" ✔ | **OK-PARCIAL** | A fonte **não** diz "primeira rede" e não classifica os carregadores como DC (item 9). Dado de 8 anos atrás. |
| 25 | Google, Places API (New), referência REST | `evChargeOptions` ✔; "Number of connectors in this aggregation that are currently available." ✔; outOfServiceCount ✔; maxChargeRateKw ✔ | **OK** | — |
| 26 | Google Maps Platform, preços | "Places API Nearby Search Enterprise + Atmosphere": **US$ 40,00/1.000** (0–100 mil) ✔; US$ 32,00 (100–500 mil); 1.000 chamadas grátis/mês | **OK** | O SKU está certo: `places.evChargeOptions` dispara Enterprise + Atmosphere (confirmado na doc de Nearby Search). |
| 27 | PlugShare API | "do not provide personal or non-commercial licenses to use our data at this time" ✔; uso por "major automakers" em apps e "in-vehicle nav" ✔ | **OK** | — |
| 28 | Open Charge Map, Develop | "Data imported from 3rd party Data Providers is copyright the original Data Provider" ✔; CC BY 4.0 para dado de usuários ✔; atribuição obrigatória ✔ | **OK** | — |
| 29 | Acende Brasil (clipping), Localiza 10 mil BYD (publ. 20/03/2026) | "acordo com a BYD para a compra de 10 mil veículos híbridos e elétricos" ✔ ("ao longo dos próximos dois anos"); menciona "carro por assinatura" ✔ | **OK** + **FONTE FRACA** | É republicação de matéria da **Exame**. Citar a original. |
| 30 | Localiza Assinatura, página BYD | "BYD Dolphin - EV 44KW Elétrico AT" ✔; "BYD Song - Plus DM-I Turbo Híbrido" ✔; "BYD King - GL DM-I Híbrido Phev" ✔; nenhuma menção a recarga, eletroposto, wallbox, carregador ou mapa ✔ | **OK** | — |
| 31 | Forbes Brasil, Meoo vira Localiza Assinatura (publ. 29/09/2026) | "acesso exclusivo a veículos de todos os tipos, incluindo carros elétricos" ✔; sem menção a recarga ✔ | **OK** | — |

**Fonte extra, usada pelo verificador (não pelo analista):** CNN Brasil, 16/12/2020: "Dos 5.570 municípios brasileiros…", para o total de municípios. A página do IBGE (agenciadenoticias) deu 403 de novo.

---

## TAREFA 2 — Contas (tolerância 0,5%)

| # | Onde | Fórmula | Analista | Verificador | Bate? |
|---|---|---|---|---|---|
| 1 | l.43 | 29.866 ÷ 4.300 | 6,9x | 6,946x | ✔ |
| 2 | l.43 | dez/23 → ago/26 | 32 meses | 32 meses | ✔ |
| 3 | l.43 | 29.866 ÷ 16.880 | 1,77 (+77%) | 1,769 | ✔ |
| 4 | l.44 | 2.430 ÷ 14.827 | 16,4% | 16,39% | ✔ (safras diferentes, item 14) |
| 5 | l.44 (fonte) | 11.397 ÷ 3.855 − 1 | 195,6% | 195,6% | ✔ |
| 6 | l.44 (fonte) | 2.792 ÷ 4.433 | 63,0% | 62,98% | ✔ |
| 7 | l.53 | 21,4 ÷ 11 | 1,9x | 1,945x | ✔ (com fev/26: 19,6 ÷ 11 = 1,78x) |
| 8 | l.54 | 639.133 ÷ 10 | 63.913 | 63.913 | ✔ |
| 9 | l.54 | 63.913 ÷ 29.866 | 2,14 | 2,140 | ✔ |
| 10 | l.47 (fonte) | 639.133 ÷ 29.866 | 21,4 | 21,40 | ✔ |
| 11 | l.56–59 (fonte) | 208.344/14.827; 302.225/16.880; 411.869/21.061; 505.806/25.429 | 14; 18; 19,6; 19,9 | 14,05; 17,90; 19,56; 19,89 | ✔ (definições de frota diferentes, item 2) |
| 12 | l.62 | 313.140 ÷ 29.866 | 10,5 | 10,48 | ✔ |
| 13 | l.63 | 302.225 ÷ 3.855 | 78,4 | 78,40 | ✔ |
| 14 | l.63 | 639.133 ÷ 11.397 | 56,1 | 56,08 | ✔ |
| 15 | l.70 | 7.864 ÷ 29.866 | 26,3% | 26,33% | ✔ |
| 16 | l.70 | 7.864+2.513+2.422+2.333+2.295 | 17.427 | 17.427 | ✔ |
| 17 | l.70 | 17.427 ÷ 29.866 | 58,4% | 58,35% | ✔ |
| 18 | l.77 | 1.156 ÷ 1.911 | 60,5% | 60,49% | ✔ |
| 19 | l.78 | 25% × 1.911 ÷ 1.363 | 35% | 35,05% (aritmética ok) / **34,3%** com IBGE 5.570 | ✘ **fora da tolerância** (diferença relativa de 2,2%): corrigir para ~34% |
| 20 | l.125 | 40 ÷ 1.000 | US$ 0,04 | 0,04 | ✔ |
| 21 | l.126 | 53.000 × 4 × 0,04 | US$ 8.480 | 8.480 | ✔ como teto. Com as faixas reais (1 mil grátis, US$ 40 até 100 mil e US$ 32 acima), dá ≈ US$ 7.544 |
| 22 | l.150 (fonte) | 44,9 × 2,50 | R$ 112,25 | 112,25 | ✔ |
| 23 | l.151 | 112,25 × 0,10 / × 0,20 | 11,2 / 22,5 | 11,225 / 22,45 | ✔ |
| 24 | l.151 | 44,9 × 2,90 | 130,2 | 130,21 | ✔ |
| 25 | l.151 | 130,21 × 0,10 / × 0,20 | 13 / 26 | 13,02 / 26,04 | ✔ |
| 26 | l.152 | 2 × 11,225 / 2 × 22,45 | R$ 22–45 | 22,45 / 44,90 | ✔ |
| 27 | Gráf. 1 | 3.855 ÷ 16.880 | 22,8% | 22,84% | ✔ |
| 28 | Gráf. 1 | 6.479 ÷ 21.061 | 30,8% | 30,76% | ✔ |
| 29 | Gráf. 1 | 8.601 ÷ 25.429 | 33,8% | 33,82% | ✔ |
| 30 | Gráf. 1 | 11.397 ÷ 29.866 | 38,2% | 38,16% | ✔ |
| 31 | Gráf. 1 (fonte) | 6.479 ÷ 2.430 − 1 | "167%" | 166,6% | ✔ |
| 32 | Gráf. 3 | 11.079 ÷ 25.429 / 2.709 ÷ 11.079 | 43,6% / 24,5% | 43,57% / 24,45% | ✔ |
| 33 | Gráf. 3 | 6.115 ÷ 25.429 / 2.273 ÷ 6.115 | 24,0% / 37,2% | 24,05% / 37,17% | ✔ |
| 34 | Gráf. 3 | 4.542 ÷ 25.429 / 1.962 ÷ 4.542 | 17,9% / 43,2% | 17,86% / 43,20% | ✔ |
| 35 | Gráf. 3 | 2.840 ÷ 25.429 / 1.186 ÷ 2.840 | 11,2% / 41,8% | 11,17% / 41,76% | ✔ |
| 36 | Gráf. 3 | 859 ÷ 25.429 / 471 ÷ 859 | 3,4% / 54,8% | 3,38% / 54,83% | ✔ |
| 37 | Gráf. 3 | soma das linhas | 25.435 | 25.435 (DC: 8.601 ✔) | ✔ |
| 38 | Gráf. 3 | (11.079 + 6.115) ÷ 25.429 | 67,6% | 67,62% | ✔ |
| 39 | Gráf. 4 | 2.513 / 2.422 / 2.333 / 2.295 ÷ 29.866 | 8,4 / 8,1 / 7,8 / 7,7% | 8,41 / 8,11 / 7,81 / 7,68% | ✔ |
| 40 | Gráf. 4 | 3.101 / 1.225 / 1.071 ÷ 29.866 | 10,4 / 4,1 / 3,6% | 10,38 / 4,10 / 3,59% | ✔ |
| 41 | Gráf. 6 | os mesmos das linhas 22–25 | — | — | ✔ |

**Total:** 41 linhas, ~57 operações. Todas batem, exceto a #19, que fica fora da tolerância.

### Os números de CONCLUSÃO / VEREDITO / IMPLICAÇÃO derivam do arquivo?

| Número ou afirmação | Onde aparece | Deriva de | Status |
|---|---|---|---|
| 21,4 vs ~11 por ponto | Veredito G3.1 | B, Gráf. 2 | ✔ (falta a ressalva de método e data na linha do veredito) |
| "ABVE diz que precisa dobrar" | Veredito G3.1 | Fonte #3 (fev/26) + conta #9 (2,14x) | ✔ |
| "a relação piora" | Veredito G3.1, Gráf. 1 | Série 14 → 21,4 | **INCONSISTENTE (parcial)**: a série mistura definições de frota (item 2). O par mai→ago/26 sustenta. |
| "rede DC triplicou em 12 meses" | Veredito G3.1 | Conta #5 (2,96x) | ✔ |
| "desconto de 10–20%" | CONCLUSÃO, B7, IMPLICAÇÃO | Tabela G3.2.B, linha 99 (só RJ/EzVolt) | **INCONSISTENTE (parcial)**: o texto atribui a faixa também a BYD+Raízen, que não tem % (item 3) |
| "bancado por operadoras" | CONCLUSÃO | Suposição 2 (declarada) | ✔ declarada como suposição |
| Suposição 1 "…pelos 39% que adiam (EY)" | Suposições | Fonte #10 | **INCONSISTENTE**: o 39% é motivo geopolítico (item 1) |
| R$ 22–45 por assinante/mês | IMPLICAÇÃO | Contas #26 | ✔ |
| ~US$ 8,5 mil/mês | IMPLICAÇÃO, Suposição 3 | Conta #21 | ✔ (como teto) |
| 10 mil BYD; 600 DC; 450+; 31 mil km | IMPLICAÇÃO | Fontes #29, #18, #14, #11 | ✔ |
| ~700 agências | IMPLICAÇÃO, fase 4 | #localiza-co | **OK-PARCIAL**: o número é Brasil + LatAm (item 8) |
| 93% em local privado | Recado para a síntese | Fonte #8 | ✔ |
| 80% para ICE | IMPLICAÇÃO, KPIs | #conversao | ✔ |
| "1 de 5 → até 3 de 5" | Recado para a síntese | #gap-central (sem tag) + suposição declarada | ✔ (falta a tag, item 16) |

---

## TAREFA 3 — Tags [dado:]

| Tag | Linha(s) | Existe no dossiê? | Valor ou trecho do analista | Valor no dossiê | Status |
|---|---|---|---|---|---|
| #preoc-2 | 23, 163 | ✔ | "Locais para recarga na rotina…" → NÃO ATENDE, "não conta com mapa de carregamento" | Idêntico | **OK** |
| #preoc-5 | 24, 163 | ✔ | NÃO ATENDE; app sem mapa | Idêntico | **OK** |
| #pdf-dores-cliente | 26 | ✔ | "insegurança sobre autonomia e disponibilidade de pontos de recarga" | Idêntico | **OK** |
| #pdf-jornada | 26, 157, 181 | ✔ | "passo 3 … leva ao passo 5" | Jornada 3 → 4 ("Percebe risco na troca") → 5 | **OK-PARCIAL**: omite o passo 4 (item 15) |
| #pdf-risco-compra | 27 | ✔ | "a infraestrutura que ainda está se formando" | Idêntico | **OK** |
| #preoc-fora-top10 | 28, 101 | ✔ | "Autonomia insuficiente para meu uso" fora do top 10 | Idêntico | **OK** |
| #app | 29, 124, 126, 158, 288 | ✔ | 80,1% dos ~70 mil; 53k MAU; telemetria de bateria | "~80% dos ~70 mil… (80,1%); 53k MAU… nível de combustível e bateria" | **OK** (o dossiê é inconsistente consigo mesmo: 80,1% × 70 mil = 56 mil ≠ 53k; item 18) |
| #conversao | 30, 157, 287, 292 | ✔ | 80% dos leads de VE que assinaram escolheram ICE | Idêntico | **OK** |
| #base-58 | 158 | ✔ | survey #58 feito por WhatsApp | "(survey por WhatsApp)" | **OK** |
| #localiza-co | 290 | ✔ | "~700 agências" | "~700 agências **no Brasil e LatAm**" | **OK-PARCIAL** (item 8) |
| #gap-central | (não usada) | ✔ | "placar de 1 de 5" (l.296) sem tag | "apenas 1 das 5" | Falta a tag (item 16) |

---

## TAREFA 4 — Comparabilidade

| # | Comparação | Problema de base | Explicitado no arquivo? | Ação |
|---|---|---|---|---|
| C1 | Série 14 → 18 → 19,6 → 19,9 → 21,4 (Gráf. 1, l.55–60, Veredito) | Definição da frota: fev/25 "soma"; fev/26 "em circulação até fevereiro"; mai/26 e ago/26 "contabilizados de 2022 a…". A frota acelera exatamente na troca de definição (+94 mil em 3 meses, contra +110 mil nos 6 meses anteriores; depois +133 mil em 3 meses) | **Não.** A Lacuna 13 cobre só a conta de DC por veículo | Ressalvar; apoiar "piora" em mai→ago/26 (mesma definição) |
| C2 | Brasil 21,4 × IEA ~11 (l.53, Gráf. 2, Veredito) | Plug-ins "desde 2022" + pontos semipúblicos (ABVE) × estoque de LDV + pontos públicos (IEA); **datas ago/26 × fim/25** | Método: **sim**. Data: **não** | Acrescentar a data; com fev/26 a razão fica 1,8x |
| C3 | "Brasil só BEV 10,5" no ranking do Gráf. 2 e como atenuante (l.108) | BEV × BEV+PHEV das referências | Só no texto (l.62); **não no gráfico nem no raciocínio** | Anotar "não comparável" ou retirar do ranking |
| C4 | DC por veículo 78,4 → 56,1 (l.63) | Frota ago/25 (302.225) × ago/26 ("desde 2022") | **Sim** (l.63, Lacuna 13) | — |
| C5 | % DC fev/25 = 16,4% (l.44, Gráf. 1) | Numerador retroativo (matéria de fev/26) × denominador original (matéria de fev/25) | Não | Nota curta |
| C6 | Gráfico 5: Deloitte (37%, 67%, 93%, 31%) lado a lado com EY (33%, 27%, 17%); l.100: "na EY, só 17%…" | Deloitte = total BR (n≈1.000) × EY = **só quem não pretende comprar VE** | **Não** | Explicitar a base EY e separar no gráfico |
| C7 | 39%/11% (EY) como efeito da barreira de recarga | Motivo é geopolítico/tarifas | **Não** (erro de sentido) | Retirar (item 1) |
| C8 | 10–20% "formato de mercado (99, BYD+Raízen)" | 99: 1 cidade (RJ), motoristas de app, faixa depende de fornecedor e horário; BYD+Raízen sem % | **Não** | Reescrever (item 3) |
| C9 | Estado de SP ~20 (ago/25) × Brasil 18 (ago/25) | Mesma fonte e mesma data | Sim | — (no Gráf. 2, SP de ago/25 aparece ao lado do Brasil de ago/26, mas a coluna de data deixa isso claro) |
| C10 | Gráf. 3 regional (mai/26) × Sudeste 42,4% (ago/26) | Datas diferentes | **Sim** (nota do Gráf. 3) | — |
| C11 | Tupi "estações" × ABVE "pontos" | Unidades diferentes | **Sim** (l.95) | — |
| C12 | Municípios: "25%" (título, fev/25) usado para escalar 1.911 (ago/26, "contagem provisória por UF e código municipal") | Arredondamento do título; método de contagem possivelmente diferente | Parcial (Lacuna 12) | Usar IBGE 5.570 → 34,3% |
| C13 | Corredores: Dutra 122 km (2018, tipo de carregador não informado), Rota Sul 200 km (2022, plano "prevê"), EPR 45 km (2026, instalado), Motiva (2026, só aprovado, "poderão") | Anos e status diferentes (plano × instalado) | Datas sim; status parcial | A leitura "eixos SE/S têm DC" deve dizer que parte é plano |
| C14 | Tarifa média R$ 2,50 (Vrum) × Volvo R$ 2,90 DC | Volvo cobra ainda R$ 2,50 por sessão | Não | Opcional (o benefício por kWh não muda) |
