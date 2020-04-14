print('Sequência de Fibonacci')
print('-'*30)

seq = int(input('Quantos termos você quer ver? '))
t1 = 0
t2 = 1
c = 2

print('-='*15)
print('{} → {} → '.format(t1, t2), end='')

while c != seq:
    t3 = t1 + t2
    print('{} → '.format(t3), end='')
    c += 1
    t1 = t2
    t2 = t3

print('FIM')

print('-='*15)