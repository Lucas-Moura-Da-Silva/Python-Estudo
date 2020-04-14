times = ('Palmeiras', 'Atlético-MG', 'Santos', 'Flamengo', 'Internacional', 'Bahia', 'Botafogo', 'São Paulo',
        'Corinthians', 'Atlético-PR', 'Ceará SC', 'Goiás', 'Chapecoense', 'Fortaleza', 'Cruzeiro',
        'Fluminense', 'CSA', 'Grêmio', 'Avaí', 'Vasco da Gama')

print('-='*30)
print(f'A lista de times do brasileirão 2019 é {times[0:20]}')

print('-='*30)
print(f'Os 5 primeiros são {times[0:5]}')

print('-='*30)
print(f'Os 4 últimos são {times[15:20]}')

print('-='*30)
print(f'Times em ordem alfabética: {sorted(times)}')

print('-='*30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')
