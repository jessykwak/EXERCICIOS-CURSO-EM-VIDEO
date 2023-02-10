lista = []
listap = []
listai = []
while True:
    c = int(input('Digite um numero: '))
    lista.append(c)
    d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if 'N' == d:
        break
    while d not in 'SsNn':
        print('OPCCAO INVALIDA.')
        d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
print(f'O numeros digitados foram: {lista}')
for i in lista:
    if i % 2 == 0:
        listap.append(i)
    elif i % 2 != 0:
        listai.append(i)
print(f'O numeros pares sao: {listap}')
print(f'O numeros pares sao: {listai}')