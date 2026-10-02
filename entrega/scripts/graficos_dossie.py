# Gráficos do Case 1 Localiza — só dados do dossiê (dados-case1.md). Cada gráfico cita o #id na fonte.
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = "C:/Davi/Ruptura/entrega/graficos/"
BG = "#F6F4EE"; INK = "#13212E"; INK2 = "#3F4A54"; MUTED = "#5E6873"; GRID = "#DDDAD0"
BLUE = "#2A78D6"; ORANGE = "#D95926"; GRAY = "#B9B6AC"; ORANGE_L = "#F0B08F"
plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": INK, "axes.labelcolor": INK2,
                     "xtick.color": MUTED, "ytick.color": MUTED, "figure.facecolor": BG, "axes.facecolor": BG,
                     "savefig.facecolor": BG, "font.size": 13})

def fonte(fig, txt):
    fig.text(0.01, 0.015, txt, fontsize=10, color=MUTED, ha="left")

# 1) Top 10 preocupações x situação da Localiza  (#preoc-1..10, p.16 do PDF da banca)
preoc = [
    (1, "Bateria e vida útil", "Atende"),
    (2, "Locais para recarga na rotina", "Não atende"),
    (3, "Instalação de wallbox em casa/trabalho", "Parcial"),
    (4, "Preço/mensalidade mais alta que combustão", "Não atende"),
    (5, "Locais para recarga em viagens", "Não atende"),
    (6, "Revenda/depreciação", "Atende"),
    (7, "Segurança/confiabilidade em pane", "Atende"),
    (8, "Contrato claro e sem surpresas", "Atende"),
    (9, "Previsibilidade de custos de manutenção", "Atende"),
    (10, "Disponibilidade para entrega rápida", "Parcial"),
]
cor = {"Atende": GRAY, "Parcial": ORANGE_L, "Não atende": ORANGE}
fig, ax = plt.subplots(figsize=(11, 6.2))
ax.set_xlim(0, 10); ax.set_ylim(10.6, 0.2); ax.axis("off")
for i, (n, txt, st) in enumerate(preoc):
    y = i + 1
    ax.text(0.15, y, f"#{n}", va="center", fontsize=13, color=MUTED, fontweight="bold")
    ax.text(0.85, y, txt, va="center", fontsize=14, color=INK if st != "Atende" else INK2,
            fontweight="bold" if st == "Não atende" else "normal")
    ax.add_patch(FancyBboxPatch((7.2, y - 0.32), 2.5, 0.64, boxstyle="round,pad=0,rounding_size=0.25",
                                fc=cor[st], ec="none"))
    ax.text(8.45, y, st.upper(), va="center", ha="center", fontsize=11.5, fontweight="bold",
            color="white" if st == "Não atende" else INK)
    if n == 5:
        ax.axhline(5.55, xmin=0.01, xmax=0.99, color=INK2, lw=1)
ax.text(0.15, 0.05, "Top 10 preocupações do lead de elétrico  ·  situação atual da Localiza", fontsize=16,
        fontweight="bold", color=INK, va="bottom")
ax.text(9.7, 5.75, "top 5 ↑", fontsize=10, color=INK2, ha="right", va="top")
fonte(fig, "Fonte: dados-case1.md #preoc-1 a #preoc-10 (Pesquisa Localiza Jul/2026, 1.000 leads RAC não-convertidos e clientes RAC; PDF da banca p.16)")
fig.tight_layout(rect=(0, 0.04, 1, 1)); fig.savefig(OUT + "01_top10_preocupacoes.png", dpi=200); plt.close(fig)

# 2) Awareness em planos de assinatura (#awareness)
marcas = ["Localiza\nAssinatura", "Movida", "Unidas", "VW\nSign&Drive"]
vals = [95, 86, 69, 20]
fig, ax = plt.subplots(figsize=(8, 4.6))
bars = ax.bar(marcas, vals, width=0.5, color=[BLUE, GRAY, GRAY, GRAY], edgecolor=BG, linewidth=2)
for b, v in zip(bars, vals):
    ax.text(b.get_x() + b.get_width() / 2, v + 2, f"{v}%", ha="center", fontsize=15, fontweight="bold", color=INK)
ax.set_ylim(0, 110); ax.set_yticks([]); [s.set_visible(False) for s in ax.spines.values()]
ax.axhline(0, color=GRID, lw=1)
ax.set_title("Awareness em planos de assinatura", loc="left", fontsize=16, fontweight="bold", color=INK, pad=14)
fonte(fig, "Fonte: dados-case1.md #awareness (pesquisa ~1.000 leads e clientes, Jul/2026)")
fig.tight_layout(rect=(0, 0.05, 1, 1)); fig.savefig(OUT + "02_awareness.png", dpi=200); plt.close(fig)

# 3) Efeito do eletrificado na vontade de assinar (#59) — barra empilhada horizontal
partes = [(59, "Aumenta minha vontade de assinar", BLUE), (36, "Não muda / não sei", GRAY), (5, "Diminui", ORANGE)]
fig, ax = plt.subplots(figsize=(11, 2.6))
left = 0
for v, lab, c in partes:
    ax.barh(0, v, left=left, height=0.5, color=c, edgecolor=BG, linewidth=2)
    if v >= 10:
        ax.text(left + v / 2, 0, f"{v}%", ha="center", va="center", fontsize=16, fontweight="bold",
                color="white" if c != GRAY else INK)
    left += v
ax.text(97.5, 0.42, "5%", ha="center", fontsize=13, fontweight="bold", color=INK)
ax.set_xlim(0, 100); ax.set_ylim(-0.6, 0.75); ax.axis("off")
import matplotlib.patches as mp
ax.legend(handles=[mp.Patch(color=c, label=l) for _, l, c in partes], loc="lower center", ncol=3,
          bbox_to_anchor=(0.5, -0.55), frameon=False, fontsize=12)
ax.set_title("Ao pensar em eletrificado, a vontade de assinar…", loc="left", fontsize=16, fontweight="bold", color=INK)
fonte(fig, "Fonte: dados-case1.md #59 / #pdf-59-vs-compra (pesquisa ~1.000 leads e clientes, Jul/2026)")
fig.tight_layout(rect=(0, 0.08, 1, 1)); fig.savefig(OUT + "03_efeito_eletrificado.png", dpi=200); plt.close(fig)

# 4) O vazamento: dos leads de VE que assinaram, 80% levaram ICE (#conversao)
fig, ax = plt.subplots(figsize=(11, 2.4))
ax.barh(0, 20, height=0.5, color=GRAY, edgecolor=BG, linewidth=2)
ax.barh(0, 80, left=20, height=0.5, color=ORANGE, edgecolor=BG, linewidth=2)
ax.text(10, 0, "20%\ndemais", ha="center", va="center", fontsize=14, fontweight="bold", color=INK)
ax.text(60, 0, "80% assinou carro a COMBUSTÃO", ha="center", va="center", fontsize=16, fontweight="bold", color="white")
ax.set_xlim(0, 100); ax.set_ylim(-0.45, 0.6); ax.axis("off")
ax.set_title("Leads de elétrico que viraram assinantes: o que eles assinaram", loc="left", fontsize=16,
             fontweight="bold", color=INK)
fonte(fig, "Fonte: dados-case1.md #conversao (\"80% dos leads de elétricos que assinaram optaram por ICE\"; conversão 3x menor que leads ICE)")
fig.tight_layout(rect=(0, 0.06, 1, 1)); fig.savefig(OUT + "04_vazamento_ice.png", dpi=200); plt.close(fig)
print("ok")
