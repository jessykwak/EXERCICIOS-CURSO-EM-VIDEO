def leiaInt(num, flag = True):
    try:
        int(num)
    except ValueError:
        flag = False
        
    if flag:
        return f'Voce digitou o numero {num}.'
    else:
        return 'ERRO! DIGITE UM NUMERO INTEIRO.'


while True:
    n = leiaInt(input('Digite um numero: '))
    if 'ERRO!' not in leiaInt(n):
        print(f'{n}')
        break
    else:
        print(f'{n}')

