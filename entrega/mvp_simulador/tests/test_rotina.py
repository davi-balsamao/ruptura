import pytest

from simulador.premissas import VE
from simulador.rotina import (
    Moradia,
    Rotina,
    autonomia_planejamento,
    bateria_por_dia,
    caminho_recarga_casa,
    fracao_casa,
    horas_wallbox_semana,
    km_na_rua_mes,
    km_semana_de_km_mes,
    paradas_por_viagem,
    recargas_por_semana,
)

AUTONOMIA = autonomia_planejamento(VE)


def test_km_do_mes_soma_rotina_e_viagens():
    r = Rotina(km_dia_util=40, dias_uteis=5, km_fim_de_semana=30, viagens_mes=1, km_viagem=400)
    assert r.km_semana == 230
    assert r.km_mes == pytest.approx(230 * 52 / 12 + 400)


def test_autonomia_de_planejamento_guarda_20_por_cento():
    # 30,08 kWh × 80% ÷ 0,10833 kWh/km ≈ 222 km
    assert AUTONOMIA == pytest.approx(222.1, abs=0.5)


@pytest.mark.parametrize("km, paradas", [(150, 0), (222, 0), (300, 1), (500, 2)])
def test_paradas_por_viagem(km, paradas):
    assert paradas_por_viagem(km, AUTONOMIA) == paradas


def test_rotina_sem_viagem_longa_recarrega_toda_em_casa():
    r = Rotina(viagens_mes=2, km_viagem=200)
    assert km_na_rua_mes(r, Moradia.CASA, AUTONOMIA) == 0
    assert fracao_casa(r, Moradia.CASA, AUTONOMIA) == 1


def test_sem_vaga_tudo_na_rua():
    r = Rotina()
    assert fracao_casa(r, Moradia.SEM_VAGA, AUTONOMIA) == 0


def test_viagem_acima_da_autonomia_vai_para_a_rua():
    r = Rotina(viagens_mes=1, km_viagem=500)
    na_rua = 500 - AUTONOMIA
    assert km_na_rua_mes(r, Moradia.CONDOMINIO, AUTONOMIA) == pytest.approx(na_rua)
    assert fracao_casa(r, Moradia.CONDOMINIO, AUTONOMIA) == pytest.approx(1 - na_rua / r.km_mes)


def test_rotina_de_40_km_por_dia():
    r = Rotina(km_dia_util=40, dias_uteis=5, km_fim_de_semana=30)
    assert bateria_por_dia(r.km_dia_util, VE) == pytest.approx(40 * 0.10833 / 30.08, abs=1e-3)
    assert horas_wallbox_semana(r.km_semana, VE) == pytest.approx(230 * 0.10833 / 7.4, abs=1e-3)
    assert recargas_por_semana(r.km_semana, AUTONOMIA) == 2


def test_modo_km_por_mes():
    # 1.000 km/mês ≈ 230,8 km/semana ≈ 3,4 h de wallbox
    km_semana = km_semana_de_km_mes(1000)
    assert km_semana == pytest.approx(230.77, abs=0.01)
    assert horas_wallbox_semana(km_semana, VE) == pytest.approx(3.38, abs=0.01)


def test_caminho_da_recarga_em_casa():
    casa_36 = caminho_recarga_casa(Moradia.CASA, 36)
    assert any("o wallbox é seu" in p for p in casa_36)
    assert any("R$ 3.000" in p and "7,4 kW" in p for p in casa_36)
    assert any("opcional" in p for p in caminho_recarga_casa(Moradia.CASA, 12))
    assert any("Lei 18.403" in p for p in caminho_recarga_casa(Moradia.CONDOMINIO, 24))
    assert not any("Lei 18.403" in p for p in casa_36)
    assert any("na rua" in p for p in caminho_recarga_casa(Moradia.SEM_VAGA, 36))
