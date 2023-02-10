'''lista=[]
for c in range(0,5):
    c = int(input('Digite um numero: '))
    lista.append(c)
m = max(lista)
for t, v in enumerate(lista):
    if max(lista) == v:
        print(f'O maior valor eh {v}, na posicao {t}}')
    elif min(lista) == v:
        print(f'O menor valor eh {v}, na posicao {t}')'''

'''
import operator

lista=[]
for c in range(0,5):
    c = int(input('Digite um numero: '))
    lista.append(c)

index, value = max(enumerate(lista), key=operator.itemgetter(1))
pos, valor = min(enumerate(lista), key=operator.itemgetter(1))

print(f'MAX {value} posicao {index}')
print(f'MIN {valor} posicao {pos}')
'''

lista = []
mai = 0
men = 0

for c in range(0,5):
    lista.append(int(input('Digite um numero: ')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print(f'Voce digitou os valores {lista}')
print(f'O maior valor digitado foi {mai}, nas posicoes: ',end='')
for i,v in enumerate(lista):
    if v == mai:
        print(f'{i} ', end='')
print(f'\nO menor valor digitado foi {men}, nas posicoes: ',end='')
for i,v in enumerate(lista):
    if v == men:
        print(f'{i} ', end='')
