km = float(input("Qual a distancia da viajem em Km? "))
if km <= 200:
    preço = km * 0.50
else:
    preço = km * 0.45
print('E o preço de seu a viajem é de R${:.2f}'.format(preço))

