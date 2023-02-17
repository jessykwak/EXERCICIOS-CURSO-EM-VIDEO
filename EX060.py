'''n = int(input('Digite um numero: '))

r = 1
count = 1

while count <= n:
    r *= count
    count += 1

print(f'O numero {n}! = {r}')
####################################
m = int(input('Digite um numero: '))

for c in range(1,m):
    m *= c

print(f'O numero {c+1}! = {m}')'''
#####################################
'''from math import factorial
n = int(input('Digite um numero para calcular o fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} eh {f}')'''
#####################################
n = int(input('Digite um numero para calcular o fatorial: '))
c = n
f = 1
print(f'Calculando {n}!')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c>1 else ' = ', end='')
    f *= c
    c -= 1
print(f'O fatorial de {n} eh {f}')
