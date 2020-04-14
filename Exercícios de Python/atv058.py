print('-='*20)
print('{:^40}'.format('Geradora de PA'))
print('-='*20)

p = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
total = 0
mais = 10

while mais != 0:
    total += mais
    print('-='*20)
    while c <= total:
        print('{}'.format(p), end='→')
        p += r
        c += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print('-='*24)
print('Progressão finalizada com {} termos mostrados.'.format(total))
