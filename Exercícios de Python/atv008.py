preço=float(input('O preço do produto é R$ '))
desconto= preço-(preço*0.05)
print('O preço do produto de R${} com desconto de 5% ficará R${:.2f}'.format(preço, desconto))