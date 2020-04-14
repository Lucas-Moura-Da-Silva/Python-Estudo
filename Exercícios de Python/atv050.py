from datetime import date

cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[4;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

atual = date.today().year
maior = 0
menor = 0

for c in range(1, 8):
    ano = int(input('Em qual ano a {}ª pessoa nasceu?'.format(c)))
    idade = atual - ano

    if idade >= 18:
        maior+= 1
    else:
        menor+= 1

print('\n')
print('''Temos {}{} pessoa(s){} com maior idade.\n
Já com menor idade temos {}{} pessoa(s){}'''.format(cores['vermelho'], maior, cores['limpa'], cores['azul'], menor, cores['limpa']))