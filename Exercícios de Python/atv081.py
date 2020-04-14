num = [[], []]

for c in range(0, 7):
    ordem = int(input(f'Digite o {c + 1}º número: '))

    if ordem % 2 == 0:
        num[0].append(ordem)

    else:
        num[1].append(ordem)

print('=-'*22)

num[0].sort()
num[1].sort()

print(f'Os valores pares digitados foram {num[0]}')
print(f'Os valores impares digitados foram {num[1]}')

print('=-'*22)