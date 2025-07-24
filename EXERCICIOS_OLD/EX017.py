import math

co = float(input('Dimensão do cateto oposto: '))
ca = float(input('Dimensão do cateto adjacente: '))
h = math.sqrt(ca**2 + co**2)
h2 = math.hypot(ca,co)

print(f'A hipotenusa do triangula de dimensões {co} e {ca} é de: {h:.2f}')
print(f'A hipotenusa do triangula de dimensões {co} e {ca} é de: {h2:.2f}')