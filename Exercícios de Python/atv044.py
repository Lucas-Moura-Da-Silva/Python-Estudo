s = 0
d = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        d = d + 1
        s = s + c

print('A somatoria dos {} números de 1 a 500 multiplos de 3 são {}'.format(d, s))