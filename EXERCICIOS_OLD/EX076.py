print('='*35)
print(f'{"BEM VINDO A LOJIN DA KWAK":^35}')
print('='*35)
'''from tabulate import tabulate

tupla = (('PRODUTO', 'PRECO'), ('prod1', 10), ('prod2', 25), ('prod3', 3))

print(tabulate(tupla))'''
print(f'{"PRODUTO":<28}', end='')
print(f'{"PRECO":<5}')
print('-'*35)
tupla = ('prod0', 3.75, 'prod1', 10.00, 'prod2', 25.00, 'prod3', 3.50)
for n in range(0,len(tupla)):
    if n % 2 == 0:
        print(f'{tupla[n]:.<27}', end='')
    else:
        print(f'R$ {tupla[n]:>5.2f}')
print('-'*35)
