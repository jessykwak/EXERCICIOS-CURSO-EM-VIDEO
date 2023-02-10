'''
x = int(input('Digite um numero: '))
y = int(input('Digite outro numero: '))
w = int(input('Digite mais um numero: '))
z = int(input('Digite mais outro numero: '))
tupla = (x, y, w, z)

par = []
for c in range (0,4):
    if tupla[c] % 2 ==0:
        par += [tupla[c]]
'''

tupla = (int(input('Digite um numero: ')),
         int(input('Digite outro numero: ')),
         int(input('Digite mais um numero: ')),
         int(input('Digite mais outro numero: ')))

print(f'\nOs numeros digitados foram: {tupla}\n')
if 9 in tupla:
    print(f'O numero 9 aparece {tupla.count(9)}x')
else:
    print(f'O numero 9 nao aparece nenhuma vez')
if 3 in tupla:
    k = tupla.index(3) + 1
    print(f'O numero 3 aparece pela 1° vez na {k}° posição')
else:
    print(f'O numero 3 nao aparece em nenhuma posição')
print(f'Os numeros pares sao: ', end='')
for n in tupla:
    if n % 2 ==0:
        print(f'{n} ', end='')
