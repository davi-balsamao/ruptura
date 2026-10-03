// --- DICIONÁRIO DE DADOS (DAVI) ---

const DB_ELETRICOS = [
    { 
        id: 'ev_mini', nome: "BYD Dolphin Mini", 
        consumo: 9.2, bateria: 30, mensalidade_base: 2870,
        par_auto: 'ice_onix_auto', par_manual: 'ice_onix_manual' 
    },
    { 
        id: 'ev_ora', nome: "GWM Ora 03 Skin", 
        consumo: 8.3, bateria: 48, mensalidade_base: 3200,
        par_auto: 'ice_polo_auto', par_manual: 'ice_polo_manual' 
    }
];

const DB_COMBUSTAO = [
    { id: 'ice_onix_auto', nome: "Onix Hatch 1.0 Turbo AT", cons_gas: 11.3, cons_eta: 8.2, tanque: 44, mensalidade_base: 2450 },
    { id: 'ice_onix_manual', nome: "Onix 1.0 Manual", cons_gas: 13.7, cons_eta: 9.9, tanque: 44, mensalidade_base: 2050 },
    { id: 'ice_polo_auto', nome: "VW Polo Highline", cons_gas: 11.5, cons_eta: 8.0, tanque: 52, mensalidade_base: 2800 },
    { id: 'ice_polo_manual', nome: "VW Polo MPI Manual", cons_gas: 14.0, cons_eta: 9.6, tanque: 52, mensalidade_base: 2400 }
];

const ENERGIA = {
    gasolina: 6.55,
    etanol: 4.30,
    tarifa_casa: 1.20,
    tarifa_rua: 2.50,
    tarifa_solar: 0.15,
    perda_recarga: 1.12 // +12% de energia dissipada como calor
};

// --- FUNÇÕES DE CÁLCULO ---

function calcularMensalidade(carro, prazo, km) {
    // Definimos a franquia como o valor mais próximo arredondado para cima (mínimo 1000)
    let franquia = Math.max(1000, Math.ceil(km / 500) * 500);
    
    let mult_prazo = 0;
    if (prazo == 12) mult_prazo = 0.15;
    else if (prazo == 24) mult_prazo = 0.05;
    else if (prazo == 36) mult_prazo = 0.00;
    
    let nominal_franquia = 0;
    if (franquia > 1000) {
        // Usa um valor nominal (ex: R$ 130 a cada 500km) em vez de % para não prejudicar a diferença contra o elétrico
        nominal_franquia = ((franquia - 1000) / 500) * 130;
    }
    
    return (carro.mensalidade_base * (1 + mult_prazo)) + nominal_franquia;
}

function calcularEnergiaMensalEV(ev, km, recarga) {
    let tarifaMedia = 0;
    if (recarga === 'casa') tarifaMedia = ENERGIA.tarifa_casa;
    else if (recarga === 'solar') tarifaMedia = ENERGIA.tarifa_solar;
    else if (recarga === 'hibrido') tarifaMedia = (ENERGIA.tarifa_casa + ENERGIA.tarifa_rua) / 2;
    else if (recarga === 'rua') tarifaMedia = ENERGIA.tarifa_rua;

    const kwhNecessarios = (km / ev.consumo) * ENERGIA.perda_recarga;
    return kwhNecessarios * tarifaMedia;
}

function calcularCombustivelMensalICE(ice, km, combustivel) {
    const consumo = combustivel === 'gasolina' ? ice.cons_gas : ice.cons_eta;
    const preco = combustivel === 'gasolina' ? ENERGIA.gasolina : ENERGIA.etanol;
    const litrosNecessarios = km / consumo;
    return litrosNecessarios * preco;
}

function formatarMoeda(valor) {
    return valor.toLocaleString('pt-BR', { style: 'currency', currency: 'BRL', maximumFractionDigits: 0 });
}

// --- LÓGICA DE INTERFACE ---

function atualizarTextoLegendaKM(km) {
    const legenda = document.getElementById("legenda-km");
    if (km <= 800) legenda.innerText = `${km} km = Uso leve, passeios e mercado local`;
    else if (km <= 1500) legenda.innerText = `${km} km = Uso diário casa-trabalho (~${Math.round(km/30)} km/dia)`;
    else if (km <= 2500) legenda.innerText = `${km} km = Uso intenso, viagens curtas ou morar longe`;
    else legenda.innerText = `${km} km = Uso severo, viagens frequentes ou trabalho externo`;
}

function carregarOpcoes() {
    const selEV = document.getElementById("select-ev");
    DB_ELETRICOS.forEach(ev => {
        let opt = document.createElement("option");
        opt.value = ev.id;
        opt.innerText = ev.nome;
        selEV.appendChild(opt);
    });

    const selICE = document.getElementById("select-ice");
    DB_COMBUSTAO.forEach(ice => {
        let opt = document.createElement("option");
        opt.value = ice.id;
        opt.innerText = ice.nome;
        selICE.appendChild(opt);
    });
}

function preSelecionarConcorrente(evId) {
    const ev = DB_ELETRICOS.find(e => e.id === evId);
    if (ev) {
        document.getElementById("select-ice").value = ev.par_auto;
    }
}

function calcularTudo() {
    const evId = document.getElementById("select-ev").value;
    const iceId = document.getElementById("select-ice").value;
    const prazo = parseInt(document.querySelector('input[name="prazo"]:checked').value);
    const recarga = document.querySelector('input[name="recarga"]:checked').value;
    const combustivel = document.querySelector('input[name="combustivel"]:checked').value;
    const km = parseInt(document.getElementById("slider-km").value);

    // Labels e Dicas
    document.getElementById("valor-km").innerText = `${km.toLocaleString('pt-BR')} km`;
    atualizarTextoLegendaKM(km);

    const ev = DB_ELETRICOS.find(e => e.id === evId);
    const ice = DB_COMBUSTAO.find(i => i.id === iceId);

    // Cálculos
    const mens_ev = calcularMensalidade(ev, prazo, km);
    const mens_ice = calcularMensalidade(ice, prazo, km);

    const energia_ev = calcularEnergiaMensalEV(ev, km, recarga);
    const comb_ice = calcularCombustivelMensalICE(ice, km, combustivel);

    const total_ev = mens_ev + energia_ev;
    const total_ice = mens_ice + comb_ice;

    const diff = total_ev - total_ice;
    const economia = total_ice - total_ev;
    const economiaAcumulada = economia * prazo;

    // Custos Variáveis (R$/km) para Break-even
    const var_ev = energia_ev / km;
    const var_ice = comb_ice / km;
    const diff_fixo = mens_ev - mens_ice;
    const dif_var = var_ice - var_ev;

    let breakeven = 0;
    let breakevenText = "";

    if (dif_var <= 0) {
        breakevenText = "A energia do elétrico não está sendo mais barata que o combustível, então ele não consegue abater a diferença da mensalidade.";
    } else if (diff_fixo <= 0) {
        breakevenText = "A mensalidade do elétrico já é igual ou menor que a do combustão. Ele <strong>já é mais barato</strong> desde o primeiro km rodado!";
    } else {
        breakeven = Math.ceil(diff_fixo / dif_var);
        breakevenText = `Neste cenário, o carro elétrico passa a ser mais barato que o a combustão a partir de <strong>${breakeven.toLocaleString('pt-BR')} km</strong> rodados por mês.`;
    }

    // Atualizar UI - Cards
    document.getElementById("nome-ev").innerText = ev.nome;
    document.getElementById("nome-ice").innerText = ice.nome;
    
    document.getElementById("valor-ev").innerHTML = `${formatarMoeda(total_ev)}<span>/mês</span>`;
    document.getElementById("det-ev").innerText = `Assinatura ${formatarMoeda(mens_ev)} + Energia ${formatarMoeda(energia_ev)}`;
    
    document.getElementById("valor-ice").innerHTML = `${formatarMoeda(total_ice)}<span>/mês</span>`;
    document.getElementById("det-ice").innerText = `Assinatura ${formatarMoeda(mens_ice)} + Combustível ${formatarMoeda(comb_ice)}`;

    // Manchete Efetivo Mensal
    const titulo = document.getElementById("titulo-resultado");
    if (diff < 0) {
        titulo.innerHTML = `Elétrico é <b>${formatarMoeda(Math.abs(diff))} mais barato</b> por mês`;
    } else if (diff > 0) {
        titulo.innerHTML = `Elétrico é <b>${formatarMoeda(diff)} mais caro</b> por mês`;
    } else {
        titulo.innerHTML = `Ambos têm o <b>mesmo custo</b> mensal`;
    }

    // Box Economia Acumulada
    const boxEco = document.getElementById("box-economia");
    const textEco = document.getElementById("texto-acumulado");
    if (economiaAcumulada > 0) {
        boxEco.className = "box-economia";
        document.querySelector(".icone-eco").innerText = "💰";
        textEco.innerHTML = `Em ${prazo} meses, você <strong>economiza ${formatarMoeda(economiaAcumulada)}</strong> optando pelo elétrico.`;
    } else {
        boxEco.className = "box-economia negativo";
        document.querySelector(".icone-eco").innerText = "⚠️";
        textEco.innerHTML = `Em ${prazo} meses, você <strong>gasta ${formatarMoeda(Math.abs(economiaAcumulada))} a mais</strong> optando pelo elétrico.`;
    }

    // Break Even
    document.getElementById("texto-breakeven").innerHTML = breakevenText;
}

// Inicialização
window.addEventListener("DOMContentLoaded", () => {
    carregarOpcoes();
    
    const selEV = document.getElementById("select-ev");
    const selICE = document.getElementById("select-ice");
    const slider = document.getElementById("slider-km");

    // Lógica de pré-seleção ao mudar o elétrico
    selEV.addEventListener("change", (e) => {
        preSelecionarConcorrente(e.target.value);
        calcularTudo();
    });

    // Atualização em inputs normais
    selICE.addEventListener("change", calcularTudo);
    slider.addEventListener("input", calcularTudo);

    // Lógica de Chips (Estilo)
    const chipsRadio = document.querySelectorAll('.chip input[type="radio"]');
    chipsRadio.forEach(radio => {
        radio.addEventListener("change", (e) => {
            // Remove active daquele grupo
            const groupName = e.target.name;
            document.querySelectorAll(`.chip input[name="${groupName}"]`).forEach(r => {
                r.parentElement.classList.remove('active');
            });
            // Add active no selecionado
            e.target.parentElement.classList.add('active');
            calcularTudo();
        });
    });

    // Iniciar
    preSelecionarConcorrente(selEV.value);
    calcularTudo();
});
