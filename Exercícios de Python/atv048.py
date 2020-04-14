num = int(input('Digite um número: '))
to = 0

print('\033[34m-='*20)

for c in range(1, num+1):
    if num % c == 0:
        print('\033[31m', end='')
        to += 1
    else:
        print('\033[32m', end='')
    print('{}'.format(c), end=' ')

print('\n\033[mO número {} foi divisivel {} vezes.'.format(num, to))

if to == 2:
    print('Portando ele é \033[1;31mPRIMO.')
else:
    print('Portanto ele \033[1;35mNÃO É PRIMO.')