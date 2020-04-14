from random import randint
import time

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[4;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

num = randint(0,10)

print('Olá, eu estou pensando em um número de 0 a 10')
print('Será que consegue advinhar qual foi?')

print('\n')
sorte = int(input('Qual é seu palpite?'))
print('{}Analisando...{}'.format(cores['amarelo'], cores['limpa']))
time.sleep(1.5)
vezes = 1

while sorte != num:
    vezes+= 1
    print('\n')
    if sorte < num:
        print('É um número {}mais alto!{} Tente de novo.'.format(cores['vermelho'], cores['limpa']))
    if sorte > num:
        print('É um número {}mais baixo!{} Tente de novo'.format(cores['roxo'], cores['limpa']))
    sorte = int(input('Qual é seu palpite?'))
    print('{}Analisando...{}'.format(cores['amarelo'], cores['limpa']))
    time.sleep(1.5)

print('\n')
print('{}-=-{}'.format(cores['verde'], cores['limpa'])*12)
print('{}Parabens!!!{} Você acertou na {}{} tentativa!{}'.format(cores['ciano'], cores['limpa'],cores['azul'], vezes, cores['limpa']))
print('{}Eu estava pensado no número {}{}'.format(cores['branco'], num, cores['limpa']))
print('{}-=-{}'.format(cores['verde'], cores['limpa'])*12)
