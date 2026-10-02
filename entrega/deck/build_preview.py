# Monta preview.html local com todos os slides (para checar layout no navegador). Uso: python build_preview.py [ordem...]
import json, os, sys
R = os.path.dirname(os.path.abspath(__file__))
order = sys.argv[1:]
if not order:
    try:
        order = json.load(open(os.path.join(R, "project", "deck.json"), encoding="utf-8"))["order"]
    except Exception:
        order = [f[:-5] for f in sorted(os.listdir(os.path.join(R, "project", "slides")))]
parts = []
for sid in order:
    p = os.path.join(R, "project", "slides", sid + ".html")
    if os.path.exists(p):
        parts.append(f'<div class="lbl">{sid}</div><div class="wrap">' + open(p, encoding="utf-8").read() + "</div>")
html = """<!doctype html><html><head><meta charset="utf-8"><title>preview</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400..700&family=IBM+Plex+Sans:ital,wght@0,400;0,600;1,400&display=swap">
<style>
*{margin:0;box-sizing:border-box}
body{background:#777;padding:20px;font-family:Arial}
.lbl{color:#fff;font:16px Arial;margin:8px 0}
.wrap{width:960px;height:540px;overflow:hidden;margin-bottom:24px}
section{width:1920px;height:1080px;position:relative;overflow:hidden;transform:scale(.5);transform-origin:0 0}
aside{display:none}
ul,ol{padding-left:1.2em}
table{border-collapse:collapse}
td,th{border-bottom:1px solid rgba(0,0,0,.15);padding:.35em .6em;text-align:left}
</style></head><body>""" + "\n".join(parts) + "</body></html>"
open(os.path.join(R, "preview.html"), "w", encoding="utf-8").write(html)
print("preview with", len(parts), "slides")
