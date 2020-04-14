massa = float(input('Qual é sua massa corporal?(Kg) '))
altura = float(input('Qual é sua altura?(m) '))

IMC = (massa)/altura**2

print('O IMC dessa pessoa é de {:.2f}.'.format(IMC))

if IMC <= 18.5:
    print('Você está ABAIXO DO PESO ideal!')

elif 25 >= IMC > 18.5:
    print('PARABÉNS, você está na faixa de PESO IDEAL!')

elif 30 >= IMC > 25:
    print('Você está em SOBREPESO!')

elif 40 >= IMC >30:
    print('Você está em OBESIDADE!')

else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')