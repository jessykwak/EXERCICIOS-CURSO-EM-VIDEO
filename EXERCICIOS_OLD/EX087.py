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
listag.append(lista1)
listag.append(lista2)
listag.append(lista3)
print(lista1)
print(lista2)
print(lista3)
s = 0
for n in listag:
    if n % 2 ==0:
        s += n
print(f'A soma dos um pares eh {s}')'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
s = s1 = max = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor para a posicao [{l},{c}]: '))
print('='*30)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^3}]', end='')
        if matriz[l][c] % 2 == 0:
            s += matriz[l][c]
    print()
print(f'A soma dos um pares eh {s}')
for l in range(0,3):
    s1 += matriz[l][2]
print(f'A soma da 3° coluna eh {s1}')
for c in range(0,3):
    if c == 0:
        max = matriz[1][c]
    elif matriz[1][c] > max:
        max = matriz[1][c]
print(f'O maior valor da 2 linha eh: {max}')