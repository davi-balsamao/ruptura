# Simulador Elétrico Web (MVP Dinâmico)

Este é o protótipo do Simulador Elétrico da Localiza Assinatura, desenvolvido inteiramente em **HTML, CSS e JavaScript Vanilla**. O objetivo é oferecer uma experiência de altíssima usabilidade (formato *App-like*), sem depender de infraestrutura de back-end ou instalação de pacotes nesta fase.

## O que o Simulador faz
O simulador foca na conversão do cliente através da comparação financeira direta entre um carro Elétrico e um a Combustão Equivalente.

1. **Questionário App-like:** O cliente escolhe seu cenário via botões interativos (*Chips*) de Prazo, Recarga e Combustível, e um Slider dinâmico para os KMs rodados por mês. Ao escolher o modelo elétrico, o concorrente a combustão é pré-selecionado automaticamente.
2. **Custo Efetivo Mensal:** Soma a mensalidade base da assinatura com a estimativa de gasto em energia/combustível da rotina declarada. Mostra o custo real de rodar com os carros.
3. **Economia Acumulada:** Expande a diferença mensal pelo prazo total do contrato escolhido (ex: 36 meses), gerando impacto financeiro de longo prazo na tomada de decisão.
4. **Ponto de Equilíbrio (Break-even):** Mostra o momento exato (em km/mês) em que a economia gerada pelo menor custo por km do elétrico consegue empatar e superar o custo inicial mais caro de sua mensalidade.

## Como rodar
Por ser **100% estático e *client-side***, o projeto não requer nenhuma instalação, servidor local ou interpretador Python. 

Basta abrir o arquivo principal diretamente no seu navegador de preferência:
**[index.html](file:///c:/Davi/Ruptura/ruptura/entrega/mvp_simulador/index.html)**

## Estrutura do Projeto

- **`index.html`**: A estrutura de marcação da interface do usuário (UI).
- **`style.css`**: A folha de estilos contendo o design moderno, paleta institucional (Verde/Lima Localiza) e design responsivo (Mobile-first).
- **`script.js`**: O motor do simulador. Contém as regras de negócio de variação de preços de franquias e prazos, além do banco de dados interno *mockado* para as simulações Iniciais (Dolphin Mini, GWM Ora 03 e seus pares a combustão).
- **`DAVI.md`**: O dicionário de dados detalhando a taxonomia, os consumos, as tarifas médias nacionais e as matrizes de contratos. Criado para alinhar exatamente o que a engenharia precisará mapear do banco de dados oficial no futuro.
