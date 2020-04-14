num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
       'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezesste', 'dezoito', 'dezenove', 'vinte')

while True:
    esc = int(input('Digite um número entre 0 e 20: '))

    while 0 > esc or esc > 20:
        print('-'*40)
        esc = int(input('Tente novamente. Digite um número entre 0 e 20: '))

    if 0 <= esc and esc <= 20:
        print(f'Você digitou o número {num[esc]}')

    print('-'*40)
    sn = str(input('Você quer continuar?[S/N] ')).strip().upper()[0]
    if sn in 'N':
        break

print('-='*20)
print('{:=^40}'.format('O program foi encerrado!'))
print('-='*20)
