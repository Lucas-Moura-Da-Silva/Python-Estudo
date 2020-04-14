print('=-'*20)
print('{:^40}'.format('bANCO DO LUCÃO'))
print('-='*20)

retirada = int(input('Que valor você quer retirar? R$'))

ced = 50
totalced = 0

while True:
    if retirada >= ced:
        retirada -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')

        totalced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1

        if retirada == 0:
            break

print('='*40)
print('Volte sempre ao BANCO DO LUCÃO! Tenha um bom dia!')