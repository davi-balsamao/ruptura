# Observação direta do orquestrador — site da Localiza Assinatura (2026-10-02)

> Navegação feita pelo orquestrador no navegador (o site é renderizado por JavaScript;
> WebFetch não enxerga esse conteúdo). Nada foi preenchido nem enviado. Os trechos abaixo são
> literais da tela. Cite como `[benchmark: <URL> | "<trecho>" | observado em 02/out/2026]`.

## 1. A mensalidade só aparece depois de cadastro completo com CPF e consulta de crédito
- URL: https://assinatura.localiza.com/personalize-seu-plano/eletrico/byd-dolphin-mini/000027%C3%8D
  (página "BYD DOLPHIN MINI GL por assinatura").
- A página mostra o carro e "Itens de série", mas **não mostra preço**. Para ver valor, o
  formulário "Preencha seus dados" pede: "Nome", "E-mail", "Telefone", "CPF ou CNPJ", "CEP"
  e o botão "Solicitar orçamento".
- Texto de consentimento ao lado do botão (trecho): "consultar o Sistema de Informações de
  Crédito para fins de análise de crédito e risco".
- Nenhum valor de mensalidade foi visto em /carros, /carros/byd, /carros/byd/dolphin%20mini
  nem na página de plano.
- **Implicação (para G1/síntese):** o lead que quer comparar elétrico × combustão não consegue
  ver o preço, e muito menos o custo total, sem entregar CPF e autorizar consulta de crédito.
  A banca lista como dor do cliente a "dificuldade para comparar o custo-benefício entre um
  elétrico e um veículo a combustão" [dado: dados-case1.md#pdf-dores-cliente].
- Isso também explica a `[lacuna: preço Localiza]` do G1: o preço não é público.

## 2. Existe franquia de 500 km/mês no configurador
- Na mesma página, o configurador mostra por padrão: "Período de assinatura 48 Meses" e
  "Franquia mensal 500 Km".
- O dossiê (#produto, PDF da banca p.5) lista franquias de 1.000 a 3.000 km. **500 km aparece
  no site e não no dossiê.** Isso importa para o G1: com 500 km/mês, a economia de energia do VE
  pesa menos, e o break-even em km fica mais longe.

## 3. Catálogo de eletrificados visível no site
- A listagem /carros diz "178 opções de carro por assinatura".
- Elétricos vistos: "BYD Dolphin EV 44KW Elétrico AT", "BYD Dolphin Mini 30KW Elétrico AT",
  "BYD Dolphin Mini 38KW Elétrico AT", "Geely EX2 PRO AT 39KW", "Geely EX2 MAX AT 39KW",
  "Geely EX5 PRO Elétrico 60 KW".
- Híbridos plug-in vistos: "BYD Song Plus DM-I Turbo Híbrido", "BYD King".
- Selo "Entrega rápida": aparece em vários ICE (Onix, HB20, Argo, Tera, Kicks, T-Cross, Onix
  Plus, Nivus) e também no "BYD Dolphin Mini 30KW" e no "BYD Song". Não aparece no "BYD
  Dolphin EV 44KW". Amostra parcial (só os ~18 primeiros cards), **não conclusiva** sobre
  entrega de VE × ICE.

## 4. Campanha em curso
- O banner da home usa imagens com nome de arquivo
  "MO_26_507_KV_PAGAMENTO_ANTECIPADO_Dolphin" e "…_Compass". Isso sugere uma campanha de
  "pagamento antecipado" que inclui o Dolphin. O conteúdo da arte não foi lido. **Não usar
  como dado**, só como pista para o time conferir.

## 5. Mensagem atual sobre elétricos na home
- Trecho literal: "Mobilidade mais sustentável, tecnológica e econômica com carros elétricos e
  todos os benefícios da assinatura." A home não traz número de economia nem custo total.

## 6. Notícia Forbes (29/set/2026): mudanças de produto relevantes para o G1
- URL: https://forbes.com.br/forbes-life/forbes-motors/2026/09/localiza-meoo-agora-e-localiza-assinatura-e-amplia-oferta-de-carros-com-planos-a-partir-de-3-meses/
- Meoo virou "Localiza Assinatura"; planos de 3, 6 e 9 meses (antes "12 a 48 meses"); "cerca de 70 mil clientes ativos".
- Pagamento antecipado: "Quanto maior o montante adiantado no início do contrato, menor será o valor das mensalidades". Isso é uma alavanca de preço percebido para a #4, e não está no G1.
- Não há perfil demográfico de assinantes de elétrico na matéria. **Perfil do assinante de VE = lacuna** (o dossiê só tem o perfil dos ~1.000 respondentes: #idade, #renda, #compra; e 5% da base já tem híbrido/elétrico, #base-58).

## 7. Calculadora pública do site não tem a categoria Elétrico (observado em 02/out/2026)
- URL: https://assinatura.localiza.com/calculadora-carro-por-assinatura (link "Acessar Calculadora" da home, bloco "Avalie todos os detalhes antes de assinar").
- Passo 1, trecho literal: "Escolha uma categoria de carro por assinatura:" com as opções "Econômico", "Intermediário", "SUV" e "Utilitário". **Não há "Elétrico"**, embora a home liste "Elétrico" como categoria do catálogo.
- Passos 2 e 3: prazos "24 meses", "36 meses", "48 meses" e franquias "1.000" a "3.000" km/mês.
- Implicação para o G1/MVP: o lead de elétrico não tem, hoje, uma conta pública de custo; o Simulador Elétrico preenche essa lacuna e pode reaproveitar o formato desta calculadora.
- Identidade visual observada (para o protótipo): fundo #F2F2F2, texto #383838, verde #018444, verde-escuro #004521, lima #78DE1F, fonte Inter, cantos de 16 px.
