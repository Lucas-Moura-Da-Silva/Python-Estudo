num = int(input('\033[4;31mDigite um número qualquer:\033[m '))
nu = num % 2
if nu == 0 :
    print('\033[1;34;40mO número {} é par\033[m'.format(num))
else:
    print('\033[1;30;44mO número {} é impar\033[m'.format(num))