while True:
    vezes = 1
    n = int(input('Quer ver a tabuada de qual número? '))
    print('-'*40)

    if n < 0:
        print('Programa tabuada encerrada. Volte sempre!')
        break

    while vezes <= 10:
        print(f'{vezes:^2} x {n:^3} = {vezes * n}')
        vezes += 1

    print('-'*40)