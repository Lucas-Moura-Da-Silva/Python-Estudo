n = str(input('Digite o seu sexo [F/M]: ')).upper().strip()[0]

while n != "F" and n != 'M':
    n = str(input('Dados invalidos. Por favor, informar o sexo [F/M]: '))

if n == 'M':
    print('Sexo Masculino registrado com sucesso.')

else:
    print('Sexo Feminino registrado com sucesso.')