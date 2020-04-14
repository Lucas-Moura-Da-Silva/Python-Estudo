salario = float(input('Qual o sálario da funcionario? R$'))

print('\033[34m-=-\033[m'*20)
#calculo do salário
if salario <= 1250:
    aumento = salario + (salario * 0.15)
if salario > 1250:
    aumento = salario + (salario * 0.1)

print('Quem ganhava \033[31mR${:.2f}\033[m vai começar a ganhar \033[35mR${:.2f}'.format(salario, aumento))