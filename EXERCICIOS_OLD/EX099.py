
def maior(num):
    m = max(num)
    print('='*30)
    print(f'Foram imputados {len(num)} numeros')
    print(f'O maior valor informado foi {m}')


lista = []
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while d not in 'SsNn':
        print('OPCCAO INVALIDA.')
        d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if 'N' == d:
        break
maior(lista)

'''
def maior(*num):
    m = max(num)
    print('='*30)
    print(f'Foram imputados {len(num)} numeros')
    print(f'O maior valor informado foi {m}')


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
'''
'''
from time import sleep

def maior(*num):
    cont = maior = 0
    for valor in num:
        print(f'{valor}', end=' ', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'\nForam imputados {len(num)} numeros')
    print(f'O maior valor informado foi {maior}')
    print('=' * 30)


maior(2,9,4,5,7,1)
maior(4,7,0)
maior(1,2)
maior(6)
maior()
'''