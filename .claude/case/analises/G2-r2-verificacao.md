# VERIFICAÇÃO DE FONTES: G2-r2 (wallbox / recarga privada), modo DELTA
Verificador de fontes (anti-alucinação) · 2026-10-02 · fontes novas e trechos recapturados reabertos com WebFetch em 02/out/2026. F18, F22 e F23 também foram baixadas em HTML bruto (curl) para confirmar os trechos decisivos.
Escopo: só o que mudou da r1 para a r2. O que não mudou (F2–F5, F7–F9, F11, F14–F17, F19 a F21) segue como em `G2-r1-verificacao.md`. Não avalio a qualidade da análise.

---

## TABELA 1: Fontes novas e trechos recapturados

URLs novas na r2: só **F22** e **F23** (diff de URLs r1 × r2: 21 → 23; nenhuma URL foi removida).

| ID | Trecho citado na r2 | Status | O que encontrei de fato |
|---|---|---|---|
| **F22** (NOVA) correiobraziliense.com.br/cbradar/carregador-carro-eletrico-vaga-condominio/ | "Bruno Siqueira gastou R$ 9 mil para instalar um carregador de carro elétrico" | **OK-PARCIAL** | O trecho é literal (Bruno Vaz, 18/09/2026, SP). Não achei marca de ficção. **Mas:** (1) os R$ 9 mil "incluíram carregador, cabos, proteções elétricas e mão de obra", ou seja, é o total e não só a instalação; (2) a ordem foi de "manter o equipamento desligado até que a segurança da instalação fosse avaliada", ou seja, suspensão provisória e não veto; (3) o motivo veio de moradores: "Alguns moradores afirmaram estar preocupados com uma possível sobrecarga elétrica" porque o prédio é anterior aos VEs. A r2 atribui o argumento à "administração", o que não é exato. É relato único, na mesma seção (CB Radar) que publica cenários fictícios (ver F23) |
| **F23** (NOVA) correiobraziliense.com.br/cbradar/carregador-carro-eletrico-condominio-sobrecarga/ | "paga R$ 11 mil pela adaptação e condomínio manda desligar equipamento" / "após técnicos apontarem risco de sobrecarga na rede do prédio" | **FONTE FRACA: CENÁRIO FICTÍCIO** | Os dois trechos existem no título (23/09/2026). Mas o 1º parágrafo diz textualmente **"O cenário é fictício"** (personagem "Henrique"). **Não é caso real e não pode contar como evidência**, nem como "caso de imprensa", nem como n=2 |
| F1 (recapturado) | "Garantia 2 anos" | **OK** | Tabela de especificações, linha "Garantia": "Garantia 2 anos". Preço "Por: R$ 3.475,80" segue igual |
| F6 (atribuição) | "a partir de R$ 3 mil" (instalação básica com portátil), lista do Vrum/EM | **OK** | Literal: "Instalação básica (com carregador portátil): a partir de R$ 3 mil". Lista editorial, sem atribuição à REVO (18/02/2025). O parêntese sugere que o portátil está incluído; o intervalo R$ 3.000–4.699 da r2 cobre as duas leituras |
| F10 (recapturado) | "a maioria da população (84,8%) morava nesse tipo de residência" | **OK** | Literal exato. "Nesse tipo" = casa. 23/02/2024 |
| F12 (recapturado) | caput "às suas expensas"; "com emissão de Anotação ou Registro de Responsabilidade Técnica (ART ou RRT)" | **OK** | Art. 1º, caput, é literal: "É assegurado ao condômino o direito de instalar, às suas expensas, estação de recarga individual…". O trecho da ART/RRT é literal. A lei não menciona "inquilino", "locatário", "possuidor" nem "morador" (confirma a Lacuna 9) |
| F13 (recapturado) | "para projetos de edificações novas, protocolados a partir da data de vigência" | **OK** | Art. 6º, I, literal, incluindo o "para" |
| F18 (recapturado) | "Com o aumento da demanda, essa prática foi abandonada." + afirmação da r2 "A F18 não diz quem paga os R$ 40–60 mil" | **OK-PARCIAL** | O literal existe (atribuído ao síndico profissional). **Mas a mesma página tem uma tabela comparativa** ("Carregamento em vaga privativa vs. sistema coletivo (pay-per-use)", "Fonte: Elite Síndicos Associados") que, na linha "Custo de instalação", diz para o sistema coletivo: **"Absorvido pela empresa operadora"**; e, na linha "Adequação à IT-41", "Responsabilidade da empresa operadora". Logo, a F18 **diz** quem paga, e o que diz contradiz o próprio texto do síndico. A afirmação "a F18 não diz explicitamente quem paga" (l.15, 299, 354) está errada, e a [suposição: em regra, o condomínio ou os condôminos] (l.299) é contrariada pela tabela. Obs.: a verificação da r1 (Problema 3) também não registrou essa tabela; a leitura certa é que **a F18 é internamente contraditória** |
| F19 (Implicação 1) | "parceria com a GreenV, para instalação, assistência técnica e garantia" | **OK** | Já verificado na r1. "Escala nacional" e "diagnóstico" saíram |

Nota: a F18 traz ainda "Segundo a E-Wolf, uma instalação simples, sem necessidade de obra, custa em torno de R$ 3 mil." A r2 não usa esse dado. Fica como informação (fonte de parte interessada), sem pendência.

---

## TABELA 2: Contas novas ou alteradas (tolerância 0,5%)

| # | Fórmula | Analista | Verificador | Bate? |
|---|---|---|---|---|
| 1 | A = 3.475,80 + 1.500; B = 3.475,80 + 3.000; C = 5.554,44 + 5.000 | 4.975,80 / 6.475,80 / 10.554,44 | 4.975,80 / 6.475,80 / 10.554,44 | ✔ |
| 2 | A ÷ 12/24/36/48 | 414,65 / 207,33 / 138,22 / 103,66 | 414,65 / 207,33 / 138,22 / 103,66 | ✔ |
| 3 | B ÷ n | 539,65 / 269,83 / 179,88 / 134,91 | 539,65 / 269,83 / 179,88 / 134,91 | ✔ |
| 4 | C ÷ n | 879,54 / 439,77 / 293,18 / 219,88 | idem | ✔ |
| 5 | A com reuso: (3.475,80 ÷ 2 + 1.500) = 3.237,90 ÷ n | 269,83 / 134,91 / 89,94 / 67,46 | idem | ✔ |
| 6 | B com reuso: (3.475,80 ÷ 2 + 3.000) = 4.737,90 ÷ n | 394,83 / 197,41 / 131,61 / 98,71 | 394,83 / 197,41 / 131,61 / 98,71 | ✔ |
| 7 | (iii) 3.475,80 ÷ n | 289,65 / 144,83 / 96,55 / 72,41 | idem | ✔ |
| 8 | (iv) mín 3.000 ÷ n | 250,00 / 125,00 / 83,33 / 62,50 | idem | ✔ |
| 9 | (iv) máx (1.699 + 3.000) = 4.699 ÷ n | 391,58 / 195,79 / 130,53 / 97,90 | 391,58 / 195,79 / 130,53 / 97,90 | ✔ |
| 10 | 2.300 / 3.800 / 15.000 ÷ n | Tab. 2 | idem | ✔ |
| 11 | A, B, C ÷ 3.000 (mensalidades) | 1,66 / 2,16 / 3,52 (texto: 1,7–2,2) | 1,659 / 2,159 / 3,518 | ✔ |
| 12 | Tab. 3: A ÷ 3.000 | 13,8 / 6,9 / 4,6 / 3,5% | 13,82 / 6,91 / 4,61 / 3,46% | ✔ |
| 13 | Tab. 3: B ÷ 3.000 | 18,0 / 9,0 / 6,0 / 4,5% | 17,99 / 8,99 / 6,00 / 4,50% | ✔ |
| 14 | Tab. 3: C ÷ 3.000 | 29,3 / 14,7 / 9,8 / 7,3% | 29,32 / 14,66 / 9,77 / 7,33% | ✔ |
| 15 | Tab. 3: A com reuso | 9,0 / 4,5 / 3,0 / 2,2% | 8,99 / 4,50 / 3,00 / 2,25% | ✔ |
| 16 | Tab. 3: B com reuso | 13,2 / 6,6 / 4,4 / 3,3% | 13,16 / 6,58 / 4,39 / 3,29% | ✔ |
| 17 | Tab. 3: portátil (iv), mín–máx | 8,3–13,1 / 4,2–6,5 / 2,8–4,4 / 2,1–3,3% | 8,33–13,05 / 4,17–6,53 / 2,78–4,35 / 2,08–3,26% | ✔ |
| 18 | Capital por carro = 7,5 bi ÷ 70 mil | ≈ R$ 107 mil / 107.142,86 | 107.142,86 | ✔ |
| 19 | A, B, C ÷ 107.142,86 | 4,6% / 6,0% / 9,9% | 4,64% / 6,04% / 9,85% | ✔ |
| 20 | Faixas de texto: 24–48 m = A48–B24; 12 m = A12–B12 | R$ 104–270 (3,5–9,0%); R$ 415–540 (13,8–18,0%) | 103,66–269,83 (3,46–8,99%); 414,65–539,65 (13,82–17,99%) | ✔ |
| 21 | Mercado aberto A–C | 24–48 m R$ 104–440 (3,5–14,7%); 12 m R$ 415–880 (13,8–29,3%) | 103,66–439,77; 414,65–879,54; % idem | ✔ |
| 22 | "Corte 12 m × 24–48 m só com teto" | máx 24–48 m com teto 9,0% < mín 12 m 13,8%; sem teto C24 14,7% > A12 13,8% | idem | ✔ |
| 23 | Upside com reuso (Impl. 2) = A-reuso 48 m a B-reuso 24 m | R$ 67–197 | 67,46–197,41 | ✔ |
| 24 | Garantia 2 anos × prazos: 36−24; 48−24 | 12–24 meses fora da garantia | 12 / 24 | ✔ |
| 25 | Piso F8 = 3 mil + 1 mil | ~R$ 4 mil | 4.000 | ✔ |
| 26 | Alternativa (a): 3.800 ÷ 36 e 15.000 ÷ 36 | "R$ 105–417" | 105,56 / 416,67 | ⚠ 105,56 arredonda para **106** (desvio de 0,53%, no limite da tolerância; a Tab. 2 está certa) |
| 27 | 1.000 contratos ÷ 70 mil (sugestão do crítico) | não usado na r2 (trocado pela comparação por unidade) | 1,43% da frota | n/a |
| 28 | 12,5 + 2,4; 1.435.984 ÷ 4.200.734 | 14,9%; ≈34,2% | 14,9%; 34,18% | ✔ |

**Resultado: 26 de 26 contas aplicáveis batem, com 1 arredondamento no limite (#26).**

Afirmação aritmética de texto com problema: G2.2, "Garantia" (l.160): "os 3 anos da GWM (F19) cobririam um contrato de 36 m, **nunca** um 2º contrato". Isso é falso como regra, porque 2 × 12 m ou 12 + 24 m cabem em 36 m. Também é inconsistente com a frase anterior, que admite "dois de 12 m" para os 2 anos do Intelbras. É detalhe de redação, não de número.

---

## TABELA 3: Rastreio (VEREDITO / CONCLUSÃO / IMPLICAÇÃO / B2–B5)

| Onde | Número ou afirmação | Origem no arquivo | Status |
|---|---|---|---|
| Veredito G2.1 | R$ 4–12 mil; R$ 1–5 mil ou mais; > R$ 17 mil | F5; F8; F6 | ✔ |
| Veredito G2.1 / B2 / Alternativa | 14,9% (população BR); ~34% (domicílios capital SP) | conta 28, bases rotuladas | ✔ |
| Veredito G2.1 | R$ 3,8–15 mil (GreenV, parte interessada) | F18 | ✔ |
| Veredito G2.1 (l.116) | "2 casos de imprensa dentro da faixa" | F22 + **F23 (fictício)** | **INCONSISTENTE**: há 1 relato (F22), e o valor dele inclui o carregador |
| Veredito G2.1 (l.117) | "há casos de desligamento por risco de sobrecarga (F22, F23)" | F23 é fictício; F22 é suspensão provisória após reclamação de moradores | **INCONSISTENTE** |
| G2.1-D (l.94) | "evidência de restrição técnica… (n=2)… 'após técnicos apontarem risco de sobrecarga' (F23)" | F23 fictício | **INCONSISTENTE** |
| Veredito G2.2 | R$ 104–270 (3,5–9,0%); R$ 415–540 (13,8–18,0%) | Tab. 2 e 3, contas 20 | ✔ |
| Veredito galho | 13,8–18,0% | Tab. 3 | ✔ |
| Veredito galho (l.173) | "risco real de veto por carga do prédio (casos F22/F23)" | F23 fictício; F22 provisório | **INCONSISTENTE** na evidência citada. O risco de veto com justificativa técnica segue sustentado pela F12 |
| CONCLUSÃO | R$ 4.975,80–6.475,80; R$ 104–270/mês; 3,5–9,0%; teto R$ 3.000; Intelbras | contas 1 e 20; suposição de teto marcada; F1 | ✔ |
| CONCLUSÃO | "com risco de veto por carga do prédio" | F12 (veto com justificativa técnica permitido) + F22 (n=1) | ⚠ sustentável se apoiado em F12 + F22, sem F23 |
| Suposições (l.186) | "o veredito se apoia… nos casos de condomínio (F22, F23)" | F23 fictício | **INCONSISTENTE** |
| B2 (tabela) | "casos de veto por sobrecarga (F22, F23)" | idem | **INCONSISTENTE** |
| B3 | 1,7–2,2 mensalidades; 4,6–6,0% do capital por carro | contas 11 e 19 | ✔ |
| B4 | garantia 2 anos | F1 | ✔ |
| B5 | R$ 104–135 / 138–180 / 207–270 / 415–540 | Tab. 2 | ✔ |
| Implicação 1 | literal GWM/GreenV | F19 | ✔ |
| Implicação 2 | R$ 4.975,80–6.475,80; R$ 104–270 (48–24 m); 3,5–9,0%; upside R$ 67–197 | contas 1, 20, 23 | ✔ |
| Implicação 3 | R$ 415 (13,8%) a R$ 540 (18,0%); reuso R$ 270 (9,0%); portátil R$ 250–392 em 12 m | Tab. 2 e 3 | ✔ |
| Implicação 4 | ~48%; 2 anos | #renovacao; F1 | ✔ |
| Implicação 5 | 60 dias, como hipótese | #preoc-10 | ✔ |
| Alternativa (a) | "2 casos de imprensa… R$ 9 mil e R$ 11 mil (F22, F23)" | F23 fictício | **INCONSISTENTE** |
| Alternativa (a) | R$ 105–417/mês em 36 m | conta 26 | ⚠ arredondamento (106) |
| Alternativa (a) (l.296) | "casos de desligamento por sobrecarga (F22, F23)" | idem | **INCONSISTENTE** |
| Alternativa (b) (l.298) | "A gratuidade da infraestrutura pelo operador **acabou**" | F18, fala do síndico; a tabela da mesma F18 diz "Absorvido pela empresa operadora" | ⚠ afirmado como fato; a fonte é contraditória |
| Alternativa (b) (l.299) e Lacuna 13 | "A fonte não diz explicitamente quem paga" + [suposição: condomínio] | F18, tabela | **INCONSISTENTE** com a fonte |
| Tab. 1 (l.219) | "Casos relatados em condomínio (n=2) 9.000–11.000" | F22 + F23 | **INCONSISTENTE** |
| Lacuna 15 | "2 casos (F22, F23)" | idem | **INCONSISTENTE** |

Tags [dado:]: as 12 usadas na r2 (#preoc-2, #preoc-3, #preoc-4, #preoc-10, #produto, #pdf-dores-cliente, #pdf-dores-localiza, #renda, #renovacao, #capital, #frota, #localiza-co) existem e batem com o dossiê. O #renda agora tem a população certa: "50% dos respondentes".

---

## TABELA 4: Checagem dos 18 itens do parecer r1

| Item | Feito? | Nota (1 linha) |
|---|---|---|
| 1 | SIM | Conclusão com R$ 4.975,80–6.475,80 (A–B). Não sobrou "R$ 4,3 mil". |
| 2 | SIM, com ressalva nova | "Operador financia" e "capex ~0" saíram, e o literal da F18 entrou. Mas o texto novo erra ao dizer que a F18 não diz quem paga: a tabela da F18 diz "Absorvido pela empresa operadora" (Problema 2). |
| 3 | SIM | Base passou a ser (i) sem reuso; reuso como upside; garantia do Intelbras (2 anos) achada e conta certa. Só ajustar o "nunca um 2º contrato" (Problema 4). |
| 4 | SIM, com ressalva nova | Texto pedido reescrito; 84,8% rotulado; "custo aberto". O "dado novo" de 2 desligamentos por sobrecarga usa a F23, que é fictícia (Problema 1). |
| 5 | PARCIAL | GreenV rotulada, veredito ancorado em F5/F8, F3/F7 rotuladas. A "fonte independente" é 1 relato real (F22) + 1 cenário fictício (F23). Faixa segue indicativa, agora com n=1. |
| 6 | SIM | Mesma base A–B nos dois prazos; "cabe com folga" removido; rótulo "tamanho demonstrado, viabilidade não"; hipótese não se confirma como escrita. |
| 7 | SIM | R$ 104–270/mês (teto, Intelbras, sem reuso); com reuso, R$ 67–197. Contas batem. |
| 8 | SIM | Conclusão restrita a casa e condomínio; trabalho é a Lacuna 11. |
| 9 | SIM | (iv) = R$ 3.000–4.699 com instalação básica; atribuição ao Vrum/EM confirmada; literal "(com carregador portátil)". |
| 10 | SIM | R$ 415 (13,8%) a R$ 540 (18,0%) integral; R$ 270 (9,0%) rotulado como reuso. |
| 11 | SIM | Só o literal da F19; instalador com cobertura suficiente marcado como [suposição]. |
| 12 | SIM | "50% dos respondentes da pesquisa". |
| 13 | SIM | Comparação por unidade: R$ 107 mil por carro; 4,6–6,0% (A–B); 9,9% (C). |
| 14 | SIM | Implicação 5 e seção F tratadas como hipótese de piloto. |
| 15 | SIM | (a)–(e) recapturados e conferidos literalmente (F10, F12 ×2, F12 sem inquilino, F13). |
| 16 | SIM | Bases rotuladas em todos os pontos em que 14,9% e ~34% aparecem juntos (l.89, 115, 194, 293, Tab. 4). |
| 17 | SIM | "Vedado em SP; outros estados não verificados" (l.106, 140, 173, 303). |
| 18 | PARCIAL | Autochecklist refeito, mas afirma n=2 casos, "F18 não diz quem paga" e não lista a F23 como inválida. Refazer após os Problemas 1 e 2. |

Placar: 14 SIM · 2 SIM com ressalva nova · 2 PARCIAL · 0 NÃO.

---

## RESUMO

**Fontes:** 2 URLs novas (F22, F23) e 7 trechos recapturados (F1, F6, F10, F12, F13, F18, F19). F1, F6, F10, F12, F13 e F19 estão OK. F22 e F18 estão OK-PARCIAL. **F23 é cenário declaradamente fictício.**
**Contas:** 26/26 batem; 1 arredondamento no limite (R$ 105 → 106).
**[dado:]:** 12/12 existem e batem.
**Os 18 itens:** 14 SIM, 2 SIM com ressalva nova, 2 PARCIAL e nenhum NÃO. A camada de números (itens 1, 3, 6, 7, 10, 13) está limpa. Os problemas restantes vêm das **evidências novas** da r2.

### Problemas remanescentes (o que está errado → o que corrigir)

1. **[BLOQUEANTE] F23 é fictícia e é usada como caso real.** A página diz "O cenário é fictício" (personagem "Henrique"). Ela sustenta hoje "2 casos (n=2)", "R$ 11 mil" e "desligamento após técnicos apontarem risco de sobrecarga", nas linhas 17, 18, 73–74, 94, 116–117, 173, 186, 194, 219, 295–296, 334, 356 e 361.
   → Retirar a F23 como evidência (no máximo, citá-la como "ilustração fictícia do jornal", sem peso). Passar a n=1 em todos os pontos. Na Tab. 1, a linha vira "Caso relatado em condomínio (n=1): R$ 9.000, inclui carregador [F22]". Na Lacuna 15, "só GreenV + 1 relato".
2. **[BLOQUEANTE] A F18 diz quem paga, e a r2 afirma que não.** A tabela da F18 ("Fonte: Elite Síndicos Associados") diz para o sistema coletivo pay-per-use: "Custo de instalação: Absorvido pela empresa operadora". O texto do síndico diz que a instalação gratuita "foi abandonada". A fonte é internamente contraditória.
   → Linhas 15, 298, 299, 354 e autochecklist: trocar "não diz quem paga" por "a F18 se contradiz: a tabela diz que a operadora absorve; o síndico diz que a gratuidade foi abandonada". Tirar o negrito de "acabou" e atribuir ao síndico. Remover a [suposição: em regra, o condomínio], ou dizer que a tabela da mesma fonte a contraria. A Lacuna 13 passa a registrar as duas leituras. O desenho "indicar, sem financiar" não depende disso. A verificação r1 (Problema 3) e o item 2 do crítico partiram de leitura incompleta da F18; essa tabela não tinha sido registrada.
3. **[MENOR] Detalhes da F22.** O motivo veio de moradores ("Alguns moradores afirmaram estar preocupados com uma possível sobrecarga elétrica"), não da "administração". A ordem é provisória ("até que a segurança da instalação fosse avaliada"). Os R$ 9 mil incluem carregador, cabos, proteções e mão de obra.
   → Na l.94, descrever como "1 relato de suspensão provisória, pendente de avaliação técnica". Nas l.117, 173, 194 e 296, apoiar o "risco de veto por carga" em **F12** (veto com justificativa técnica permitido) + F22 (n=1).
4. **[MENOR] Garantia GWM (l.160):** "cobririam um contrato de 36 m, nunca um 2º contrato" está errado, porque 2 × 12 m e 12 + 24 m cabem em 36 m.
   → "Cobririam um contrato de até 36 m; um 2º contrato só se a soma for ≤ 36 m".
5. **[MENOR] Arredondamento (l.295):** "R$ 105–417/mês em 36 m" → **"R$ 106–417"** (3.800 ÷ 36 = 105,56).
6. **[PROCESSO]** Refazer o AUTOCHECKLIST (itens "fontes fracas rotuladas" e "trechos literais") depois dos Problemas 1 e 2, incluindo a F23 como inválida e a F18 como contraditória.
