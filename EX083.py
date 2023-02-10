expr = str(input('Digite uma expressão matematica: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print(f'Expressão válida.')
else:
    print(f'Expressão INválida.')
    