# Simulador Elétrico (MVP)

Protótipo do item 1 do MVP (`entrega/CONCLUSOES.md` §4): o lead de elétrico faz a conta **sem CPF e
sem cadastro**. Visual inspirado no site da Localiza Assinatura (cores, fonte Inter, passos
numerados); é um protótipo do Case Ruptura 2026, não um site oficial.

**Fora desta versão:** mapa e rota de eletropostos (próxima fase).

## O que faz
| Aba | Responde | Base |
|---|---|---|
| **Custo total** | Mensalidade + energia do elétrico contra o combustão automático e o de entrada, pela rodagem do lead; empate em km/mês; gráfico de 300 a 3.000 km | G1-r2 |
| **Minha rotina** | km por semana, quantas vezes ligar na tomada, horas de wallbox, % da bateria por dia, paradas numa viagem e o passo a passo da recarga em casa (casa, condomínio, sem vaga) | G2-r3/r6 |
| **Resumo para o consultor** | Texto pronto para copiar no WhatsApp ou baixar; nenhum dado pessoal | — |

Os testes (`tests/`) conferem que o simulador reproduz os números validados pelo crítico:
+R$ 463/mês contra o combustão de entrada a 1.000 km; empate em ~2.330 km/mês; −R$ 446/mês contra o
automático; wallbox a R$ 104–270/mês para a Localiza.

## Rodar
Usa o ambiente virtual desta pasta (`.venv`, com Streamlit e pytest). O Python global não é alterado.

```bash
.venv/Scripts/python.exe rodar.py
```

Abre em http://localhost:8501. Testes:

```bash
.venv/Scripts/python.exe -m pytest -q
```

Para recriar o ambiente do zero: `python -m venv .venv` e
`.venv/Scripts/python.exe -m pip install -r requirements.txt`.

## Estrutura
- `simulador/premissas.py`: todos os números e as fontes. **Troque aqui pela tabela oficial** quando
  a Localiza liberar o preço (hoje só com CPF); a tela "Ajustar premissas" faz o mesmo sem código.
- `simulador/custo.py` e `simulador/rotina.py`: cálculo puro, sem dependências.
- `app.py`: a tela (Streamlit). `rodar.py`: atalho que já aplica o tema de `.streamlit/config.toml`.

## Limitações honestas
- Mensalidades são **indicativas de mercado** (out/2026) e iguais em todos os prazos e franquias:
  a tabela por prazo e franquia é lacuna até a cotação oficial.
- A autonomia para planejar (~222 km) é bateria ÷ consumo PBEV com 20% de reserva (suposição de
  planejamento). Cada parada de recarga rápida devolve essa autonomia (simplificação).
- O tempo de wallbox usa 7,4 kW; o carro pode aceitar menos.
