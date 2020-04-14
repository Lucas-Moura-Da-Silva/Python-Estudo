cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[4;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

frase = str(input('Escreva uma frase:')).lower().strip()
palavra = frase.split()
junto = ''.join(frase)
inverso = ''

for letra in range(len(junto)-1, -1, -1):
    inverso+= junto[letra]
    print(inverso)

if junto == inverso:
    print('A palavra {}{}{} é um polindromo.'.format(cores['branco'] ,frase, cores['limpa']))

else:
    print('A palavra não é um polindromo.')