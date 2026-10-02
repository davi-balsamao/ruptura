# Slide G2 (validado na r3). Dados: analises/G2-r3.md Tab. 2/3/4 e Implicação.
INK="#13212E"; INK2="#3F4A54"; MUTED="#5E6873"; BLUE="#2A78D6"; BLUE_L="#9EC5F4"; GRID="#D9D6CC"
prazos=["12 meses","24 meses","36 meses","48 meses"]
A=[414.65,207.33,138.22,103.66]; B=[539.65,269.83,179.88,134.91]
H=250; mx=560
def bar(v,c,lab):
    h=round(H*v/mx)
    return (f'<div style="display:flex;flex-direction:column;align-items:center;gap:6px;width:92px">'
            f'<p style="font-size:24px;font-weight:600;color:{INK};white-space:nowrap">{lab}</p>'
            f'<div style="width:64px;height:{h}px;background:{c};border-radius:6px 6px 0 0"></div></div>')
groups=[]
for i,p in enumerate(prazos):
    rec = i>0
    ca = BLUE if rec else "#B9B6AC"; cb = BLUE_L if rec else "#DDDAD0"
    groups.append(f'<div style="display:flex;flex-direction:column;align-items:center;gap:10px">'
                  f'<div style="display:flex;align-items:end;gap:4px;height:{H+40}px">{bar(A[i],ca,round(A[i]))}{bar(B[i],cb,round(B[i]))}</div>'
                  f'<p style="font-size:24px;color:{INK if rec else MUTED};font-weight:{600 if rec else 400}">{p}</p></div>')
chart=(f'<div style="display:flex;flex-direction:column;gap:20px;width:880px">'
       f'<p style="font-size:26px;color:{INK2}">Custo para a Localiza, R$/mês por contrato</p>'
       f'<div style="display:flex;gap:40px;align-items:end;border-bottom:2px solid {GRID};padding:0 0 0 8px">{"".join(groups[:])}</div>'
       f'<div style="display:flex;gap:28px;align-items:center">'
       f'<div style="width:24px;height:24px;background:{BLUE};border-radius:4px"></div><p style="font-size:24px;color:{INK2}">Instalação simples (R$ 4.976)</p>'
       f'<div style="width:24px;height:24px;background:{BLUE_L};border-radius:4px"></div><p style="font-size:24px;color:{INK2}">No teto (R$ 6.476)</p></div>'
       f'<p style="font-size:24px;color:{MUTED}">12 meses: opcional com coparticipação (14–18% da mensalidade)</p>'
       f'</div>')
right=(f'<div style="flex:1;display:flex;flex-direction:column;gap:20px">'
 f'<div style="background:#FFFFFF;border:1px solid {GRID};border-radius:16px;padding:28px 32px;display:flex;flex-direction:column;gap:10px">'
 f'<h3 style="font-family:\'Space Grotesk\', Arial, sans-serif;font-size:32px;font-weight:600;color:{INK}">Como funciona</h3>'
 f'<p style="font-size:26px;line-height:1.35;color:{INK2}"><b>1.</b> Diagnóstico elétrico por instalador parceiro: o teste da Meoo vira produto</p>'
 f'<p style="font-size:26px;line-height:1.35;color:{INK2}"><b>2.</b> Wallbox 7,4 kW em comodato + instalação até R$ 3.000, sem linha extra na fatura</p>'
 f'<p style="font-size:26px;line-height:1.35;color:{INK2}"><b>3.</b> Na saída, a fiação fica e o equipamento volta; se o cliente renova, fica tudo</p></div>'
 f'<div style="background:#13212E;border-radius:16px;padding:28px 32px;display:flex;flex-direction:column;gap:10px">'
 f'<h3 style="font-family:\'Space Grotesk\', Arial, sans-serif;font-size:32px;font-weight:600;color:#F6F4EE">Mora em condomínio?</h3>'
 f'<p style="font-size:26px;line-height:1.35;color:#BFCAD3">Kit Localiza: estudo de carga antes de assinar, ART e aviso ao síndico. Em SP, a Lei 18.403/2026 só permite veto com justificativa técnica</p></div>'
 f'</div>')
html=f'''<section id="g2" data-transition="fade" style="background:#F6F4EE;color:{INK};font-family:'IBM Plex Sans', Arial, sans-serif;padding:128px 128px 160px;display:flex;flex-direction:column;gap:40px">
<div style="display:flex;flex-direction:column;gap:16px">
<p style="font-size:24px;font-weight:600;letter-spacing:2px;text-transform:uppercase;color:#2A78D6">Barreira #3 · Recarga em casa</p>
<h2 style="font-family:'Space Grotesk', Arial, sans-serif;font-size:56px;font-weight:600;line-height:1.1;color:{INK}">Wallbox instalado e incluso custa à Localiza R$ 104 a R$ 270 por mês em contratos de 24 a 48 meses</h2>
</div>
<div style="display:flex;gap:64px">
{chart}
{right}
</div>
<p style="position:absolute;left:128px;bottom:64px;width:1664px;font-size:24px;color:{MUTED}">Fonte: análise G2 validada (Intelbras, Estado de Minas, blog Localiza, Lei SP 18.403/2026). Amortização sem custo de capital; teto = desenho</p>
<aside>Barreira número 3: instalar o carregador em casa. A proposta: a Localiza inclui o wallbox e a instalação, até um teto de 3 mil reais, nos contratos de 24 a 48 meses. Para a Localiza, isso custa entre 104 e 270 reais por mês por contrato, ou de 3,5% a 9% de uma mensalidade de referência de 3 mil reais. Não entra como linha extra na fatura, porque preço já é a barreira número 4. Em contratos de 12 meses o peso sobe para 14 a 18%, então ali fica opcional com coparticipação. Para quem mora em condomínio, o problema é processo: estudo de carga antes de assinar, ART e aviso ao síndico. Em São Paulo, a lei de 2026 só permite vetar com justificativa técnica. Ressalva honesta: se esse custo cabe na margem a gente não consegue provar sem a margem por contrato, que não é pública.</aside>
</section>'''
open("project/slides/g2.html","w",encoding="utf-8").write(html)
print("ok")
