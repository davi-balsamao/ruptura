"""Números no padrão brasileiro (1.234,56)."""


def num(valor: float, casas: int = 0) -> str:
    texto = f"{valor:,.{casas}f}"
    return texto.replace(",", "_").replace(".", ",").replace("_", ".")


def brl(valor: float, casas: int = 0) -> str:
    sinal = "−" if valor < 0 else ""
    return f"{sinal}R$ {num(abs(valor), casas)}"


def pct(fracao: float, casas: int = 0) -> str:
    return f"{num(fracao * 100, casas)}%"
