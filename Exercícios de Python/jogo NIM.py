print('Bem-vindo ao jogo NIM! Escolha:')

print('1 - para jogar isolado \n2 - para jogar um campeonato')

def partida(n, m):
    if n < 0 or m < n:
        print('Escolha de parâmetros errada.')
    else:
        if n % (m+1) == 0:
            print('Você começa')

        else:
            print('Computdor começa')

def usuario_escolhe_jogada(z):
    if z > m or z > n:

