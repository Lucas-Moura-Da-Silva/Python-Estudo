cores = {'limpa':'\033[m',
         'vermelho':'\033[31m',
         'azul':'\033[1;34m',
         'amarelo':'\033[1;33m',
         'roxo':'\033[1;35m'}

from datetime import date
ano = int(input('{}Que ano quer analisar? Coloque 0 para analisar o ano atual:{} '.format(cores['amarelo'], cores['limpa'])))

print('{}--={}'.format(cores['roxo'], cores['limpa'])*25)

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100!= 0 or ano % 400 == 0:
    print('O ano de {}{}{} é {}BISSEXTO{}'.format(cores['amarelo'], ano, cores['limpa'], cores['azul'], cores['limpa']))

else:
    print('O ano de {}{}{} {}não é BISSEXTO{}'.format(cores['amarelo'], ano, cores['limpa'], cores['vermelho'], cores['limpa']))