n0 = int(input('Digite um número na posição 0: '))
n1 = int(input('Digite um número na posição 1: '))
n2 = int(input('Digite um número na posição 2: '))
n3 = int(input('Digite um número na posição 3: '))
n4 = int(input('Digite um número na posição 4: '))

lista = [n0, n1, n2, n3, n4]

print('-=-'*20)

print(f'Você digitou os valores {lista}')

print('-=-'*20)

print(f'O maior valor digitado foi {max(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == max(lista):
        print(f'{i}... ', end='')
print()

print(f'O menor valor digitado foi {min(lista)} nas posições ', end='')
for i, v in enumerate(lista):
    if v == min(lista):
        print(f'{i}... ', end='')

