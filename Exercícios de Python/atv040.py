#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'roxo':'\033[1;35m',
         'ciano':'\033[1;36m'}

#nome da loja
print('{}{}{}{}{:^25}{}{}{}{}'.format(cores['azul'], '-=-'*5, cores['limpa'], cores['vermelho'], 'LUCAS LOJAS', cores['limpa'], cores['azul'], '-=-'*5, cores['limpa']))

#preço dos produtos
preço = float(input('Qual é valor da compra? R$'))

print('{}=-={}'.format(cores['azul'], cores['limpa'])*18)

#forma de pagamento
print('''Qual é a forma do pagamento:
{}[1]{} À vista no dinheiro/cheque
{}[2]{} À vista no cartão
{}[3]{} No cartão em 2x
{}[4]{} No cartão em 3x ou mais'''.format(cores['branco'], cores['limpa'], cores['roxo'], cores['limpa'], cores['amarelo'], cores['limpa'], cores['azul'], cores['limpa']))

opção = int(input('Qual a opção? '))

print('{}=-={}'.format(cores['azul'], cores['limpa'])*18)

#condições
if opção == 1:
    print('Sua compra de R${:.2f}, vai custar R${:.2f} no final, com desconto de 10%.'.format(preço, preço - (preço * 0.1)))

elif opção == 2:
    print('Sua compra de R${:.2f}, vai custar R${:.2f} no final, com 5% de desconto.'.format(preço, preço - (preço * 0.05)))

elif opção == 3:
    print('Sua compra de R${:.2f}, com 2 parcelas vai custar R${:.2f} sem juros, no final.'.format(preço, preço))

elif opção == 4:
    parcelas = int(input('Quantas parcelas vai ser? '))
    print('{}=-={}'.format(cores['branco'], cores['limpa'])*18)
    print('Sua compra será parcelada em {}x de R${:.2f} com juros.'.format(parcelas, (preço + (preço * 0.2))/parcelas))
    print('Sua compra de R${:.2f}, vai custar R${:.2f} final.'.format(preço, preço + (preço * 0.2)))