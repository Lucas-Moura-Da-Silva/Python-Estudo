a = int(input('\033[35mPrimeiro valor: '))
b = int(input('\033[36mSegundo valor: '))
c = int(input('\033[37mTerceiro valor: '))

print('\033[1;34m-\033[m'*25)

#menor valor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

#maior valor
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

print('\033[1;31m O menor valor é {}'.format(menor))

print('\033[1;34m-\033[m'*25)

print('\033[1;32m O maior valor é {}'.format(maior))

