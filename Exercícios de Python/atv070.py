from random import randint
total = maior = menor = 0
n = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10),)

print(f'Eu sortei os números: ', end='')
for c in n:
    print(f'{c} ', end='')

while total != 4:
    if total == 0:
        maior = menor = n[0]
    else:
        if n[total] > maior:
            maior = n[total]
        elif n[total] < menor:
            menor = n[total]

    total += 1

print(f'\nO maior valor sorteado foi {maior}')
print(f'O menor valor sorteado foi {menor}')

'''ou pode ser desse modo'''

print(f'O maior valor sorteado foi {max(n)}')
print(f'O menor valor sorteado foi {min(n)}')