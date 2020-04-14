#valores
valor = float(input('Qual é o valor da casa? R$ '))
salario = float(input('Qual é o seu salário? R$ '))
anos = int(input('Em quantos anos você ira pagar? '))

#prestação
mensal = float(valor/(anos*12))

#cores
cores = {'limpa': '\033[m',
         'vermelho': '\033[1;31m',
         'amarelo': '\033[1;33;45m',
         'roxo': '\033[1;36m'}

#mensagem
print('Para pagar uma casa de {}R${:.2f}{} em {}{} anos{}'.format(cores['roxo'], valor, cores['limpa'], cores['roxo'], anos, cores['limpa']), end='')
print(' a prestação será de {}R${:.2f}{}.'.format(cores['roxo'], mensal, cores['limpa']))

#condição
if mensal > (salario * 0.3):
    print('O emprestimo {}NÃO{} pode ser {}CONCEDIDO!{}'.format(cores['vermelho'], cores['limpa'], cores['vermelho'], cores['limpa']))

else:
    print('Emprestimo pode ser {}CONCEDIDO!{}'.format(cores ['amarelo'], cores['limpa']))