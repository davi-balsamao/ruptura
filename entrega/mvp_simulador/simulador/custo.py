"""Aba "Custo total": mensalidade + energia do elétrico contra o combustão.

Mesmo modelo da análise G1-r2: custo do mês = mensalidade + km × R$/km, com a mensalidade
constante entre franquias (a tabela por franquia é lacuna até a cotação oficial).
"""
from dataclasses import dataclass

from .premissas import FRANQUIAS, WALLBOX, Carro, Energia, Wallbox


@dataclass(frozen=True)
class CustoMensal:
    carro: Carro
    km: float
    mensalidade: float
    energia: float  # eletricidade ou gasolina, R$/mês

    @property
    def total(self) -> float:
        return self.mensalidade + self.energia

    @property
    def por_km(self) -> float:
        return self.total / self.km if self.km else 0.0


def tarifa_media(energia: Energia, fracao_casa: float) -> float:
    """R$/kWh ponderado entre recarga em casa e recarga rápida na rua."""
    f = min(max(fracao_casa, 0.0), 1.0)
    return f * energia.tarifa_casa + (1 - f) * energia.tarifa_rua


def custo_por_km(carro: Carro, energia: Energia, fracao_casa: float = 1.0) -> float:
    if carro.eletrico:
        return carro.consumo * tarifa_media(energia, fracao_casa)
    return energia.gasolina / carro.consumo


def custo_mensal(carro: Carro, km: float, energia: Energia, fracao_casa: float = 1.0) -> CustoMensal:
    return CustoMensal(carro, km, carro.mensalidade, km * custo_por_km(carro, energia, fracao_casa))


def empate_km(ve: Carro, ice: Carro, energia: Energia, fracao_casa: float = 1.0) -> float | None:
    """km/mês a partir do qual o elétrico fica mais barato que o combustão.

    0 se o elétrico já é mais barato com qualquer rodagem; None se nunca empata.
    """
    dif_mensalidade = ve.mensalidade - ice.mensalidade
    economia_km = custo_por_km(ice, energia) - custo_por_km(ve, energia, fracao_casa)
    if dif_mensalidade <= 0:
        return 0.0
    if economia_km <= 0:
        return None
    return dif_mensalidade / economia_km


def franquia_sugerida(km: float) -> int | None:
    """Menor franquia que cobre a rodagem; None se passar da maior."""
    return next((f for f in FRANQUIAS if km <= f), None)


def curva(carro: Carro, energia: Energia, fracao_casa: float, kms) -> list[tuple[float, float]]:
    return [(km, custo_mensal(carro, km, energia, fracao_casa).total) for km in kms]


# --- Wallbox (G2-r3 caso-base, sem reuso; regra de fim de contrato da G2-r6) ---

def wallbox_custo_contrato(wb: Wallbox = WALLBOX, no_teto: bool = True) -> float:
    return wb.equipamento + (wb.instalacao_teto if no_teto else wb.instalacao_simples)


def wallbox_custo_mensal_localiza(prazo: int, wb: Wallbox = WALLBOX, no_teto: bool = True) -> float:
    """Amortização linear sem custo de capital (piso), como na Tab. 2 da G2-r3."""
    return wallbox_custo_contrato(wb, no_teto) / prazo


def wallbox_incluso(prazo: int, wb: Wallbox = WALLBOX) -> bool:
    return prazo in wb.prazos_incluso


def wallbox_saldo_saida_antecipada(prazo: int, mes_saida: int, wb: Wallbox = WALLBOX, no_teto: bool = True) -> float:
    """Saldo não amortizado se o cliente sair antes do fim e quiser ficar com o wallbox."""
    restantes = max(prazo - mes_saida, 0)
    return wallbox_custo_contrato(wb, no_teto) * restantes / prazo
