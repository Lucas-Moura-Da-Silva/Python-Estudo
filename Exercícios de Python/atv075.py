ficha = []

while True:
    num = float(input('Digite um número: '))

    while num in ficha:
        print('Valor duplicado! Não vou adicionar')
        num = float(input('Digite um número: '))

    ficha.append(num)
    print('Valor adicionado com sucesso...')

    son = str(input('Quer continuar? [S/N]')).strip().upper()[0]

    while son not in 'NS':
        print('Escolha incorreta! ')
        son = str(input('Quer continuar? [S/N]')).strip().upper()

    if son in 'N':
        break
    print('_-'*20)
print('-='*20)
print(f'Você digitou os valores {sorted(ficha)}')