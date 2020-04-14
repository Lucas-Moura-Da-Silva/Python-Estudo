dias = int(input('Quantos dias foi alugado? '))
km = float(input('Quantos Km foram rodados? '))
aluguel = (dias * 60) + (km * 0.15)
print('O preço total a ser pago é R${:.2f}'.format(aluguel))