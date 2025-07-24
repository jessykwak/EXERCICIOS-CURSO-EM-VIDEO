lista=[]
while True:
    c = int(input('Digite um numero: '))
    if c in lista:
        print('numero ja inputado')
    else:
        lista.append(c)
    d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if d in 'SsNn':
        if 'N' == d:
            break
    while d not in 'SsNn':
        print('OPCCAO INVALIDA.')
        d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

print(f'Os valores inputados foram: {sorted(lista)}')