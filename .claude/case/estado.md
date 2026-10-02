# ESTADO DO CASE — Case 1 Localiza (Mobilidade Elétrica)

> Mantido pelo orquestrador (lider-caso). Fonte de verdade do progresso.
> Dossiê: `case/dados-case1.md` (+ COMPLEMENTO do PDF da banca) · Brainstorm: `case/brainstorm.md`
> Árvore completa e classificação do brainstorm: `case/arvore.md`

## Etapa atual
**5. SINTETIZAR concluído — síntese em case/sintese.md; deck de 12 slides em entrega/deck/**

## Core Question (adotada — gates dispensados pelo usuário em 2026-10-01)
> Como a Localiza deve redesenhar a oferta e a jornada da Assinatura de
> elétricos para remover as barreiras que hoje não atende, de modo que o lead
> que já quer um VE assine um VE — e não migre para combustão?

## Árvore (Hipóteses/How) — resumo
- **G1 CUSTO** (conta do cliente: mensalidade+energia VE×ICE; assinar×comprar; alavancas) — PRIORITÁRIO
- **G2 RECARGA PRIVADA** (wallbox: custo/viabilidade; modelo comercial/devolução) — PRIORITÁRIO
- **G3 RECARGA PÚBLICA** (malha de eletropostos; mapa/rota no app + parceria) — PRIORITÁRIO
- G4 PROCESSO DE COMPRA (educação, experimentação, entrega 60 dias, força de venda) — fora do Pareto (viabilizador na síntese)
- G5 RISCO DO ATIVO (bateria, revenda, pane, manutenção) — fora: JÁ ATENDE (vira argumento)

## Galhos
| Galho | Status | Rodada | Arquivo | Observação |
|---|---|---|---|---|
| G1 Custo | ✅ VALIDADO (r2) | r2 | analises/G1-r2.md | ×ICE de entrada = Falsa no uso típico (gap R$463–604 a 1.000 km; empate ~2.330 km casa) — indicativo de mercado; ×compra = Parcial (SP assinar < financiar; RJ indefinido; à vista mais barato); alavancas existem, fechar gap = Não-comprovável |
| G2 Wallbox | ✅ VALIDADO (r3) | r3 | analises/G2-r3.md | Verdadeira/Relevante (forma restrita): wallbox incluso sem reuso, teto R$3.000 → R$104–270/mês (24–48m); condomínio = rota própria; viabilidade econômica e técnica do lead = Não-comprovável |
| G3 Rede pública | ✅ VALIDADO (r2) | r2 | analises/G3-r2.md | G3.1 malha suficiente = Falsa (21,4 VE/ponto vs ~11); corredores = Não-comprovável; G3.2a mapa/rota = Verdadeira; G3.2b efeito na conversão = Não-comprovável |

## Pipeline de validação (por galho)
analista → **verificador de URLs** (abre cada [benchmark:] e confere o trecho/número)
→ **critico-mece** (lê análise + relatório de verificação) → APROVADO ou re-despacho (≤3 rodadas).
> O crítico é read-only e não acessa a web; por isso a checagem de URL é feita
> por um verificador antes dele, e o crítico julga com esse relatório em mãos.

## Pendências / alertas
- `PLAYBOOK.md` e `RASCUNHO-case1.md` não existem; usuário mandou ignorar o rascunho.
- `agents/lider-caso.md` diz "siga sem parar" — contradiz o README/skills (registrado; usuário dispensou os gates nesta rodada).
- Dossiê ganhou seção **COMPLEMENTO** com dados do PDF oficial da banca (top 10
  completo de preocupações, base da pesquisa, produto, Localiza&Co, app, critérios
  da banca), cada item com página. Cópia da raiz `dados-case1.md` sincronizada.
- `#nps` ambíguo resolvido pelo PDF: 85 = "NPS do produto" (Big Numbers); ~45 = NPS relacional (#nps-relacional).

## Log
- 2026-10-01 — Etapa 1 (SCQ) produzida.
- 2026-10-01 — Usuário dispensou gates; Core Question proposta adotada.
- 2026-10-01 — PDF da banca lido; COMPLEMENTO adicionado ao dossiê.
- 2026-10-01 — Etapa 2: árvore MECE + classificação do brainstorm (case/arvore.md). Pareto: G1, G2, G3.
- 2026-10-01 — Etapa 3: analistas G1, G2, G3 disparados (rodada 1).
- 2026-10-02 07:50 — Incidente: G1 e G3 travaram logo no início (stream sem progresso; máquina/rede
  ociosa durante a noite). G2 avançou, foi interrompido por engano e retomado do ponto onde parou.
  G1 e G3 retomados. Gráficos do dossiê gerados em `entrega/graficos/01–04`.
- 2026-10-02 — G2 r1 entregue (21 fontes). Verificador de URLs/contas disparado.
- 2026-10-02 — G2 r1 verificado: 21/21 URLs abertas e trechos presentes; 22/22 contas batem; 3 problemas (nº sem origem na conclusão, conta da garantia, afirmação contradita por F18). Crítico disparado.
- 2026-10-02 — G1 r1 entregue (27 fontes). Verificador disparado. Orquestrador tentando preços reais na calculadora pública da Localiza.
- 2026-10-02 14:00 — Sessão anterior encerrada às ~08:15 com G3 (analista), G1 (verificador) e G2 (crítico) em andamento, sem concluir. Os três foram retomados de onde pararam.
- 2026-10-02 — Crítico REPROVOU G2 r1 (18 itens; ver analises/G2-r1-critica.md). Analista G2 re-despachado para r2.
- 2026-10-02 — G3 r1 entregue (31 fontes). Verificador disparado.
- 2026-10-02 — G1 r1 verificado: 27/27 URLs ok (3 parciais), 40/40 contas batem; 10 problemas de redação/base (ver G1-r1-verificacao.md). Crítico disparado.
- 2026-10-02 — Orquestrador no site da Localiza: preço só com cadastro + CPF + consulta de crédito; franquia de 500 km existe; catálogo de 6 elétricos (analises/obs-site-localiza.md).
- 2026-10-02 — G2 r2 entregue (18 itens corrigidos; base = wallbox incluso SEM reuso, teto R$3.000; R$104–270/mês em 24–48m). Verificador delta disparado.
- 2026-10-02 — G3 r1 verificado: 31/31 URLs ok (6 parciais), 41 contas (1 fora: municípios 34,3%); 3 problemas ALTA (EY geopolítico, base de frota 14→21,4, 10–20% de um caso só). Crítico disparado.
- 2026-10-02 — Crítico REPROVOU G1 r1 (22 itens; ver analises/G1-r1-critica.md): vereditos além das tabelas, fontes fracas em números centrais, bases incomparáveis. Analista G1 re-despachado para r2.
- PENDÊNCIA HUMANA: cotação oficial Localiza (Dolphin Mini × Onix/HB20/Polo, 36 m, todas as franquias) exige CPF + consulta de crédito — só o time pode fazer.
- 2026-10-02 — Verificação G2 r2: 14/18 itens corrigidos; BLOQUEANTE — fonte F23 (Correio Braziliense) é cenário FICTÍCIO usado como caso real; F18 se contradiz sobre quem paga a infra coletiva. Crítico r2 acionado.
- 2026-10-02 — Crítico REPROVOU G2 r2 (5 itens cirúrgicos: F23 fictícia, F18 contraditória, garantia, arredondamento, checklist). Números/lógica aprovados. Analista G2 em r3 (última).
- 2026-10-02 — Crítico REPROVOU G3 r1 (19 itens; ver analises/G3-r1-critica.md): EY com sentido trocado, série de frota com bases diferentes, 10–20% de um caso só, G3.1 sem critério de suficiência (contraexemplo EUA). Analista G3 em r2.
- NOTA: dossiê #app — 80,1% × ~70 mil ≈ 56 mil ≠ 53 mil MAU (frota ≠ nº de clientes?). Não usar os dois números juntos no pitch.
- 2026-10-02 — G2 r3 entregue (F23 fora; F22 n=1; veto apoiado na F12; F18 contraditória registrada). Crítico r3 (final) acionado.
- 2026-10-02 — ✅ G2 APROVADO na r3 (analises/G2-r3-critica.md). Inconclusos levados à síntese: margem, viabilidade técnica do lead, inquilino, reuso, trabalho.
- 2026-10-02 — G1 r2 entregue (vereditos rebaixados a 'indicativo de mercado'; gap 1.000 km R$463–604; break-even ~2.330 km casa; Onix R$102.740; Dolphin Mini SKD/35%). G3 r2 entregue (critério de suficiência ≤~11 VE/ponto; SP=Falsa, corredores=Não-comprovável; G3.2a Verdadeira, G3.2b Não-comprovável). Verificadores delta disparados para ambos.
- 2026-10-02 — G3 r2 verificado: 9 URLs novas ok, 34/34 contas, 19/19 itens atendidos; 8 ajustes de redação. Crítico r2 acionado.
- 2026-10-02 19:08 — Usuário interrompeu o verificador delta do G1 r2 e o crítico do G3 r2. Loop pausado; nada novo disparado. Próximos passos aguardam o usuário.
- 2026-10-02 — Retomado a pedido do usuário: novo crítico G3 r2 e novo verificador delta G1 r2 (os anteriores foram cancelados). Perfil do assinante de VE: lacuna (busca web sem dado demográfico); Forbes 29/set/26 registrada em obs-site-localiza.md §6 (planos de 3–9 meses; pagamento antecipado reduz a mensalidade).
- 2026-10-02 — ✅ G3 APROVADO na r2 (analises/G3-r2-critica.md, 9 notas de redação para a síntese).
- 2026-10-02 — ✅ G1 APROVADO na r2 (analises/G1-r2-critica.md). Os 3 galhos estão validados. Síntese aguarda autorização do usuário (pediu contenção de tokens).
- 2026-10-02 — Síntese escrita (sintese.md) e deck de 12 slides concluído (entrega/deck/). Etapa 5 concluída.
