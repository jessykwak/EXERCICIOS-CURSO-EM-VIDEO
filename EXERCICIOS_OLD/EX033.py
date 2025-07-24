'''a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite mais um numero: '))

list=[a,b,c]
print(f'Os numeros sao: {list}')

x = sorted(list)

print(f'O maior numero e {x[2]}')
print(f'O menor numero e {x[0]}')'''

a = int(input('Digite um numero: '))
b = int(input('Digite outro numero: '))
c = int(input('Digite mais um numero: '))
#verificando quem e o menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print(f'o menor valor digitado foi {menor}')

maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print(f'o maior valor digitado foi {maior}')