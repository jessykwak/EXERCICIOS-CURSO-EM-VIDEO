'''listag = []
lista1 = []
lista2 = []
lista3 = []

for n in range(0,3):
    listag.append(int(input(f'Digite um valor para [0, {n}]: ')))
    lista1.append(listag[:])
    listag.clear()
for n in range(0, 3):
    listag.append(int(input(f'Digite um valor para [1, {n}]: ')))
    lista2.append(listag[:])
    listag.clear()
for n in range(0, 3):
    listag.append(int(input(f'Digite um valor para [2, {n}]: ')))
    lista3.append(listag[:])
    listag.clear()

print(lista1)
print(lista2)
print(lista3)'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posicao [{l},{c}]: '))
print('='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^3}]', end='')
    print()
