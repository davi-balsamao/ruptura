# Conclusões das análises (validadas pelo crítico), com fontes reais

> Documento de referência do que as análises concluíram. Cada número tem a fonte original (site).
> As análises completas, com trechos literais, contas e lacunas, estão em `.claude/case/analises/`:
> `G1-r2.md`, `G2-r3.md` e `G3-r2.md`, com os pareceres `*-critica.md`.
> "Material do case" = apresentação oficial da Localiza no Ruptura 2026 (PDF na raiz do repo):
> pesquisa de jul/2026 com ~1.000 leads RAC não convertidos e clientes RAC.

---

## 0. O problema (material do case)
- Leads de elétrico foram de 1% para 29% em menos de 1 ano. 59% dizem que o elétrico aumenta a
  vontade de assinar em vez de comprar.
- Mas o lead de elétrico converte 3x menos, e 80% dos leads de elétrico que assinam levam um carro a
  combustão.
- No top 5 de preocupações, a Localiza atende só 1:
  - abertas: #2 recarga na rotina, #4 preço, #5 recarga em viagem;
  - parcial: #3 wallbox.

## 1. G1: Preço (validado, rodada 2)
**Conclusão:**
- Contra o combustão de entrada, o elétrico é mais caro no uso típico.
- Contra o combustão automático, sai mais barato.
- O lead hoje não vê nenhuma das duas contas: o preço só aparece com CPF.
- Os números são **indicativos de mercado**, não preço da Localiza.

| Achado | Número | Fonte |
|---|---|---|
| Mensalidade VE (Dolphin Mini) | R$ 2.870/mês | https://www.byd.com/br/byd-por-assinatura · https://subscription.rentcars.com/pt-br/fleet/byd/dolphin-mini |
| Mensalidade ICE de entrada (Onix 1.0, 36 m, 1.000 km) | R$ 2.058,99/mês | https://www.livre.com.br/carro-por-assinatura/Chevrolet_Onix_1.0_2025/ |
| Mensalidade ICE automático (Onix Plus Turbo AT) | ~R$ 2.909/mês | https://subscription.rentcars.com/pt-br/fleet/chevrolet/onix |
| Gasolina | R$ 6,55/L | https://precos.petrobras.com.br/precos-gasolina · https://www.gov.br/anp/pt-br/assuntos/precos-e-defesa-da-concorrencia/precos/levantamento-de-precos-de-combustiveis-ultimas-semanas-pesquisadas |
| Consumo Onix 1.0 | 13,7 km/L | https://revistacarro.com.br/onix-2026-segue-como-carro-mais-economico-do-brasil-veja-lista-do-inmetro/ |
| Consumo Onix Plus Turbo AT | 12,2 km/L | https://onlycars.com.br/2026/01/avaliacao-chevrolet-onix-plus-2026.html |
| Consumo do VE | ~0,108 kWh/km | https://canalve.com.br/dez-centavos-km-conheca-carros-mais-eficientes-brasil/ |
| Tarifa residencial | R$ 0,92 sem impostos; ~R$ 1,20 com impostos | https://www.cemig.com.br/valores-e-tarifas/tarifas-vigentes/ · https://www.calculadoradomundo.com.br/energia/tarifa-energia-por-distribuidora/cemig |
| Recarga rápida pública | R$ 2,50/kWh | https://www.vrum.com.br/avaliacoes/2026/08/7475942-carro-eletrico-quanto-custa-carregar-em-casa-vs-postos-fizemos-a-conta.html |
| **Diferença VE × ICE de entrada a 1.000 km** | **+R$ 463 a +R$ 604/mês** (a energia cobre 21–43% da diferença de mensalidade) | cálculo com as fontes acima |
| **Empate com o ICE de entrada** | **~2.330 km/mês** (em casa); ~2.650 (mix) | cálculo |
| VE × ICE automático a 1.000 km | −R$ 446/mês (indicativo, carros não equivalentes) | cálculo |
| Assinar × financiar o VE (SP, 24 m) | −R$ 168 a −R$ 492/mês | juros: https://api.bcb.gov.br/dados/serie/bcdata.sgs.25471/dados/ultimos/3?formato=json · IPVA: https://www.vrum.com.br/aceleradas/2026/07/7471454-ipva-para-carro-eletrico-em-2026-guia-de-isencao-e-descontos-por-estado.html · depreciação 13,7%: https://mecanicaonline.com.br/2026/09/byd-dolphin-mini-perde-137-do-valor-em-dois-anos-e-muito-para-um-eletrico/ |
| Preço só com CPF + consulta de crédito | observação direta (out/26) | https://assinatura.localiza.com/personalize-seu-plano/eletrico/byd-dolphin-mini/000027%C3%8D |
| Pagamento antecipado reduz a mensalidade; planos de 3–9 meses | Forbes, 29/09/2026 | https://forbes.com.br/forbes-life/forbes-motors/2026/09/localiza-meoo-agora-e-localiza-assinatura-e-amplia-oferta-de-carros-com-planos-a-partir-de-3-meses/ |

**Objeção do Zarp (incorporada):**
- Rodar mais de 2.330 km/mês é perfil de motorista de aplicativo. Esse público já é atendido pelo
  Zarp Localiza, que aluga por semana para motoristas de app e tem projeto-piloto de elétricos em SP
  (https://zarp.localiza.com/).
- O uso típico de carro novo no Brasil é de ~12,9 mil km/ano, ou ~1.075 km/mês
  (https://www.automotivebusiness.com.br/noticias/veiculos-novos-rodam-em-media-129-mil-km-no-brasil).
- **Por isso a proposta deixou de mirar "alta rodagem".** O argumento de preço passa a ser:
  - mostrar a conta sem CPF;
  - comparar com o **combustão equivalente (automático)**, contra o qual o elétrico já ganha.
- **Pergunta-chave para a banca:** os 80% que trocaram o VE por ICE assinaram qual categoria? Se foi
  automático ou SUV, o problema é mais de recarga e percepção do que de preço.

## 2. G2: Recarga em casa / wallbox (validado, rodada 3)
**Conclusão:** incluir o wallbox custa à Localiza **R$ 104 a R$ 270/mês por contrato** de 24–48 meses.

| Achado | Número | Fonte |
|---|---|---|
| Wallbox Intelbras 7,4 kW | R$ 3.475,80 (garantia 2 anos) | https://loja.intelbras.com.br/estacao-recarga-veiculos-eletricos-home-ac74-kw/p |
| Instalação | R$ 1.500 a R$ 5.000 | https://www.em.com.br/trends/2026/04/7392994-carro-eletrico-em-casa-quanto-custa-para-instalar-um-carregador.html · https://assinatura.localiza.com/blog/post/wallbox |
| Custo por contrato | R$ 4.975,80 (instalação R$ 1.500) a R$ 6.475,80 (teto R$ 3.000) | cálculo |
| **R$/mês** | **R$ 104 (48 m) a R$ 270 (24 m)**; 12 m: R$ 415–540 | cálculo: custo ÷ meses |
| Moradia | 84,8% em casa; 14,9% em apartamento/condomínio (Censo 2022) | https://www.sindiconet.com.br/informese/censo-ibge-moradores-apartamentos-noticias-mercado |
| Lei SP de recarga em condomínio | veto só com justificativa técnica | https://www.al.sp.gov.br/repositorio/legislacao/lei/2026/lei-18403-18.02.2026.html |
| Portátil proibido em garagem coletiva (SP) | Bombeiros SP | https://canalve.com.br/recarga-predios-bombeiros-sp-atualizam-parecer-tecnico/ |
| Montadora dá wallbox (precedente) | GWM ORA 03 | https://www.gwmmotors.com.br/pt/media-center/news/2024/gwm-oferece-wallbox-gratis-para-a-linha-ora-03 |

**Revisão de desenho: o wallbox fica com quem deixa a assinatura** (análise `G2-r6.md`).
- **Regra (24–48 m):** durante o contrato o wallbox é da Localiza, em comodato. Se o cliente renova,
  segue em comodato, com reparo por conta da Localiza. **Quando o cliente deixa a assinatura, o
  wallbox é transferido a ele**, sem cobrança e sem retirada.
- **12 m:** wallbox opcional com coparticipação; no fim, retirada ou compra pelo valor residual
  (regra da r3), porque ali a renúncia seria a maior (~R$ 145/mês). Depois de 12 m restam 12 meses
  de garantia, que cobrem um 2º contrato só se ele também for de 12 m.
- **Custo:** no custo gerencial do caso-base (incluso, sem reuso, amortização linear **sem custo de
  capital**) a regra não acrescenta custo. O custo fiscal e jurídico da transferência é lacuna.
- **O que a Localiza renuncia** (só para quem sai):
  - o reuso, de R$ 1.737,90 por contrato (metade do equipamento), ou R$ 36–72/mês em 48–24 m,
    antes dos custos de retirada, que não têm dado;
  - a venda pelo valor residual;
  - o motivo de renovar para manter o carregador.
- **Como fechar o que falta:**
  - custo de retirar: cotação com os instaladores do teste Meoo no mês 1, antes do A/B;
  - efeito isolado na conversão: só com uma 3ª célula no A/B (com retirada × com transferência), se o
    volume de leads permitir;
  - efeito na renovação: não dá para medir em 90 dias; só a intenção declarada no piloto e o ciclo real
    no fim dos primeiros contratos (≥ 24 m). A regra não é usada como argumento de renovação.
- Saída antecipada: o cliente quita o saldo não amortizado ou opta pela retirada. É regra de
  desenho, a calibrar.
- Alternativa avaliada: um parceiro instalador ou de energia é dono do wallbox e cobra o cliente
  depois do contrato ("carregador como serviço"). Cria um segundo contrato para o cliente. Fica como
  opção B.

## 3. G3: Recarga pública (validado, rodada 2)
**Conclusão:**
- A rede pública não é suficiente.
- O que a Localiza pode fazer, sem construir rede, é dar o mapa e a rota que a banca apontou como
  ausentes.

| Achado | Número | Fonte |
|---|---|---|
| Pontos públicos e semipúblicos | 29.866 (ago/26), 38% recarga rápida | https://abve.org.br/recarga-rapida-dc-quase-triplica-em-12-meses-e-ja-responde-por-38-da-rede-brasileira/ |
| VEs por ponto | Brasil 21,4 × média global ~11 | ABVE (acima) · https://www.evinfrastructurenews.com/ev-networks/iea-1-8-million-public-ev-chargepoints-added-globally-in-2025-china-accounts-for-65- |
| EUA (33/ponto) recarregam ~80% em casa | — | https://www.energy.gov/topics/national-ev-charging-network |
| Consumidores esperam carregar em casa/trabalho | 93%; 67% não têm carregador | https://www.deloitte.com/br/pt/about/press-room/global-automotive-consumer-study.html |
| Dados para o mapa | APIs disponíveis | https://developers.google.com/maps/billing-and-pricing/pricing · https://openchargemap.org/develop · https://tupimob.com/app-de-recarga/ |
| Precedente de desconto em rede | 99 Recarga: até 20% (motoristas de app, RJ) | https://olhardigital.com.br/2026/09/21/carros-e-tecnologia/99-lanca-app-de-recarga-eletrica-no-rj-que-reune-postos-de-diferentes-redes-e-oferece-ate-20-de-desconto |
| Acordo Localiza × BYD | compra de 10 mil carros em 2 anos | https://braziljournal.com/exclusivo-localiza-fecha-acordo-para-comprar-10-mil-carros-da-byd/ |

**Não comprovável:** se o mapa aumenta a conversão (exige o A/B) e quem banca o desconto em rede
parceira.

---

## 4. MVP proposto
1. **Simulador Elétrico, aberto e sem CPF**, com duas abas da mesma ferramenta:
   - **Custo total:** mensalidade + energia × combustão equivalente, pela rodagem do lead.
   - **Minha rotina:** CEP de casa e do trabalho e destinos de viagem contra os pontos de recarga
     rápida.
   Fica no site, com o vendedor e no WhatsApp.
2. **Mapa e rota de eletropostos no app** (com o parceiro do time), usando a telemetria de bateria
   que o app já tem.
3. **Operacional, não software:** o kit wallbox incluso, com os instaladores do teste da Meoo.

Tudo é validado no **piloto A/B em São Paulo**, com 1 mês de construção, 3 de teste e a decisão no
mês 5. Métrica principal: % de leads de elétrico que assinam elétrico.
