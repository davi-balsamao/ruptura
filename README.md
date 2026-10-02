# Máquina de Problem Solving — RUPTURA 2026 (Case 1 Localiza)

Pipeline de agentes do Claude Code que replica o método da EloGroup
(**Definir → Enquadrar → Priorizar/Analisar → Sintetizar**) para resolver
um case de consultoria em grupo, com um líder que comanda, analistas em
paralelo e um crítico que valida em loop.

> Isto **não** é um gerador de código. A entrega é uma recomendação
> estruturada + pitch. Os agentes mapeiam nas etapas do método, não em
> camadas de software.

---

## ⚠️ LEIA ISTO ANTES DE QUALQUER COISA — os 4 pontos cegos

A máquina foi desenhada em torno de quatro falhas que **derrubam** um case.
Elas estão codificadas como regras dentro de cada agente, mas você precisa
entender por que existem, senão vai desligá-las na pressão da madrugada.

### 1. Alucinação de dado — o inimigo nº 1
Agente de IA inventa estatística com confiança total. Num case que vive de
número (95% de awareness, "endereça só 1 das 5 preocupações"), um dado
falso no pitch e o jurado te desmonta.

**Mecanismo de defesa:** existe uma **fonte única da verdade** em
`case/dados-case1.md`. Toda afirmação de um analista tem que carregar uma
tag de origem:
- `[dado: dados-case1.md#id]` → veio do dossiê do case
- `[benchmark: fonte/url]` → veio de fora e é verificável
- `[suposição]` → é palpite do time, assumido explicitamente

O **crítico reprova qualquer número sem tag** `[dado:]` ou `[benchmark:]`, e
sinaliza toda `[suposição]` que sustenta uma conclusão. Não relaxe essa
regra — ela é o motivo da máquina existir.

### 2. Garbage in — problema mal definido mata tudo
O próprio método diz: *"a definição correta do problema determinará o
sucesso ou fracasso"*. Se a Core Question ou a árvore saírem erradas, 8
analistas em paralelo só produzem lixo mais rápido.

**Mecanismo de defesa:** as etapas **Definir** e **Enquadrar** têm um
**gate humano obrigatório**. O `lider-caso` para e espera você (e o time)
aprovarem a Core Question e a árvore MECE **antes** de qualquer analista
rodar. Não pule esse aceite. É o passo mais barato e o mais importante.

### 3. Pareto nas hipóteses — menos galhos, mais fundo
Juiz premia insight e narrativa, não volume de análise. Oito hipóteses
rasas perdem para três que movem o ponteiro.

**Mecanismo de defesa:** o `lider-caso` é instruído a **priorizar e cortar
a árvore para no máximo 3 galhos** antes do fan-out, usando 80/20. Se você
se pegar abrindo o 6º analista, parou de fazer consultoria e virou
fazenda de texto.

### 4. Humano vs. agente — onde cada um ganha
O julgamento humano decide em **Definir**, **Enquadrar** e **Sintetizar**.
O trabalho de agente é o fan-out braçal do **Analisar** (coletar e cruzar
dado). Vocês são 4 pessoas: gastem o cérebro de vocês nas pontas, deixem o
meio para os agentes.

---

## Estrutura dos arquivos

```
ruptura-agentes/
├── README.md                      ← você está aqui
├── PLAYBOOK.md                    ← o passo a passo do loop na madrugada
├── case/
│   └── dados-case1.md             ← FONTE ÚNICA DA VERDADE (dados reais do case)
└── .claude/
    ├── skills/
    │   ├── definir-scq/SKILL.md           ← método da etapa 1
    │   ├── arvore-mece/SKILL.md           ← método da etapa 2
    │   └── sintese-piramide-scr/SKILL.md  ← método da etapa 4
    └── agents/
        ├── lider-caso.md          ← orquestrador (etapas 1, 2 e comando do loop)
        ├── analista.md            ← worker paralelo (etapa 3, 1 por galho)
        ├── critico-mece.md        ← o gate de validação (read-only)
        └── sintetizador.md        ← monta a pirâmide e o pitch (etapa 4)
```

## Como instalar
1. Copie a pasta `.claude/` para a raiz do repositório do seu grupo.
2. Copie `case/` junto. No dia, substitua `dados-case1.md` pelos dados do
   case que você for atacar (já vem preenchido com o Case 1 da Localiza
   como teste).
3. Abra o Claude Code na raiz do projeto. Os agentes aparecem para o
   comando `/agents` e as skills ficam disponíveis.

## Como rodar
Siga o `PLAYBOOK.md`. Resumo:
1. `definir-scq` → Core Question → **você aprova**.
2. `arvore-mece` → árvore de hipóteses MECE, cortada em ≤3 galhos → **você aprova**.
3. Dispare N `analista` em paralelo (1 por galho).
4. `critico-mece` valida cada análise → aprovado ou re-despacho (loop ≤3).
5. `sintetizador` → pirâmide SCR + roteiro do pitch.

## Teste ANTES de sexta
Rode o pipeline inteiro no Case 1 (que já está em `case/`) hoje. O objetivo
não é a resposta — é descobrir onde a máquina trava **sem** a pressão do
relógio. Chegue sexta só trocando o dossiê.
