lista1 = []
lista2 = []
max = min = 0
maior = 'a'
menor = 'b'
while True:
    lista2.append(str(input('Digite seu nome: ')).strip().capitalize())
    lista2.append(float(input('Digite seu peso: ')))
    if len(lista1) == 0:
        max = min = lista2[1]
    else:
        if lista2[1] > max:
            max = lista2[1]
        if lista2[1] < min:
            min = lista2[1]
    lista1.append(lista2[:])
    lista2.clear()
    d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while d not in 'SsNn':
        print('OPCCAO INVALIDA.')
        d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if 'N' == d:
        break
print('='*30)
print(f'Foram cadastradas {len(lista1)} pessoas')
print(f'A pessoa de maior peso eh {max}kg, da(o) ',end = '')
for p in lista1:
    if p[1] == max:
        print(f'{p[0]} ',end='')
print()
print(f'A pessoa de menor peso eh {min}kg do(a) ',end ='')
for p in lista1:
    if p[1] == min:
        print(f'{p[0]} ',end='')
print()
