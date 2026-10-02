# Verificação de fontes — G1 rodada 2 (modo DELTA)

> Verificador anti-alucinação · 02/out/2026 · alvo: `analises/G1-r2.md`. Referências: `G1-r1-critica.md`, `G1-r1-verificacao.md`, `obs-site-localiza.md` (aceita como observação direta).
> Método: as URLs novas ou trocadas que sustentam números de VEREDITO/CONCLUSÃO foram abertas com WebFetch. Todas as contas de veredito foram refeitas em Python (tolerância de 0,5%).

## 1. URLs novas/trocadas

| Número | URL | Achado na fonte | Status |
|---|---|---|---|
| Gasolina R$ 6,55 | precos.petrobras.com.br/precos-gasolina | R$ 6,55, semana "20/09/2026 a 26/09/2026", "Elaboração Petrobras a partir de dados da ANP e CEPEA/USP" | **OK** |
| Tarifa sem impostos 0,92214 | cemig.com.br/.../tarifas-vigentes | B1: verde 0,90329, amarela 0,92214, sob o título "antes de impostos" | **OK** (primária) |
| Tarifa com impostos R$ 1,1963 | calculadoradomundo.com.br/.../cemig | "R$ 1,1963/kWh a 200 kWh", com ICMS de 18%, atualizada em 02/out/2026 | **PARCIAL/FRACA**: é de terceiro (já rotulado), vale para a faixa de 200 kWh, e a página não diz a bandeira. Se for a verde, o fator de impostos é 1,324, não 1,297. Não muda a base |
| Recarga DC R$ 2,50 | vrum.com.br/.../7475942 | "o custo do kWh pode variar de R$ 2,30 a R$ 2,85. Com um valor médio de R$ 2,50" | **OK** |
| Onix 1.0 MT R$ 102.740 / CNPJ R$ 88.356 / Turbo AT R$ 115.940 | mundodoautomovelparapcd.com.br/... | Os três valores batem; artigo de 10/abr/2026 | **OK** |
| 2ª fonte do Onix 1.0 | autossegredos.com.br/... | R$ 102.990, 14/jul/2025 | **OK** |
| Onix Plus LTZ AT Turbo R$ 132.390 | onlycars.com.br/2026/01/... | Tabela: "LTZ AT Turbo R$ 132.390" (LT AT Turbo R$ 126.390). A página também traz o Inmetro/PBEV "AT 1.0 Turbo" (LT/LTZ/Premier): 12,2 km/l na cidade, 16,0 na estrada | **OK** |
| Onix Plus TB AT 12,2 km/l | nonamarcha.com.br/... | "12,2 km/l na cidade" (versão LT), **sem citar o PBEV** | **PARCIAL**: o valor confere, mas a fonte não é PBEV. A onlycars cobre o LTZ com o PBEV, o que elimina a suposição 7 |
| Onix hatch 13,7/17,7 km/l | revistacarro.com.br/... | "13,7 km/l na cidade e 17,7 km/l na estrada com gasolina" (hatch 1.0 aspirado MT) | **OK** |
| Dolphin Mini SKD | motorshow.com.br/byd-dolphin-mini-brasileiro | "as unidades vêm desmontadas (SKD) da China, e são finalizadas por aqui" (29/out/2025) | **OK** (dado de 2025; o regime em out/2026 já está marcado como lacuna 11) |
| SKD 35% / CKD 14%→35% / cota | dgabc.com.br/Noticia/4330955 | Os trechos sobre SKD e CKD conferem; cota de "US$ 463 milhões" com "validade por mais seis meses a partir de 1º de julho" | **OK** |
| Juros 1,97% a.m. / Selic 13,75% | api.bcb.gov.br SGS 25471 e 432 | Hoje dá erro de certificado TLS (WebFetch e curl) | **INACESSÍVEL** hoje. Os valores foram confirmados na mesma API na verificação da r1 (25471 = 1,97 em ago/2026; 432 = 13,75) |

## 2. Contas de VEREDITO/CONCLUSÃO (refeitas)

| Conta | G1-r2 | Refeito | Status |
|---|---|---|---|
| R$/km: ICE 13,7 / casa c/ imp. / DC / mix | 0,4781 / 0,1296 / 0,2708 / 0,1720 | 0,47810 / 0,12960 / 0,27083 / 0,17197 | OK |
| ΔPMT | 811,01 | 811,01 | OK |
| Gap a 1.000 km: casa c/ imp. / s/ imp. / mix / DC | 463 / 430 / 505 / 604 | 462,51 / 430,41 / 504,88 / 603,74 | OK |
| Gap a 500 km: casa / DC | 637 / 707 | 636,76 / 707,38 | OK |
| Parcela da energia: 500 / 1.000 / 2.000 km | 21 / 43 / 86% | 21,5 / 43,0 / 85,9% | OK |
| Break-even: casa c/ imp. / s/ imp. / mix / DC | ~2.330 / ~2.130 / ~2.650 / ~3.910 | 2.327 / 2.131 / 2.649 / 3.913 | OK |
| Break-even com ΔPMT de 561 / 629 (casa c/ imp.) | ~1.610 / ~1.805 | 1.610 / 1.805 | OK |
| G1.2: financiado SP / RJ | 3.362,22 / 3.015,17 | 3.362,30 / 3.015,25 | OK (juros de 24 m: 37.375,6 contra 37.374,6 no texto; diferença irrelevante) |
| G1.2: à vista SP / RJ | 2.626,74 / 2.279,69 | 2.626,75 / 2.279,69 | OK |
| Custo de oportunidade da amortização | 159,52 | 159,55 | OK |
| Δ assinatura, financiado SP: R$ 2.870 / com cobertura própria | −492,22 / −167,98 | −492,30 / −168,06 | OK |
| Δ assinatura, financiado RJ | −145,17 / +179,07 | −145,25 / +178,99 | OK |
| Δ assinatura, à vista SP / RJ | +243,26 / +590,31 (+567,50 / +914,55 com cobertura) | idem (±0,01) | OK |
| Estresse | 3.231,61 / −361,61 | 3.231,61 / −361,61 | OK |
| Resíduo após a A1 | ≥ R$ 174; 3,5 p.p. | 173,51; 3,50 p.p. (A1 = 11.990 × 2,412% = 289,19) | OK |
| Resíduo sem impostos | 141,41; 2,85 p.p. | 141,41; 2,85 | OK |
| "~R$ 485 acima do proporcional" | 485 | 485,35 | OK |
| Capex VE/ICE: +15,8%; LTZ/VE: +11% | 15,8% / 11% | 15,82% / 11,26% | OK |
| Gráfico 3 a 1.000 km: casa / DC | −446,29 / −305,06 | −446,29 / −305,05 | OK |
| Robustez: < R$ 90,60, > 72 km/l | 90,60 / 72 | 90,60 / 72,3 | OK |
| VE de entrada: casa / mix / DC | 2.407 / 2.365 / 2.266 | 2.407,49 / 2.365,12 / 2.266,26 | OK |
| Decomposição: 330,77 + 186,20 + 54,17 + 112,55 = 683,69; resíduo de 127,32 | idem | idem | OK |

**Contas: 22/22 dentro da tolerância.**

## 3. Os 22 itens do parecer r1

| # | Atendido? | Nota |
|---|---|---|
| 1 | SIM | G1.3: "existem"; fechar o gap é Não-comprovável. A CONCLUSÃO ficou condicional e a A8 saiu |
| 2 | SIM | Franquia de 2.000 foi para a Impl. 4 com [suposição]/[lacuna]. O VE a 2.407 empata só em casa (mix 2.365; DC 2.266) |
| 3 | SIM | ≥ ~2.330 / 2.130 / 2.650 km, com "se ΔPMT constante". Tentativa na Unidas registrada |
| 4 | SIM | SP / RJ / à vista qualificados. A amortização foi calculada, e o sinal dado pelo analista está **correto** (é custo da compra e favorece a assinatura), contra o que o parecer supôs |
| 5 | SIM | Ressalva dentro do G1.2 e coluna de sensibilidade com cobertura própria |
| 6a | SIM | Petrobras/ANP, R$ 6,55, confirmado |
| 6b | SIM | revistacarro 13,7/17,7 e R$ 102.740 com 2ª fonte, confirmados |
| 6c | SIM | Vrum R$ 2,50 confirmado. R$ 1,80 virou sensibilidade de vendedor |
| 6d | SIM | Saiu da CONCLUSÃO e virou indicativo. LTZ a R$ 132.390 confirmado |
| 6e | PARCIAL | A parte sem impostos é primária (Cemig). O valor com impostos segue da calculadora (rotulado), sem bandeira declarada |
| 7 | SIM | 12,2 km/l correto. Ressalva: a nonamarcha não é PBEV. Citar a onlycars (PBEV LT/LTZ) |
| 8 | SIM | Base com impostos em todas as seções |
| 9 | SIM | Quadro de bases, rótulo "indicativo", direção do viés, tentativa de mesma operadora e sensibilidade a R$ 2.309 |
| 10 | SIM | G1.1 Parcial, veredito em três partes, Impl. 2 como hipótese |
| 11 | SIM | SKD com fonte. Impl. 6 reescrita |
| 12 | SIM | Break-evens padronizados (nenhum resquício de 2.100/2.310/431) |
| 13 | SIM | "36 m" removido |
| 14 | SIM | Proxies rotulados; frase "estrutural" retirada |
| 15 | SIM | +2,8% nominal / +3,6% na mesma bateria |
| 16 | SIM | Bases explicitadas; "só parece caro" removido |
| 17 | SIM | Linha de 500 km; 21% |
| 18 | SIM | Obs §1/§5 em vez da suposição |
| 19 | SIM | Aviso de wallbox (G2) na CONCLUSÃO |
| 20 | SIM | Hipótese / A/B |
| 21 | SIM | Base e interpretação marcadas |
| 22 | PARCIAL | O autochecklist cita "seguro Creditas", mas a fonte do seguro é a otempo, então a linha está desatualizada. O item 7 da tabela de correções chama a nonamarcha de "PBEV" |

## RESUMO — problemas remanescentes (nenhum bloqueante)
1. **Tarifa com impostos (R$ 1,1963)** segue de calculadora de terceiro, na faixa de 200 kWh e sem bandeira declarada. Está rotulada e as contas não mudam. Para fechar: alíquotas de ICMS e PIS/COFINS da Cemig, ou só declarar "faixa de 200 kWh".
2. **12,2 km/l:** a fonte citada (nonamarcha) não menciona o PBEV. Trocar para a onlycars (PBEV "AT 1.0 Turbo", LT/LTZ/Premier), o que também elimina a suposição 7.
3. **BCB inacessível hoje** (erro de TLS no ambiente). Os valores ficam como confirmados na r1.
4. **Autochecklist:** remover "seguro Creditas" (a fonte é a otempo).
5. **SKD:** a fonte é de out/2025. O regime em out/2026 já está declarado como lacuna 11, o que é correto.

**Veredito do verificador:** todos os números de veredito/CONCLUSÃO conferem com as fontes e com as contas. 20/22 itens atendidos e 2 parciais, nenhum dos quais muda veredito ou conclusão.
