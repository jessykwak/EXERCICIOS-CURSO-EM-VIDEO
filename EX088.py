
from random import sample
d = int(input('Quantos palpites devem ser gerados? (minimo 1 jogo) '))
lista = []
n = []
num = range(1,60)
if d == 0:
    while d == 0:
        str(input('OPCAO INVALIDA'))
        d = int(input('Quantos palpites devem ser gerados? (minimo 1 jogo) '))
else:
    for x in range(0,d):
        n = sample(num,6)
        lista.append(n[:])
        print(f'Jogo {x+1}: {sorted(lista[x])}')

'''

from random import randint
cont = 0
lista = []
jogos = []
print('='*30)
quant = int(input('Quantos jogos vc qr q sejam sorteados? '))
tot = 1
while tot <= quant:
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >=6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('='*5, f'SORTEANDO {quant} JOGOS', '='*5)
for i,l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
#print(f'{"<BOA SORTE>:"^30}')
'''
