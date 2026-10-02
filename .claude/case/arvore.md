# ETAPA 1 e 2 — Core Question e Árvore MECE (Case 1 Localiza)

> Gates humanos dispensados pelo usuário em 2026-10-01 ("siga sem parar").
> Esta é a versão adotada pelo orquestrador. Pode ser revista pelo time.

## ETAPA 1 — SCQ (adotada)

**SITUAÇÃO:** O interesse por elétricos explodiu: leads em VE saltaram de 1% para
29% em menos de 1 ano [dado: dados-case1.md#leads-salto] e, no 1S26, o mercado de
eletrificados já atingiu 96% de todo o volume de 2025 [dado: dados-case1.md#pdf-1s26].
A Localiza Assinatura é líder em awareness (95%) [dado: dados-case1.md#awareness],
59% dizem que o eletrificado aumenta a vontade de assinar em vez de comprar
[dado: dados-case1.md#pdf-59-vs-compra], e a assinatura já resolve 5 das 10
maiores preocupações (bateria, revenda, pane, contrato, manutenção)
[dado: dados-case1.md#preoc-1, #preoc-6, #preoc-7, #preoc-8, #preoc-9].

**COMPLICAÇÃO:** O interesse não vira contrato de VE: leads de elétrico convertem
3x menos que os de combustão, e 80% dos leads de elétrico que assinaram escolheram
um ICE [dado: dados-case1.md#conversao]. O lead confia na Assinatura, mas não no
elétrico dentro dela. As preocupações do top 5 que a Localiza não resolve são
todas de recarga (#2, #3 parcial, #5) e de preço (#4)
[dado: dados-case1.md#gap-central].

**CORE QUESTION:**
> **Como a Localiza deve redesenhar a oferta e a jornada da Assinatura de
> elétricos para remover as barreiras que hoje não atende, de modo que o lead que
> já quer um VE assine um VE, e não migre para combustão?**

---

## ETAPA 2 — Classificação das barreiras do brainstorm

Legenda: **(a) CONFIRMA**: o dossiê sustenta, com #id · **(b) SUPOSIÇÃO**: sem
dado no dossiê, precisa de benchmark · **(c) CONTRADIZ**: o dado vai contra.

| # | Barreira / ideia do brainstorm | Classificação | Evidência | Vai para |
|---|---|---|---|---|
| B1 | "Verificar se a conta fecha ao alugar um elétrico; assumimos que fecha porque a demanda cresce" | **(a)+(c)+(b)**. (a) Preço é barreira real: a mensalidade do VE é maior que a do ICE e a Localiza "não atende". (c) A premissa "a demanda cresce, logo a conta fecha" é **contradita**: o interesse cresce, mas 80% dos leads de VE que assinaram foram de ICE. Interesse ≠ conta fechando. (b) Se o TCO fecha ou não, não está no dossiê: precisa de benchmark (preço Meoo, energia, combustível). | #preoc-4, #leads-salto, #conversao, #pdf-dores-cliente ("dificuldade para comparar custo-benefício") | **G1** |
| B2 | "A maior barreira seria a instalação do wallbox; muitas residências não comportam" | **(a)+(c)+(b)**. (a) Wallbox é barreira do top 5, e a Localiza só atende parcialmente. (c) **Não é "a maior"**: no ranking ela é a #3; recarga na rotina (#2) vem antes, e preço (#4) e recarga em viagem (#5) também não são atendidos. (b) "Residência não comporta" é suposição: precisa de benchmark (moradia em condomínio, normas, custo). | #preoc-3, #preoc-2, #gap-central | **G2** |
| B3 | "Wallbox de graça na assinatura aumenta a viabilidade, mas até que ponto é viável para a Localiza?" | **(b) SUPOSIÇÃO**. O custo de instalação é uma lacuna declarada do dossiê. A direção existe (a Meoo já testa parceria com instaladores), mas o custo não. | #preoc-3, lacunas | **G2** |
| B4 | "Wallbox alugado pelo cliente? Como seria a devolução junto com o carro?" | **(b) SUPOSIÇÃO** (pergunta aberta). Precisa de benchmark de modelos (incluso, aluguel, portátil) e da logística de reaproveitamento. | — | **G2** |
| B5 | "Quanto deveria ser a taxa do wallbox, e como negociar para reduzir atrito?" | **(b) SUPOSIÇÃO**. Depende do custo (B3) e do prazo de contrato (12–48 meses). | #produto | **G2** |
| B6 | "Mapa de eletropostos no app, para rotina e viagens/rotas" | **(a) CONFIRMA**. #2 e #5 "não atendem" justamente porque o app não tem mapa de carregamento. O app já tem alcance: 80% dos clientes acessam no mês, NPS 84, e já mostra nível de bateria. | #preoc-2, #preoc-5, #app | **G3** |
| B7 | "Promoção para assinantes ao usar eletropostos" | **(b) SUPOSIÇÃO**. Precisa de benchmark de parcerias e preço de recarga pública. | — | **G3** |
| B8 | "Crença de que alugar carro no Brasil é errado/prejuízo; mostrar outros contextos" | **(c) CONTRADIZ como barreira do VE** e **(a) confirma um gap de entendimento geral**. (c) Quem vazou para ICE **já aceitou assinar** (80% assinaram ICE). E, para o elétrico, 59% dizem que a vontade de **assinar** aumenta "ao invés de comprar". (a) Mas 28% não entendem como a assinatura funciona (20% nada), e 44% consideram comprar. A parte econômica ("é prejuízo?") é testada em **G1.2** (assinar × comprar). A parte de comunicação fica em G4 (fora do Pareto). | #conversao, #pdf-59-vs-compra, #educacao, #compra | **G1.2 / G4** |

**Leitura do brainstorm:** o time acertou o território (wallbox, recarga, preço),
mas superestimou o wallbox como barreira nº 1 e subestimou duas coisas: a
**recarga fora de casa** (o dossiê tem 2 itens de top 5 nela, #2 e #5) e o
**preço** (#4). O brainstorm trata o preço como premissa ("assumimos que a conta
fecha"), quando é a pergunta central.

---

## ETAPA 2 — Árvore de Hipóteses (How?)

**TIPO DE ÁRVORE:** Hipóteses (How), porque o foco é *o que fazer*. O "porquê" já
está dado pela banca (#gap-central).

**Eixo de quebra (MECE):** as dimensões da decisão do cliente de VE =
**Custo** · **Recarga em ponto privado** · **Recarga em rede pública** ·
**Processo de compra** · **Risco do ativo**. Toda preocupação do top 10, e as de
fora dele, cai em exatamente uma.

```
CORE QUESTION
├── G1  CUSTO: a conta do cliente  ............................ [PRIORITÁRIO]
│   ├── G1.1 Custo mensal total (mensalidade + energia) do VE vs ICE na assinatura, mesma categoria e franquia
│   ├── G1.2 VE por assinatura vs VE comprado (financiado/à vista): depreciação, IPVA, seguro, manutenção, custo de capital
│   └── G1.3 Alavancas para baixar a mensalidade ou o custo percebido (escala de compra, preço dos chineses,
│            canal de seminovos, IPVA, energia inclusa, comunicação do custo total)
├── G2  RECARGA EM PONTO PRIVADO (casa/trabalho/condomínio): wallbox ... [PRIORITÁRIO]
│   ├── G2.1 Custo e viabilidade de instalação no Brasil (casa × condomínio, normas, prazo)
│   └── G2.2 Modelo comercial (incluso / alugado / subsidiado / carregador portátil),
│            impacto em R$/mês no contrato e logística de devolução/reuso
├── G3  RECARGA EM REDE PÚBLICA (rotina fora de casa + viagens) ..... [PRIORITÁRIO]
│   ├── G3.1 Tamanho, crescimento e distribuição da malha de eletropostos (cidades e rodovias): é suficiente?
│   └── G3.2 Solução: mapa/rota no app (construir × integrar), parceria/benefício com redes de recarga
├── G4  PROCESSO DE COMPRA: jornada de venda, educação, experimentação, entrega ... [fora do Pareto]
│   ├── G4.1 Entendimento da assinatura (28% não entendem; 20% nada)
│   ├── G4.2 Experimentação (test-drive, período de teste) e onboarding
│   ├── G4.3 Prazo de entrega (até 60 dias)
│   └── G4.4 Capacitação da força de venda em VE
└── G5  RISCO DO ATIVO: bateria, revenda, pane, manutenção, marca ..... [fora: JÁ ATENDE]
    └── (#preoc-1, #6, #7, #8, #9 = ATENDE) → não é barreira; vira ARGUMENTO do pitch
```

### Regras de fronteira (para garantir o ME)
- **G1 × G2:** G1 é dono de toda comparação de custo mensal do cliente,
  inclusive a tarifa de energia (R$/kWh residencial e público) como insumo. G2 é
  dono do custo e do modelo do **equipamento + instalação** do wallbox e do seu
  impacto em R$/mês no contrato. A síntese soma os dois.
- **G2 × G3:** G2 cobre ponto de recarga **privado/dedicado** (casa, trabalho,
  condomínio). G3 cobre a **rede pública/semipública** (eletropostos urbanos e
  rodoviários) e as funções de app para achá-la. O #preoc-2 ("casa/trabalho ou
  eletropostos") é dividido: a parte casa/trabalho fica em G2, a parte
  eletropostos em G3.
- **G3 × G1:** desconto em eletroposto (brainstorm B7) é alavanca de G3. G1 usa
  as tarifas públicas de mercado, sem desconto.
- **G4:** cobre o "como vender/entregar". Não reavalia o custo (G1) nem a
  recarga (G2/G3).
- **"Autonomia insuficiente"** (fora do top 10) → G3, porque é ansiedade de
  recarga em trajeto. **"Não confiar em chinesas"** (fora do top 10) → G5.

**CHECK MECE:** os cinco galhos são disjuntos pelas regras de fronteira acima, e
todas as 10 preocupações do top 10, mais as de fora dele (#preoc-fora-top10),
mapeiam em exatamente um galho:
- #1, #6, #7, #8, #9 → G5
- #4 → G1
- #3 e a parte privada do #2 → G2
- #5 e a parte pública do #2 → G3
- #10 → G4

O conjunto é exaustivo para a decisão do cliente.

### Pareto: GALHOS A ANALISAR (≤3): **G1, G2, G3**
Justificativa:
1. **G1 + G2 + G3 cobrem 100% das preocupações do top 5 que a Localiza não
   resolve ou resolve só em parte** (#2, #3, #4, #5) [dado: dados-case1.md#gap-central].
   Só a recarga (G2+G3) responde por 3 das 5 maiores preocupações
   [dado: dados-case1.md#preoc-2, #preoc-3, #preoc-5].
2. **G5 está fora porque já é atendido** (#1, #6–#9) [dado: dados-case1.md#preoc-1, #preoc-6..9].
   Vira argumento ("o risco do ativo a assinatura já tira de você").
3. **G4 está fora do Pareto.** O dado de vazamento mostra que **o lead aceitou
   a assinatura e rejeitou o VE**: 80% dos leads de VE que assinaram foram de ICE
   [dado: dados-case1.md#conversao]. Isso aponta para barreiras específicas do VE
   (custo, recarga), não para o processo de venda da assinatura em si. A entrega
   rápida é só a 10ª preocupação [dado: dados-case1.md#preoc-10]. G4 reaparece na
   síntese como **viabilizador** (onboarding de recarga, comunicação do custo
   total), sem analista próprio. [suposição: o processo de venda não é a causa
   principal do vazamento; não há dado de funil por etapa para provar isso]
