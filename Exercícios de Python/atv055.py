import time

primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))

m = 0

print('Escolha uma opção: ')
print('-=-'*12)

while m != 5:
    print('''[1]Soma
[2]Multiplicar
[3]Maior 
[4]Novos números
[5]Sair do programa''')

    m = int(input('>>>Qual sua opção? '))
    if m == 1:
        print('-_-' * 10)
        print('A soma dos números {} e {} é {}'.format(primeiro, segundo, primeiro+segundo))
        print('_-_' * 10)

    elif m == 2:
        print('-_-' * 10)
        print('A multiplicação dos números {} e {} é {}'.format(primeiro, segundo, primeiro * segundo))
        print('_-_' * 10)

    elif m == 3:
        print('-_-' * 10)
        if primeiro > segundo:
            print('Entre os números {} e {}, o maior é {}'.format(primeiro, segundo, primeiro))
        elif segundo > primeiro:
            print('Entre os números {} e {}, o maior é {}'.format(primeiro, segundo, segundo))
        else:
            print('Ambos são iguais')
        print('_-_'*10)

    elif m == 4:
        print('-_-' * 10)
        print('Informe os novos números')
        primeiro = int(input('Primeiro valor: '))
        segundo = int(input('Segundo valor: '))
        print('_-_' * 10)

    elif m == 5:
        print('-_-' * 10)
        print('Finalizando...')
        time.sleep(2)
        print('-=-'*12)
        print('Fim do programa! Volte sempre!')

    else:
        print('-_-' * 10)
        print('Opção invalida')
        print('_-_' * 10)
