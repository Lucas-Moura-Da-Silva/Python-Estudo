pessoas = list()
peso = list()
pesadas = list()
pesados = list()
leves = list()
leve = list()
menor = maior = 0

while True:
    pessoas.append(str(input('Nome: ')).capitalize().strip())
    pessoas.append(int(input('Peso: ')))
    peso.append(pessoas[:])
    pessoas.clear()
    perg = str(input('Quer continuar?[S/N]')).strip().upper()[0]

    while perg not in 'SN':
        perg = str(input('Ocorreu um erro! Quer continuar?[S/N]')).strip().upper()[0]

    if perg in 'N':
        break

for c in peso:
    if c[1] > maior and c != peso[0]:
           del pesados[0]
    if c[1] >= maior:
        pesadas.append(c)
        maior = c[1]
        pesados.append(c[0])

    if c[1] < menor and c != peso[0]:
        del leve[0]
    if c == peso[0]:
        leves.append(c)
        menor = c[1]
    elif c[1] <= menor:
        leves.append(c)
        menor = c[1]
        leve.append(c[0])

print(f'Ao todo foram cadastrados {len(peso)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de {pesados}')
print(f'O menor peso foi de {menor}Kg. Peso de {leve}')
