s = 0

for c in range(0,6):
    n = int(input('Digite um numero inteiro: '))
    if n % 2 == 0:
        s += n
print(f'A soma dos numeros pares é {s}')
