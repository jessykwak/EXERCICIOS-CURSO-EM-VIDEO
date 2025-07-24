'''lista1 = []
par = []
impar = []

for c in range(0,7):
    n = int(input('Digite um numero: '))
    if n % 2 ==0:
        par.append(n)
    elif n % 2 != 0:
        impar.append(n)
lista1.append(sorted(par))
lista1.append(sorted(impar))

print(f'num pares: {sorted(par)}')
print(f'num impares: {sorted(impar)}')
print(f'todos os numeros: {lista1}')'''

num = [[],[]]
valor = 0
for c in range(0,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 ==0:
        num[0].append(valor)
    elif valor % 2 != 0:
        num[1].append(valor)
num[1].sort()
num[0].sort()
print(f'num pares: {num[0]}')
print(f'num impares: {num[1]}')
print(f'todos os numeros: {num}')
