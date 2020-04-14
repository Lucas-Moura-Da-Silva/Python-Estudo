lista = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM', 'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR'
         'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR', 'FUTURO')

for n in lista:
    print(f'\nNa palavra {n} temos ', end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')
