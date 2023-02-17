a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
c = float(input('Digite mais um valor: '))

if a < b+c and b < a+c and c < a+b:
    print(f'O triangulo de lados {a}, {b} e {c} e possivel.')
else:
    print('Um triangulos com essas dimensoes nao e possivel.')
