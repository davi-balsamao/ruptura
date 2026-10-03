"""Aba "Minha rotina": quanto o lead roda, onde recarrega e como fica a recarga em casa.

Sem mapa: os pontos de recarga no trajeto e a rota de viagem ficam para a próxima fase.
"""
import math
from dataclasses import dataclass
from enum import Enum

from .formato import brl, num
from .premissas import BATERIA, WALLBOX, Bateria, Carro, Wallbox

SEMANAS_POR_MES = 52 / 12


class Moradia(str, Enum):
    CASA = "Casa com garagem"
    CONDOMINIO = "Condomínio com vaga"
    SEM_VAGA = "Sem vaga própria"


@dataclass(frozen=True)
class Rotina:
    km_dia_util: float = 40.0  # ida e volta
    dias_uteis: int = 5
    km_fim_de_semana: float = 30.0  # sábado + domingo
    viagens_mes: int = 0
    km_viagem: float = 0.0  # ida e volta

    @property
    def km_semana(self) -> float:
        return self.km_dia_util * self.dias_uteis + self.km_fim_de_semana

    @property
    def km_rotina_mes(self) -> float:
        return self.km_semana * SEMANAS_POR_MES

    @property
    def km_viagens_mes(self) -> float:
        return self.viagens_mes * self.km_viagem

    @property
    def km_mes(self) -> float:
        return self.km_rotina_mes + self.km_viagens_mes


def autonomia_planejamento(carro: Carro, bateria: Bateria = BATERIA) -> float:
    """km que dá para planejar com a bateria cheia, guardando a reserva."""
    return bateria.capacidade_kwh * (1 - bateria.reserva) / carro.consumo


def paradas_por_viagem(km_viagem: float, autonomia: float) -> int:
    """Recargas rápidas no caminho, saindo de casa com a bateria cheia.

    Simplificação do MVP: cada parada devolve a autonomia de planejamento.
    """
    if km_viagem <= autonomia:
        return 0
    return math.ceil((km_viagem - autonomia) / autonomia)


def km_na_rua_mes(rotina: Rotina, moradia: Moradia, autonomia: float) -> float:
    """km do mês rodados com energia da recarga pública."""
    if moradia is Moradia.SEM_VAGA:
        return rotina.km_mes
    return rotina.viagens_mes * max(rotina.km_viagem - autonomia, 0.0)


def fracao_casa(rotina: Rotina, moradia: Moradia, autonomia: float) -> float:
    if rotina.km_mes <= 0:
        return 0.0 if moradia is Moradia.SEM_VAGA else 1.0
    return 1 - km_na_rua_mes(rotina, moradia, autonomia) / rotina.km_mes


def energia_kwh(km: float, carro: Carro) -> float:
    return km * carro.consumo


def horas_wallbox_semana(km_semana: float, carro: Carro, wb: Wallbox = WALLBOX) -> float:
    """Horas de wallbox por semana para repor a rotina (o carro pode aceitar menos que 7,4 kW)."""
    return energia_kwh(km_semana, carro) / wb.potencia_kw


def bateria_por_dia(km_dia: float, carro: Carro, bateria: Bateria = BATERIA) -> float:
    """Fração da bateria gasta num dia de rotina."""
    return energia_kwh(km_dia, carro) / bateria.capacidade_kwh


def recargas_por_semana(km_semana: float, autonomia: float) -> int:
    """Quantas vezes por semana é preciso ligar o carro na tomada para a rotina."""
    return math.ceil(km_semana / autonomia) if km_semana > 0 else 0


def km_semana_de_km_mes(km_mes: float) -> float:
    return km_mes / SEMANAS_POR_MES


def caminho_recarga_casa(moradia: Moradia, prazo: int, wb: Wallbox = WALLBOX) -> list[str]:
    """Passo a passo da recarga em casa para o perfil do lead (G2-r3, regra de fim da G2-r6)."""
    teto = brl(wb.instalacao_teto)
    if moradia is Moradia.SEM_VAGA:
        return [
            "Sem vaga própria, a recarga é na rua: a aba Custo total já usa a tarifa da recarga rápida.",
            "Recarregar só na rua custa mais por km do que em casa; compare os cenários na aba Custo total.",
            "Os pontos de recarga perto de você entram na próxima fase (mapa de eletropostos).",
        ]
    diagnostico = "Diagnóstico elétrico com um instalador parceiro, antes de você assinar."
    if prazo in wb.prazos_incluso:
        passos = [
            diagnostico,
            f"Wallbox de {num(wb.potencia_kw, 1)} kW e instalação até {teto} inclusos na mensalidade.",
            "Quando você deixar a assinatura, o wallbox é seu: sem retirada e sem visita técnica. "
            "Se renovar, ele continua com a manutenção por nossa conta.",
        ]
    else:
        passos = [
            diagnostico,
            "No plano de 12 meses o wallbox é opcional, com coparticipação. Nos planos de 24 a 48 meses ele é incluso.",
        ]
    if moradia is Moradia.CONDOMINIO:
        passos += [
            "Kit condomínio: estudo de carga antes de assinar, ART e comunicação ao síndico.",
            "Em SP, a Lei 18.403/2026 só admite veto com justificativa técnica ou de segurança.",
            f"Em condomínio a obra pode passar de {teto}: você paga só o que passar do teto, com orçamento aberto.",
            "Carregador portátil não resolve: em SP ele é vedado em garagem coletiva.",
        ]
    return passos
