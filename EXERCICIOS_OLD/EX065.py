'''s = c = m = lista = 0
d = 1
p = 'S'
list = []

while p != 'N':
    c = int(input('Digite um numero inteiro: '))
    s += c
    d += 1
    m = s/(d-1)
    list += [c]
    lista = list.sort()
    p = str(input('Voce gostaria de continuar? [S/N] ')).strip().capitalize()
    if 'N' != p != 'S':
        print('opcao invalida tente novamente\n')

d1 = d-1
print(f'A soma de todos os numeros, deu: {s}')
print(f'Voce digitou {d1} numero(s)')
print(f'A media dos numeros digitados deu {m}')
print(f'O maior numero digitado foi {list[d1-1]}, e o menor foi {list[0]}')'''

resp = 'S'
soma = quant = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um numero: '))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = numbers
        elif num < menor:
            menor = num
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
media = soma/quant
print(f'\nA soma de todos os numeros, deu: {soma}')
print(f'Voce digitou {quant} numero(s)')
print(f'A media dos numeros digitados deu {media}')
print(f'O maior numero digitado foi {maior}, e o menor foi {menor}')
