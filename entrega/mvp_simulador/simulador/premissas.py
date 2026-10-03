"""Premissas do Simulador Elétrico, com a fonte de cada número.

Todos os valores vêm das análises validadas pelo crítico (G1-r2, G2-r3/r4, G3-r2) e estão
listados com URL em entrega/CONCLUSOES.md. Preços de mensalidade são INDICATIVOS DE MERCADO:
a Localiza só mostra o preço com CPF e consulta de crédito. Quando a tabela oficial existir,
basta trocar os valores aqui (ou na tela "Premissas" do app).
"""
from dataclasses import dataclass, replace


@dataclass(frozen=True)
class Carro:
    nome: str
    eletrico: bool
    mensalidade: float  # R$/mês
    consumo: float  # elétrico: kWh/km · combustão: km/L
    fonte_preco: str
    fonte_consumo: str


@dataclass(frozen=True)
class Energia:
    gasolina: float = 6.55  # R$/L, média nacional, semana 20–26/09/2026
    tarifa_casa: float = 1.1963  # R$/kWh residencial COM impostos (Cemig B1, bandeira amarela)
    tarifa_rua: float = 2.50  # R$/kWh, recarga rápida (DC) pública, valor médio


@dataclass(frozen=True)
class Wallbox:
    equipamento: float = 3475.80  # Intelbras Home AC 7,4 kW, loja oficial
    instalacao_simples: float = 1500.00  # piso da média de imprensa
    instalacao_teto: float = 3000.00  # teto incluso no contrato (regra de desenho)
    potencia_kw: float = 7.4
    garantia_meses: int = 24
    prazos_incluso: tuple = (24, 36, 48)  # em 12 m é opcional, com coparticipação


@dataclass(frozen=True)
class Bateria:
    capacidade_kwh: float = 30.08  # Dolphin Mini GL
    reserva: float = 0.20  # planejar sem usar os últimos 20% [suposição de planejamento]


VE = Carro(
    nome="Elétrico (BYD Dolphin Mini)",
    eletrico=True,
    mensalidade=2870.00,
    consumo=0.39 / 3.6,  # 0,39 MJ/km (PBEV) = 0,10833 kWh/km
    fonte_preco="byd.com/br/byd-por-assinatura (a partir de R$ 2.870,40)",
    fonte_consumo="canalve.com.br, PBEV mar/2026 (0,39 MJ/km)",
)
ICE_AUTOMATICO = Carro(
    nome="Combustão automático (Onix Hatch 1.0 Turbo AT)",
    eletrico=False,
    mensalidade=2450.00,
    consumo=11.3,
    fonte_preco="comparacar.com.br (Onix Hatch 1.0 Turbo AT)",
    fonte_consumo="Inmetro (11,3 km/L cidade gasolina)",
)
ICE_ENTRADA = Carro(
    nome="Combustão de entrada (Onix 1.0 manual)",
    eletrico=False,
    mensalidade=2058.99,
    consumo=13.7,
    fonte_preco="livre.com.br, Unidas Livre (36 m, 1.000 km)",
    fonte_consumo="revistacarro.com.br, Inmetro (13,7 km/L cidade)",
)

ENERGIA = Energia()
WALLBOX = Wallbox()
BATERIA = Bateria()

PRAZOS = (12, 24, 36, 48)
# 500 km aparece no site da Localiza (out/2026); 1.000–3.000 km vêm do material do case.
FRANQUIAS = (500, 1000, 1500, 2000, 2500, 3000)

# O que a mensalidade da Assinatura já inclui (material do case, #produto) e o que já é
# risco da Localiza (#preoc-1, #preoc-6 a #preoc-9).
INCLUSO_NA_MENSALIDADE = (
    "Documentação, impostos e licenciamento",
    "Manutenção preventiva e corretiva, troca de pneus e reboque",
    "Cobertura total, com proteção de terceiros, e suporte 24h",
    "Bateria, revenda e depreciação: o risco é da Localiza, não seu",
)

FONTES = (
    ("Mensalidade do elétrico", "https://www.byd.com/br/byd-por-assinatura"),
    ("Mensalidade do combustão de entrada", "https://www.livre.com.br/carro-por-assinatura/Chevrolet_Onix_1.0_2025/"),
    ("Mensalidade do combustão automático", "https://www.comparacar.com.br"),
    ("Gasolina", "https://precos.petrobras.com.br/precos-gasolina"),
    ("Tarifa residencial", "https://www.cemig.com.br/valores-e-tarifas/tarifas-vigentes/"),
    ("Recarga rápida pública", "https://www.vrum.com.br/avaliacoes/2026/08/7475942-carro-eletrico-quanto-custa-carregar-em-casa-vs-postos-fizemos-a-conta.html"),
    ("Consumo do elétrico (PBEV)", "https://canalve.com.br/dez-centavos-km-conheca-carros-mais-eficientes-brasil/"),
    ("Consumo do Onix 1.0", "https://revistacarro.com.br/onix-2026-segue-como-carro-mais-economico-do-brasil-veja-lista-do-inmetro/"),
    ("Wallbox Intelbras 7,4 kW", "https://loja.intelbras.com.br/estacao-recarga-veiculos-eletricos-home-ac74-kw/p"),
    ("Custo de instalação", "https://www.em.com.br/trends/2026/04/7392994-carro-eletrico-em-casa-quanto-custa-para-instalar-um-carregador.html"),
    ("Lei SP 18.403/2026 (recarga em condomínio)", "https://www.al.sp.gov.br/repositorio/legislacao/lei/2026/lei-18403-18.02.2026.html"),
)


def com_mensalidade(carro: Carro, valor: float) -> Carro:
    """Cópia do carro com outra mensalidade (para plugar a tabela oficial)."""
    return replace(carro, mensalidade=valor)
