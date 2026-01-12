# EXERCICIO 016:
# Crie um programa que leia um num Real qlqr pelo teclado e mostre na tela a sua porcao inteira.

#resolucao sem import:
n = float(input('Digite um numero Real qualquer: '))
i = n//1

print('A parte inteira do numero {} eh: {}'.format(n, i))
print('A parte inteira do numero {} eh: {}'.format(n, int(n)))

#resolucao com import:
from math import floor, trunc

n1 = float(input('Digite um numero Real qualquer: '))

print('A parte inteira do numero {} eh: {}'.format(n1, floor(n1)))
print('A parte inteira do numero {} eh: {}'.format(n1, trunc(n1)))