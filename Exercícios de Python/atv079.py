exp = str(input('Digite a expressão: '))
pilha = []

for simb in exp:
    if simb in '(':
        pilha.append("(")
    elif simb in ')':
        if len(pilha) == 0:
            pilha.append(')')
        else:
            pilha.pop()

if len(pilha) == 0:
    print('Sua expressão está correta!!')
else:
    print('Sua expressão está incorreta!!')
