# alguns tipos primitivos
# int: 1 78 6 5 -5  0
# float: 1.78 5 0.6 8.0 -5684 -65.5
# bool: True False
# str 'a' 'iaush' '7.5' '' 

########################################################

num1 = input('Primeiro numero: ')
num2 = input('Segundo numero: ')
soma = num1 + num2

print('A soma de', num1, 'e', num2, 'eh igual a', num1 + num2)
print(num1, '+', num2, '=', soma)

########################################################

n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
#necessario int para fazer soma. sem int, num eh tratado como letra
s = n1 + n2

print('A soma de {} e {} eh igual a {}'.format(n1, n2, n1+n2))
print('{} + {} = {}'.format(n1, n2, s))

########################################################

# DESAFIO 004:
# Faca um programa que leia algo pelo teclado e mostre 
# na tela o seu tipo primitivo e todas as informacoes possiveis sobre ela.

a = input('digite algo:')
print(type(a))
print(a.isnumeric())
print(a.isalpha())
print(a.isalnum())
print(a.isalnum())
print(a.isascii())
print(a.isdecimal(), a.isdigit(), a.isidentifier(), a.islower(), a.isprintable(), a.isspace(), a.istitle())
print(a.isupper(), a.__init_subclass__()A)