# Crítico MECE — G2 rodada 5 (delta: regra de fim de contrato)

ALVO: G2, wallbox, rodada 5 (`analises/G2-r5.md`)
VEREDITO DO GATE: **REPROVADO**

Os 9 itens do parecer r4 estão resolvidos dentro da análise; as contas batem e não há número inventado. A reprovação vem de um erro de lógica (aceito pelo próprio crítico na r4 e corrigido agora), da regra para quem renova que não chegou ao deck e da síntese que ainda diz "sem custo extra" sem condição.

## Motivos acionáveis
1. **[critério 2, bloqueia] O piloto não mede o que a r5 promete.** Piloto = 1 mês de construção, 3 de teste, decisão no mês 5; a regra vale para 24–48 m, que não terminam no piloto. (a) Renovação não é mensurável no piloto; (b) o A/B compara o pacote inteiro e não isola a regra; (c) o custo de retirada não precisa de piloto: cotar com os instaladores do teste Meoo [#preoc-3], vida útil com o fabricante. Dizer como e quando cada efeito é medido (3ª célula no A/B para conversão; survey ou ciclo real ≥ 24 m para renovação; cotação para retirada) e refazer a frase segura, a CONCLUSOES e o `<aside>` do g2.
2. **[critério 2, bloqueia] Item 7 não chegou ao deck.** "no fim do contrato ele é do cliente" / "no fim, o wallbox é do cliente" em `slides/resposta.html`, `slides/proposta.html`, `slides_rest.py` (l.39, l.83), `patch_v2.py` (l.11, l.23), `preview.html` (l.15, l.146). Trocar por "quando o cliente deixa a assinatura".
3. **[item 9, bloqueia a síntese]** `sintese.md` l.7–8 ("sem custo extra, porque a amortização já é de 100%") e l.12 ("G2 (r3)"); `ENTREGA.md` l.34 (regra da r3). Alinhar à regra nova.
4. **[menor]** 12 m: "o reuso fica dentro da garantia" exagera; restam 12 meses, que cobrem um 2º contrato só se também for de 12 m. A regra se sustenta pela renúncia de ~R$ 145/mês.
5. **[menor]** (a) A exposição a reparo fora da garantia para quem renova não tem teto (24 m + renovação = 24 meses fora). (b) Falta regra para quem começa em 12 m e renova para 24–48 m.
6. **[menor]** R$ 1.737,90 depende de [suposição r3: reuso em 2 contratos]; escrever 1.737,90 ÷ 48 e ÷ 24 (36,21 / 72,41 × 36,20 / 72,42 pela tabela).
7. **[menor]** Renúncias 1 (reuso) e 2 (valor residual) são alternativas, não se somam; "ponto útil depois da assinatura" depende da suposição de compatibilidade.
8. **[rastreabilidade]** Simulador (`rotina.py` l.98, `custo.py` l.66, `README.md` l.13) cita a r4 reprovada; `CONCLUSOES.md` l.71 cita a r5 como validada antes da aprovação.

Fora do G2, para o líder: `sintese.md`, MENSAGEM PRINCIPAL, ainda diz "começar ... pelos de alta rodagem", contra a atualização v2.

## NÚMEROS CHECADOS
#renovacao, #preoc-8, F1 → sim · 4.975,80 / 6.475,80; 103,66; 269,83; 67,46; 197,41 → sim · 1.737,90 → sim (suposição não marcada) · 36,21 / 72,41 → sim (36,20 / 72,42 pela tabela) · 144,83 → sim · 4.317,20 → sim (igual a `wallbox_saldo_saida_antecipada`) · 12–24 meses fora da garantia → sim · R$ 415–540 e 13,8–18,0% → sim · R$ 3.800–15.000 → sim · premissas do simulador batem com a r3 · prazo do piloto × contratos de 24–48 m → **não comporta medir renovação**.

## Nota de pitch (provisória)
Pode dizer: "No caso-base, deixar o wallbox com quem sai da assinatura não acrescenta custo à conta de amortização e dispensa a retirada." Não dizer: "a gente mede renovação no piloto", "no fim do contrato o wallbox é do cliente" (vale só para quem sai), "sem custo extra" sem a condição do caso-base.
