from math import hypot
catadj = float(input('Digite o numero do cateto adjacente: '))
catop = float(input('Digite o número do cateto oposto: '))
hip = hypot(catop, catadj)
print('A hipotenusa do triângulo com cateto adjacente {} e cateto oposto {}, é {:.2f}'.format(catadj, catop, hip))
