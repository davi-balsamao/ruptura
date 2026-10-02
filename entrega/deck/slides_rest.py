from charts import line_chart, INK, INK2, MUTED, BLUE, ORANGE
GRID = "#D9D6CC"; BG = "#F6F4EE"; DARK = "#13212E"
H2 = "font-family:'Space Grotesk', Arial, sans-serif;font-weight:600;line-height:1.1"
SG = "font-family:'Space Grotesk', Arial, sans-serif"


def sec(id_, body, notes, dark=False, foot=None):
    bg = DARK if dark else BG
    col = "#F6F4EE" if dark else INK
    fc = "#BFCAD3" if dark else MUTED
    f = f'<p style="position:absolute;left:128px;bottom:64px;width:1664px;font-size:24px;color:{fc}">{foot}</p>' if foot else ""
    return (f'<section id="{id_}" data-transition="fade" style="background:{bg};color:{col};font-family:\'IBM Plex Sans\', Arial, sans-serif;'
            f'padding:128px 128px 160px;display:flex;flex-direction:column;gap:44px">\n{body}\n{f}\n<aside>{notes}</aside>\n</section>')


def head(eye, title, dark=False, ec=BLUE, size=56):
    tc = "#F6F4EE" if dark else INK
    return (f'<div style="display:flex;flex-direction:column;gap:16px"><p style="font-size:24px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:{ec}">{eye}</p>'
            f'<h2 style="{H2};font-size:{size}px;color:{tc}">{title}</h2></div>')


def card(title, text, accent=BLUE):
    return (f'<div style="flex:1;display:flex;flex-direction:column;gap:10px;background:#FFFFFF;border:1px solid {GRID};border-top:6px solid {accent};border-radius:16px;padding:22px 28px">'
            f'<h3 style="{SG};font-size:32px;font-weight:600;line-height:1.2;color:{INK}">{title}</h3>'
            f'<p style="font-size:26px;line-height:1.35;color:{INK2}">{text}</p></div>')


S = {}
S["capa"] = (f'<section id="capa" style="background:{DARK};color:#F6F4EE;font-family:\'IBM Plex Sans\', Arial, sans-serif;padding:128px;display:flex;flex-direction:column;justify-content:space-between">'
             f'<p style="font-size:28px;font-weight:600;letter-spacing:3px;text-transform:uppercase;color:#3987E5">Case 1 · Localiza Assinatura · Ruptura 2026</p>'
             f'<div style="display:flex;flex-direction:column;gap:32px"><h1 style="{H2};font-size:120px;color:#F6F4EE">Elétrico sem atrito</h1>'
             f'<p style="font-size:40px;line-height:1.3;color:#BFCAD3;width:1400px">Como fazer o lead que já quer um elétrico assinar um elétrico, e não um carro a combustão</p></div>'
             f'<p style="font-size:24px;color:#BFCAD3">Equipe [nome] · Outubro 2026</p><aside>Abertura. Apresentem a equipe em uma frase e vão direto para a resposta.</aside></section>')

S["resposta"] = sec("resposta",
    head("A resposta em 15 segundos", "Vender o elétrico como um pacote sem atrito, e provar com um piloto em quem já ganha com ele", size=60) +
    '<div style="display:flex;gap:28px">' +
    card("Conta à vista", "Custo total do elétrico contra o combustão, sem pedir CPF, e foco em quem roda mais de ~2.300 km/mês") +
    card("Recarga em casa inclusa", "Wallbox instalado e incluso nos contratos de 24 a 48 meses, com rota própria para condomínio") +
    card("Recarga na rua planejada", "Mapa, rota e simulador da rotina no app e na pré-venda, com rede parceira") + '</div>' +
    f'<p style="font-size:30px;line-height:1.35;color:{INK2}"><b>Primeiro passo:</b> piloto A/B de 90 dias numa praça, medindo quantos leads de elétrico assinam elétrico.</p>',
    "Esta é a resposta inteira. Os próximos slides mostram por quê. Três frentes, cada uma respondendo a uma barreira que a Localiza hoje não atende, e um piloto para provar o efeito antes de escalar.")

brl = lambda v: f"R$ {v:,.0f}".replace(",", ".")
km = [500, 1000, 1500, 2000, 2500, 3000]
ch = line_chart(960, 400, km, ["500", "1.000", "1.500", "2.000", "2.500", "3.000 km"],
                [dict(values=[2298.04, 2537.09, 2776.14, 3015.19, 3254.25, 3493.30], color=ORANGE),
                 dict(values=[2934.80, 2999.60, 3064.40, 3129.20, 3194.00, 3258.80], color=BLUE)],
                2200, 3600, [2200, 2600, 3000, 3400], brl, vline=2330,
                extra_labels=[(1000, 2820, 260, "+R$ 463", 28, INK, 600, "left"),
                              (2330, 3590, 320, "empate ≈ 2.330 km/mês", 24, INK, 600, "left"),
                              (500, 3590, 200, "— Combustão", 24, ORANGE, 600, "left"), (1000, 3590, 200, "— Elétrico", 24, BLUE, 600, "left")])
S["g1"] = sec("g1",
    head("Barreira #4 · Preço", "No uso típico o elétrico custa R$ 460 a 600 a mais por mês, e o lead nem consegue ver essa conta") +
    f'<div style="display:flex;gap:56px"><div style="display:flex;flex-direction:column;gap:12px"><p style="font-size:26px;color:{INK2}">Custo mensal total por km rodado no mês</p>{ch}</div>'
    f'<div style="flex:1;display:flex;flex-direction:column;gap:20px">' +
    card("A energia cobre só 21–43%", "da diferença de mensalidade (R$ 811) a 500–1.000 km", ORANGE) +
    card("Preço escondido atrás do CPF", "No site, a mensalidade só aparece após CPF e consulta de crédito", ORANGE) +
    card("Onde já ganha", "Acima de ~2.330 km/mês e contra o combustão automático (indicativo)", BLUE) + '</div></div>',
    "Barreira 4, preço. Sendo honestos: com preços de mercado, o elétrico custa de 460 a 600 reais a mais por mês no uso típico, contra um combustão de entrada. A economia de energia cobre só uma parte. Ele empata acima de 2.330 km por mês, e contra um combustão automático já sai mais barato. E hoje o lead nem consegue fazer essa conta: o site só mostra preço depois do CPF. Por isso a primeira frente é mostrar a conta e mirar quem já ganha. Ressalva: preço oficial da Localiza não é público; os números são indicativos de mercado.",
    foot="Fonte: análise G1 validada. Indicativo de mercado (VE R$ 2.870; ICE Unidas R$ 2.059); energia R$ 1,20/kWh; gasolina R$ 6,55")


def hb(lab, v, c, b=False):
    w = round(700 * v / 34)
    return (f'<div style="display:flex;align-items:center;gap:16px"><p style="width:240px;font-size:26px;text-align:right;font-weight:{600 if b else 400};color:{INK if b else INK2}">{lab}</p>'
            f'<div style="width:{w}px;height:44px;background:{c};border-radius:0 6px 6px 0"></div><p style="font-size:28px;font-weight:600;color:{INK}">{str(v).replace(".", ",")}</p></div>')


bars = ('<div style="display:flex;flex-direction:column;gap:18px">' + f'<p style="font-size:26px;color:{INK2}">Veículos elétricos por ponto público de recarga</p>' +
        hb("China", 10, "#B9B6AC") + hb("Média global", 11, "#B9B6AC") + hb("Brasil (mai/26)", 19.9, ORANGE, True) + hb("Brasil (ago/26)", 21.4, ORANGE, True) + hb("EUA*", 33, "#B9B6AC") +
        f'<p style="font-size:24px;color:{MUTED}">*Nos EUA ~80% da recarga é em casa (energy.gov)</p></div>')
S["g3"] = sec("g3",
    head("Barreiras #2 e #5 · Recarga na rua", "A rede pública é rala, então a Localiza não deve construí-la, e sim ajudar o cliente a navegar nela") +
    f'<div style="display:flex;gap:56px">{bars}<div style="flex:1;display:flex;flex-direction:column;gap:20px">' +
    card("O motivo da banca é o app", "#2 e #5 “não atendem” porque o app não tem mapa de carregamento") +
    card("Simulador da minha rotina", "Na pré-venda: casa, trabalho e viagens contra os pontos rápidos") +
    card("Rede parceira", "Pagar no app e desconto a negociar (precedente da 99: até 20%)") + '</div></div>',
    "Barreiras 2 e 5, recarga fora de casa. São quase 30 mil pontos públicos, mas 21 elétricos por ponto, quase o dobro da média global. A Localiza não vai resolver a malha, e não precisa: o motivo que a banca deu para o não atende é que o app não tem mapa. Então colocamos mapa e rota no app, que já é usado por 80% dos clientes, e um simulador da rotina na pré-venda, porque o vazamento acontece antes de a pessoa virar cliente. O efeito na conversão a gente não consegue provar sem teste, por isso vai para o piloto.",
    foot="Fonte: análise G3 validada. ABVE/Tupi (ago/26: 29.866 pontos, 38% DC); IEA via EV Infrastructure News (fim/25); app: dossiê #app")

rows = [("Conta à vista", "#4 Preço", "Simulador de custo total sem CPF; empate pela rodagem do lead; foco em ≥ ~2.300 km/mês; alavancas a testar (frota, revenda, pagamento antecipado)", "R$ 0 de preço"),
        ("Recarga em casa", "#3 e #2 casa", "Diagnóstico + wallbox 7,4 kW em comodato + instalação até R$ 3.000 em 24–48 m; kit condomínio", "R$ 104–270/mês por contrato"),
        ("Recarga na rua", "#5 e #2 rua", "Simulador da rotina na pré-venda; mapa e rota no app; pagamento e desconto em rede parceira", "API: teto ~US$ 8,5 mil/mês")]
tbl = (f'<table style="font-size:26px;color:{INK2}"><tr><th style="width:17%">Frente</th><th style="width:15%">Barreira</th><th style="width:46%">O que muda</th><th style="width:22%">Custo dimensionado</th></tr>' +
       "".join(f'<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>' for a, b, c, d in rows) + '</table>')
S["proposta"] = sec("proposta",
    head("A proposta", "Elétrico sem atrito: três frentes que levam a resposta da Localiza de 1 para até 4 das 5 maiores preocupações") + tbl +
    f'<p style="font-size:28px;line-height:1.35;color:{INK2}"><b>E o argumento que já temos:</b> bateria, revenda, pane e manutenção já são risco da Localiza, não do cliente.</p>',
    "A proposta inteira numa tabela. Três frentes, cada uma ligada a uma barreira, cada uma com custo dimensionado. Juntas, levam o placar de 1 para até 4 das 5 maiores preocupações. No preço, a resposta é parcial: mostramos a conta e miramos quem ganha, mas não fechamos a diferença para quem roda pouco sem dado de margem.",
    foot="Fonte: análises G1, G2 e G3 validadas; placar a partir do dossiê #gap-central. Preço #4 = atendido em parte")

steps = [("Interesse", "59% querem assinar em vez de comprar", "Campanha com custo total real"),
         ("Pesquisa", "preço só com CPF", "Simulador de custo total sem CPF"),
         ("Dúvidas", "#2, #3, #4 e #5 abertas", "Simulador da rotina + wallbox incluso"),
         ("Percebe risco", "risco do carro novo", "“Bateria, revenda e pane são nossos”"),
         ("Decide", "80% levam combustão", "Carro chega com o ponto instalado; mapa no app")]
cols = "".join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:12px"><p style="font-size:24px;font-weight:600;color:{BLUE}">{i + 1}</p>'
    f'<p style="{SG};font-size:30px;font-weight:600;color:{INK};line-height:1.2">{a}</p>'
    f'<p style="font-size:24px;line-height:1.35;color:#8A3410;background:#FBE7DD;padding:12px 14px;border-radius:10px">Hoje: {b}</p>'
    f'<p style="font-size:24px;line-height:1.35;color:{INK};background:#DCEAFB;padding:12px 14px;border-radius:10px">Novo: {c}</p></div>'
    for i, (a, b, c) in enumerate(steps))
S["jornada"] = sec("jornada", head("Jornada do cliente", "Cada etapa em que o lead hoje adia ou desiste ganha uma resposta concreta") + f'<div style="display:flex;gap:24px">{cols}</div>',
    "A jornada que a banca desenhou termina em adia ou abandona. A nossa troca cada ponto de dúvida por uma resposta: custo total sem CPF na pesquisa, simulador de rotina e wallbox incluso nas dúvidas, o risco do ativo como argumento, e o carro chegando com o ponto de recarga instalado.",
    foot="Jornada atual: dossiê #pdf-jornada (banca). Dados: #59, #conversao, #gap-central, observação do site (preço só com CPF)")

boxes = [("Desenho", "Leads de VE de uma praça em dois grupos: com o pacote e sem o pacote (controle)"),
         ("Métrica principal", "% de leads de elétrico que assinam elétrico (hoje 80% dos que assinam levam combustão)"),
         ("Métricas de apoio", "Uso do simulador; instalação na janela de entrega; recargas na rede parceira; NPS")]
S["piloto"] = sec("piloto",
    head("Como provar", "Um piloto A/B de 90 dias numa praça decide se o pacote escala, antes de qualquer investimento nacional", dark=True, ec="#3987E5") +
    '<div style="display:flex;gap:28px">' +
    "".join(f'<div style="flex:1;display:flex;flex-direction:column;gap:12px;background:#1C2E3F;border-radius:16px;padding:32px">'
            f'<h3 style="{SG};font-size:32px;font-weight:600;color:#F6F4EE">{t}</h3><p style="font-size:26px;line-height:1.35;color:#BFCAD3">{x}</p></div>' for t, x in boxes) + '</div>' +
    '<p style="font-size:30px;line-height:1.35;color:#F6F4EE"><b>O que pedimos:</b> aprovar o piloto e fazer a cotação oficial de preço VE × combustão para fechar a conta com números da própria Localiza.</p>',
    "Fechamento. Nada disso precisa ser apostado no escuro. Propomos um piloto de 90 dias com grupo de controle, medindo a métrica que importa: quantos leads de elétrico assinam elétrico. E pedimos a cotação oficial de preço, que é o único dado que nos falta para fechar a conta com os números da Localiza.",
    dark=True, foot="Métrica base: dossiê #conversao. Duração e praça do piloto = parâmetros de desenho")

for k, v in S.items():
    open(f"project/slides/{k}.html", "w", encoding="utf-8").write(v)
print(list(S))
