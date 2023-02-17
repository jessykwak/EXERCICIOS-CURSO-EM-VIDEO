print('=='*9)
print('LOJA DA KWAK')
print('=='*9)
'''
listp = []
continuar = 1
t = g = n = 0
while continuar != 2:

    nome = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o valor do produto: '))
    t += preco
    listp += [preco]
    g = listp.sort
    if preco > 1000:
        n += 1
    continuar = int(input('Digite as opcoes abaixo:\n'
                          '[1] registrar produto\n'
                          '[2] finalizar compra\n'))
    if continuar == 2:
        print('Obrigada pela preferencia! Volte sempre!\n')
        break
    elif 1 != continuar != 2:
        print('OPCAO INVALIDA. TENTE NOVAMENTE')
        break

print(f'O valor final da compra ficou: R$ {t}')
print(f'Temos {n} produtos custam acima de R$ 1000,00')
#print(f'O produto mais barato foi o {}')
'''
total = totmil = menor = cont = 0
barato = ''
while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preco: R$ '))
    cont +=1
    total += preco
    if preco > 1000:
        totmil += 1
    if cont == 1 or preco < menor:
        menor = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Gostaria de continuar? [S/N]')).strip().capitalize()[0]
    if resp == 'N':
        print('Obrigada pela preferencia! Volte sempre!\n')
        break
print(f'O valor final da compra ficou: R$ {total}')
print(f'Temos {totmil} produtos custam acima de R$ 1000,00')
print(f'O produto mais barato foi de {menor:.2f}, no produto {barato}.')