num = int(input('Digite um número para ver sua tabuada: '))

print('-='*8)
for c in range(1, 11):
    print('{:2} x {:2} = {:3}'.format(num, c, num*c))
print('-='*8)