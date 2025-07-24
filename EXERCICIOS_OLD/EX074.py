from random import randint
from time import sleep

tupla = (randint(0,9999), randint(0,9999), randint(0,9999), randint(0,9999), randint(0,9999))
'''
print(f'Os numeros gerados foram {tupla}')
print('processando...')
sleep(1)
print(f'O maior numero gerado foi {sorted(tupla)[4]} e o menor numero {sorted(tupla)[0]}')
'''
print('Os valores sorteados foram: ', end='')
for n in tupla:
    print(f'{n} ', end='')
print(f'\nO maior numero gerado foi {max(tupla)} e o menor numero {min(tupla)}')
