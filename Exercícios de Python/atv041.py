from random import randint
import emoji
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

#itens
itens = ('Pedra', 'Papel', 'Tesoura')
num = randint(0, 2)
act = str(input('eae man! Bora jogar?[S/N] ')).upper()

#condições
if act == 'N':
    print((emoji.emojize(':broken_heart: Que pena. Então deixa para a proxima...')))

if act == 'S':
    print('''Então escolha uma opção:
{}[0]{} PEDRA
{}[1]{} PAPEL
{}[2]{} TESOURA'''.format(cores['vermelho'], cores['limpa'], cores['branco'], cores['limpa'], cores['roxo'], cores['limpa']))

    print('{}[-]{}'.format(cores['azul'], cores['limpa'])*9)

    esc = int(input('Qual opção escolheu? '))

    print('{}[-]{}'.format(cores['azul'], cores['limpa'])*9)

    print('JO')
    time.sleep(0.7)
    print('KEM')
    time.sleep(0.8)
    print('PO')
    time.sleep(0.9)

    print('{}-={}'.format(cores['ciano'], cores['limpa'])*14)

    print('''O computador jogou {}{}{}
E o jogador jogou {}{}{}.'''.format(cores['amarelo'] ,itens[num], cores['limpa'], cores['amarelo'], itens[esc], cores['limpa']))

    print('{}-={}'.format(cores['ciano'], cores['limpa'])*14)

    if esc == 0 and num == 1 or esc == 1 and num == 2 or esc == 2 and num == 0:
        print(emoji.emojize('Você perdeu!:tongue:'))

    elif esc == num:
        print(emoji.emojize('Parece que o jogo empato!:eyes:'))

    elif esc == 0 and num == 2 or esc == 1 and num == 0 or esc == 2 and num == 1:
        print(emoji.emojize('PARABENS!! Você ganhou.:balloon:'))
