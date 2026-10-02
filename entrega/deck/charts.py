# Geradores de gráficos nativos para o formato de slide (SVG sem <text> + rótulos <p> fixados).
# Cada função devolve um bloco HTML: <div style="position:relative;width;height"> ... </div>

FONT = "'IBM Plex Sans', Arial, sans-serif"
INK = "#13212E"; INK2 = "#3F4A54"; MUTED = "#5E6873"; GRID = "#DDDAD0"
BLUE = "#2A78D6"; ORANGE = "#D95926"; GRAY = "#B9B6AC"


def _p(left, top, w, text, size=24, color=INK2, weight=400, align="left", h=None):
    hs = f"height:{h}px;" if h else ""
    return (f'<p style="position:absolute;left:{left:.0f}px;top:{top:.0f}px;width:{w:.0f}px;{hs}'
            f'font-size:{size}px;font-weight:{weight};color:{color};text-align:{align};line-height:1.2;white-space:nowrap">{text}</p>')


def line_chart(W, H, xs, xlabels, series, ymin, ymax, yticks, yfmt, pad=(150, 20, 60, 30), extra_labels=(), vline=None):
    """series: list of dict(values, color, width, dash, end_label)."""
    L, T, B, R = pad[0], pad[1], pad[2], pad[3]
    pw, ph = W - L - R, H - T - B
    x0, x1 = xs[0], xs[-1]
    fx = lambda x: L + (x - x0) / (x1 - x0) * pw
    fy = lambda y: T + (1 - (y - ymin) / (ymax - ymin)) * ph
    svg = [f'<svg aria-label="gráfico de linhas" width="{W}" height="{H}" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg">']
    for t in yticks:
        svg.append(f'<line x1="{L}" y1="{fy(t):.1f}" x2="{W-R}" y2="{fy(t):.1f}" stroke="{GRID}" stroke-width="1"/>')
    if vline is not None:
        svg.append(f'<line x1="{fx(vline):.1f}" y1="{T}" x2="{fx(vline):.1f}" y2="{T+ph}" stroke="{INK2}" stroke-width="2" stroke-dasharray="6 6"/>')
    for s in series:
        pts = " ".join(f"{fx(x):.1f},{fy(y):.1f}" for x, y in zip(xs, s["values"]))
        dash = f' stroke-dasharray="{s["dash"]}"' if s.get("dash") else ""
        svg.append(f'<polyline points="{pts}" fill="none" stroke="{s["color"]}" stroke-width="{s.get("width",4)}" stroke-linejoin="round" stroke-linecap="round"{dash}/>')
        if s.get("dots", True):
            for x, y in zip(xs, s["values"]):
                svg.append(f'<circle cx="{fx(x):.1f}" cy="{fy(y):.1f}" r="8" fill="{s["color"]}" stroke="#F6F4EE" stroke-width="3"/>')
    svg.append("</svg>")
    out = [f'<div style="position:relative;width:{W}px;height:{H}px">', "".join(svg)]
    for t in yticks:
        out.append(_p(0, fy(t) - 15, L - 16, yfmt(t), 24, MUTED, 400, "right"))
    for x, lab in zip(xs, xlabels):
        out.append(_p(fx(x) - 90, T + ph + 14, 180, lab, 24, MUTED, 400, "center"))
    for (x, y, w, txt, size, color, weight, align) in extra_labels:
        out.append(_p(fx(x) if x is not None else 0, fy(y) if y is not None else 0, w, txt, size, color, weight, align))
    out.append("</div>")
    return "\n".join(out)


def hbars(rows, width_px, max_val, bar_h=44, gap=18, label_w=300, fmt=lambda v: f"{v}"):
    """rows: list of (label, value, color, emphasis_bool). Flex rows, no SVG."""
    out = [f'<div style="display:flex;flex-direction:column;gap:{gap}px;width:{width_px}px">']
    track = width_px - label_w - 120
    for lab, v, color, emph in rows:
        w = max(4, round(track * v / max_val))
        wt = 600 if emph else 400
        out.append(f'<div style="display:flex;align-items:center;gap:16px">'
                   f'<p style="width:{label_w}px;font-size:26px;font-weight:{wt};color:{INK if emph else INK2};text-align:right">{lab}</p>'
                   f'<div style="width:{w}px;height:{bar_h}px;background:{color};border-radius:0 6px 6px 0"></div>'
                   f'<p style="font-size:28px;font-weight:600;color:{INK}">{fmt(v)}</p></div>')
    out.append("</div>")
    return "\n".join(out)


def columns(cols, height_px, max_val, col_w=110, gap=40, fmt=lambda v: f"{v}", label_size=24):
    """cols: list of (label, [(value, color), ...] stacked bottom→top, top_label). Bars grow from baseline."""
    out = [f'<div style="display:flex;align-items:end;gap:{gap}px;height:{height_px + 80}px">']
    for lab, parts, top in cols:
        tot = sum(v for v, _ in parts)
        out.append(f'<div style="display:flex;flex-direction:column;align-items:center;gap:8px;width:{col_w + 40}px">')
        out.append(f'<p style="font-size:24px;font-weight:600;color:{INK};text-align:center">{top if top is not None else fmt(tot)}</p>')
        out.append(f'<div style="display:flex;flex-direction:column;width:{col_w}px;gap:2px">')
        for i, (v, c) in enumerate(reversed(parts)):
            hh = max(2, round(height_px * v / max_val))
            rad = "border-radius:6px 6px 0 0;" if i == 0 else ""
            out.append(f'<div style="height:{hh}px;background:{c};{rad}"></div>')
        out.append('</div>')
        out.append(f'<p style="font-size:{label_size}px;color:{MUTED};text-align:center">{lab}</p></div>')
    out.append("</div>")
    return "\n".join(out)
