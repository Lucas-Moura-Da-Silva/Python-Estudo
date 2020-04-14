#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[4;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

print('\n')
print('{}={}'.format(cores['azul'], cores['limpa'])*30)
print('{}{:^30}{}'.format(cores['vermelho'], '10 TERMOS DE UM PA', cores['limpa']))
print('{}={}'.format(cores['azul'], cores['limpa'])*30)
print('\n')

p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
d = p + (10-1)*r

print('{}-={}'.format(cores['amarelo'], cores['limpa'])*30)

for c in range(p, d+1, r):
    print('{}'.format(c), end=' → ')

print('FIM')

print('{}-={}'.format(cores['amarelo'], cores['limpa'])*30)