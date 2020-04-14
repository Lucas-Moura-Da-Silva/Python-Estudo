lista = []

for c in range(0,5):
    n = int(input('Digite um número: '))

    if c == 0:
        lista.append(n)
        print(f'número {n} foi adicionado na posição 0')

    elif n > lista[-1]:
        lista.append(n)
        print(f'O numero {n} foi adicionado na ultima possição.')

    else:
        for i, v in enumerate(lista):
            if n <= v:
                lista.insert(i, n)
                print(f'O número {n} foi adicionado na posição {i}')
                break

print('-='*30)

print(f'A lista em ordem será: {lista}')
