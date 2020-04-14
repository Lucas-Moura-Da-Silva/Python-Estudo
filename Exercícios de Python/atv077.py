lista = []

while True:
    lista.append(int(input('Digite um número para ser adicionado na lista: ')))
    

    per = input('Você quer continuar? [S/N]').strip().upper()[0]

    while per not in 'SN':
        per = input('Resposta invalida!! Você quer continuar? [S/N]').strip().upper()[0]

    if per in 'N':
        break

print('=-'*30)

print(f'Foram adicionados {len(lista)} elementos')
lista.sort(reverse=True)
print(f'A ordem da lista em ordem decrescente foi {lista}')

if 5 in lista:
    print('O valor 5 foi encontrado na lista!')
else:
    print('O valor 5 não foi encontredo na lista!')