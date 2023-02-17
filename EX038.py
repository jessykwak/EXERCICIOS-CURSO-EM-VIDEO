n1 = int(input('Digite um numero inteiro qualquer: '))
n2 = int(input('Digite outro numero inteiro qualquer: '))

if n1>n2:
    print(f'O primeiro numero, {n1}, e maior que o segundo numero, {n2}.')
elif n1<n2:
    print(f'O segundo numero, {n2}, eh maior que o primeiro numero, {n1}.')
else:
    print(f'O primeiro numero, {n1}, possui o mesmo valor do segundo numero, {n2}.')

