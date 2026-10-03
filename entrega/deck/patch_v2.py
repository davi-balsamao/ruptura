# Patch v2 do deck: fontes reais, G1 sem foco em alta rodagem (Zarp), wallbox fica com o cliente,
# "Como provar" em 2 slides e anexo de fontes.
import re

p = "slides_rest.py"
s = open(p, encoding="utf-8").read()
R = [
    ('"Custo total do elétrico contra o combustão, sem pedir CPF, e foco em quem roda mais de ~2.300 km/mês"',
     '"Simulador de custo total sem pedir CPF, comparando o elétrico com o combustão equivalente (automático)"'),
    ('"Wallbox instalado e incluso nos contratos de 24 a 48 meses, com rota própria para condomínio"',
     '"Wallbox instalado e incluso em 24 a 48 meses; quando o cliente sai da assinatura, fica com ele"'),
    ('<b>Primeiro passo:</b> piloto A/B de 90 dias numa praça, medindo quantos leads de elétrico assinam elétrico.',
     '<b>Primeiro passo:</b> MVP digital (simulador de custo e de rotina + mapa no app) e piloto A/B de 90 dias em São Paulo.'),
    ('card("Onde já ganha", "Acima de ~2.330 km/mês e contra o combustão automático (indicativo)", BLUE)',
     'card("Onde já ganha: contra o automático", "−R$ 446/mês a 1.000 km (indicativo). Rodar 2.330 km/mês é perfil de motorista de app, que é o Zarp", BLUE)'),
    ('foot="Fonte: análise G1 validada. Indicativo de mercado (VE R$ 2.870; ICE Unidas R$ 2.059); energia R$ 1,20/kWh; gasolina R$ 6,55")',
     'foot="Fontes: byd.com/br (R$ 2.870), livre.com.br (R$ 2.059), cemig.com.br, precos.petrobras.com.br. Indicativo de mercado")'),
    ('foot="Fonte: análise G3 validada. ABVE/Tupi (ago/26: 29.866 pontos, 38% DC); IEA via EV Infrastructure News (fim/25); app: dossiê #app")',
     'foot="Fontes: abve.org.br (ago/26), evinfrastructurenews.com (IEA, fim/25), energy.gov; app: material Localiza do case")'),
    ('"Simulador de custo total sem CPF; empate pela rodagem do lead; foco em ≥ ~2.300 km/mês; alavancas a testar (frota, revenda, pagamento antecipado)"',
     '"Simulador de custo total sem CPF, contra o combustão equivalente (automático); alavancas a testar: frota, revenda, pagamento antecipado"'),
    ('"Diagnóstico + wallbox 7,4 kW em comodato + instalação até R$ 3.000 em 24–48 m; kit condomínio"',
     '"Diagnóstico + wallbox 7,4 kW + instalação até R$ 3.000 em 24–48 m; quem sai da assinatura fica com o wallbox; kit condomínio"'),
    ('foot="Fonte: análises G1, G2 e G3 validadas; placar a partir do dossiê #gap-central. Preço #4 = atendido em parte")',
     'foot="Placar: pesquisa Localiza jul/2026 (material do case). Custos: loja.intelbras.com.br, em.com.br, developers.google.com/maps")'),
    ('foot="Jornada atual: dossiê #pdf-jornada (banca). Dados: #59, #conversao, #gap-central, observação do site (preço só com CPF)")',
     'foot="Jornada e dados: material Localiza do case (pesquisa jul/2026); preço só com CPF: assinatura.localiza.com (out/26)")'),
]
for a, b in R:
    assert a in s, a[:60]
    s = s.replace(a, b)

i = s.index('boxes = [("Desenho"')
j = s.index('for k, v in S.items():')
novo = '''def box(t, x, dark=True):
    bg = "#1C2E3F" if dark else "#FFFFFF"; tc = "#F6F4EE" if dark else INK; xc = "#BFCAD3" if dark else INK2
    return (f'<div style="flex:1;display:flex;flex-direction:column;gap:10px;background:{bg};border-radius:16px;padding:26px 28px">'
            f'<h3 style="{SG};font-size:30px;font-weight:600;color:{tc}">{t}</h3><p style="font-size:24px;line-height:1.35;color:{xc}">{x}</p></div>')


S["piloto"] = sec("piloto",
    head("Como provar · o piloto", "Um teste A/B em São Paulo mede se o pacote faz o lead de elétrico assinar elétrico", dark=True, ec="#3987E5") +
    '<div style="display:flex;gap:24px">' +
    box("Onde", "São Paulo capital: maior malha de recarga do país (3.101 pontos) e lei que protege a instalação em condomínio") +
    box("Quem", "Leads de elétrico que chegam no período, sorteados em dois grupos: com o pacote e sem (controle)") +
    box("O quê", "Grupo teste: simulador sem CPF, simulador de rotina, wallbox incluso e mapa no app") + '</div>' +
    '<div style="display:flex;gap:24px">' +
    box("Métrica principal", "% de leads de elétrico que assinam elétrico. Hoje, 80% dos que assinam levam combustão") +
    box("Métricas de apoio", "Uso dos simuladores; conversão por etapa do funil; instalação dentro dos 60 dias de entrega") +
    box("Limites", "Custo do wallbox por contrato (R$ 104–270/mês), custo da API do mapa e NPS do assinante") + '</div>',
    "Como provar. O piloto roda em São Paulo, onde estão a maior malha de recarga e a lei que protege quem mora em condomínio. Os leads de elétrico são sorteados: metade recebe o pacote, metade segue o processo atual. A métrica que decide é uma só: quantos leads de elétrico assinam elétrico. Medimos também onde o funil melhora e controlamos o custo por contrato.",
    dark=True, foot="Fontes: abve.org.br (pontos por capital, ago/26); al.sp.gov.br (Lei 18.403/2026); material Localiza do case (80% para combustão)")

fases = [("Mês 1", "Construir o MVP", "Simulador de custo e de rotina no site e no WhatsApp; mapa no app com o parceiro; kit wallbox com os instaladores do teste da Meoo"),
         ("Meses 2 a 4", "Rodar o A/B", "Leads de elétrico em SP sorteados em teste e controle; acompanhamento semanal do funil"),
         ("Mês 5", "Decidir", "Escalar se o grupo teste converter mais em elétrico sem estourar o custo por contrato; o limite é definido com a Localiza")]
fcols = "".join(
    f'<div style="flex:1;display:flex;flex-direction:column;gap:12px;background:#FFFFFF;border:1px solid {GRID};border-top:6px solid {BLUE};border-radius:16px;padding:28px">'
    f'<p style="font-size:24px;font-weight:600;color:{BLUE}">{a}</p><h3 style="{SG};font-size:34px;font-weight:600;color:{INK}">{b}</h3>'
    f'<p style="font-size:26px;line-height:1.35;color:{INK2}">{c}</p></div>' for a, b, c in fases)
S["roadmap"] = sec("roadmap",
    head("Como provar · cronograma", "Em cinco meses a Localiza sabe se o pacote converte, antes de investir em escala") +
    f'<div style="display:flex;gap:24px">{fcols}</div>' +
    f'<p style="font-size:30px;line-height:1.35;color:{INK2}"><b>O que pedimos hoje:</b> aprovar o piloto, liberar a cotação oficial de preço VE × combustão e os dados de funil dos leads de elétrico.</p>',
    "O cronograma: um mês para construir o MVP digital e o kit do wallbox, três meses de teste, e no quinto mês a decisão de escalar ou não. Pedimos três coisas: aprovar o piloto, a cotação oficial de preço e os dados de funil, que hoje não são públicos.",
    foot="Duração e critérios do piloto: proposta da equipe, a calibrar com a Localiza")

refs = [("Pesquisa e números da Localiza", "Material oficial do case Ruptura 2026 (pesquisa jul/2026, ~1.000 leads e clientes); assinatura.localiza.com; forbes.com.br (29/09/2026)"),
        ("Preço e custo", "byd.com/br/byd-por-assinatura; livre.com.br (Unidas Livre); precos.petrobras.com.br; gov.br/anp; cemig.com.br; vrum.com.br; api.bcb.gov.br"),
        ("Wallbox", "loja.intelbras.com.br; em.com.br; assinatura.localiza.com/blog/post/wallbox; al.sp.gov.br (Lei 18.403/2026); sindiconet.com.br (Censo 2022)"),
        ("Recarga pública", "abve.org.br; evinfrastructurenews.com (IEA); energy.gov; deloitte.com; developers.google.com/maps; olhardigital.com.br (99 Recarga)"),
        ("Zarp", "zarp.localiza.com (aluguel para motoristas de app)")]
rrows = "".join(f'<tr><td><b>{a}</b></td><td>{b}</td></tr>' for a, b in refs)
S["fontes"] = sec("fontes", head("Anexo", "Fontes dos números desta apresentação") +
    f'<table style="font-size:24px;color:{INK2}"><tr><th style="width:24%">Tema</th><th style="width:76%">Fontes</th></tr>{rrows}</table>',
    "Lista completa de URLs no documento de conclusões das análises (entrega/CONCLUSOES.md).")

'''
s = s[:i] + novo + s[j:]
open(p, "w", encoding="utf-8").write(s)

p = "slide_g2.py"
g = open(p, encoding="utf-8").read()
for a, b in [('<b>3.</b> Na saída, a fiação fica e o equipamento volta; se o cliente renova, fica tudo',
              '<b>3.</b> Quando o cliente sai da assinatura, o wallbox fica com ele, sem retirada'),
             ('Fonte: análise G2 validada (Intelbras, Estado de Minas, blog Localiza, Lei SP 18.403/2026). Amortização sem custo de capital; teto = desenho',
              'Fontes: loja.intelbras.com.br (R$ 3.475,80), em.com.br (instalação), al.sp.gov.br (Lei 18.403/2026). Sem custo de capital')]:
    assert a in g, a[:40]
    g = g.replace(a, b)
g = g.replace("Não entra como linha extra na fatura, porque preço já é a barreira número 4.",
              "Não entra como linha extra na fatura, porque preço já é a barreira número 4. Quando o cliente deixa a assinatura, o wallbox fica com ele: no caso-base isso não acrescenta custo à conta de amortização e dispensa a retirada. O custo de retirar a gente cota com os instaladores no primeiro mês; o efeito na renovação só aparece quando os primeiros contratos terminarem.")
open(p, "w", encoding="utf-8").write(g)

F = {"situacao.html": "Fonte: material Localiza do case Ruptura 2026 (pesquisa jul/2026, ~1.000 leads e clientes)",
     "complicacao.html": "Fonte: material Localiza do case Ruptura 2026: “3x menos conversão de leads vs veículos à combustão; 80% … optaram por ICE”",
     "diagnostico.html": "Fonte: material Localiza do case Ruptura 2026 (pesquisa jul/2026, 1.000 leads e clientes). Linha = corte do top 5",
     "arvore.html": "Árvore de hipóteses (How?). G4 entra como viabilizador; G5 vira argumento de venda"}
for fn, t in F.items():
    h = open("slides/" + fn, encoding="utf-8").read()
    h = re.sub(r'(bottom:64px;width:1664px;font-size:24px;color:#[0-9A-F]+">)[^<]*', lambda m: m.group(1) + t, h, count=1)
    open("slides/" + fn, "w", encoding="utf-8").write(h)
print("patched")
