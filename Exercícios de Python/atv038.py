r1 = int(input('Primeiro Segmento: '))
r2 = int(input('Segundo Segmento: '))
r3 = int(input('Terceiro Segmento: '))

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

print('{}-=-{}'.format(cores['amarelo'], cores['limpa'])*15)

if r1 < r2 + r3  and r2 < r1 + r3 and r3 < r1 + r2:
#print('Os segmentos acima PODEM FORMAR um triangulo', end='')

    if r1!=r2 and r2!=r3 and r3!=r1: #ou pode ser r1==r2==r3
        print('Os segmentos acima {}PODEM FORMAR{} um triângulo {}ESCALENO!{}'.format(cores['azul'], cores['limpa'], cores['amarelo'], cores['limpa']))

    elif r1!=r2 or r2!=r3 or r3!=r1: #ou pode ser r1!=r2!=r31=r1
        print('Os segmentos acima {}PODEM FORMAR{} um triângulo {}ISOCELES!{}'.format(cores['azul'], cores['limpa'], cores['branco'], cores['limpa']))

    else:
        print('Os segmentos acima {}PODEM FORMAR{} um triângulo {}EQUILATERO!{}'.format(cores['azul'], cores['limpa'], cores['roxo'], cores['limpa']))

else:
    print('Os segmentos acima {}NÃO PODEM FORMAR{} um triângulo!'.format(cores['vermelho'], cores['limpa']))