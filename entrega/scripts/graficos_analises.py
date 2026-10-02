# Gráficos das análises G1/G3 (tabelas com contas conferidas pelo verificador).
# Fontes: .claude/case/analises/G1-r2.md (Gráficos 1 e 5) e G3 (Gráficos 1 e 2).
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mt

OUT = "C:/Davi/Ruptura/entrega/graficos/"
BG = "#F6F4EE"; INK = "#13212E"; INK2 = "#3F4A54"; MUTED = "#5E6873"; GRID = "#DDDAD0"
BLUE = "#2A78D6"; ORANGE = "#D95926"; GRAY = "#9A978D"; BLUE_L = "#86B6EF"
plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": INK, "axes.labelcolor": INK2,
                     "xtick.color": MUTED, "ytick.color": MUTED, "figure.facecolor": BG, "axes.facecolor": BG,
                     "savefig.facecolor": BG, "font.size": 12, "axes.edgecolor": GRID,
                     "text.parse_math": False})  # "R$" não vira fórmula
brl = mt.FuncFormatter(lambda v, p: f"R$ {v:,.0f}".replace(",", "."))


def fonte(fig, txt):
    fig.text(0.01, 0.012, "\n".join(textwrap.wrap(txt, 135)), fontsize=9, color=MUTED, ha="left", va="bottom")


def clean(ax):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_color(GRID); ax.spines["bottom"].set_color(GRID)
    ax.grid(axis="y", color=GRID, lw=0.8); ax.set_axisbelow(True)


# ---- G1 Gráfico 1 (r2): custo mensal total x km — Dolphin Mini R$ 2.870 vs Onix 1.0 MT R$ 2.058,99 ----
km = [500, 1000, 1500, 2000, 2500, 3000]
ice = [2298.04, 2537.09, 2776.14, 3015.19, 3254.25, 3493.30]
ve_casa = [2934.80, 2999.60, 3064.40, 3129.20, 3194.00, 3258.80]   # tarifa residencial com impostos R$ 1,1963/kWh
ve_dc = [3005.42, 3140.83, 3276.25, 3411.67, 3547.08, 3682.50]     # 100% recarga rápida R$ 2,50/kWh
fig, ax = plt.subplots(figsize=(10, 5.8))
ax.plot(km, ice, color=ORANGE, lw=2.4, marker="o", ms=7, mec=BG, mew=2, label="Combustão de entrada (Onix 1.0): mensalidade + gasolina")
ax.plot(km, ve_casa, color=BLUE, lw=2.4, marker="o", ms=7, mec=BG, mew=2, label="Elétrico (Dolphin Mini): mensalidade + energia em casa")
ax.plot(km, ve_dc, color=BLUE, lw=1.6, ls=(0, (4, 3)), label="Elétrico só com recarga rápida pública")
ax.axvline(2330, color=INK2, lw=1)
ax.annotate("empate ≈ 2.330 km/mês" + chr(10) + "(recarga em casa)", xy=(2330, 3200), xytext=(2390, 2560), fontsize=11, color=INK,
            arrowprops=dict(arrowstyle="-", color=INK2, lw=0.8))
ax.text(1030, 2700, "+R$ 463 a 1.000 km", fontsize=12, fontweight="bold", color=INK, ha="left")
ax.text(530, 2480, "+R$ 637", fontsize=12, fontweight="bold", color=INK, ha="left")
ax.text(2970, 3330, "−R$ 235", fontsize=12, fontweight="bold", color=INK, ha="right")
ax.set_xticks(km); ax.set_xticklabels([f"{k:,}".replace(",", ".") + " km" for k in km])
ax.yaxis.set_major_formatter(brl); ax.set_ylim(2200, 3800); clean(ax)
ax.set_title("No uso típico, o elétrico custa R$ 460–640/mês a mais que o" + chr(10) + "combustão de entrada; só empata acima de ~2.330 km/mês",
             loc="left", fontsize=14, fontweight="bold", color=INK, pad=12)
ax.legend(frameon=False, fontsize=10.5, loc="upper left")
fonte(fig, "Fonte: G1 r2 (Gráfico 1). INDICATIVO DE MERCADO, não é preço Localiza (que só aparece com CPF): VE R$ 2.870 (canal BYD/Rentcars); ICE Unidas R$ 2.058,99 (36 m). "
           "Energia R$ 1,1963/kWh com impostos (MG); DC R$ 2,50/kWh; gasolina R$ 6,55 (ANP). Mensalidade suposta constante entre franquias.")
fig.tight_layout(rect=(0, 0.08, 1, 1)); fig.savefig(OUT + "05_g1_custo_total_vs_km.png", dpi=200); plt.close(fig)

# ---- G1 Gráfico 5 (r2): ponte do gap a 1.000 km (em casa, com impostos) ----
fig, ax = plt.subplots(figsize=(9.5, 5.4))
ax.bar(0, 811.01, width=0.55, color=ORANGE); ax.text(0, 831, "+R$ 811", ha="center", fontsize=13, fontweight="bold")
ax.bar(1, -348.50, bottom=811.01, width=0.55, color=BLUE); ax.text(1, 831, "−R$ 349", ha="center", fontsize=13, fontweight="bold")
ax.bar(2, 462.51, width=0.55, color=ORANGE); ax.text(2, 482, "+R$ 463", ha="center", fontsize=13, fontweight="bold")
ax.bar(3, -289, bottom=462.51, width=0.55, color=GRAY, hatch="//", edgecolor=BG); ax.text(3, 482, "−R$ 289?", ha="center", fontsize=13, fontweight="bold")
ax.bar(4, 173.51, width=0.55, color=ORANGE); ax.text(4, 193, "+R$ 174", ha="center", fontsize=13, fontweight="bold")
for a, b, y in [(0, 1, 811.01), (1, 2, 462.51), (2, 3, 462.51), (3, 4, 173.51)]:
    ax.plot([a + 0.275, b - 0.275], [y, y], color=INK2, lw=0.8)
ax.set_xticks(range(5)); ax.set_xticklabels(["Diferença na" + chr(10) + "mensalidade", "Economia de" + chr(10) + "energia", "Diferença" + chr(10) + "real", "Desconto de frota" + chr(10) + "(condicional)", "Ainda em" + chr(10) + "aberto"], fontsize=10.5)
ax.yaxis.set_major_formatter(brl); ax.set_ylim(0, 950); clean(ax)
ax.set_title("A mensalidade mostra +R$ 811; o custo real é +R$ 463 (1.000 km/mês)," + chr(10) + "e nenhuma alavanca comprovada fecha a diferença", loc="left", fontsize=14, fontweight="bold", pad=12)
fonte(fig, "Fonte: G1 r2 (Gráfico 5). Indicativo de mercado (não é preço Localiza). Energia em casa R$ 1,1963/kWh com impostos; gasolina R$ 6,55 (ANP). "
           "Desconto de frota só se a Localiza obtiver ≥ preço CNPJ e repassar; fechar o resto exigiria −3,5 p.p. de depreciação, sem evidência.")
fig.tight_layout(rect=(0, 0.08, 1, 1)); fig.savefig(OUT + "06_g1_ponte_percebido_real.png", dpi=200); plt.close(fig)

# ---- G3 Gráfico 1: pontos de recarga públicos (total e DC) ----
datas = ["dez/23", "mar/24", "jul/24", "ago/24", "fev/25", "ago/25", "fev/26", "mai/26", "ago/26"]
tot = [4300, 7758, 8800, 10622, 14827, 16880, 21061, 25429, 29866]
dc = [None, None, None, None, 2430, 3855, 6479, 8601, 11397]
fig, ax = plt.subplots(figsize=(10, 5.4))
xs = list(range(len(datas)))
ax.bar(xs, tot, width=0.6, color=BLUE_L, label="Pontos públicos e semipúblicos (total)")
ax.bar([i for i, d in enumerate(dc) if d], [d for d in dc if d], width=0.6, color=BLUE, label="dos quais recarga rápida DC")
for i, t in enumerate(tot):
    ax.text(i, t + 400, f"{t/1000:.1f} mil".replace(".", ","), ha="center", fontsize=10.5, color=INK)
ax.set_xticks(xs); ax.set_xticklabels(datas)
ax.yaxis.set_major_formatter(mt.FuncFormatter(lambda v, p: f"{v/1000:.0f} mil"))
ax.set_ylim(0, 33000); clean(ax); ax.legend(frameon=False, loc="upper left", fontsize=10.5)
ax.set_title("A rede pública cresceu ~7x em 32 meses,\ne 38% já é recarga rápida", loc="left", fontsize=14, fontweight="bold", pad=12)
fonte(fig, "Fonte: G3 (Gráfico 1): ABVE/Tupi (fev/25–ago/26), CNN Brasil (2023–2024), Forbes (ago/25). DC sem dado antes de fev/25.")
fig.tight_layout(rect=(0, 0.07, 1, 1)); fig.savefig(OUT + "07_g3_pontos_recarga.png", dpi=200); plt.close(fig)

# ---- G3 Gráfico 2: VEs por ponto público ----
mk = [("China", 10), ("Média global", 11), ("União Europeia", 11), ("Brasil mai/26", 19.9), ("Brasil ago/26", 21.4), ("EUA", 33)]
fig, ax = plt.subplots(figsize=(9, 5))
cols = [GRAY if "Brasil" not in m else ORANGE for m, _ in mk]
ax.barh(range(len(mk)), [v for _, v in mk], height=0.55, color=cols)
for i, (m, v) in enumerate(mk):
    ax.text(v + 0.4, i, f"{v:g}".replace(".", ","), va="center", fontsize=12, fontweight="bold", color=INK)
ax.set_yticks(range(len(mk))); ax.set_yticklabels([m for m, _ in mk]); ax.invert_yaxis()
ax.axvline(10, color=INK2, lw=1, ls=(0, (3, 3))); ax.text(10.3, -0.55, "meta ABVE 10:1", fontsize=10, color=INK2)
ax.set_xlim(0, 37); ax.set_xticks([]); [ax.spines[s].set_visible(False) for s in ax.spines]
ax.set_title("Veículos elétricos por ponto público:\no Brasil tem quase o dobro da média global", loc="left", fontsize=14, fontweight="bold", pad=12)
fonte(fig, "Fonte: G3 (Gráfico 2): ABVE (plug-ins desde 2022 por ponto público/semipúblico, mai/26 e ago/26, mesma base), IEA via EV Infrastructure News (fim 2025). "
           "Metodologias diferem: comparação de ordem de grandeza.")
fig.tight_layout(rect=(0, 0.08, 1, 1)); fig.savefig(OUT + "08_g3_ve_por_ponto.png", dpi=200); plt.close(fig)
print("ok")
