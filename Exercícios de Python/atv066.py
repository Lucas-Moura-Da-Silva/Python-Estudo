total = menor = totmil = cont = 0
barato = ' '

print('-='*15)
print('{:^30}'.format('LOJA SUPER BARATÃO'))
print('-='*15)

while True:
    produto = str(input('Nome do Produto: '))
    preço = float(input('Preço: R$'))
    print('-'*30)
    total += preço
    cont += 1

    if cont == 1 or preço < menor:
        menor = preço
        barato = produto

    if preço > 1000:
        totmil += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if resp in 'N':
        break

print('{:-^40}'.format('FIM DO PROGRAMA'))
print(f'''O total da compra foi R${total:.2f}
Temos {totmil} produto(s) custando mais de R$1000,00
O produto mais barato foi {barato} que custa R${menor:.2f}''')