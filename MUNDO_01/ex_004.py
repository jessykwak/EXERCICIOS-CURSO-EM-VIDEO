# EXERCICIO 004:
# Faca um programa que leia algo pelo teclado e mostre na tela o seu tipo 
# primitivo e todas as informacoes possiveis sobre ela.

algo = input('Digite algo: ')
print('O tipo primitivo desse valor eh:', type(algo))
print('Soh ten espacos? {}'.format(algo.isspace()))
print('Eh um numero?', algo.isnumeric())
print('Eh alfabetico? {}'.format(algo.isalpha()))
print('Eh alfanumerico? {}'.format(algo.isalnum()))
print('Esta em maiusculas? {}'.format(algo.isupper()))
print('Esta em minusculas? {}'.format(algo.islower()))
print('Esta capitalizada? {}'.format(algo.istitle()))