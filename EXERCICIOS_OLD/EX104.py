'''def leiaInt(num, flag = True):
    if num.isnumeric():
        num = int(num)
        flag == True
        return f'Voce digitou o numero {num}.'
    else:
        flag == False
        return 'ERRO! DIGITE UM NUMERO INTEIRO.'


n = leiaInt(input('Digite um numero: '))
print(f'{n}')'''


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('ERRO! digite um numero inteiro valido')
        if ok:
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'voce digitou o numero {n}')

