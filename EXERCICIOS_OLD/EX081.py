lista = []
while True:
    c = int(input('Digite um numero: '))
    lista.append(c)
    d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if 'N' == d:
        break
    while d not in 'SsNn':
        print('OPCCAO INVALIDA.')
        d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]

lista.sort(reverse=True)
print(f'foram inseridos {len(lista)} numeros na lista')
print(f'A lista de valores ordenada de forma decrescente eh: {lista}')
if 5 in lista:
    print(f'O numero 5 foi digitado e esta na lista')
else:
    print('O numero 5 nao foi digitado e nao esta na lista')
