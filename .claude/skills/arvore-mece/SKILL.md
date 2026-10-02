---
name: arvore-mece
description: Quebra a Core Question em uma árvore lógica MECE (de Hipóteses/How ou de Problemas/Why) e prioriza em no máximo 3 galhos via Pareto. Use na ETAPA 2 (Enquadrar), depois que a Core Question foi aprovada.
---

# Enquadrar o problema — árvore lógica MECE

Você está na **etapa 2**. Pega a Core Question aprovada e quebra em partes
menores, analisáveis, sem sobreposição e sem buraco.

## Escolha o tipo de árvore
- **Árvore de Hipóteses (How?)** — formula hipóteses de solução a partir da
  Core Question. Os galhos são motivos/razões que respondem a pergunta.
  Use quando o foco é *o que fazer*.
- **Árvore de Problemas (Why?)** — formula perguntas-chave / causas. Os
  galhos são questões de dimensões diferentes. Use quando ainda é preciso
  entender *por que* o problema existe.

Escolha uma. Não misture os dois modelos na mesma árvore.

## A estrutura TEM que ser MECE
- **Mutuamente Excludente (ME):** nenhum overlap entre os galhos. Se duas
  hipóteses se cruzam, você as fundiu ou redefine.
- **Coletivamente Exaustiva (CE):** a soma dos galhos cobre todo o espaço do
  problema. Se existe uma causa plausível fora da árvore, ela está incompleta.
- Em **cada nível** a quebra tem que ser MECE, não só no topo.
- Cada sub-hipótese (galho mais fino) precisa ser **pesquisável** — dá para
  provar verdadeira ou falsa com um dado.

## ⚠️ Pareto: corte para no máximo 3 galhos
Depois de montar a árvore completa e MECE, **priorize**. Use 80/20:
quais 2-3 galhos concentram a maior parte do impacto sobre a Core Question?
Marque só esses como "a analisar". O resto fica documentado mas **não vira
analista**. Abrir 6-8 frentes de análise não aprofunda nada e dilui o pitch.

Critérios de priorização: impacto no objetivo, viabilidade dada a
restrição de tempo, e relevância (o galho realmente destrava a conversão?).

## ⚠️ Regra de dado
A própria escolha dos galhos prioritários tem que se apoiar em evidência
(`[dado:]` / `[benchmark:]`), não em "achismo". Se a priorização é um
palpite do time, marque `[suposição]` e deixe claro — o crítico vai cobrar.

## Formato de saída
```
TIPO DE ÁRVORE: Hipóteses | Problemas
CORE QUESTION: <repete a aprovada>

GALHOS (árvore completa):
  G1. <hipótese/problema>  — [PRIORITÁRIO | fora de escopo] — <justificativa com tag>
    G1.1 <sub, pesquisável>
    G1.2 <sub, pesquisável>
  G2. ...
  ...

CHECK MECE: <uma frase afirmando que não há overlap e que o conjunto é exaustivo>
GALHOS A ANALISAR (≤3): G_, G_, G_
```

## ⚠️ Gate humano — pare aqui
Depois da árvore priorizada, **PARE e peça aprovação humana** da estrutura
e dos ≤3 galhos escolhidos, antes de disparar os analistas. Árvore não-MECE
ou mal priorizada = N analistas produzindo lixo em paralelo.
