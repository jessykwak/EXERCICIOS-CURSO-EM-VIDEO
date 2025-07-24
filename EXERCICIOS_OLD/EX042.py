a = float(input('Digite um valor: '))
b = float(input('Digite outro valor: '))
c = float(input('Digite mais um valor: '))

if a < b+c and b < a+c and c < a+b:
    print(f'O triangulo de lados {a}, {b} e {c} e possivel.')

    if a == b == c:
        print('E um triangulo Equilatero!')
    elif a != b != c != a:
        print('E um triangulo Escaleno!')
    elif (a == b != c) or (a == c != b) or (b == c != a):
        print('e um triangulo Isosceles!')

else:
    print('Um triangulos com essas dimensoes nao e possivel.')
