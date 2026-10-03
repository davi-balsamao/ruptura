# Dicionário de Dados do Simulador (DAVI)

Este documento contém a taxonomia e os dados estáticos que alimentam o Simulador Elétrico. Estes dados representam a estrutura que a Localiza deve fornecer em seu banco de dados para que o simulador funcione com precisão.

## A. Veículos e Desempenho

O MVP utiliza 6 carros, formando 2 grupos de simulação. Cada grupo contém 1 Elétrico, 1 Combustão Automático e 1 Combustão Manual.

### Simulação 1: Hatch Compacto
1. **BYD Dolphin Mini** (Elétrico)
   - Consumo Urbano: 9.2 km/kWh
   - Bateria: 30 kWh
   - Mensalidade Base (36m): R$ 2.870,00
   - Par Sugerido Automático: Onix Hatch 1.0 Turbo AT
   - Par Sugerido Manual: Onix 1.0 Manual

2. **Onix Hatch 1.0 Turbo AT** (Combustão Automático)
   - Consumo Urbano Gasolina: 11.3 km/L
   - Consumo Urbano Etanol: 8.2 km/L
   - Tanque: 44 L
   - Mensalidade Base (36m): R$ 2.450,00

3. **Onix 1.0 Manual** (Combustão Manual)
   - Consumo Urbano Gasolina: 13.7 km/L
   - Consumo Urbano Etanol: 9.9 km/L
   - Tanque: 44 L
   - Mensalidade Base (36m): R$ 2.050,00

### Simulação 2: Hatch Premium
4. **GWM Ora 03 Skin** (Elétrico)
   - Consumo Urbano: 8.3 km/kWh
   - Bateria: 48 kWh
   - Mensalidade Base (36m): R$ 3.200,00
   - Par Sugerido Automático: VW Polo Highline
   - Par Sugerido Manual: VW Polo MPI Manual

5. **VW Polo Highline** (Combustão Automático)
   - Consumo Urbano Gasolina: 11.5 km/L
   - Consumo Urbano Etanol: 8.0 km/L
   - Tanque: 52 L
   - Mensalidade Base (36m): R$ 2.800,00

6. **VW Polo MPI Manual** (Combustão Manual)
   - Consumo Urbano Gasolina: 14.0 km/L
   - Consumo Urbano Etanol: 9.6 km/L
   - Tanque: 52 L
   - Mensalidade Base (36m): R$ 2.400,00

## B. Dados de Preço e Contrato

- **Prazos Disponíveis:** 12, 24 e 36 meses.
- **Franquias de KM:** 1.000, 1.500, 2.000, 2.500 e 3.000 km.
- **Regra de Variação (Mock do MVP):**
  - Contrato de 12 meses: +15% na mensalidade base
  - Contrato de 24 meses: +5% na mensalidade base
  - Contrato de 36 meses: Mensalidade base (0%)
  - Franquia: A cada 500 km acima de 1.000, soma-se 5% na mensalidade.
- **Wallbox:** Custo e oferta suspensos nesta fase do MVP (não avaliado).

## C. Dados de Energia e Combustível (Médias Nacionais)

- **Preço Gasolina:** R$ 6,55 / Litro
- **Preço Etanol:** R$ 4,30 / Litro
- **Tarifa Residencial (kWh):** R$ 1,20
- **Tarifa Eletroposto Rua (kWh):** R$ 2,50
- **Tarifa Solar (kWh):** R$ 0,15 (taxa residual de disponibilidade/fio)
- **Taxa de Perda de Recarga:** 12% (Multiplica o consumo final de energia em kWh por 1.12 para cobrir perdas de conversão em calor).
