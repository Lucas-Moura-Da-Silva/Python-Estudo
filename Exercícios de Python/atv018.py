nome = str(input('Digite seu nome completo: '))
nome = nome.lstrip()
print(nome.upper())

print('-'*25)

print(nome.lower())

print('-'*25)

print('Seu nome contém {} letras'.format(len(''.join(nome.split()))))

print('-'*25)

print('Seu primeiro nome tem {} letras'.format(len(nome.split()[0])))
