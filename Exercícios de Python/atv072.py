listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.35,
            'Canetas', 22.30,
            'Livro', 34.90)

print('-'*41)
print('{:^41}'.format("LISTAGEM DE PREÇOS"))
print('-'*41)

for n in range(0, len(listagem)):
    if n % 2 == 0:
        print('{:.<32}R$'.format(listagem[n]), end='')
    elif n % 2 == 1:
        print('{:>7.2f}'.format(listagem[n]))

print('-'*41)
