# SÍNTESE: Pirâmide SCR e roteiro do pitch (Case 1 Localiza)

> Construída só com conclusões validadas pelo crítico: G1 (r2), G2 (r3), G3 (r2).
> Tags: `[dado: dados-case1.md#id]` = dossiê · `[G1]`/`[G2]`/`[G3]` = análise validada (arquivo
> `analises/G1-r2.md`, `G2-r3.md`, `G3-r2.md`, cada número com fonte primária lá) ·
> `[obs]` = observação direta no site da Localiza (`analises/obs-site-localiza.md`) ·
> `[suposição]` / `[lacuna]` como sempre.
> **Números de preço VE × ICE são indicativos de mercado**: a Localiza só mostra preço com CPF e
> consulta de crédito [obs §1].

---

## MENSAGEM PRINCIPAL (R)
> **A Localiza converte o lead de elétrico se vender o VE como um pacote "sem atrito de recarga e
> com a conta à vista": custo total visível antes do CPF, wallbox instalado e incluso, e recarga na
> rua planejada no app. Começar por um piloto A/B com os leads que já ganham com o elétrico, os de
> alta rodagem.**

Teste dos 15 segundos: *"O lead quer o elétrico, mas desiste por recarga e preço. Resolvemos a
recarga dentro da assinatura, mostramos a conta de verdade e começamos por quem já economiza."*

**S:**
- O interesse explodiu: leads em VE foram de 1% para 29% em menos de um ano
  [dado: #leads-salto].
- 59% dizem que o elétrico aumenta a vontade de **assinar em vez de comprar**
  [dado: #pdf-59-vs-compra].
- A Localiza tem 95% de awareness [dado: #awareness] e já resolve 5 das 10 maiores preocupações
  [dado: #preoc-1, #preoc-6 a #preoc-9].

**C:**
- O lead de VE converte 3x menos, e 80% dos que assinam levam um carro a combustão
  [dado: #conversao]. Ele confia na Assinatura, mas não no elétrico dentro dela.
- As 4 preocupações abertas do top 5 são recarga em casa, na rotina e em viagem, e preço
  [dado: #gap-central].
- E as três são concretas:
  - o VE custa mais no uso típico [G1];
  - a recarga em casa tem custo e burocracia [G2];
  - a rede pública é rala [G3].

---

## PIRÂMIDE

### ARGUMENTO 1: Recarga é 3 das 5 barreiras, e a Localiza consegue resolvê-la dentro da assinatura sem construir rede
**Em casa (#3 e a parte "casa" da #2) [G2, validado]:**
- O custo é dimensionável. Wallbox 7,4 kW em comodato + instalação até R$ 3.000 custa à Localiza
  R$ 4.976–6.476 por contrato, ou **R$ 104–270/mês em contratos de 24–48 m**. Isso equivale a
  3,5–9,0% de uma mensalidade de referência de R$ 3.000 [G2, Tab. 2–3].
  - Base: preço de varejo Intelbras R$ 3.475,80; instalação de R$ 1.500–5.000 (imprensa e blog
    da Localiza) [G2].
- Em 12 m o peso sobe para 14–18%. Ali, o wallbox fica opcional com coparticipação [G2].
- Condomínio: 14,9% da população brasileira mora em apartamento ou condomínio [G2, Censo 2022].
  - Em SP, a Lei 18.403/2026 garante o direito de instalar e só admite veto com justificativa
    técnica ou de segurança [G2].
  - Resposta: estudo de carga antes de assinar, ART e aviso ao síndico.
  - O portátil é vedado em garagem coletiva em SP [G2].
- O teste da Meoo com instaladores já existe [dado: #preoc-3]. A proposta o transforma em produto.

**Na rua (#5 e a parte "rua" da #2) [G3, validado]:**
- A rede cresce, mas é rala: 29.866 pontos públicos (ago/26), 38% de recarga rápida, e **21,4 VEs
  por ponto**, ~1,9x a média global (~11) [G3].
- A Localiza não resolve a malha. Mas a razão que a banca deu para o "não atende" é "o app não
  tem mapa de carregamento" [dado: #preoc-2, #preoc-5]. Mapa e rota atacam exatamente isso
  (**Verdadeira**) [G3].
- O app já tem alcance e telemetria de bateria: 80% de uso mensal, NPS 84 [dado: #app].
- O custo de API tem teto de ~US$ 8,5 mil/mês [G3; cálculo com suposição de 4 buscas por MAU].

### ARGUMENTO 2: Preço é barreira real, e a resposta é mostrar a conta, mirar quem ganha e testar alavancas
- **Contra o combustão de entrada, o VE custa mais no uso típico.**
  - A 1.000 km/mês: **+R$ 463–604/mês**. A 500 km: +R$ 637–707.
  - A economia de energia cobre só 21–43% da diferença de mensalidade.
  - Empata acima de **~2.330 km/mês** com recarga em casa (~2.650 no mix casa/rua)
    [G1, indicativo de mercado].
- **Contra o combustão automático equipado (Onix Plus Turbo AT), o VE sai mais barato** em todas
  as franquias (−R$ 446/mês a 1.000 km). É indicativo: os carros não são equivalentes, e a tabela
  do ICE é 11% maior [G1].
- **Hoje o lead não consegue fazer essa conta.** O preço só aparece após CPF e consulta de crédito,
  e a home diz "econômica" sem número [obs §1, §5]. Comparar custo-benefício é dor declarada pela
  banca [dado: #pdf-dores-cliente].
- **Contra comprar, assinar ganha em parte.** Em SP sai mais barato que financiar (−R$ 168 a −492);
  no RJ fica indefinido; contra a compra à vista, perde [G1].
- **Alavancas existem, mas fechar a diferença é Não-comprovável** [G1]:
  - desconto de frota (até ~R$ 289/mês, se a Localiza obtiver o preço CNPJ e repassar);
  - gestão de revenda (263 lojas de seminovos [dado: #localiza-co]);
  - pagamento antecipado, que reduz a mensalidade exibida, não o custo econômico [obs §6].

### ARGUMENTO 3: Viável e mensurável, com piloto barato, sem capex de rede, e risco do ativo já coberto
- O risco do ativo já é da Localiza: bateria, revenda, pane e manutenção estão atendidos
  [dado: #preoc-1, #preoc-6 a #preoc-9; #pdf-risco-compra]. Isso vira argumento de venda.
- Custos dimensionados:
  - wallbox: R$ 104–270/mês por contrato [G2];
  - API do mapa: teto ~US$ 8,5 mil/mês [G3];
  - desconto em rede parceira: ~0 se a operadora bancar [suposição], ou R$ 22–45 por assinante/mês
    se a Localiza bancar [G3, cálculo com suposição].
- O efeito na conversão é **Não-comprovável hoje** [G1, G3]. Por isso a recomendação é um **piloto
  A/B**, não um lançamento nacional.
- Métrica principal: % dos leads de VE que assinam VE. Hoje, 80% dos que assinam vão para ICE
  [dado: #conversao].

---

## A PROPOSTA (para o slide de solução)
**"Elétrico Localiza sem atrito"**

| Frente | O que muda | Barreira | Base |
|---|---|---|---|
| 1. Conta à vista | Simulador de custo total (mensalidade + energia × ICE) **sem CPF**, com empate calculado pela rodagem do lead. Comparar com o ICE equivalente. Foco comercial em quem roda ≥ ~2.300 km | #4 | G1, obs §1 |
| 2. Recarga em casa inclusa | Diagnóstico elétrico + wallbox 7,4 kW em comodato + instalação até R$ 3.000, inclusos em 24–48 m. Kit condomínio. Instalação na janela de entrega (hipótese de piloto) | #3, #2 (casa) | G2 |
| 3. Recarga na rua planejada | "Simulador da minha rotina" na pré-venda + mapa e rota no app (dados Tupi/OCPI, Google) + desconto em rede parceira a negociar | #5, #2 (rua) | G3 |
| Viabilizador | Vendedor com o simulador; jornada sem CPF até a decisão; mensagem "o risco do carro é nosso" | Processo (G4) e risco (G5) | dossiê |
| Prova | Piloto A/B de 90 dias numa praça [suposição de desenho], com leads de VE | — | G1, G3 |

**Placar das 5 maiores preocupações** (desenho, a validar no piloto):
- Hoje a Localiza atende 1 de 5 [dado: #gap-central].
- Com o pacote, passam a ter resposta:
  - #2 (casa + rua);
  - #3;
  - #5;
  - #4 de forma parcial: transparência e segmentação, sem fechar a diferença para quem roda pouco.

**Jornada** (a banca descreve: interesse → pesquisa → dúvidas sobre autonomia, recarga e custos →
percebe risco → adia ou abandona [dado: #pdf-jornada]). Cada etapa ganha uma resposta:
1. Pesquisa: simulador de custo total sem CPF.
2. Dúvidas: simulador da rotina + wallbox incluso.
3. Risco: o risco do ativo é nosso.
4. Decisão: o carro chega com o ponto pronto.
5. Uso: mapa no app.

---

## STORYLINE (dot-dash do pitch, ordem de fala)
1. **Capa + resposta em 15 s:** "Elétrico sem atrito: recarga resolvida, conta à vista, piloto
   com quem já ganha."
2. **Situação:** o interesse explodiu (29% dos leads; 59% preferem assinar; 95% de awareness).
3. **Complicação:** 80% dos leads de VE que assinam levam combustão. Confiam na Assinatura, não no
   elétrico.
4. **Diagnóstico:** top 10. Risco do ativo resolvido; o que trava é recarga (3 de 5) e preço.
5. **Como estruturamos:** árvore MECE com 5 frentes; Pareto em 3 que cobrem 100% das lacunas do
   top 5.
6. **Preço (G1):** a conta real (+R$ 463 a 1.000 km; empate ~2.330 km) e a conta invisível (CPF).
7. **Casa (G2):** wallbox incluso por R$ 104–270/mês; rota para condomínio.
8. **Rua (G3):** rede rala (21,4 VEs/ponto) → mapa, rota e simulador de rotina.
9. **A proposta:** pacote "sem atrito", com 3 frentes, viabilizadores e jornada nova.
10. **Piloto e métricas:** A/B de 90 dias; KPI principal = % de leads de VE que assinam VE; custo
    dimensionado.
11. **Pedido:** aprovar o piloto + a cotação oficial do preço VE × ICE para fechar a conta.

---

## LIMITAÇÕES HONESTAS (inconclusos dos galhos validados)
- **G1:** todo número VE × ICE é indicativo de mercado, sem preço Localiza. Se as alavancas fecham
  a diferença: Não-comprovável.
- **G2:** não é comprovável:
  - se o custo cabe na margem;
  - se o lead consegue instalar;
  - se a lei de SP protege o inquilino.
  Também ficam em aberto o reuso do equipamento e a recarga no trabalho (não analisada).
- **G3:** não é comprovável:
  - se o mapa aumenta a conversão (exige A/B);
  - quem banca o desconto;
  - a situação dos corredores rodoviários.
  Onde a malha é fina, o mapa pode expor a escassez.
- **G4 (processo de venda) não foi analisado.** Entra só como viabilizador.

## LACUNAS DE DADO (o que ainda falta provar)
1. **Preço oficial da Localiza.** Dolphin Mini × Onix 1.0 / Onix Turbo AT, 36 m, 500–3.000 km.
   Exige CPF; tarefa do time.
2. **Perfil do assinante de VE da Localiza.** Não é público; perguntar à banca. O #idade e o #renda
   descrevem os respondentes, não os assinantes de VE.
3. Margem por contrato e custo de capital: fecham o retorno do wallbox incluso e das alavancas.
4. Volume de leads de VE e taxa de conversão por etapa do funil: dimensionam o impacto do piloto.
5. Moradia e vaga dos leads de VE: dizem quantos conseguem instalar wallbox.
6. Dossiê desatualizado: hoje há planos de 3, 6 e 9 meses e franquia de 500 km [obs §2, §6].
7. Reconfirmar as séries do BCB antes do pitch (o acesso falhou em 02/out por TLS) [G1].
