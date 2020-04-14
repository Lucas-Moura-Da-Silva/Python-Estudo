ano = 0
mioridade = 0
hn = ''
menoridade = 0

for i in range(1,5):
    print('-=-=-{}ªPessoa-=-=-'.format(i))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).lower()

    ano+= idade

    if sexo in 'm':
        if i == 1:
            maioridade = idade
            hn = nome
        else:
            if idade > maioridade:
                maioridade = idade
                hn = nome

    if sexo in 'f':
        if idade < 20:
            menoridade+= 1

print('A media da idade do grupo é de {} anos.'. format(ano/4))

if sexo in 'm':
    print('O homem mais velho é o {}, com idade de {} anos.'.format(hn, maioridade))
else:
    print('Não existe nenhum homem neste grupo.')

if sexo in 'f':
    print('Existe nesse grupo {} mulher(es) com idade menor de 20 anos.'.format(menoridade))
else:
    print('Não existe nenhuma mulher neste grupo.')