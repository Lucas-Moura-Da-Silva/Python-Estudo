maior = masc = menos = 0

while True:
    print('-='*15)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('=-'*15)

    idade = int(input('Idade: '))
    sexo = str(input('Sexo{M/F]: ')).strip().upper()[0]

    if idade > 18:
        maior += 1

    if sexo in 'M':
        masc += 1

    if sexo in 'F':
        if idade < 20:
            menos += 1

    print('=-'*15)
    cont = str(input('Quer continuar?[S/N]: ')).strip().upper()[0]

    if cont == 'N':
        break

print('=-'*15)

print(f'''Total de pessoas com mais de 18 anos: {maior};
Ao todo temos {masc} homem(ns) cadastrados;
E temos {menos} mulher(es) com menos de 20 anos.''')