'''s = float(input('Qual o valor do salario? '))
if s > 1250:
    print(f'O salario com aumento ficara {s*1.1:.2f} reais')
else:
    print(f'O salario com aumento sera de {s*1.15:.2f} reais')'''

s = float(input('Qual o valor do salario? '))
if s <= 1250:
    n = s * 1.15
else:
    n = s * 1.1
print(f'O salario com aumento sera de {n:.2f} reais')

