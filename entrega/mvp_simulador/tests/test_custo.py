"""O simulador tem que reproduzir os números validados pelo crítico (G1-r2, Gráficos 1–3; G2-r3, Tab. 2)."""
import pytest

from simulador.custo import (
    custo_mensal,
    custo_por_km,
    empate_km,
    franquia_sugerida,
    wallbox_custo_contrato,
    wallbox_custo_mensal_localiza,
    wallbox_incluso,
    wallbox_saldo_saida_antecipada,
)
from simulador.formato import brl, num
from simulador.premissas import ENERGIA, ICE_AUTOMATICO, ICE_ENTRADA, VE

CENT = 0.01


@pytest.mark.parametrize(
    "km, ice, ve_casa, ve_dc",
    [
        (500, 2298.04, 2934.80, 3005.42),
        (1000, 2537.09, 2999.60, 3140.83),
        (2000, 3015.19, 3129.20, 3411.67),
        (3000, 3493.30, 3258.80, 3682.50),
    ],
)
def test_grafico_1_ve_contra_ice_de_entrada(km, ice, ve_casa, ve_dc):
    assert custo_mensal(ICE_ENTRADA, km, ENERGIA).total == pytest.approx(ice, abs=CENT)
    assert custo_mensal(VE, km, ENERGIA, fracao_casa=1).total == pytest.approx(ve_casa, abs=CENT)
    assert custo_mensal(VE, km, ENERGIA, fracao_casa=0).total == pytest.approx(ve_dc, abs=CENT)


def test_gap_a_1000_km_e_mix_70_30():
    ve = custo_mensal(VE, 1000, ENERGIA, fracao_casa=1).total
    ice = custo_mensal(ICE_ENTRADA, 1000, ENERGIA).total
    assert ve - ice == pytest.approx(462.51, abs=CENT)
    assert custo_mensal(VE, 1000, ENERGIA, fracao_casa=0.7).total == pytest.approx(3041.97, abs=CENT)
    assert custo_por_km(VE, ENERGIA, 0.7) == pytest.approx(0.1720, abs=1e-4)


@pytest.mark.parametrize("km, delta", [(500, 194.98), (1000, -30.05), (3000, -930.14)])
def test_grafico_3_ve_contra_automatico(km, delta):
    ve = custo_mensal(VE, km, ENERGIA, fracao_casa=1).total
    ice = custo_mensal(ICE_AUTOMATICO, km, ENERGIA).total
    assert ve - ice == pytest.approx(delta, abs=CENT)


@pytest.mark.parametrize("fracao_casa, esperado", [(1.0, 2330), (0.7, 2650), (0.0, 3910)])
def test_grafico_2_empate(fracao_casa, esperado):
    assert empate_km(VE, ICE_ENTRADA, ENERGIA, fracao_casa) == pytest.approx(esperado, abs=10)


def test_contra_automatico_ve_empata():
    assert empate_km(VE, ICE_AUTOMATICO, ENERGIA) == pytest.approx(933.24, abs=CENT)


def test_franquia_sugerida():
    assert franquia_sugerida(450) == 500
    assert franquia_sugerida(1000) == 1000
    assert franquia_sugerida(1001) == 1500
    assert franquia_sugerida(3200) is None


def test_wallbox_tabela_2_g2_r3():
    assert wallbox_custo_contrato(no_teto=False) == pytest.approx(4975.80)
    assert wallbox_custo_contrato(no_teto=True) == pytest.approx(6475.80)
    assert wallbox_custo_mensal_localiza(48, no_teto=False) == pytest.approx(103.66, abs=CENT)
    assert wallbox_custo_mensal_localiza(24, no_teto=True) == pytest.approx(269.83, abs=CENT)
    assert wallbox_custo_mensal_localiza(12, no_teto=True) == pytest.approx(539.65, abs=CENT)


def test_wallbox_incluso_so_de_24_a_48_meses():
    assert [p for p in (12, 24, 36, 48) if wallbox_incluso(p)] == [24, 36, 48]


def test_wallbox_saida_antecipada_g2_r4():
    assert wallbox_saldo_saida_antecipada(36, 12) == pytest.approx(4317.20, abs=CENT)
    assert wallbox_saldo_saida_antecipada(36, 36) == 0


def test_formato_brasileiro():
    assert brl(2999.6) == "R$ 3.000"
    assert brl(-446.29, 2) == "−R$ 446,29"
    assert num(7.4, 1) == "7,4"
