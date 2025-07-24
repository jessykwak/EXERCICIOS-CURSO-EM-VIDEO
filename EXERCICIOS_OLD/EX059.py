from random import random

operacao = 0

while operacao != 5:
    n1 = float(input('Digite um valor: '))
    n2 = float(input('Digite outro valor: '))
    operacao = int(input("Escolha as opções abaixo:\n"
                         "[1] SOMA\n"
                         "[2] MULTIPLICAÇÃO\n"
                         "[3] MAIOR\n"
                         "[4] NOVOS NUMEROS\n"
                         "[5] SAIR DO PROGRAMA\n"))
    if operacao == 1:
        print(f'A soma entre {n1} e {n2} é: {n1+n2}')
    elif operacao == 2:
        print(f'O produto entre {n1} e {n2} é: {n1*n2:.2f}')
    elif operacao == 3:
        if n1 > n2:
            print(f'O maior numero entre {n1} e {n2} é: {n1}')
        elif n2 > n1:
            print(f'O maior numero entre {n1} e {n2} é: {n2}')
        else:
            print('Os numeros possuem valores iguais.')
    elif operacao == 4:
        print(f'{random()*n1*n2:.2f}')
    elif 0 <= operacao > 5:
        print('OPERAÇÃO INVALIDA, TENTE NOVAMENTE.')
