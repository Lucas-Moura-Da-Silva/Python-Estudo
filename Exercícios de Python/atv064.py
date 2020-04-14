from random import randint
vitorias = 0

print('=-'*15)
print('{:^30}'.format('Jogo do Par e Impar'))
print('=-'*15)

while True:
    jogador = int(input('Digite um número: '))
    computador = randint(0, 10)
    resposta = (jogador + computador)/2
    escolha = ' '

    while escolha not in 'PI':
        escolha = str(input('Par ou Impar[P/I]: ')).strip().upper()[0]

    print('-='*20)
    if escolha == 'P':
        if resposta % 2 == 0:
            print('Você venceu')
            vitorias += 1
        else:
            print('Você perdeu')
            break

    elif escolha == 'I':
        if resposta % 2 != 0:
            print('Você venceu')
            vitorias += 1
        else:
            print('Você perdeu')
            print('-='*20)
            break

    print('-='*20)

print(f'GAME OVER! Você venceu {vitorias} vezes!!')