while True:
    print('='*60)
    f = int(input('Digite um numero positivo e calcularemos sua tabuada: '))
    print('='*60)
    c = 0
    if f < 0:
        print('NUMERO INVALIDO')
        break
    while c < 10 and f > 0:
        c += 1
        p = f*c
        print(f'{f} x {c} = {p}')


OSError
'''
while True:
    print('='*60)
    f = int(input('Digite um numero positivo e calcularemos sua tabuada: '))
    print('='*60)
    c = 0
    if f < 0:
        print('OPCAO INVALIDA. PROGRAMA ENCERRADO.')
        break
    for c in range(1,11):
        print(f'{f} x {c} = {f*c}')
'''