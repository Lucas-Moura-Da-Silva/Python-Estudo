quant = 0
resp = 's'
soma = 0

while resp in 'Ss':
    num = int(input('Digite um número: '))
    resp = str(input('Quer continuar?[S/N]: ')).lower().strip()[0]
    quant += 1
    soma += num
    while resp not in 'NnSs':
        resp = str(input('Quer continuar?[S/N]: ')).lower().strip()[0]
    if quant == 1:
        menor = maior = num
    else:
        if maior < num:
            maior = num
        if menor > num:
            menor = num

print('Você digitou {} números e a média foi {}'.format(quant, soma/quant))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))
