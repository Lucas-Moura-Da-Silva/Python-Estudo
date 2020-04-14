''' matriz = [[],[],[],[],[],[],[],[],[]]

linha = coluna = m = l = c = 0
while m != 9:
    matriz[m].append(int(input(f'Digite um valor para a posição [{l}, {c}]: ')))

    m += 1
    c += 1

    if c == 3:
        l +=1
        c = 0
for z in range(0, 3):
    print(f'{matriz[z]:^5}', end=' ')
print()

for x in range(3, 6):
    print(matriz[x], end=' ')
print()

for v in range(6, 9):
    print(matriz[v], end=' ')'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição[{l}, {c}]: '))

print('=-'*15)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
    print()
print('=-'*15)
