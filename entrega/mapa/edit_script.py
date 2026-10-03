import sys

file_path = 'c:\\Davi\\Ruptura\\ruptura\\entrega\\mapa\\Rota Elétrica MG.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

target = '''  <header>
    <h1>Rota Elétrica MG</h1>
    <p class="sub">Protótipo de planejador de viagem com paradas de recarga, pensado para o assinante de elétrico da Localiza.</p>
  </header>'''

replacement = '''  <header>
    <h1>Rota Elétrica MG</h1>
    <p class="sub">Protótipo de planejador de viagem com paradas de recarga, pensado para o assinante de elétrico da Localiza.</p>
    <div style="margin-top:10px;">
      <a href="http://localhost:8501" target="_blank" class="btn primary" style="text-decoration:none; display:inline-flex; align-items:center; justify-content:center; width:100%;">Ver Simulador de Custos</a>
    </div>
  </header>'''

if target in content:
    content = content.replace(target, replacement)
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Sucesso')
else:
    print('Alvo nao encontrado.')
