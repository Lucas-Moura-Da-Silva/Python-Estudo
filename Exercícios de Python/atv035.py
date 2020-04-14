from datetime import date

#cores
cores = {'limpa':'\033[m',
         'vermelho':'\033[1;31m',
         'ciano':'\033[1;36m',
         'roxo':'\033[1;35m',
         'azul':'\033[1;34m',
         'amarelo':'\033[1;33m'}

sexo = input('Qual é o seu sexo? ').lower()
ano = int(input('Qual o ano em que você nasceu? '))

#calculos
atual = date.today().year
data = atual - ano
falta = 18 - data
atraso = data - 18
alistameno = ano + 18

#fala
print('{}-=-{}'.format(cores['amarelo'], cores['limpa'])*15)

print('Quem nasceu em {} tem {} anos em {}'.format(ano, data, atual))

print('{}-=-{}'.format(cores['ciano'], cores['limpa'])*15)

#condições
if sexo == 'feminino':
    print('O seu alistamento {}NÃO É OBRIGATORIO{}.'.format(cores['vermelho'], cores['limpa']))

if sexo == 'feminino':
    print('{}-=-{}'.format(cores['roxo'], cores['limpa'])*15)

#condições
if data < 18:
    print('''Ainda falta {} ano(s) para o alistamento.
Seu alistamento será em {}.'''.format(falta, alistameno))
elif data > 18:
    print('''Você já deveria ter se alistado há {} ano(s)
Seu alistamento foi em {}.'''.format(atraso, alistameno))

#condições
if sexo == 'masculino':
    if data == 18:
        print('Você tem que se alistar {}IMEDIATAMENTE{}!!!'.format(cores['vermelho'], cores['limpa']))
else:
    if data == 18:
        print('Caso você queria se alistar este é o ano do seu alistamento.')