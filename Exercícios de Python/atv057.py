print('-='*10)
print('Geradora de PA')
print('-='*10)

p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
print('-='*10)

while c != 10:
    print('{}'.format(p), end='→')
    p += r
    c += 1

print('FIM')