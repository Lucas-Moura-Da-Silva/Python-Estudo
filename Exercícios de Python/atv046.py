soma = 0
cont = 0

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[4;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

for c in range(1, 7):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1

print('{}-={}'.format(cores['branco'], cores['limpa'])*30)
print('Você informou {} número(s) {}PARES{} e a soma deles foi {}'.format(cont, cores['vermelho'], cores['limpa'], soma))

