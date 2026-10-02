# Verificação de fontes — G1-r1 (CUSTO: a conta do cliente)

> Verificador de fontes (anti-alucinação) · 2026-10-02 · arquivo verificado: `analises/G1-r1.md`
> Escopo: só a existência e a fidelidade das evidências, a aritmética e a comparabilidade. Não avalio o mérito da análise.
> Método: as 27 URLs foram abertas com WebFetch pedindo os trechos literais. Juros e Selic também foram conferidos na fonte primária (API SGS do BCB). Todas as contas foram refeitas em Python.

---

## RESUMO

**Placar:** 27 URLs · **24 OK** · **3 OK-PARCIAL** · **0 NÃO ENCONTRADO** · **0 INACESSÍVEL** · 6 com **FONTE FRACA**. Todas as contas batem dentro de 0,5% (só há diferenças de arredondamento). Todas as tags [dado:] existem e conferem. **Não há número inventado.** Os problemas estão em quatro frases de conclusão/implicação que vão além do que as próprias tabelas mostram, em uma fonte descrita de forma errada e em comparações com bases diferentes.

### Problemas (o que está errado → o que corrigir)

| # | Gravidade | Problema | Correção |
|---|---|---|---|
| P1 | **INCONSISTENTE** | Implicação 4: "Leads com uso ≥ 2.000 km/mês já pagam menos no VE com recarga em casa". O Gráfico 1 do próprio arquivo mostra o VE **+R$ 50,65 mais caro a 2.000 km**. O break-even é 2.133 km. | Trocar por "≥ ~2.130 km/mês com recarga em casa (na grade de franquias, 2.500 e 3.000 km)". |
| P2 | **INCONSISTENTE** | Veredito G1.3 ("somadas, cobrem a diferença de R$ 431") e CONCLUSÃO ("deve ser fechada com desconto de frota e gestão de valor residual"). O Gráfico 5 deixa **≈ +R$ 142 em aberto** depois da A1. Para fechar esse resto, a depreciação em 24 m teria que cair **≥ 2,86 p.p.** (de 13,7% para ≤ 10,8%) [142 ÷ 49,58], e nenhuma fonte mostra isso. A A1 (R$ 289) depende de duas suposições: o repasse do desconto e que o R$ 2.870 de benchmark ainda não embuta desconto. A A8 (comunicação) entra como alavanca, mas **vale R$ 0 sobre a diferença real**, porque os R$ 431 já descontam a energia. Isso também contradiz o autochecklist ("nenhuma conclusão se apoia só em suposição"). | Reescrever como condicional: "podem fechar **se** a Localiza tiver desconto ≥ CNPJ e repassar, **e** reduzir a depreciação em ~3 p.p.". Tirar a A8 da soma que fecha os R$ 431. |
| P3 | **INCONSISTENTE (parcial)** | CONCLUSÃO "ganha do financiamento" e Veredito G1.2 "mais vantajosa que comprar financiado" sem qualificação. Pela tabela do G1.2, isso só vale em SP (assinatura −R$ 333). No RJ a assinatura sai **+R$ 14 mais cara** (empate). | Qualificar: "mais barata que financiar em SP (−R$ 333/mês); empate em estados de IPVA baixo (RJ +R$ 14)". |
| P4 | Impreciso | CONCLUSÃO "empata ou ganha do ICE de entrada a partir de ~2.100 km/mês" e G1.1 "zera em ~2.100 km". A conta dá **2.133 km só com recarga em casa**: 2.311 no mix 70/30 e 2.869 só em DC. A A8 diz "zera ou inverte de 2.000–2.500 km", mas a 2.000 km ainda sobram +R$ 51. | Usar "~2.130 km/mês com recarga em casa (~2.310 no mix 70/30)" em todas as seções. |
| P5 | Fonte mal descrita | Achado-chave 2: o arquivo diz que o consumo de 13,9 km/l "não especifica a versão turbo automática". A fonte (revistacarro) **especifica sim**: é o Onix Plus **1.0 Ecotec aspirado, câmbio manual de 6 marchas**. O número está sendo aplicado ao Onix Plus LTZ 1.0 **TB Aut.**, outra versão. | Corrigir a ressalva e buscar o PBEV do 1.0 turbo automático, ou rotular como [suposição]. O sentido do achado é robusto: para o VE perder a 1.000 km, o ICE teria que gastar menos de R$ 58,50 de gasolina por mês. |
| P6 | Rótulo sem suporte | Insumo "Mensalidade VE alternativa (plano de 36 m) ≈ R$ 2.688". A matéria do Vrum **não liga o valor a 36 meses** (só diz que "os planos mais comuns são de 36 meses") e não nomeia o operador. | Tirar "plano de 36 m" ou marcar [suposição]. |
| P7 | Comparabilidade | O G1.2 compara a assinatura "a partir de R$ 2.870", com prazo e franquia desconhecidos, contra a compra num horizonte de **24 m**. Planos de 24 m costumam ser mais caros. A página da BYD lista como benefício "Seguro para terceiros", enquanto a compra foi modelada com seguro completo (R$ 324/mês). O G1.2 não deixa isso explícito; só a lacuna 2 aparece, e de forma genérica. | Dizer no G1.2 que o prazo e a cobertura da assinatura são desconhecidos e que isso tende a **favorecer a assinatura** no comparativo. O ideal é usar a mensalidade de 24 m com cobertura equivalente. |
| P8 | Comparabilidade | A tarifa base de R$ 0,90 (canalve, base tributária não informada) é "checada" contra o R$ 0,849 da ANEEL (a pv-magazine não diz se inclui impostos). A Cemig sem impostos dá R$ 0,922 (TUSD + TE + bandeira) e com impostos R$ 1,1963. Ou seja, o número da ANEEL parece **sem impostos**, e a "checagem" não valida o 0,90 como tarifa paga pelo consumidor. | Explicitar a base tributária de cada tarifa. Considerar um cenário base com impostos (≈ R$ 1,10–1,20/kWh). Nesse caso o break-even sobe para ~2.330 km, número já calculado no Gráfico 2. |
| P9 | Comparabilidade | A decomposição da ΔPMT usa **três ICE diferentes**: preço do Onix 1.0 hatch, depreciação do Polo Track e seguro do **Onix Sedan Plus**. Só o Polo está rotulado como proxy. A fonte do seguro não tem o Onix hatch. | Rotular o seguro como proxy (Onix Sedan Plus ≠ Onix 1.0 hatch). |
| P10 | Comparabilidade | A7 "tabela do Dolphin Mini subiu 2,8%": compara R$ 115.800 (fev/2024, **38 kWh**) com R$ 118.990 (2026, GL **30,08 kWh**), em valores **nominais**. A versão está explícita; o fato de ser nominal, não. | Dizer "+2,8% nominal, versão com bateria menor". Se a conclusão "não caiu" depende disso, comparar a mesma versão (GS 38 kWh) e deflacionar. |
| P11 | Fonte fraca | Fontes fracas: elektrocharge (vende recarga: tem eletropostos próprios), combustiveis-anp.com.br (agregador, não é a ANP), calculadoradomundo (calculadora de terceiros), seucarrousado (blog assinado "Equipe", data "8/11/2026" ambígua), Rentcars (agregador, "1 locadora" sem nome). | Trocar pelas primárias quando possível: planilha semanal da ANP (gov.br), tabela PBEV do Inmetro, tarifa homologada da ANEEL. Juros (SGS 25471 = 1,97% em 08/2026) e Selic (SGS 432 = 13,75%) **já confirmados no BCB**. |
| P12 | Menor | "Contexto": compara o ticket médio da Localiza (> R$ 3 mil, todas as categorias, 33 m) com o VE de outro canal (BYD) para dizer que o VE fica "abaixo do ticket médio". | Explicitar que são operador e mix de categorias diferentes. |

---

## TAREFA 1 — URLs e trechos

Legenda: **OK** · **OK-PARCIAL** · **NÃO ENCONTRADO** · **INACESSÍVEL** · **FONTE FRACA** (registrada mesmo quando o trecho confere).

| # | URL | Citado no G1-r1 | O que a página traz (literal devolvido pelo WebFetch) | Status | Obs. |
|---|---|---|---|---|---|
| 1 | byd.com/br/byd-por-assinatura | "Preços a partir de R$ 2.870,40" | "BYD DOLPHIN MINI / Preços a partir de R$ 2.870,40" | **OK** | Sem prazo, sem franquia e sem operador. A lista de benefícios cita "Seguro para terceiros" (cobertura talvez diferente da Unidas/Localiza; ver P7). Fabricante é parte interessada, mas aqui é a fonte da própria oferta. |
| 2 | subscription.rentcars.com/…/byd/dolphin-mini | "a partir de R$ 2.870/mês" (GL) | "Dolphin Mini GL" · "1 locadora" · "a partir de" · "R$ 2.870/mês" (GS: R$ 3.049) | **OK · FONTE FRACA** | Agregador. Locadora não identificada, sem prazo/franquia. |
| 3 | subscription.rentcars.com/…/chevrolet/onix | "a partir de R$ 2.909/mês" · "a partir de R$ 2.059/mês" | "ONIX SEDAN Plus LTZ 1.0 12V TB Flex Aut." R$ 2.909/mês · "ONIX HATCH 1.0 12V Flex 5p Mec." R$ 2.059/mês | **OK · FONTE FRACA** | Agregador, "1 locadora". Há também uma 2ª oferta do Onix Hatch 1.0 Mec. a R$ 2.309. |
| 4 | livre.com.br | "a partir de: R$ 2.058,99/mês" | "Chevrolet Onix 1.0 / MT 5P / 2027 / Completo / … a partir de: / R$ 2.058,99/mês" | **OK** | Câmbio manual, ano-modelo 2027. |
| 5 | livre.com.br/…/Chevrolet_Onix_1.0_2025/ | 36 meses · 1.000 km/mês · R$ 2.058,99 | "R$ 2.058,99 mensalidade" · "Período 36 meses" · "KM mensal 1000 Km/mês" · "MT 5P \| 2027 \| Completo" | **OK** | — |
| 6 | vrum.com.br/…/7348483-carro-da-byd-por-assinatura… | "mensalidades que partem de aproximadamente R$ 2.688 para o Dolphin Mini" (rotulado "plano de 36 m") | Trecho literal confere. Sobre prazo, só "os planos mais comuns são de 36 meses", sem ligar ao R$ 2.688. Operador: "empresas parceiras da montadora". Data 05/02/2026 | **OK-PARCIAL** | O trecho existe; o rótulo "36 m" não tem suporte (P6). |
| 7 | assinatura.localiza.com/blog/post/byd-dolphin-mini-2026 | "R$ 118.990" · "8 anos ou 200 mil quilômetros" | "A versão GL… tem preço inicial a partir de R$ 118.990." · "garantia que pode chegar a 8 anos ou 200 mil quilômetros" · GL "bateria de 30,08 kWh". Publicado 18/09/2026 | **OK** | Garantia: "pode chegar a" (é um teto). |
| 8 | seucarrousado.com.br/chevrolet-onix-1-0-aspirado-2026… | "R$ 86.900" · "13,8 km/l na cidade e 16,9 km/l na estrada" | "preço público sugerido a partir de R$ 86.900" · "até 13,8 km/l no ciclo urbano" · "16,9 km/l no ciclo rodoviário" (gasolina, PBEV, manual 6 marchas) | **OK-PARCIAL · FONTE FRACA** | Números corretos, mas o trecho foi parafraseado e não é literal. Blog assinado "Equipe Seu Carro Usado". A data mostrada, "8/11/2026", é ambígua (se for dd/mm, está no futuro). |
| 9 | revistacarro.com.br/onix-2026-segue… | "13,9 km/l" para o Onix Plus (usado como LTZ TB Aut.) | "O sedã compartilha o mesmo conjunto mecânico do hatch e entrega consumo de 13,9 km/l em trajetos urbanos e 17,1 km/l em rodovias". Os dois são "1.0 Ecotec aspirado de 82 cv com câmbio manual de seis marchas". 13/10/2025 | **OK-PARCIAL** | O número existe, mas é de **outra versão** (aspirado manual). O G1-r1 diz que a fonte "não especifica" (P5). |
| 10 | canalve.com.br/dez-centavos-km… | "consumo energético declarado de 0,39 megajoule por quilômetro (MJ/km)" · "R$ 0,90 por kWh" | "Ambos possuem consumo energético declarado de 0,39 megajoule por quilômetro (MJ/km)" (BYD Dolphin Mini GL 5EV e Geely EX2) · "Considerando um valor médio da energia elétrica residencial no Brasil de R$ 0,90 por kWh" · "R$ 0,097 por quilômetro". Cita PBEV/Inmetro. 03/03/2026 | **OK** | Não diz se a tarifa inclui impostos (P8). |
| 11 | pv-magazine-brasil.com/2026/03/17/aneel-projeta… | "sairá de R$ 786/MWh em dezembro de 2025 para R$ 849/MWh" | "a tarifa residencial média paga no Brasil sairá de R$ 786/MWh em dezembro de 2025 para R$ 849/MWh até o final de 2026." | **OK** | A matéria não diz se inclui impostos. Comparada com a Cemig sem impostos (R$ 0,922), parece ser sem impostos (P8). |
| 12 | calculadoradomundo.com.br/…/cemig | R$ 1,1963/kWh com ICMS 18% + PIS/COFINS + bandeira amarela | "R$ 1,1963" · "Minas cobra 18% de ICMS em qualquer consumo: R$ 1,1963/kWh a 200 kWh." Componentes: TUSD 0,59308 + TE 0,31021 + bandeira amarela 0,01885 + ICMS 18% + PIS/COFINS | **OK · FONTE FRACA** | Calculadora de terceiros, não ANEEL nem Cemig. Página atualizada em 02/10/2026. |
| 13 | elektrocharge.com.br/blog/kwh-preco-eletroposto-brasil | "carregamento rápido DC no Brasil em 2026 gira em torno de R$ 1,80" · "Shell Recharge \| R$ 1,79–2,29" | "O preço médio do kWh em carregamento rápido DC no Brasil em 2026 gira em torno de R$ 1,80." · tabela: Shell Recharge "R$ 1,79–2,29" (DC Rápido). Autor Alexandre Crispim, abr/2026 | **OK · FONTE FRACA** | **Vendedor interessado**: promove eletropostos próprios (Pinhais, 60 kW DC). |
| 14 | combustiveis-anp.com.br/preco-da-gasolina | "R$ 6,592" · "20/09/2026 a 26/09/2026" | "Média nacional R$ 6,592 por litro" (Gasolina Comum) · "Período de referência: 20/09/2026 a 26/09/2026 · Fonte: ANP" | **OK · FONTE FRACA** | Agregador fora do gov.br, como o próprio G1-r1 sinaliza. |
| 15 | automotivebusiness.com.br/…/veiculos-novos-rodam… | "o brasileiro roda em média 12,9 mil quilômetros no primeiro ano" | "o brasileiro roda em média 12,9 mil quilômetros no primeiro ano de uso de um veículo" (KBB Brasil), 11/04/2019 | **OK** | Dado de 2019, já sinalizado. |
| 16 | assinatura.localiza.com/blog/post/quanto-gasta… | "Um carro elétrico pode gastar, em média, entre R$ 120 e R$ 350 por mês" · R$ 539,50 · 12 km/l · 15 kWh/100 km | Frase exata confirmada (2ª abertura). Também "83 × R$ 6,50 = R$ 539,50", "Consumo médio: 12 km/l", "Consumo médio: 15 kWh/100 km". 24/07/2026 | **OK** | — |
| 17 | automotivebusiness.com.br/…/abx26-carro-por-assinatura… | "33 meses, com tíquete mensal superior a R$ 3 mil" · "custa menos que a compra em 90% dos casos" | "o contrato médio na companhia gira em torno de 33 meses" · "com tíquete mensal superior a R$ 3 mil" · corpo: "em mais de 90% dos casos analisados, assinar… resulta em menor custo total de propriedade (TCO)". 01/10/2026; Bruno Saliba (Localiza) | **OK** | A frase dos "90%" é o título/slug; o corpo diz o mesmo com outras palavras. Sem metodologia publicada, como o G1-r1 já sinaliza. |
| 18 | mecanicaonline.com.br/2026/09/byd-dolphin-mini-perde-137… | "Dolphin Mini 2024 de 38 kWh uma referência de R$ 99.905 em fevereiro de 2026" · "A diferença é de R$ 7.165, equivalente a aproximadamente 8,14%." | Os dois trechos são literais e foram confirmados. R$ 115.800 (fev/2024). Polo Track R$ 87.990 → R$ 80.825. "Tabela Fipe disponibilizado pela Webmotors". 30/09/2026 | **OK** | Compara o preço de lançamento do 0 km com a FIPE do usado. |
| 19 | eletricos.app/noticias/carro-eletrico-usado… | Kwid E-Tech −25,9% · Dolphin Mini −3,6% · Dolphin −14,9% (12 m, FIPE) | "Renault Kwid E-Tech \| R$ 139.990 \| R$ 103.733 \| -25,9%" · "BYD Dolphin Mini \| -3,6%" · "BYD Dolphin \| -14,9%" · "Dados FIPE de 12 meses". 15/07/2026 | **OK** | — |
| 20 | quantilica.com/hedgehog/series/25471/… | 1,97% a.m., 08/2026 | "registrou 1,97 em 08/2026" | **OK** | **Confirmado na primária**: API BCB SGS 25471 → 01/08/2026 = 1,97; jul = 1,98; jun = 1,97. |
| 21 | creditas.com/exponencial/taxa-selic-hoje/ | "está em 13,75% ao ano" | "A taxa Selic… está em 13,75% ao ano. Esse patamar foi divulgado pelo Copom, em setembro de 2026." | **OK** | **Confirmado na primária**: API BCB SGS 432 = 13,75. |
| 22 | vrum.com.br/aceleradas/2026/07/7471454-ipva… | SP 4% · RJ 0,5% · PR 1,9% · MG só fabricados no estado | Os quatro trechos estão literais na página. | **OK** | — |
| 23 | otempo.com.br/autotempo/2026/4/30/seguro… | R$ 3.890,91 (Dolphin Mini) · R$ 2.540,26 (Onix Sedan Plus), masculino | "o seguro do hatch elétrico chinês sai, em média, por R$ 3.890,91" (texto) · tabela: Dolphin Mini R$ 3.886,45 · "Chevrolet Onix Sedan Plus: R$ 2.540,26". Fonte: Creditas | **OK** | O valor do Dolphin vem do texto e o do Onix da tabela (diferença de R$ 4,46/ano, irrelevante). **Não há Onix hatch** na matéria (P9). |
| 24 | motorshow.com.br/tag/byd-dolphin-mini-nacional | "Por cerca de R$ 107 mil para clientes CNPJ" · título "brasileiro" · título "R$ 120 mil" | "Por cerca de R$ 107 mil para clientes CNPJ, o Dolphin Mini GL 2026 acaba custando menos que hatches compactos a combustão" (11/02/26) · "…'brasileiro' já está nas concessionárias" (29/10/25; montado em Camaçari-BA) · "Geely EX2 ou BYD Dolphin Mini…" (14/11/25) | **OK** | "Cerca de" (valor aproximado). É da versão GL 2026. |
| 25 | localiza.com/…/alugar-um-carro-eletrico-byd | "compra de 10 mil veículos híbridos e elétricos" | "O acordo prevê a compra de 10 mil veículos híbridos e elétricos nos próximos dois anos" | **OK** | A página não traz data, como o G1-r1 indica ("data n/d"). |
| 26 | dgabc.com.br/Noticia/4330955/camex-aprova… | SKD 35% a partir de julho · CKD 14% até fim de 2026 e 35% em jan/2027 · US$ 463 mi · 6 meses | Trechos SKD e CKD literais · "US$ 463 milhões" · "validade por mais seis meses a partir de 1º de julho" · "alíquota zero". 23/06/2026 | **OK** | — |
| 27 | techcrunch.com/2024/01/11/hertz-sell-evs… | "approximately $245 million of incremental net depreciation expense related to the sale" · "lower demand for EVs and higher-than-expected repair costs" | Os dois trechos estão literais. "a third of its electric vehicle fleet" / "selling 20,000 EVs". 11/01/2024 | **OK** | O G1-r1 diz "vendeu"; a matéria fala em venda anunciada ("is selling"). Diferença trivial. |

URLs citadas no corpo e fora da tabela de fontes: nenhuma. As 27 do corpo são as mesmas 27 da tabela.

---

## TAREFA 2 — Contas (tolerância 0,5%)

| # | Conta | Fórmula | Analista | Verificador | Bate? |
|---|---|---|---|---|---|
| 1 | % que financiaria | (21+15)/44 | ≈82% | 81,8% | ✔ |
| 2 | Consumo VE | 0,39 ÷ 3,6 | 0,1083 kWh/km | 0,10833 | ✔ |
| 3 | R$/km VE casa / tarifa alta | 0,1083×0,90 · ×1,1963 | 0,0975 · 0,1296 | 0,0975 · 0,12960 | ✔ |
| 4 | R$/km VE mix 70/30 | 0,7×0,0975 + 0,3×0,195 | 0,1268 | 0,12675 | ✔ |
| 5 | R$/km VE DC / teto | 0,1083×1,80 · ×2,29 | 0,195 · 0,248 | 0,195 · 0,2481 | ✔ |
| 6 | R$/km ICE cidade / estrada / Plus | 6,592÷13,8 · ÷16,9 · ÷13,9 | 0,4777 · 0,3901 · 0,4742 | 0,47768 · 0,39006 · 0,47424 | ✔ |
| 7 | ΔPMT e % | 2.870 − 2.058,99; ÷2.058,99 | 811,01; +39,4% | 811,01; +39,39% | ✔ |
| 8 | ΔPMT alternativa | 2.688 − 2.058,99 | 629,01 | 629,01 | ✔ |
| 9 | Δ total a 1.000 km (casa) e % | (2.870+97,50) − (2.058,99+477,68) | +430,83; +17% | +430,83; +16,98% | ✔ |
| 10 | % da ΔPMT que a energia compensa | 380,18 ÷ 811,01 · (2.000 km) 760,36 ÷ 811,01 | 47% · 94% | 46,9% · 93,8% | ✔ |
| 11 | Δ a 1.000 km só DC | 3.065 − 2.536,67 | 528 | 528,33 | ✔ |
| 12 | Break-even casa / mix / DC | 811,01 ÷ (0,47768 − x) | 2.133 · 2.311 · 2.869 | 2.133,2 · 2.311,0 · 2.869,0 | ✔ |
| 13 | Break-even com ΔPMT 629 | 629,01 ÷ (…) | 1.655 · 1.792 · 2.225 | 1.654,5 · 1.792,4 · 2.225,2 | ✔ |
| 14 | Break-even tarifa alta / DC teto | 811,01 ÷ (0,47768 − 0,12960) · ÷(…−0,24808) | 2.330 · 3.532 | 2.329,9 · 3.532,3 | ✔ |
| 15 | Break-even estrada casa / DC | 811,01 ÷ (0,39006 − x) | 2.772 · 4.158 | 2.772,1 · 4.157,8 | ✔ |
| 16 | Break-even 15 kWh/100 km | 811,01 ÷ (0,47768 − 0,135) | 2.367 | 2.366,7 | ✔ |
| 17 | Gráfico 1 (5 franquias × 4 colunas + Δ) | mensalidade + km × R$/km | ex.: 2.000 km → 3.014,35 / 3.065 / 3.123,50 / 3.260 / +50,65; 3.000 → −329,53 | Todos idênticos. Única diferença: mix a 1.500 = 3.060,12 vs 3.060,13 (arredondamento) | ✔ |
| 18 | Tabela de energia/combustível | km × R$/km | 477,68 … 1.433,04; 97,50 … 585,00 | idênticos | ✔ |
| 19 | Achado 2 / Gráfico 3 (Onix Plus) | (2.870 + km×0,0975) − (2.909 + km×0,47424) | −415,74 · −792,49 · −1.169,24; DC −318,24 · −597,49 · −876,74 | −415,74 · −792,49 · −1.169,23; DC −318,24 · −597,49 · −876,73 (ICE a 3.000 km: 4.331,73 vs 4.331,74) | ✔ (arred.) |
| 20 | Capex VE vs ICE; mensalidade/preço | 118.990/86.900 − 1; 2.870/118.990; 2.058,99/86.900 | 36,9%; 2,41%; 2,37% | 36,93%; 2,412%; 2,369% | ✔ |
| 21 | Depreciação VE (24 m) | 118.990 × 13,7% ÷ 24 | 679,23 | 679,23 (13,7% confere: (115.800−99.905)/115.800 = 13,73%) | ✔ |
| 22 | Taxa líquida | 13,75% × 0,85 | 11,69% | 11,6875% | ✔ |
| 23 | Custo de oportunidade à vista / entrada | 118.990 × (1,116875² − 1) ÷ 24 · 23.798 × 0,24741 ÷ 24 | 1.226,64 · 245,33 | 1.226,64 · 245,33 | ✔ |
| 24 | PMT do financiamento | 95.192, 1,97% a.m., 48x | 3.084,49 | 3.084,52 | ✔ (0,001%) |
| 25 | Juros dos primeiros 24 m ÷ 24 | amortização Price | 37.374,6 → 1.557,27 | 37.375,58 → 1.557,32 | ✔ (0,003%) |
| 26 | IPVA SP / RJ; seguro | 118.990×4%÷12 · ×0,5%÷12 · 3.890,91÷12 | 396,63 · 49,58 · 324,24 | 396,63 · 49,58 · 324,24 | ✔ |
| 27 | Totais G1.2 | soma dos componentes | 2.626,74 · 3.202,70 · 2.279,69 · 2.855,65 | 2.626,75 · 3.202,75 · 2.279,69 · 2.855,70 | ✔ |
| 28 | Diferenças vs R$ 2.870 / R$ 2.688 | total − mensalidade | +333/+515 · −14/+168 · −243/−61 · −590/−408 | 332,75/514,75 · −14,30/167,70 · −243,25/−61,25 · −590,31/−408,31 | ✔ |
| 29 | Estresse 25,9% | 118.990×25,9%÷24 + 1.226,64 + 396,63 + 324,24 | 3.231,61; +362 / +544 | 3.231,61; 361,61 / 543,61 | ✔ |
| 30 | Fluxo de caixa SP | 3.084,49 + 396,63 + 324,24 | 3.805,36 | 3.805,40 | ✔ |
| 31 | Decomposição: depreciação ICE e Δ | 86.900 × 8,14% ÷ 24; 679,23 − 294,74 | 294,74; 384,49 | 294,74; 384,49 | ✔ |
| 32 | Custo de capital, IPVA e seguro a mais | 32.090×13,75%÷12 · 32.090×4%÷12 · (3.890,91−2.540,26)÷12 | 367,70 · 106,97 · 112,55 | 367,70 · 106,97 · 112,55 | ✔ |
| 33 | Soma da decomposição | Σ | 971,71 | 971,72 | ✔ |
| 34 | A1 desconto de frota | 11.990/118.990; 11.990 × 2,41% | 10,1%; ≈289 | 10,08%; 289,0 | ✔ (premissa: P2) |
| 35 | A2 R$ por p.p. de depreciação | 118.990 × 1% ÷ 24 | 49,58 | 49,58 | ✔ |
| 36 | A5 IPVA SP − RJ | 396,63 − 49,58 | 347 | 347,05 | ✔ |
| 37 | A7 variação de tabela | 118.990/115.800 − 1 | +2,8% | +2,75% | ✔ (base: P10) |
| 38 | Gráfico 5 (ponte) | 811,01 − 380,18 − 289 | ≈ +142 | 141,83 | ✔ |
| 39 | Oferta "VE de entrada" | 2.870 − 430 | ~2.440 | 2.439,17 | ✔ |
| 40 | Custo de absorver a diferença | 431 × 12; × 1.000 | R$ 5,2 mil; R$ 5,2 mi | 5.172; 5,17 mi | ✔ |

### Conclusão, veredito e implicação: os números derivam das contas?

| Afirmação | Deriva de | Status |
|---|---|---|
| G1.1 "+39% vira +17%", "R$ 431–528" | contas 7, 9, 11 | ✔ Consistente |
| G1.1 Veredito "zera em ~2.130 km" / texto "zera em ~2.100 km" | conta 12 (2.133, só casa) | ⚠ Impreciso (P4) |
| CONCLUSÃO "empata ou ganha do ICE de entrada a partir de ~2.100 km/mês" | conta 12 | ⚠ Impreciso: 2.133 com casa; 2.311 no mix (P4) |
| CONCLUSÃO "ganha do ICE automático em qualquer franquia" | Gráfico 3 | ✔ Consistente (insumo de consumo de outra versão, P5; sentido robusto) |
| CONCLUSÃO "ganha do financiamento" · Veredito G1.2 "mais vantajosa que comprar financiado" | tabela G1.2 | **INCONSISTENTE (parcial)**: RJ dá assinatura +R$ 14 (P3) |
| G1.2 Leitura "comprar é R$ 60–590/mês mais barato" à vista | conta 28 | ✔ |
| Veredito G1.3 "somadas, cobrem a diferença de R$ 431" · CONCLUSÃO "deve ser fechada com desconto de frota e gestão de valor residual" | Gráfico 5 deixa +142; exige ≥2,86 p.p. sem evidência; A8 = R$ 0 sobre a diferença real | **INCONSISTENTE** (P2) |
| G1 galho "núcleo real de ~R$ 430/mês" | conta 9 | ✔ |
| Implicação 1 "a 2.000 km cai para R$ 51; a 2.500+ o VE aparece mais barato" | Gráfico 1 | ✔ |
| Implicação 2 "R$ 416/mês mais barato" | conta 19 | ✔ |
| Implicação 3 "~R$ 2.440/mês", "R$ 5,2 mil/contrato/ano" | contas 39, 40 | ✔ |
| Implicação 4 "≥ 2.000 km/mês já pagam menos no VE com recarga em casa" | Gráfico 1 mostra +50,65 a 2.000 km | **INCONSISTENTE** (P1) |
| Implicação 5 "~R$ 333/mês mais barata em SP", "R$ 23,8 mil de entrada", "estresse: R$ 362" | contas 28, 29 | ✔ |
| Implicação 6 "+2,8%", "35% SKD jul/2026, CKD jan/2027" | conta 37; fonte 26 | ✔ (base de comparação: P10) |
| A8 "zera ou inverte de 2.000–2.500 km em diante" | Gráfico 1 (+51 a 2.000) | ⚠ Impreciso (P4) |

---

## TAREFA 3 — Tags [dado:]

| Tag no G1-r1 | Existe no dossiê? | Valor citado | Valor no dossiê | Bate? |
|---|---|---|---|---|
| #preoc-4 | Sim | "NÃO ATENDE" · "PMT para eletrificados é mais alto que o de carro a combustão" | idem | ✔ |
| #pdf-dores-cliente | Sim | "dificuldade para comparar o custo-benefício entre um elétrico e um veículo a combustão" | idem | ✔ |
| #preoc-fora-top10 | Sim | "Não ver vantagem financeira clara" fora do top 10 | idem | ✔ |
| #produto | Sim | franquias de 1.000 a 3.000; prazos de 12 a 48 m; inclui impostos, licenciamento, manutenção, pneus, cobertura total | 12/24/36/48 m; 1.000/1.500/2.000/2.500/3.000; itens inclusos idem | ✔ |
| #compra | Sim | 44%; 21% entrada + financiamento; 15% "financiariam sem entrada"; 8% à vista | "44% consideram comprar um carro (21% com entrada+financiamento, 15% sem entrada, 8% à vista)" | ✔ Ler "15% sem entrada" como financiamento sem entrada é razoável, mas é interpretação. |
| #pdf-risco-compra | Sim | depreciação e revenda como riscos do comprador | "assumir sozinho os riscos… depreciação, revenda e a infraestrutura" | ✔ |
| Seção "Lacunas conhecidas" | Sim | falta o preço exato da mensalidade de VE vs ICE na Localiza | "Preço exato da mensalidade de um VE vs. combustível equivalente na Localiza." | ✔ |
| #localiza-co (3 usos) | Sim | +15% das vendas de montadoras; 263 lojas de seminovos; +298K vendidos/ano | "+15% de share das vendas de montadoras; 263 lojas de seminovos"; "+298K vendidos no ano" | ✔ A Implicação 3b diz "263 pontos" em vez de "lojas"; sem efeito. |

---

## TAREFA 4 — Comparabilidade

| # | Comparação | Bases misturadas | Está explícito no G1-r1? | Efeito provável |
|---|---|---|---|---|
| C1 | ΔPMT de R$ 811 (núcleo do G1.1, Gráficos 1, 2 e 5) | VE: canal BYD/Rentcars "a partir de", operador, prazo e franquia desconhecidos, cobertura listada "seguro para terceiros". ICE: Unidas Livre, 36 m, 1.000 km, manual | **Parcial**: lacunas 1 e 2, suposição 1 e ressalva do Achado 3. As tabelas e a conclusão tratam os dois preços como mesma base. | Desconhecido. Se o VE "a partir de" for um plano de 48 m ou tiver cobertura menor, a diferença real é maior. |
| C2 | VE R$ 2.688 "(plano de 36 m)" vs ICE 36 m | O "36 m" não está na fonte, e o operador também não | **Não**: o rótulo sugere uma base comum que não existe | Pode superestimar a comparabilidade (P6) |
| C3 | Dolphin Mini (hatch) vs Onix Plus LTZ TB Aut. (sedã) com consumo do Onix Plus 1.0 aspirado manual | Categoria (hatch × sedã), operador (BYD × Rentcars "1 locadora") e versão do consumo | Hatch × sedã sim; a versão do consumo é descrita de forma errada (P5) | O sentido do achado é robusto. A magnitude é incerta. |
| C4 | G1.2: assinatura (R$ 2.870 "a partir de") vs compra em 24 m | Prazo da assinatura desconhecido vs horizonte de 24 m; cobertura possivelmente diferente (BYD: "seguro para terceiros" × seguro completo na compra) | **Não** no G1.2 | Tende a favorecer a assinatura (P7) |
| C5 | Decomposição da ΔPMT | Preço do Onix 1.0 hatch; depreciação do Polo Track; seguro do Onix Sedan Plus; VE da safra 2024 de 38 kWh aplicado à GL de 30 kWh | Polo e safra: sim. Seguro do Onix Sedan Plus usado como ICE de entrada: **não** | Ordem de grandeza só indicativa, como o analista já diz (P9) |
| C6 | Tarifa base R$ 0,90 vs "checagem" ANEEL R$ 0,849 vs Cemig R$ 1,1963 | Base tributária: não informada × provavelmente sem impostos × com impostos | **Não** | O cenário base pode estar otimista para o VE (P8) |
| C7 | A7: tabela 2024 vs 2026 | Bateria de 38 kWh × GL 30,08 kWh; valores nominais | Versão sim; nominal **não** | O "+2,8%" não é variação de preço like-for-like (P10) |
| C8 | Custo de capital: decomposição (Selic bruta 13,75%, simples) vs G1.2 (11,69% líquido, composto) | Agentes diferentes: Localiza × PF | Sim, ambos marcados [suposição] | Aceitável. Só não somar os dois. |
| C9 | A1: desconto CNPJ (fev/2026, "cerca de R$ 107 mil") sobre tabela de set/2026 (R$ 118.990); razão mensalidade/preço com mensalidade BYD e preço do blog Localiza | Datas e fontes diferentes; a razão trata a mensalidade inteira (que inclui serviços) como proporcional ao capex | Parcial: [suposição] e [lacuna] presentes | Magnitude incerta (P2) |
| C10 | "VE abaixo do ticket médio" | Ticket Localiza (todas as categorias, contrato de 33 m) × preço de entrada do VE no canal BYD | **Não** | Leitura frágil (P12) |
| C11 | Seguro do Dolphin Mini (texto, média nacional) vs Onix Sedan Plus (tabela) | Texto × tabela da mesma matéria | Não | Irrelevante (R$ 4,46/ano) |
| C12 | Franquia contratada = km rodado; ΔPMT constante de 1.000 a 3.000 km | Gráficos 1–3 usam a mesma ΔPMT em todas as franquias | **Sim**: suposição 2 e lacuna 3 | Os resultados a 2.500–3.000 km são os mais sensíveis |

---

*Fim da verificação. Nenhuma fonte inacessível. Nenhum trecho inventado foi encontrado.*
