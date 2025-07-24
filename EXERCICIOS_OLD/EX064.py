s = d = 0
c = int(input('Digite um numero inteiro: '))
while c != 999:
    s += c
    d += 1
    c = int(input('Digite um numero inteiro: '))
print(f'A soma de todos os numeros menos 999, deu: {s}')
print(f'Voce digitou {d} numero(s) antes do 999')

'''s = d = c = 0

while c != 999:
    c = int(input('Digite um numero inteiro: '))
    s += c
    d += 1
    
print(f'A soma de todos os numeros menos 999, deu: {s-999}')
print(f'Voce digitou {d-1} numero(s) antes do 999')'''