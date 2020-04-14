#Escolha do número
num = int(input('Digite um número para convesção: '))

#cores
cores = {'limpa' : '\033[m',
         'vermelho' : '\033[1;31m',
         'azul' : '\033[1;34m',
         'ciano' : '\033[1;36m',
         'roxo' : '\033[1;35m',
         'amarelo' : '\033[1;32m'}

#barra
print('{}--={}'.format(cores['roxo'], cores['limpa'])*20)

#tipos de opções
print('''Escolha uma opção para a conversão:
{}[1]{} conversão em {}BINÁRIO{}
{}[2]{} conversão em {}OCTAL{}
{}[3]{} conversão em {}HEXADECIMAL{}'''.format(cores['vermelho'], cores['limpa'], cores['vermelho'], cores['limpa'], cores['azul'],cores['limpa'], cores['azul'], cores['limpa'], cores['ciano'], cores['limpa'], cores['ciano'], cores['limpa']))

#escolha da opção
op = int(input('Sua opção é: '))

#barra
print('{}--={}'.format(cores['roxo'], cores['limpa'])*20)

#condição
if op == 1:
    print('A conversão de {}{}{} para {}BINÁRIO{} é {}{}{}'.format(cores['amarelo'], num, cores['limpa'], cores['vermelho'], cores['limpa'], cores['roxo'], bin(num)[2:], cores['limpa']))

elif op == 2:
    print('A conversão de {}{}{} para {}OCTAL{} é {}{}{}'.format(cores['amarelo'], num, cores['limpa'],  cores['azul'], cores['limpa'], cores['roxo'], oct(num)[2:], cores['limpa']))

elif op == 3:
    print("A conversão de {}{}{} para {}HEXADECIMAL{} è {}{}{}".format(cores['amarelo'], num, cores['limpa'], cores['ciano'], cores['limpa'], cores['roxo'], hex(num)[2:], cores['limpa']))

else:
    print('Opção invalida. Tente novamente.')
