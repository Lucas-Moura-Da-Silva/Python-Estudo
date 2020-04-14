#cores
cores = {'limpa':'\033[m',
         'vermelho':'\033[1;31m',
         'ciano':'\033[1;36m',
         'roxo':'\033[1;35m',
         'azul':'\033[1;34m'}

#números
x = int(input('Qual é o {}PRIMEIRO{} número? '.format(cores['vermelho'], cores['limpa'])))
y = int(input('Qual o {}SEGUNDO{} número? '.format(cores['ciano'], cores['limpa'])))

print(('{}--={}'.format(cores['roxo'], cores['limpa']) + '{}--={}'.format(cores['azul'], cores['limpa']))*4)

#condição
if x > y:
    print('O {}MAIOR{} número é {}{}{}.'.format(cores['azul'], cores['limpa'], cores['vermelho'], x, cores['limpa']))
elif y > x:
    print('O {}MAIOR{} número é {}{}{}.'.format(cores['azul'], cores['limpa'],cores['ciano'], y, cores['limpa'] ))
else:
    print('Ambos os números {}{}{} e {}{}{} são {}IGUAIS{}.'.format(cores['vermelho'], x, cores['limpa'], cores['ciano'], y, cores['limpa'], cores['roxo'], cores['limpa']))
