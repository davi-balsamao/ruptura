"""Simulador Elétrico (MVP): custo total e rotina do elétrico por assinatura, sem CPF.

Rodar:  python rodar.py   (ou: streamlit run app.py, de dentro desta pasta)
Fora do escopo desta versão: mapa e rota de eletropostos (próxima fase).
"""
from dataclasses import replace

import altair as alt
import pandas as pd
import streamlit as st

from simulador.custo import custo_mensal, empate_km, franquia_sugerida, wallbox_incluso
from simulador.formato import brl, num, pct
from simulador.premissas import (
    ENERGIA,
    FONTES,
    ICE_AUTOMATICO,
    ICE_ENTRADA,
    INCLUSO_NA_MENSALIDADE,
    PRAZOS,
    VE,
    WALLBOX,
)
from simulador.rotina import (
    Moradia,
    Rotina,
    autonomia_planejamento,
    bateria_por_dia,
    caminho_recarga_casa,
    fracao_casa,
    horas_wallbox_semana,
    km_semana_de_km_mes,
    paradas_por_viagem,
    recargas_por_semana,
)

VERDE, VERDE_ESCURO, LIMA = "#018444", "#004521", "#78DE1F"
TEXTO, TEXTO_2, FUNDO = "#383838", "#6B6B6B", "#F2F2F2"
CINZA_LINHA = "#9A9A9A"

st.set_page_config(page_title="Simulador Elétrico", page_icon="⚡", layout="wide")

CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');
html, body, [data-testid="stAppViewContainer"], [data-testid="stMarkdownContainer"],
button, input, label, textarea, h1, h2, h3, p, li, div, span:not([data-testid="stIconMaterial"]), [data-baseweb] {{ font-family: 'Inter', Arial, sans-serif !important; }}
header[data-testid="stHeader"], #MainMenu, footer, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stStatusWidget"] {{ display: none !important; }}
[data-testid="stMain"] {{ overflow-x: hidden; }}
.block-container {{ padding-top: 0 !important; padding-bottom: 2rem; max-width: 1240px; }}
[data-testid="stAppViewContainer"] {{ background: #FFFFFF; color: {TEXTO}; }}

.faixa {{ position: relative; left: 50%; right: 50%; margin-left: -50vw; margin-right: -50vw; width: 100vw; }}
.faixa > .miolo {{ max-width: 1240px; margin: 0 auto; padding: 0 1rem; }}
.topo {{ background: {FUNDO}; }}
.topo .miolo {{ display: flex; align-items: center; justify-content: space-between; height: 72px; }}
.marca {{ display: flex; align-items: center; gap: 10px; color: {VERDE}; font-weight: 700; font-size: 19px; line-height: 1; }}
.marca small {{ display: block; font-weight: 500; font-size: 12px; color: {TEXTO_2}; margin-top: 3px; }}
.marca .icone {{ width: 34px; height: 34px; border-radius: 10px; background: {VERDE}; display: flex; align-items: center; justify-content: center; }}
.pilula {{ background: {LIMA}; color: {VERDE_ESCURO}; font-weight: 600; font-size: 15px; border-radius: 16px; padding: 10px 20px; text-decoration: none !important; }}
.heroi {{ background: {VERDE_ESCURO}; color: #FFF; overflow: hidden; }}
.heroi .miolo {{ display: flex; align-items: center; justify-content: space-between; min-height: 210px; position: relative; }}
.heroi h1 {{ color: #FFF !important; font-size: 34px; font-weight: 700; line-height: 1.15; margin: 0 0 12px; padding: 0; }}
.heroi p {{ color: #FFF; font-size: 17px; font-weight: 600; margin: 0; max-width: 620px; line-height: 1.45; }}
.heroi .selos {{ display: flex; gap: 8px; margin-top: 18px; flex-wrap: wrap; }}
.heroi .selo {{ border: 1.5px solid {LIMA}; color: {LIMA}; border-radius: 999px; padding: 5px 14px; font-size: 13px; font-weight: 600; }}
.arco {{ width: 230px; height: 190px; border-radius: 115px 115px 0 0; background: {LIMA}; align-self: flex-end;
         display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
.arco > div {{ width: 170px; height: 140px; border-radius: 85px 85px 0 0; background: {VERDE_ESCURO}; margin-top: 50px;
               display: flex; align-items: center; justify-content: center; }}

.passo {{ display: flex; align-items: center; gap: 12px; font-size: 16px; font-weight: 600; color: {TEXTO}; margin: 6px 0 2px; }}
.passo .n {{ width: 28px; height: 28px; border-radius: 50%; background: {LIMA}; color: {VERDE_ESCURO}; font-weight: 700;
             font-size: 14px; display: flex; align-items: center; justify-content: center; flex-shrink: 0; }}
.dica {{ color: {TEXTO_2}; font-size: 13.5px !important; margin: 0 0 4px; }}
.st-key-perfil {{ position: sticky; top: 16px; background: #FFF; border-radius: 16px !important; box-shadow: 0 2px 14px rgba(0,0,0,.08); border: none !important; padding: 8px 6px; }}

.manchete .tag {{ display: inline-block; background: {FUNDO}; color: {TEXTO_2}; border-radius: 999px; padding: 4px 12px; font-size: 13px; font-weight: 500; }}
.manchete h2 {{ font-size: 25px; font-weight: 700; color: {TEXTO}; line-height: 1.25; margin: 10px 0 6px; padding: 0; }}
.manchete h2 b {{ color: {VERDE}; }}
.manchete p {{ font-size: 15px !important; color: {TEXTO_2}; margin: 0; }}
.cartoes {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 14px; margin: 18px 0 8px; }}
.cartao {{ background: #FFF; border-radius: 16px; box-shadow: 0 2px 14px rgba(0,0,0,.08); padding: 18px 20px; display: flex; flex-direction: column; gap: 6px; }}
.cartao .rot {{ font-size: 13px; font-weight: 600; color: {TEXTO_2}; }}
.cartao .modelo {{ font-size: 12px; color: {TEXTO_2}; margin-top: -4px; }}
.cartao .valor {{ font-size: 28px; font-weight: 800; color: {TEXTO}; line-height: 1.1; }}
.cartao .valor span {{ font-size: 14px; font-weight: 500; }}
.cartao .det {{ font-size: 13px; color: {TEXTO_2}; }}
.cartao .dif {{ align-self: flex-start; border-radius: 999px; padding: 4px 10px; font-size: 12.5px; font-weight: 600; background: {FUNDO}; color: {TEXTO}; margin-top: 4px; }}
.cartao .dif.bom {{ background: #E3F6D2; color: {VERDE_ESCURO}; }}
.cartao.destaque {{ background: {VERDE_ESCURO}; }}
.cartao.destaque .rot, .cartao.destaque .modelo, .cartao.destaque .det {{ color: #CFE3D6; }}
.cartao.destaque .valor {{ color: #FFF; }}
.cartao.destaque .dif {{ background: {LIMA}; color: {VERDE_ESCURO}; }}

.lista {{ list-style: none; padding: 0; margin: 4px 0 0; display: grid; grid-template-columns: 1fr 1fr; gap: 8px 18px; }}
.lista li {{ display: flex; gap: 10px; align-items: flex-start; font-size: 14px; color: {TEXTO}; }}
.lista li::before {{ content: "✓"; flex-shrink: 0; width: 20px; height: 20px; border-radius: 50%; background: {LIMA}; color: {VERDE_ESCURO};
                    font-weight: 800; font-size: 12px; display: flex; align-items: center; justify-content: center; margin-top: 1px; }}
.lista li.forte {{ font-weight: 600; }}
.etapas {{ counter-reset: e; list-style: none; padding: 0; margin: 6px 0 0; display: flex; flex-direction: column; gap: 10px; }}
.etapas li {{ counter-increment: e; display: flex; gap: 12px; align-items: flex-start; font-size: 14.5px; color: {TEXTO}; }}
.etapas li::before {{ content: counter(e); flex-shrink: 0; width: 24px; height: 24px; border-radius: 50%; background: {VERDE}; color: #FFF;
                     font-weight: 700; font-size: 12px; display: flex; align-items: center; justify-content: center; }}
.legenda {{ display: flex; flex-wrap: wrap; align-items: center; gap: 6px 18px; font-size: 13px; color: {TEXTO}; margin: 14px 0 0; }}
.legenda span {{ display: inline-flex; align-items: center; gap: 6px; }}
.legenda .eixo {{ color: {TEXTO_2}; margin-left: auto; }}
.secao {{ font-size: 17px; font-weight: 700; color: {TEXTO}; margin: 22px 0 8px; }}
.nota {{ font-size: 12.5px !important; color: {TEXTO_2}; line-height: 1.5; margin-top: 14px; }}
.aviso {{ background: {FUNDO}; border-radius: 16px; padding: 14px 18px; font-size: 14px; color: {TEXTO}; margin-top: 12px; }}
.aviso b {{ color: {VERDE}; }}
.rodape {{ background: {FUNDO}; margin-top: 36px; }}
.rodape .miolo {{ padding: 18px 1rem; font-size: 12.5px; color: {TEXTO_2}; }}

[data-testid="stButtonGroup"] button {{ padding-left: 12px !important; padding-right: 12px !important; }}
button[data-baseweb="tab"] p {{ font-size: 15px; font-weight: 600; }}
[data-testid="stSlider"] [data-testid="stTickBarMin"], [data-testid="stSlider"] [data-testid="stTickBarMax"] {{ color: {TEXTO_2}; }}
@media (max-width: 900px) {{ .cartoes, .lista {{ grid-template-columns: 1fr; }} .arco {{ display: none; }} }}
</style>
"""

RAIO = (
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="none"><path d="M13 2 4 14h7l-1 8 9-12h-7l1-8z" '
    'fill="{cor}"/></svg>'
)


def _traco(cor: str, dash: str, largura: float) -> str:
    return (f'<svg width="28" height="10"><line x1="1" y1="5" x2="27" y2="5" stroke="{cor}" '
            f'stroke-width="{largura}" stroke-dasharray="{dash}" stroke-linecap="round"/></svg>')


LEGENDA = (
    '<div class="legenda">'
    f'<span>{_traco(VERDE, "0", 3.5)}Elétrico</span>'
    f'<span>{_traco(TEXTO, "7 4", 2)}Combustão automático</span>'
    f'<span>{_traco(CINZA_LINHA, "2 3", 2)}Combustão de entrada</span>'
    '<span class="eixo">R$ por mês (mensalidade + energia)</span></div>'
)


def passo(n: int, texto: str, dica: str = "") -> None:
    html = f'<div class="passo"><span class="n">{n}</span>{texto}</div>'
    if dica:
        html += f'<p class="dica">{dica}</p>'
    st.markdown(html, unsafe_allow_html=True)


def topo_e_heroi() -> None:
    st.markdown(
        f"""
<div class="faixa topo"><div class="miolo">
  <div class="marca"><span class="icone">{RAIO.format(cor=LIMA)}</span>
    <div>Simulador Elétrico<small>Assinatura de carros · protótipo do Case Ruptura 2026</small></div></div>
  <a class="pilula" href="#resumo">Fale com um consultor</a>
</div></div>
<div class="faixa heroi"><div class="miolo">
  <div style="padding:32px 0">
    <h1>Quanto custa ter um elétrico por assinatura?</h1>
    <p>Compare com o carro a combustão e veja como fica a recarga na sua rotina.
       Sem CPF e sem cadastro.</p>
    <div class="selos"><span class="selo">Custo total do mês</span><span class="selo">Recarga em casa inclusa</span>
      <span class="selo">Risco da bateria é nosso</span></div>
  </div>
  <div class="arco"><div>{RAIO.format(cor=LIMA).replace('width="18" height="18"', 'width="64" height="64"')}</div></div>
</div></div>
""",
        unsafe_allow_html=True,
    )


def perfil() -> dict:
    with st.container(border=True, key="perfil"):
        passo(1, "Onde você mora?")
        escolha = st.segmented_control(
            "Onde você mora?", [m.value for m in Moradia], default=Moradia.CASA.value,
            label_visibility="collapsed", key="moradia",
        )
        moradia = Moradia(escolha or Moradia.CASA.value)

        passo(2, "Por quanto tempo você quer ficar com o carro?")
        rotulos = [f"{p} meses" for p in PRAZOS]
        escolha = st.segmented_control(
            "Prazo", rotulos, default="36 meses", label_visibility="collapsed", key="prazo",
        )
        prazo = int((escolha or "36 meses").split()[0])

        passo(3, "Quanto você roda?")
        modo = st.segmented_control(
            "Como informar", ["Por mês", "Pela minha rotina"], default="Por mês",
            label_visibility="collapsed", key="modo",
        ) or "Por mês"
        rotina = None
        if modo == "Pela minha rotina":
            c1, c2 = st.columns(2)
            km_dia = c1.number_input("km por dia (ida e volta)", 0, 400, 40, step=5)
            dias = c2.number_input("Dias com esse trajeto por semana", 0, 7, 5)
            extras = c1.number_input("Passeios e extras (km por semana)", 0, 1500, 30, step=10)
            viagens = c2.number_input("Viagens longas por mês", 0, 10, 1)
            km_viagem = st.number_input("km por viagem longa (ida e volta)", 0, 2000, 400, step=50)
            rotina = Rotina(km_dia, dias, extras, viagens, km_viagem)
            km_mes = rotina.km_mes
        else:
            km_mes = st.slider("km por mês", 300, 3000, 1000, step=50, format="%d km", label_visibility="collapsed")

        franquia = franquia_sugerida(km_mes)
        texto_franquia = f"franquia sugerida de {num(franquia)} km" if franquia else "acima da maior franquia (3.000 km)"
        st.markdown(f'<p class="dica">≈ <b>{num(km_mes)} km por mês</b> · {texto_franquia}</p>', unsafe_allow_html=True)

        autonomia = autonomia_planejamento(VE)
        if rotina:
            casa_auto = fracao_casa(rotina, moradia, autonomia)
        else:
            casa_auto = 0.0 if moradia is Moradia.SEM_VAGA else 1.0

        with st.expander("Ajustar premissas"):
            st.caption("Preços indicativos de mercado (out/2026). A tabela oficial substitui estes valores.")
            c1, c2 = st.columns(2)
            m_ve = c1.number_input("Mensalidade do elétrico (R$)", 0.0, 20000.0, VE.mensalidade, step=50.0)
            m_auto = c2.number_input("Combustão automático (R$)", 0.0, 20000.0, ICE_AUTOMATICO.mensalidade, step=50.0)
            m_entr = c1.number_input("Combustão de entrada (R$)", 0.0, 20000.0, ICE_ENTRADA.mensalidade, step=50.0)
            gas = c2.number_input("Gasolina (R$/L)", 0.0, 20.0, ENERGIA.gasolina, step=0.05)
            t_casa = c1.number_input("Energia em casa (R$/kWh)", 0.0, 5.0, ENERGIA.tarifa_casa, step=0.05, format="%.4f")
            t_rua = c2.number_input("Recarga rápida na rua (R$/kWh)", 0.0, 10.0, ENERGIA.tarifa_rua, step=0.10)
            rua = st.slider(
                "Parte da recarga feita na rua", 0, 100, round((1 - casa_auto) * 100), format="%d%%",
                key=f"rua-{moradia.name}-{modo}-{round(casa_auto * 100)}",
            )
            st.markdown(
                "<p class='dica'>Fontes: " + " · ".join(f"<a href='{u}' target='_blank'>{r}</a>" for r, u in FONTES) + "</p>",
                unsafe_allow_html=True,
            )

    return {
        "moradia": moradia, "prazo": prazo, "rotina": rotina, "km_mes": km_mes, "autonomia": autonomia,
        "casa": 1 - rua / 100,
        "ve": replace(VE, mensalidade=m_ve),
        "auto": replace(ICE_AUTOMATICO, mensalidade=m_auto),
        "entrada": replace(ICE_ENTRADA, mensalidade=m_entr),
        "energia": replace(ENERGIA, gasolina=gas, tarifa_casa=t_casa, tarifa_rua=t_rua),
    }


def calcular(p: dict) -> dict:
    km, en, casa = p["km_mes"], p["energia"], p["casa"]
    r = {
        "ve": custo_mensal(p["ve"], km, en, casa),
        "auto": custo_mensal(p["auto"], km, en),
        "entrada": custo_mensal(p["entrada"], km, en),
        "empate": empate_km(p["ve"], p["entrada"], en, casa),
        "wallbox": p["moradia"] is not Moradia.SEM_VAGA and wallbox_incluso(p["prazo"]),
    }
    r["d_auto"] = r["ve"].total - r["auto"].total
    r["d_entrada"] = r["ve"].total - r["entrada"].total
    return r


def frase_diferenca(d: float) -> str:
    return f"{brl(abs(d))} mais barato" if d < 0 else f"{brl(d)} mais caro"


def sinal(d: float) -> str:
    return brl(d) if d < 0 else "+" + brl(d)


def frase_empate(empate: float | None) -> str:
    if empate is None:
        return "com essa recarga, não chega a empatar"
    if empate > 3000:
        return "empataria só acima de 3.000 km/mês"
    return f"empata a partir de ~{num(round(empate, -1))} km/mês"


def grafico(p: dict) -> alt.LayerChart:
    series = [("Elétrico", p["ve"], p["casa"]), ("Combustão automático", p["auto"], 1.0),
              ("Combustão de entrada", p["entrada"], 1.0)]
    ordem = [s[0] for s in series]
    kms = list(range(300, 3001, 50))
    longo = pd.DataFrame(
        [{"km": km, "carro": nome, "total": custo_mensal(c, km, p["energia"], f).total}
         for nome, c, f in series for km in kms]
    )
    largo = longo.pivot(index="km", columns="carro", values="total").reset_index()
    largo["km_txt"] = largo["km"].map(lambda v: f"{num(v)} km/mês")
    for nome in ordem:
        largo[nome] = largo[nome].map(brl)

    cor = alt.Scale(domain=ordem, range=[VERDE, TEXTO, CINZA_LINHA])
    traco = alt.Scale(domain=ordem, range=[[1, 0], [7, 4], [2, 3]])
    eixo_x = alt.X("km:Q", title="km por mês", scale=alt.Scale(domain=[300, 3000], nice=False),
                   axis=alt.Axis(values=[500, 1000, 1500, 2000, 2500, 3000],
                                 labelExpr="replace(format(datum.value, ',.0f'), ',', '.')"))
    eixo_y = alt.Y("total:Q", title=None, scale=alt.Scale(zero=False),
                   axis=alt.Axis(labelExpr="'R$ ' + replace(format(datum.value, ',.0f'), ',', '.')", tickCount=5))

    linhas = alt.Chart(longo).mark_line().encode(
        x=eixo_x, y=eixo_y,
        color=alt.Color("carro:N", scale=cor, legend=None, sort=ordem),
        strokeDash=alt.StrokeDash("carro:N", scale=traco, legend=None, sort=ordem),
        size=alt.Size("carro:N", scale=alt.Scale(domain=ordem, range=[3.5, 2, 2]), legend=None),
    )
    passa = alt.selection_point(fields=["km"], nearest=True, on="pointerover", clear="pointerout", empty=False)
    regua = alt.Chart(largo).mark_rule(color="#C9C9C9", strokeWidth=1).encode(
        x="km:Q",
        opacity=alt.condition(passa, alt.value(1), alt.value(0)),
        tooltip=[alt.Tooltip("km_txt:N", title="Rodando")] + [alt.Tooltip(f"{n}:N", title=n) for n in ordem],
    ).add_params(passa)

    voce = pd.DataFrame({"km": [p["km_mes"]], "rotulo": [f"Você: {num(p['km_mes'])} km"]})
    marca = alt.Chart(voce).mark_rule(color=VERDE_ESCURO, strokeDash=[4, 4], strokeWidth=1.5).encode(x="km:Q")
    marca_txt = alt.Chart(voce).mark_text(align="left", dx=6, y=6, fontSize=12, fontWeight=600,
                                          color=VERDE_ESCURO, font="Inter").encode(x="km:Q", text="rotulo:N")
    pontos = alt.Chart(longo[longo["km"] == min(kms, key=lambda k: abs(k - p["km_mes"]))]).mark_point(
        filled=True, size=90, opacity=1, stroke="#FFFFFF", strokeWidth=2
    ).encode(x="km:Q", y="total:Q", color=alt.Color("carro:N", scale=cor, legend=None))

    return (
        alt.layer(linhas, regua, marca, marca_txt, pontos)
        .properties(height=330)
        .configure_axis(labelFont="Inter", titleFont="Inter", labelColor=TEXTO_2, titleColor=TEXTO_2,
                        labelFontSize=12, titleFontSize=12, titleFontWeight=500, gridColor="#EDEDED",
                        domainColor="#D6D6D6", tickColor="#D6D6D6")
        .configure_axisX(grid=False)
        .configure_legend(labelFont="Inter")
        .configure_view(strokeWidth=0)
    )


def cartao(rotulo: str, modelo: str, total: float, detalhe: str, dif: str = "", classe_dif: str = "",
           destaque: bool = False) -> str:
    chip = f'<span class="dif {classe_dif}">{dif}</span>' if dif else ""
    return (f'<div class="cartao{" destaque" if destaque else ""}"><div class="rot">{rotulo}</div>'
            f'<div class="modelo">{modelo}</div><div class="valor">{brl(total)}<span>/mês</span></div>'
            f'<div class="det">{detalhe}</div>{chip}</div>')


def aba_custo(p: dict, r: dict) -> None:
    ve, auto, entrada = r["ve"], r["auto"], r["entrada"]
    recarga = f"{pct(p['casa'])} da recarga em casa" if p["casa"] > 0 else "recarga só na rua"
    if r["d_auto"] < 0:
        h2 = f"Contra um combustão automático, o elétrico sai <b>{brl(-r['d_auto'])} mais barato</b> por mês"
    else:
        h2 = f"Contra um combustão automático, o elétrico custa {brl(r['d_auto'])} a mais por mês"
    if r["d_entrada"] > 0:
        sub = (f"Contra um combustão de entrada (manual), custa {brl(r['d_entrada'])} a mais e "
               f"{frase_empate(r['empate'])}.")
    else:
        sub = f"Contra um combustão de entrada (manual), também sai {brl(-r['d_entrada'])} mais barato."
    st.markdown(
        f'<div class="manchete"><span class="tag">{num(p["km_mes"])} km/mês · {recarga} · plano de {p["prazo"]} meses</span>'
        f"<h2>{h2}</h2><p>{sub}</p></div>",
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="cartoes">'
        + cartao("Elétrico", "BYD Dolphin Mini", ve.total,
                 f"Mensalidade {brl(ve.mensalidade)} + energia {brl(ve.energia)}",
                 "Wallbox incluso" if r["wallbox"] else ("Recarga em casa" if p["casa"] > 0 else "Recarga na rua"),
                 destaque=True)
        + cartao("Combustão automático", "Onix Hatch 1.0 Turbo AT", auto.total,
                 f"Mensalidade {brl(auto.mensalidade)} + gasolina {brl(auto.energia)}",
                 f"Elétrico: {sinal(r['d_auto'])}", "bom" if r["d_auto"] < 0 else "")
        + cartao("Combustão de entrada", "Onix 1.0 manual", entrada.total,
                 f"Mensalidade {brl(entrada.mensalidade)} + gasolina {brl(entrada.energia)}",
                 f"Elétrico: {sinal(r['d_entrada'])}", "bom" if r["d_entrada"] < 0 else "")
        + "</div>",
        unsafe_allow_html=True,
    )
    st.markdown(LEGENDA, unsafe_allow_html=True)
    st.altair_chart(grafico(p), theme=None, width="stretch")

    itens = [f"<li>{i}</li>" for i in INCLUSO_NA_MENSALIDADE]
    if r["wallbox"]:
        itens.insert(0, f'<li class="forte">Wallbox de {num(WALLBOX.potencia_kw, 1)} kW e instalação até '
                        f'{brl(WALLBOX.instalacao_teto)}; quando você deixar a assinatura, o wallbox é seu</li>')
    elif p["moradia"] is not Moradia.SEM_VAGA:
        itens.insert(0, '<li class="forte">Wallbox opcional no plano de 12 meses, com coparticipação</li>')
    st.markdown(f'<div class="secao">Já está na sua mensalidade</div><ul class="lista">{"".join(itens)}</ul>',
                unsafe_allow_html=True)
    st.markdown(
        '<p class="nota">Mensalidades indicativas de mercado (out/2026), iguais em todos os prazos e franquias: '
        "não são preços da Localiza, que hoje só aparecem com CPF. Energia em casa a "
        f"{brl(p['energia'].tarifa_casa, 2)}/kWh com impostos; recarga rápida a {brl(p['energia'].tarifa_rua, 2)}/kWh; "
        f"gasolina a {brl(p['energia'].gasolina, 2)}/L. Ajuste em “Ajustar premissas”.</p>",
        unsafe_allow_html=True,
    )


def aba_rotina(p: dict) -> None:
    rotina, autonomia = p["rotina"], p["autonomia"]
    km_semana = rotina.km_semana if rotina else km_semana_de_km_mes(p["km_mes"])
    horas = horas_wallbox_semana(km_semana, p["ve"])
    vezes = recargas_por_semana(km_semana, autonomia)
    if rotina:
        quarto = (f"{pct(bateria_por_dia(rotina.km_dia_util, p['ve']))}", "da bateria num dia de trajeto")
    else:
        quarto = (f"~{num(autonomia)} km", "para planejar com a bateria cheia")
    sem_vaga = p["moradia"] is Moradia.SEM_VAGA
    cartoes = [
        (f"{num(km_semana)} km", "por semana"),
        (f"{vezes}×", "por semana na tomada" if not sem_vaga else "por semana na recarga rápida"),
        (f"{num(horas, 1)} h" if not sem_vaga else "—", "de wallbox por semana (7,4 kW)" if not sem_vaga else "sem wallbox"),
        quarto,
    ]
    st.markdown(
        '<div class="cartoes" style="grid-template-columns:repeat(4,1fr)">'
        + "".join(f'<div class="cartao"><div class="valor">{v}</div><div class="det">{t}</div></div>' for v, t in cartoes)
        + "</div>",
        unsafe_allow_html=True,
    )
    if not sem_vaga:
        noite = "Uma noite no wallbox repõe a semana inteira." if horas <= 8 else "A semana pede mais de uma noite no wallbox."
        st.markdown(f'<p class="dica">{noite} O carro pode aceitar menos que 7,4 kW; o tempo real pode ser maior.</p>',
                    unsafe_allow_html=True)

    st.markdown('<div class="secao">Vai viajar?</div>', unsafe_allow_html=True)
    padrao = int(rotina.km_viagem) if rotina and rotina.km_viagem else 400
    km_viagem = st.number_input("Distância da viagem, ida e volta (km)", 0, 3000, padrao, step=50)
    paradas = paradas_por_viagem(km_viagem, autonomia)
    if paradas == 0:
        frase = "Dá para ir e voltar com uma carga, sem parar para recarregar."
    else:
        frase = f"<b>{paradas} {'parada' if paradas == 1 else 'paradas'}</b> para recarga rápida no caminho."
    st.markdown(
        f'<div class="aviso">{frase} Conta feita saindo de casa com a bateria cheia e guardando 20% de reserva.<br>'
        "<b>Próxima fase:</b> mapa e rota de eletropostos no app, mostrando onde parar.</div>",
        unsafe_allow_html=True,
    )

    titulo = "Recarga em casa: o seu caminho" if not sem_vaga else "Sem vaga própria"
    passos = "".join(f"<li>{t}</li>" for t in caminho_recarga_casa(p["moradia"], p["prazo"]))
    st.markdown(f'<div class="secao">{titulo}</div><ol class="etapas">{passos}</ol>', unsafe_allow_html=True)


def resumo_texto(p: dict, r: dict) -> str:
    linhas = [
        "Simulação: elétrico por assinatura (protótipo)",
        f"Perfil: {p['moradia'].value} · plano de {p['prazo']} meses · {num(p['km_mes'])} km/mês",
        f"Elétrico: {brl(r['ve'].total)}/mês (mensalidade {brl(r['ve'].mensalidade)} + energia {brl(r['ve'].energia)})",
        f"Combustão automático: {brl(r['auto'].total)}/mês → elétrico {frase_diferenca(r['d_auto'])}",
        f"Combustão de entrada: {brl(r['entrada'].total)}/mês → elétrico {frase_diferenca(r['d_entrada'])}",
    ]
    if r["wallbox"]:
        linhas.append(f"Recarga em casa: wallbox {num(WALLBOX.potencia_kw, 1)} kW + instalação até "
                      f"{brl(WALLBOX.instalacao_teto)} inclusos; ao deixar a assinatura, o wallbox é seu")
    linhas.append("Valores indicativos de mercado. A cotação oficial é feita com o consultor.")
    return "\n".join(linhas)


def aba_resumo(p: dict, r: dict) -> None:
    st.markdown('<div id="resumo" class="secao" style="margin-top:6px">Leve esta conta para o consultor</div>'
                '<p class="dica">Copie e mande no WhatsApp, ou baixe o arquivo. Nenhum dado pessoal é pedido.</p>',
                unsafe_allow_html=True)
    texto = resumo_texto(p, r)
    st.code(texto, language=None, wrap_lines=True)
    c1, c2 = st.columns(2)
    c1.download_button("Baixar resumo", texto, file_name="simulacao-eletrico.txt", width="stretch")
    if c2.button("Fale com um consultor", type="primary", width="stretch"):
        st.toast("No piloto, este botão abre o WhatsApp do consultor já com este resumo.")


def main() -> None:
    st.markdown(CSS, unsafe_allow_html=True)
    topo_e_heroi()
    st.write("")
    col_perfil, col_resultado = st.columns([0.38, 0.62], gap="large")
    with col_perfil:
        p = perfil()
    r = calcular(p)
    with col_resultado:
        custo, rotina, resumo = st.tabs(["Custo total", "Minha rotina", "Resumo para o consultor"])
        with custo:
            aba_custo(p, r)
        with rotina:
            aba_rotina(p)
        with resumo:
            aba_resumo(p, r)
    st.markdown(
        '<div class="faixa rodape"><div class="miolo">Protótipo do Case Ruptura 2026, não é um site oficial. '
        "Valores indicativos de mercado (out/2026), não são preços da Localiza. "
        "Mapa e rota de eletropostos: próxima fase.</div></div>",
        unsafe_allow_html=True,
    )


main()
