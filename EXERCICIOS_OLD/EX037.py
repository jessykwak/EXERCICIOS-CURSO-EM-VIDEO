n = int(input('Digite um numero inteiro qualquer: '))
c = int(input('Selecione a base de conversao [1] - para binario [2] - para octal ou [3] - para hexadecimal: '))

if c == 1:
    print(f'{n} convertido para BINARIO, fica igual a: {bin(n)[2:]}.')
elif c == 2:
    print(f'{n} convertido para OCTAL, fica igual a: {oct(n)[2:]}.')
elif c == 3:
    print(f'{n} convertido para HEXADECIMAL, fica igual a: {hex(n)[2:]}')
else:
    print('Opção invalida.')
