# EXERCICIO 022:
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas.
# O nome com todas minusculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))
prinome = nome.split(' ')

print('SEU NOME É: {}'.format(nome.upper()))
print('seu nome é: {}'.format(nome.lower()))
print('QTD LETRAS: {}'.format((len(nome)-nome.count(' '))))
print('QTD 1 NOME: {}'.format(len(prinome[0])))