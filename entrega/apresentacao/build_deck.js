// Pitch de 3 minutos do Case 1 Localiza (Ruptura 2026). Uso: npm run build  →  Pitch_3min_Eletrico_sem_atrito.pptx
// Números: só conclusões validadas pelo crítico (G1-r2, G2-r3 + regra de fim de contrato G2-r6, G3-r2).
const path = require("path");
const pptxgen = require("pptxgenjs");
const { applyTheme } = require("./apply_theme.js");

const OUT = path.join(__dirname, "Pitch_3min_Eletrico_sem_atrito.pptx");
const THEME = {
  name: "Eletrico sem atrito",
  headFontFace: "Arial",
  bodyFontFace: "Arial",
  colors: {
    dk1: "2E2E2E", lt1: "FFFFFF", dk2: "004521", lt2: "F2F2F2",
    accent1: "018444", accent2: "78DE1F", accent3: "6B6B6B",
    accent4: "B86E14", accent5: "C8463D", accent6: "E3F6D2",
    hlink: "018444", folHlink: "004521",
  },
};
const HEX = THEME.colors;

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13,333 × 7,5 pol
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "Elétrico sem atrito";
pres.subject = "Case 1 Localiza · Ruptura 2026";
const C = pres.SchemeColor;
const S = pres.ShapeType;

// Cores fora do tema (só onde a opção aceita apenas hex)
const BARRA_CLARA = "8CCB9B";
const sombra = () => ({ type: "outer", color: "000000", opacity: 0.12, blur: 8, offset: 2, angle: 90 });

// ---------- Layouts ----------
const M = 0.6; // margem lateral
pres.defineSlideMaster({
  title: "CAPA",
  background: { color: C.text2 },
  objects: [
    { placeholder: { options: { name: "title", type: "title", x: M + 0.1, y: 2.05, w: 8.4, h: 1.5, fontSize: 54, bold: true, color: C.background1, valign: "bottom", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "subtitulo", type: "body", x: M + 0.1, y: 3.7, w: 7.6, h: 1.2, fontSize: 22, color: C.background1, valign: "top", margin: 0 }, text: "" } },
    { placeholder: { options: { name: "rodape", type: "body", x: M + 0.1, y: 6.45, w: 8, h: 0.4, fontSize: 14, color: C.accent2, valign: "middle", margin: 0 }, text: "" } },
  ],
});
const conteudo = (titulo, escuro) =>
  pres.defineSlideMaster({
    title: titulo,
    background: { color: escuro ? C.text2 : C.background1 },
    margin: [0.5, M, 0.6, M],
    objects: [
      { placeholder: { options: { name: "kicker", type: "body", x: M, y: 0.42, w: 12.1, h: 0.34, fontSize: 13, bold: true, charSpacing: 1.5, color: escuro ? C.accent2 : C.accent1, valign: "middle", margin: 0 }, text: "" } },
      { placeholder: { options: { name: "title", type: "title", x: M, y: 0.8, w: 12.1, h: 1.15, fontSize: 30, bold: true, color: escuro ? C.background1 : C.text1, valign: "top", margin: 0 }, text: "" } },
      { placeholder: { options: { name: "fonte", type: "body", x: M, y: 6.98, w: 11.3, h: 0.32, fontSize: 10, color: escuro ? C.background2 : C.accent3, valign: "middle", margin: 0 }, text: "" } },
    ],
    slideNumber: { x: 12.33, y: 6.98, w: 0.4, h: 0.32, fontSize: 10, color: escuro ? C.background2 : C.accent3, align: "right" },
  });
conteudo("CONTEUDO", false);
conteudo("CONTEUDO_ESCURO", true);

// ---------- Peças de composição ----------
function cartao(slide, nome, x, y, w, h, fill = C.background1, comSombra = true) {
  slide.addShape(S.roundRect, { objectName: nome, x, y, w, h, rectRadius: 0.16, fill: { color: fill }, line: { type: "none" }, shadow: comSombra ? sombra() : undefined });
}
function selo(slide, nome, n, x, y, d = 0.42, fill = C.accent2, cor = C.text2) {
  slide.addShape(S.ellipse, { objectName: nome + "-circulo", x, y, w: d, h: d, fill: { color: fill }, line: { type: "none" } });
  slide.addText(String(n), { objectName: nome + "-numero", x, y, w: d, h: d, align: "center", valign: "middle", fontSize: d > 0.4 ? 16 : 13, bold: true, color: cor, margin: 0, isTextBox: true });
}
function pilula(slide, nome, texto, x, y, w, fill, cor = C.background1, h = 0.34) {
  slide.addShape(S.roundRect, { objectName: nome + "-fundo", x, y, w, h, rectRadius: h / 2, fill: { color: fill }, line: { type: "none" } });
  slide.addText(texto, { objectName: nome + "-texto", x, y, w, h, align: "center", valign: "middle", fontSize: 11, bold: true, color: cor, margin: 0, isTextBox: true });
}
function texto(slide, nome, t, x, y, w, h, o = {}) {
  slide.addText(t, { objectName: nome, x, y, w, h, margin: 0, valign: "top", fontSize: 15, color: C.text1, isTextBox: true, ...o });
}
function novo(master, secao, kicker, titulo, fonte) {
  const s = pres.addSlide({ masterName: master, sectionTitle: secao });
  if (kicker) s.addText(kicker.toUpperCase(), { placeholder: "kicker" });
  s.addText(titulo, { placeholder: "title" });
  if (fonte) s.addText(fonte, { placeholder: "fonte" });
  return s;
}

// ---------- 1. Capa ----------
pres.addSection({ title: "Pitch (3 min)" });
{
  const s = pres.addSlide({ masterName: "CAPA", sectionTitle: "Pitch (3 min)" });
  s.addText("Elétrico sem atrito", { placeholder: "title" });
  s.addText("Como a Localiza Assinatura transforma o lead que quer um elétrico em assinante de elétrico", { placeholder: "subtitulo" });
  s.addText("Equipe [nome] · Ruptura 2026 · Case 1 Localiza", { placeholder: "rodape" });
  // Arco lima com o raio (mesmo motivo do Simulador Elétrico)
  s.addShape(S.roundRect, { objectName: "arco-externo", x: 9.35, y: 1.25, w: 3.4, h: 7.2, rectRadius: 1.7, fill: { color: C.accent2 }, line: { type: "none" } });
  s.addShape(S.roundRect, { objectName: "arco-interno", x: 9.8, y: 1.7, w: 2.5, h: 6.3, rectRadius: 1.25, fill: { color: C.text2 }, line: { type: "none" } });
  s.addShape(S.lightningBolt, { objectName: "raio", x: 10.45, y: 2.75, w: 1.2, h: 1.55, fill: { color: C.accent2 }, line: { type: "none" } });
  s.addNotes(
    "[0:00–0:10] Somos a equipe [nome]. Em três minutos: por que o lead que quer um elétrico acaba assinando um carro a combustão, e como a Localiza muda isso com um pacote que a gente já começou a construir."
  );
}

// ---------- 2. O problema ----------
{
  const s = novo("CONTEUDO", "Pitch (3 min)", "O problema",
    "O lead quer o elétrico, mas 8 em cada 10 que assinam acabam levando um carro a combustão",
    "Fonte: material Localiza do case Ruptura 2026 (pesquisa jul/2026, ~1.000 leads e clientes)");
  const stats = [
    ["1% → 29%", "dos leads da Assinatura passaram a ser de elétrico, em menos de 1 ano", false],
    ["3x menos", "conversão do lead de elétrico, comparado ao lead de combustão", false],
    ["80%", "dos leads de elétrico que assinaram levaram um carro a combustão", true],
  ];
  const w = 3.85, gap = 0.28, y = 2.35, h = 2.75;
  stats.forEach(([n, t, destaque], i) => {
    const x = M + i * (w + gap);
    cartao(s, `stat-${i + 1}`, x, y, w, h, destaque ? C.text2 : C.background1);
    texto(s, `stat-${i + 1}-numero`, n, x + 0.35, y + 0.4, w - 0.7, 1.1, { fontSize: 50, bold: true, color: destaque ? C.accent2 : C.accent1, valign: "middle" });
    texto(s, `stat-${i + 1}-texto`, t, x + 0.35, y + 1.6, w - 0.7, 0.95, { fontSize: 16, color: destaque ? C.background1 : C.text1 });
  });
  cartao(s, "faixa-59", M, 5.5, 12.1, 1.05, C.background2, false);
  texto(s, "frase-59", [
    { text: "59% ", options: { bold: true, color: C.accent1 } },
    { text: "dizem que o elétrico aumenta a vontade de assinar em vez de comprar. A Assinatura é o caminho natural para o elétrico, mas a venda não fecha." },
  ], M + 0.35, 5.5, 11.4, 1.05, { fontSize: 17, valign: "middle" });
  s.addNotes(
    "[0:10–0:35] O interesse explodiu: os leads de elétrico foram de 1% para 29% em menos de um ano, e 59% dizem que o elétrico aumenta a vontade de assinar. Mas esse lead converte três vezes menos, e oito em cada dez que assinam levam um carro a combustão. Ele confia na Assinatura; não confia no elétrico dentro dela."
  );
}

// ---------- 3. Diagnóstico ----------
{
  const s = novo("CONTEUDO", "Pitch (3 min)", "Por que a venda não fecha",
    "A Localiza resolve só 1 das 5 maiores preocupações do lead: o que trava é recarga e preço",
    "Fontes: pesquisa Localiza jul/2026 (material do case); abve.org.br (ago/26) e IEA; loja.intelbras.com.br e em.com.br; assinatura.localiza.com (02/out/2026)");
  const linhas = [
    ["Bateria e vida útil", "ATENDE", C.accent1],
    ["Recarga na rotina (casa, trabalho, rua)", "NÃO ATENDE", C.accent5],
    ["Wallbox em casa ou no trabalho", "PARCIAL", C.accent4],
    ["Mensalidade mais alta que a do combustão", "NÃO ATENDE", C.accent5],
    ["Recarga em viagens", "NÃO ATENDE", C.accent5],
  ];
  const x0 = M, y0 = 2.2, lw = 6.9, lh = 0.8;
  cartao(s, "top5-cartao", x0, y0 - 0.15, lw, lh * 5 + 0.3);
  linhas.forEach(([nome, status, cor], i) => {
    const y = y0 + i * lh;
    selo(s, `top5-${i + 1}`, i + 1, x0 + 0.3, y + 0.17, 0.42);
    texto(s, `top5-${i + 1}-nome`, nome, x0 + 0.95, y, 3.9, lh, { fontSize: 16, valign: "middle" });
    pilula(s, `top5-${i + 1}-status`, status, x0 + lw - 1.85, y + 0.22, 1.55, cor);
    if (i < 4) s.addShape(S.line, { objectName: `top5-divisor-${i + 1}`, x: x0 + 0.3, y: y + lh, w: lw - 0.6, h: 0, line: { color: HEX.lt2, width: 1 } });
  });
  // Evidência ao lado
  const ex = 7.85, ew = 4.85;
  texto(s, "evidencia-titulo", "E as barreiras são concretas", ex, 2.05, ew, 0.4, { fontSize: 17, bold: true });
  const ev = [
    ["21,4", "carros elétricos por ponto de recarga público no Brasil, quase o dobro da média global"],
    ["R$ 5–6,5 mil", "para comprar e instalar um wallbox em casa, à vista"],
    ["Só com CPF", "o preço aparece; e a calculadora do site não tem a categoria Elétrico"],
  ];
  ev.forEach(([n, t], i) => {
    const y = 2.6 + i * 1.3;
    cartao(s, `evidencia-${i + 1}`, ex, y, ew, 1.12, C.background2, false);
    texto(s, `evidencia-${i + 1}-numero`, n, ex + 0.25, y + 0.12, ew - 0.5, 0.42, { fontSize: 20, bold: true, color: C.accent1 });
    texto(s, `evidencia-${i + 1}-texto`, t, ex + 0.25, y + 0.55, ew - 0.5, 0.5, { fontSize: 13 });
  });
  s.addNotes(
    "[0:35–1:00] Por quê? Das cinco maiores preocupações, a Localiza resolve só a da bateria. As outras são recarga e preço, e são reais: a rede pública tem 21 carros por ponto, quase o dobro da média global; o wallbox custa de 5 a 6,5 mil reais para quem instala; e o preço só aparece com CPF. A calculadora do site nem tem a categoria elétrico."
  );
}

// ---------- 4. Proposta ----------
{
  const s = novo("CONTEUDO", "Pitch (3 min)", "A proposta",
    "Três frentes levam a Localiza de 1 para 4 das 5 maiores preocupações, e o preço em parte",
    "Placar a partir da pesquisa Localiza jul/2026 (material do case). Preço: o simulador mostra a conta, mas não fecha a diferença para quem roda pouco");
  const frentes = [
    ["Conta à vista", "Simulador Elétrico sem CPF: mensalidade + energia, contra o combustão equivalente", "Preço (#4), em parte", "MVP pronto"],
    ["Recarga em casa inclusa", "Wallbox 7,4 kW e instalação até R$ 3.000 inclusos nos planos de 24 a 48 meses", "Wallbox (#3) e rotina em casa (#2)", "Operação com instaladores"],
    ["Recarga na rua planejada", "Mapa e rota de eletropostos no app, usando a telemetria de bateria que o app já tem", "Viagem (#5) e rotina na rua (#2)", "Próxima fase"],
  ];
  const w = 3.85, gap = 0.28, y = 2.25, h = 3.6;
  frentes.forEach(([t, d, b, fase], i) => {
    const x = M + i * (w + gap);
    cartao(s, `frente-${i + 1}`, x, y, w, h);
    selo(s, `frente-${i + 1}`, i + 1, x + 0.35, y + 0.35, 0.5);
    texto(s, `frente-${i + 1}-titulo`, t, x + 0.35, y + 1.0, w - 0.7, 0.5, { fontSize: 20, bold: true });
    texto(s, `frente-${i + 1}-texto`, d, x + 0.35, y + 1.55, w - 0.7, 1.1, { fontSize: 15, color: C.text1 });
    texto(s, `frente-${i + 1}-barreira`, [{ text: "Responde: ", options: { bold: true } }, { text: b }], x + 0.35, y + 2.7, w - 0.7, 0.35, { fontSize: 13, color: C.accent3 });
    pilula(s, `frente-${i + 1}-fase`, fase, x + 0.35, y + 3.1, 2.3, i === 2 ? C.background2 : C.accent6, C.text2, 0.32);
  });
  texto(s, "argumento", [
    { text: "E o que já é forte vira argumento de venda: ", options: { bold: true } },
    { text: "bateria, revenda, pane e manutenção são risco da Localiza, não do cliente." },
  ], M, 6.1, 12.1, 0.5, { fontSize: 16, valign: "middle" });
  s.addNotes(
    "[1:00–1:20] Nossa resposta é vender o elétrico como um pacote sem atrito, em três frentes: a conta à vista, sem CPF; a recarga em casa inclusa; e a recarga na rua planejada no app. Isso leva a Localiza de uma para quatro das cinco preocupações, e o preço em parte. E o que ela já faz bem, bateria e revenda, vira argumento."
  );
}

// ---------- 5. Wallbox ----------
{
  const s = novo("CONTEUDO", "Pitch (3 min)", "Recarga em casa · a nova regra do wallbox",
    "Wallbox incluso custa à Localiza R$ 104 a 270 por mês, e quem sai da assinatura fica com ele",
    "Fontes: loja.intelbras.com.br (R$ 3.475,80), em.com.br (instalação). Amortização linear sem custo de capital, sem reuso. Análise G2 validada pelo crítico");
  cartao(s, "grafico-cartao", M, 2.1, 6.4, 4.6);
  s.addChart(pres.ChartType.bar, [
    { name: "Instalação simples (R$ 4.976 por contrato)", labels: ["24 meses", "36 meses", "48 meses"], values: [207, 138, 104] },
    { name: "Instalação no teto (R$ 6.476 por contrato)", labels: ["24 meses", "36 meses", "48 meses"], values: [270, 180, 135] },
  ], {
    objectName: "grafico-wallbox", x: M + 0.2, y: 2.25, w: 6.0, h: 4.3,
    barDir: "col", barGrouping: "clustered", barGapWidthPct: 60, chartColors: [HEX.accent1, BARRA_CLARA],
    showTitle: true, title: "Custo para a Localiza, R$ por mês por contrato", titleFontSize: 14, titleColor: HEX.dk1, titleFontFace: "+mn-lt",
    showValue: true, dataLabelPosition: "outEnd", dataLabelFormatCode: '"R$ "0', dataLabelFontSize: 12, dataLabelColor: HEX.dk1, dataLabelFontFace: "+mn-lt",
    showLegend: true, legendPos: "b", legendFontSize: 11, legendColor: HEX.accent3, legendFontFace: "+mn-lt",
    catAxisLabelFontSize: 13, catAxisLabelColor: HEX.dk1, catAxisLabelFontFace: "+mn-lt", catAxisLineShow: false,
    valAxisHidden: true, valAxisMinVal: 0, valAxisMaxVal: 300, valGridLine: { style: "none" }, catGridLine: { style: "none" },
  });
  // Como funciona
  const rx = 7.3, rw = 5.4;
  texto(s, "regra-titulo", "Como funciona", rx, 2.1, rw, 0.4, { fontSize: 18, bold: true });
  const passos = [
    "Diagnóstico elétrico antes de assinar, com os instaladores do teste da Meoo",
    "Durante o contrato, o wallbox é da Localiza; quem renova segue com ele em comodato",
    "Quem deixa a assinatura fica com o wallbox: sem retirada e sem visita técnica",
  ];
  passos.forEach((p, i) => {
    const y = 2.62 + i * 0.72;
    selo(s, `regra-${i + 1}`, i + 1, rx, y + 0.04, 0.36, C.accent1, C.background1);
    texto(s, `regra-${i + 1}-texto`, p, rx + 0.55, y, rw - 0.55, 0.62, { fontSize: 14.5, valign: "middle" });
  });
  cartao(s, "regra-custo", rx, 4.85, rw, 1.85, C.text2, false);
  texto(s, "regra-custo-texto", [
    { text: "No caso-base, isso não acrescenta custo ", options: { bold: true, color: C.accent2 } },
    { text: "à conta de amortização e dispensa a retirada. Em troca, a Localiza abre mão do reuso (R$ 36 a 72/mês por contrato de quem sai) e de um motivo de renovar.", options: { color: C.background1, breakLine: true } },
    { text: "Plano de 12 meses: wallbox opcional, com coparticipação.", options: { color: C.background2, fontSize: 12.5 } },
  ], rx + 0.3, 4.95, rw - 0.6, 1.65, { fontSize: 14, valign: "middle", paraSpaceAfter: 6 });
  s.addNotes(
    "[1:20–1:45] A recarga em casa: o wallbox e a instalação, até 3 mil reais, entram nos planos de 24 a 48 meses. Para a Localiza custa de 104 a 270 reais por mês por contrato. Quem renova segue com o wallbox; quem sai da assinatura fica com ele. No caso-base isso não acrescenta custo à conta e dispensa a retirada; em troca, a Localiza abre mão de reaproveitar o equipamento. O custo de retirar a gente cota com os instaladores no primeiro mês."
  );
}

// ---------- 6. MVP ----------
{
  const s = novo("CONTEUDO", "Pitch (3 min)", "O MVP · Simulador Elétrico",
    "O MVP já funciona: o lead compara o elétrico com o combustão sem dar CPF",
    "Simulador em Python (Streamlit), em entrega/mvp_simulador. Preços indicativos de mercado (byd.com/br, livre.com.br, rentcars.com); energia: cemig.com.br; gasolina: petrobras.com.br");
  const ih = 4.85, iw = ih * (1240 / 1150);
  cartao(s, "print-moldura", M, 2.0, iw + 0.2, ih + 0.2);
  s.addImage({ objectName: "print-simulador", path: path.join(__dirname, "mvp_custo.png"), x: M + 0.1, y: 2.1, w: iw, h: ih });
  const cx = M + iw + 0.65, cw = 13.333 - M - cx;
  const callouts = [
    ["−R$ 446/mês", "contra um combustão automático, a 1.000 km/mês com recarga em casa (indicativo de mercado)"],
    ["+R$ 463/mês", "contra um combustão de entrada; empata a partir de ~2.330 km/mês"],
    ["3 abas", "custo total, minha rotina (recarga em casa e paradas na viagem) e resumo para o consultor no WhatsApp"],
  ];
  callouts.forEach(([n, t], i) => {
    const y = 2.05 + i * 1.33;
    texto(s, `mvp-${i + 1}-numero`, n, cx, y, cw, 0.5, { fontSize: 24, bold: true, color: C.accent1 });
    texto(s, `mvp-${i + 1}-texto`, t, cx, y + 0.52, cw, 0.72, { fontSize: 14 });
  });
  cartao(s, "mvp-proxima", cx, 6.05, cw, 0.75, C.accent6, false);
  texto(s, "mvp-proxima-texto", [
    { text: "Próxima fase: ", options: { bold: true, color: C.text2 } },
    { text: "mapa e rota de eletropostos no app. A tabela oficial de preços entra sem mudar o código." },
  ], cx + 0.2, 6.05, cw - 0.4, 0.75, { fontSize: 12.5, valign: "middle" });
  s.addNotes(
    "[1:45–2:15] E o MVP já funciona. É o Simulador Elétrico: o lead diz onde mora, o prazo e quanto roda, e vê a conta na hora, sem CPF. A mil quilômetros por mês, o elétrico sai 446 reais mais barato que um combustão automático; contra o de entrada, custa 463 a mais e empata perto de 2.300 quilômetros. Na aba Minha rotina ele vê a recarga em casa e as paradas numa viagem. O mapa de eletropostos é a próxima fase."
  );
}

// ---------- 7. Piloto e pedido ----------
{
  const s = novo("CONTEUDO_ESCURO", "Pitch (3 min)", "Como provar",
    "Um piloto A/B de 90 dias em São Paulo decide no mês 5 se o pacote escala",
    "Duração e critérios: proposta da equipe, a calibrar com a Localiza. SP: maior malha de recarga do país (abve.org.br) e Lei 18.403/2026 para condomínios");
  const fases = [
    ["Mês 1", "Construir", "Simulador no site e no WhatsApp; kit wallbox com os instaladores; cotação do custo de retirada"],
    ["Meses 2 a 4", "Testar", "Leads de elétrico de SP sorteados em dois grupos: com o pacote e com o processo atual"],
    ["Mês 5", "Decidir", "Escalar se o grupo do pacote converter mais em elétrico, dentro do custo por contrato"],
  ];
  const w = 3.85, gap = 0.28, y = 2.2, h = 2.25;
  fases.forEach(([quando, oque, d], i) => {
    const x = M + i * (w + gap);
    cartao(s, `fase-${i + 1}`, x, y, w, h, "1C5C3A", false);
    texto(s, `fase-${i + 1}-quando`, quando.toUpperCase(), x + 0.3, y + 0.25, w - 0.6, 0.3, { fontSize: 12, bold: true, color: C.accent2, charSpacing: 1 });
    texto(s, `fase-${i + 1}-oque`, oque, x + 0.3, y + 0.58, w - 0.6, 0.45, { fontSize: 22, bold: true, color: C.background1 });
    texto(s, `fase-${i + 1}-texto`, d, x + 0.3, y + 1.1, w - 0.6, 1.05, { fontSize: 14, color: C.background2 });
  });
  cartao(s, "metrica", M, 4.7, 12.1, 0.95, C.accent2, false);
  texto(s, "metrica-texto", [
    { text: "A métrica que decide: ", options: { bold: true } },
    { text: "% dos leads de elétrico que assinam elétrico. Hoje, 80% dos que assinam levam um combustão." },
  ], M + 0.35, 4.7, 11.4, 0.95, { fontSize: 17, color: C.text2, valign: "middle" });
  texto(s, "pedido", [
    { text: "O que pedimos hoje: ", options: { bold: true, color: C.accent2 } },
    { text: "aprovar o piloto, liberar a cotação oficial do elétrico × combustão e os dados de funil dos leads de elétrico.", options: { color: C.background1 } },
  ], M, 5.9, 12.1, 0.8, { fontSize: 18, valign: "middle" });
  s.addNotes(
    "[2:15–2:45] Como provar: um piloto A/B de 90 dias em São Paulo, onde está a maior malha de recarga do país. No mês 1, o simulador entra no ar e o kit wallbox sai com os instaladores; nos meses 2 a 4, metade dos leads de elétrico recebe o pacote; no mês 5, a Localiza decide com uma métrica só: quantos leads de elétrico assinam elétrico. Pedimos a aprovação do piloto, a cotação oficial e os dados de funil. Obrigado."
  );
}

// ---------- Anexo: fontes ----------
pres.addSection({ title: "Anexo" });
{
  const s = novo("CONTEUDO", "Anexo", "Anexo", "Fontes dos números desta apresentação",
    "Lista completa de URLs em entrega/CONCLUSOES.md. Análises e pareceres do crítico em .claude/case/analises/");
  const linhas = [
    ["Pesquisa e números da Localiza", "Material oficial do case Ruptura 2026 (pesquisa jul/2026, ~1.000 leads e clientes); assinatura.localiza.com (observado em 02/out/2026)"],
    ["Preço e custo (G1)", "byd.com/br/byd-por-assinatura; livre.com.br; subscription.rentcars.com; precos.petrobras.com.br; cemig.com.br; vrum.com.br. Indicativos de mercado"],
    ["Wallbox (G2)", "loja.intelbras.com.br; em.com.br; assinatura.localiza.com/blog/post/wallbox; al.sp.gov.br (Lei 18.403/2026)"],
    ["Recarga pública (G3)", "abve.org.br; evinfrastructurenews.com (IEA); energy.gov; developers.google.com/maps"],
    ["Regra de fim de contrato", "Análise G2-r6 (delta sobre a G2-r3): custo gerencial do caso-base inalterado; custo fiscal e jurídico da transferência é lacuna"],
  ];
  const rows = [[
    { text: "Tema", options: { bold: true, color: C.background1, fill: { color: C.text2 } } },
    { text: "Fontes", options: { bold: true, color: C.background1, fill: { color: C.text2 } } },
  ]].concat(linhas.map(([a, b]) => [{ text: a, options: { bold: true } }, { text: b }]));
  s.addTable(rows, {
    objectName: "tabela-fontes", x: M, y: 2.1, w: 12.1, colW: [3.0, 9.1], fontSize: 13, color: C.text1,
    border: { type: "solid", pt: 0.75, color: HEX.lt2 }, margin: [6, 8, 6, 8], valign: "middle",
  });
}

(async () => {
  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("ok:", OUT);
})();
