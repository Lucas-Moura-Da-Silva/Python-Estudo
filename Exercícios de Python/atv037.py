from datetime import date

ano = int(input('Qual o ano de seu nascimento? '))
atual = date.today().year

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

#calcular
idade = atual - ano

#fala
print(('{}_=_{}'.format(cores['azul'], cores['limpa'] + '{}-=-{}'.format(cores['ciano'],cores['limpa'])))*7)

print('O atleta tem {} anos.'.format(idade))

print(('{}-=-{}'.format(cores['ciano'], cores['limpa'] + '{}_=_{}'.format(cores['azul'],cores['limpa'])))*7)

if idade <= 9:
    print('Classificação:{}MIRIM{}'.format(cores['roxo'], cores['limpa']))

elif idade <= 14:
    print('Classificação:{}INFANTIL{}'.format(cores['ciano'], cores['limpa']))

elif idade <= 19:
    print('Classificação:{}JUNIOR{}'.format(cores['amarelo'], cores['limpa']))

elif idade <= 25:
    print('Classificação:{}SÊNIOR{}'.format(cores['branco'], cores['limpa']))

else:
    print('Classificação:{}MASTER{}'.format(cores['vermelho'], cores['limpa']))
