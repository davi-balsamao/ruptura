# Entrega parcial — Case 1 Localiza (RUPTURA 2026)

> Status em 02/out/2026. Execução pausada pelo usuário. Abaixo, só o que foi concluído.
> Legenda: ✅ validado pelo crítico. Os 3 galhos priorizados estão validados. Notas do crítico para a síntese: `analises/G*-critica.md`.

## 1. Core Question (adotada)
> Como a Localiza deve redesenhar a oferta e a jornada da Assinatura de elétricos para remover
> as barreiras que hoje não atende, de modo que o lead que já quer um VE assine um VE, e não
> migre para combustão?

Base: o lead de VE converte 3x menos, e 80% dos que assinam levam ICE (#conversao). A Localiza
atende só 1 das 5 maiores preocupações; as abertas são recarga (#2, #3, #5) e preço (#4).

## 2. Árvore MECE e Pareto ✅ (estrutura)
Arquivo completo: `.claude/case/arvore.md`
- **G1 Custo** · **G2 Recarga em casa** · **G3 Recarga na rua**: priorizados. Juntos cobrem 100% das
  lacunas do top 5.
- G4 Processo de compra (viabilizador) · G5 Risco do ativo (já atendido; vira argumento).

**Brainstorm confrontado com os dados:**
- Wallbox **não** é a maior barreira: é a #3, atrás de recarga na rotina.
- "Alugar é prejuízo" é contradito: quem vazou para ICE já tinha aceitado assinar.
- "A conta fecha" não é premissa; é a pergunta central (ver G1).

## 3. Achados por galho

### G2 Wallbox ✅ VALIDADO (rodada 3) — `.claude/case/analises/G2-r3.md`
- Wallbox 7,4 kW em comodato + instalação até R$ 3.000, inclusos em contratos de 24–48 m, custam à
  Localiza **R$ 104–270/mês** por contrato (3,5–9,0% de uma mensalidade de referência de R$ 3.000).
- Em 12 m pesa 14–18%, então ali fica opcional com coparticipação. Não cobrar como linha extra
  (preço já é barreira #4).
- Condomínio: estudo de carga antes de assinar + ART + aviso ao síndico. A Lei SP 18.403/2026 só
  admite veto com justificativa técnica.
- Fim do contrato (24–48 m): a fiação fica; quem renova segue com o wallbox em comodato e quem deixa a
  assinatura fica com ele, sem retirada (`G2-r6.md`). Em 12 m: retirada ou compra pelo valor residual.
- **Não comprovável:** se o custo cabe na margem; se o lead consegue instalar; proteção a
  inquilino; recarga no trabalho.

### G1 Custo ✅ VALIDADO (rodada 2) — `.claude/case/analises/G1-r2.md`
Preços de mercado, indicativos: a Localiza só mostra preço após CPF e consulta de crédito.
- O VE custa **R$ 463–604/mês a mais** que o ICE de entrada a 1.000 km, e R$ 637–707 a 500 km.
- A energia compensa só 21–43% da diferença de mensalidade. Empata só acima de **~2.330 km/mês**
  (recarga em casa).
- Assinar sai mais barato que financiar em SP; empata no RJ; sai mais caro que comprar à vista.
- Alavancas (desconto de frota, valor residual) existem, mas **fechar o gap é Não-comprovável**.
- Observação direta no site: o preço não é visível sem CPF, o que piora a comparação de custo, uma
  dor citada pela banca.

### G3 Recarga pública ✅ VALIDADO (rodada 2) — `.claude/case/analises/G3-r2.md`
- Malha pública: 29.866 pontos (ago/26), 38% de recarga rápida, mas **21,4 VEs por ponto**, ~1,9x
  a média global (critério ≤ ~11). Estado de SP: insuficiente. Corredores: não comprovável.
- Solução: mapa e rota no app, mais um simulador "minha rotina" na pré-venda, integrando dados
  existentes (Tupi/OCPI, Google), e desconto em rede parceira. Isso ataca o motivo do "não atende"
  de #2 e #5.
- O efeito na conversão é Não-comprovável (exige teste A/B). Desconto de até 20% tem um único
  precedente (99).

## 4. Arquivos prontos
| O quê | Onde |
|---|---|
| Gráficos (8 PNG) | `entrega/graficos/` (01–04 dossiê; 05–06 G1 r2; 07–08 G3) |
| Scripts dos gráficos | `entrega/scripts/` |
| **Deck completo (12 slides)**: capa, resposta, situação, complicação, diagnóstico, árvore, G1, G2, G3, proposta, jornada, piloto (com notas do apresentador em `<aside>`) | `entrega/deck/preview.html` (abrir no navegador); fontes em `entrega/deck/slides/` |
| **Síntese SCR + roteiro do pitch** | `.claude/case/sintese.md` |
| Dossiê ampliado com dados do PDF da banca | `.claude/case/dados-case1.md` |
| Análises, verificações e pareceres do crítico | `.claude/case/analises/` |
| Histórico do processo | `.claude/case/estado.md` |

## 5. Pendências
- Publicar o deck como apresentação editável/exportável para PPTX (não feito para poupar tokens).
- **Pendência humana:** cotação oficial na Localiza (Dolphin Mini × Onix/HB20/Polo, 36 m, todas as
  franquias) exige CPF; é o dado que confirma ou ajusta o G1.
- Perguntar à banca: perfil do assinante de VE e volume de leads de VE (dimensionam o impacto).
- Preencher "Equipe [nome]" na capa.
