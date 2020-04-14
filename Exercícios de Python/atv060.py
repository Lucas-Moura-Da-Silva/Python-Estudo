num = contagem = cont = 0

while cont != 999:
    cont = int(input('Digite um número [999 para parar]: '))
    if cont != 999:
        num += cont
        contagem += 1

print('Você digitou {} números e a soma entre eles foi {}'.format(contagem, num))
