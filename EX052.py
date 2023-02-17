n = int(input('Digite um numero inteiro: '))

if n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0 or (n == 2 or n == 3 or n == 5 or n == 7):
    print('Esse numero eh primo!')
else:
    print('Esse numero nao eh primo')
