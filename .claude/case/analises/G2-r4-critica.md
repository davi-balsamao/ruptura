# Crítico MECE — G2 rodada 4 (delta: regra de fim de contrato)

ALVO: G2, recarga em ponto privado (wallbox), rodada 4 (`analises/G2-r4.md`)
VEREDITO DO GATE: **REPROVADO**

A aritmética bate com a r3, mas um número da Tab. 2 está sendo usado com outro significado, e o "R$ 0 adicional" está escrito sem condições, embora dependa de uma lacuna que a própria r4 declara. Na renovação, a r4 foi honesta: inverteu o "reforça a renovação" da `CONCLUSOES.md` §2, disse que a regra **remove** o incentivo e mandou o efeito líquido para o piloto como Não-comprovável. Esse ponto passa.

## Motivos acionáveis
1. **[critério 1 e 2] "Upside" de R$ 67–197/mês rotulado errado.** Na Tab. 2 da r3, 67,46 e 197,41 são o custo mensal **com reuso**, não o ganho perdido. A perda é a diferença: 3.475,80 ÷ 2 = R$ 1.737,90 por contrato, ou R$ 36,21/mês (48 m) a R$ 72,41/mês (24 m). A r4 superestima a perda em 2–3 vezes; e ela só ocorre para quem **não renova**.
2. **[critério 2] "R$ 0 adicional" sem condições.** O §4 declara lacuna a forma jurídica e o tratamento fiscal/contábil da transferência; o zero vem da premissa de valor residual nulo. Condicionar ("no custo gerencial do caso-base") e pôr nas SUPOSIÇÕES: (a) transferência sem custo de transação; (b) valor residual zero.
3. **[critério 2] "Abre mão só de..." incompleto e contraditório.** Faltou a opção de compra pelo valor residual da r3. Listar as três renúncias nos dois lugares: reuso, venda pelo valor residual, incentivo de renovação.
4. **[critério 2] "Retirar é pior que transferir" não demonstrado.** O ganho de retirar tem número; os custos são lacuna. Saldo Não-comprovável. O "Verdadeira" vale só para "não altera o custo do caso-base".
5. **[critério 2] §3c liga a transferência às dores da banca sem base.** O risco na adoção já é resolvido durante o contrato (r3); onboarding é no início, não no fim. Ficar só com o benefício direto.
6. **[critério 2] Extensão para 12 m não declara a perda.** Em 12 m o reuso fica dentro da garantia (r3, "dois de 12 m") e a renúncia é a maior: 1.737,90 ÷ 12 ≈ R$ 145/mês. Declarar ou manter a regra da r3 em 12 m.
7. **[critério 2] Regra para quem renova ambígua** (§1 "fica" × §5 "transferido, renovando ou não"). Decide quem paga reparo fora da garantia num 2º contrato de 36–48 m. Escolher uma.
8. **[critério 1, menor]** "Na r3 funcionava como incentivo a renovar" é inferência da r4. Marcar.
9. **[fora da r4, bloqueia a síntese]** `entrega/CONCLUSOES.md` (linhas 72 e 84) e a nota do apresentador do slide G2 (`slide_g2.py`, `patch_v2.py`, `slides/g2.html`, `preview.html`) ainda dizem "reforça a renovação" e "a conta já paga 100% do equipamento". "Paga" é falso (custo da Localiza; cobertura pelo preço é lacuna de margem) e "só traria custo" ignora o ganho de reuso.

Fronteiras: sem invasão de G1 ou G3. Nenhuma suposição sustenta sozinha o veredito, mas o "R$ 0" depende de duas suposições não declaradas (item 2).

## NÚMEROS CHECADOS
- #pdf-dores-cliente, #pdf-dores-localiza, #renovacao (~48% e 7%, Case 2), #preoc-8 → sim
- F1 "Garantia 2 anos" → sim
- R$ 4.975,80 e R$ 6.475,80; 103,66 = 4.975,80 ÷ 48; 269,83 = 6.475,80 ÷ 24 → sim
- 67,46 e 197,41 → conta bate; **significado não bate** (custo com reuso, não perda)
- Perda correta: 1.737,90 ÷ 48/36/24/12 = 36,21 / 48,28 / 72,41 / 144,83 → ausente na r4
- R$ 4.317,20 = 6.475,80 × 24 ÷ 36 → sim
- 12–24 meses fora da garantia → sim
- R$ 415–540/mês e 13,8–18,0% em 12 m; R$ 3.800–15.000 (F18 + F22, n=1); R$ 104–270/mês → sim

## Nota de pitch
Até a r5 ser aprovada, não dizer "a conta já paga o wallbox", "reforça a renovação" nem "abrimos mão de R$ 67–197/mês". Frase segura: "No caso-base, a transferência não acrescenta custo à conta de amortização. O efeito em renovação e conversão vai para o piloto."
