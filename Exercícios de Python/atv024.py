from random import randint
import time

num = randint(0, 5)

print('\033[33m--=\033[m'*25)

print('\033[1;34mEstou pensando em um número de 0 a 5. Tente adivinhar...\033[m')

print('\033[33m--=\033[m'*25)

n = int(input('\033[1;33;46mDigite um número:\033[m '))

print('\033[1;31mPROCESSANDO...\033[m')

time.sleep(1)

if n == num:
    print('\033[1;35mVocê acertou, meus PARABENS!!!\033[m')

else:
    print('\033[7;30mVocê errou, eu estava pensando no número {} e você digitou {}\033[m'.format(num, n))
print('\033[33m--=\033[m'*25)
print('{:^75}'.format('\033[1;31mFim\033[m'))
print('\033[33m--=\033[m'*25)
