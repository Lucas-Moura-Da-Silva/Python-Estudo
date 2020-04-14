variaveis = []
par = []
impar = []

while True:
    variaveis.append(int(input('Digite um número:')))
    res = input('Você quer continuar?[S/N]').upper().strip()[0]

    while res not in 'SN':
        res = input('Resposta invalida! Você quer continuar?[S/N]').upper().strip()[0]

    if res in 'N':
        break

print('=-'*30)

print(f'A sua lista {variaveis}')

for c in range(len(variaveis)):
    if variaveis[c] % 2 == 0:
        par.append(variaveis[c])
    else:
        impar.append(variaveis[c])

print(f'A lista com os números par {par}')

print(f'A lista com os números impares {impar}')