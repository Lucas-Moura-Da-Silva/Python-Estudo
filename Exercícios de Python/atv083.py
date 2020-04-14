matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna3 = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição[{l}, {c}]: '))

print('=-'*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('=-'*15)

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
print(f'A soma dos valores pares é {pares}')

coluna3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {coluna3}')

print(f'O maior valor da segunda linha é {max(matriz[1])}')
