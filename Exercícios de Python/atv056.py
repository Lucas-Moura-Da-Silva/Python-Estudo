print('Digite um número para')
num = int(input('Calcular seu Fatorial: '))
fat = 1
print('{}! = '.format(num), end = '')

'''while num > 0:
    print('{}'.format(num), end = '')
    print(' x ' if num > 1 else ' = ', end = '')
    fat *= num
    num -= 1

print('{}'.format(fat))'''

while num > 0:
    for c in range(1, num+1):
        print('{}'.format(num), end='')
        print(' x ' if num > 1 else ' = ', end='')
        fat *= num
        num -= 1

print('{}'.format(fat))