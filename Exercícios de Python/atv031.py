print('\033[36m--=\033[m'*17)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

print('\033[36m--=\033[m'*17)

if r1 < r2 + r3  and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[34mOs segmentos acima \033[1;32mPODEM FORMAR\033[m \033[34m um triângulo')
else:
    print('\033[34mOs segmentos acima \033[1;31mNÃO PODEM FORMAR\033[m \033[34m um triângulo')


