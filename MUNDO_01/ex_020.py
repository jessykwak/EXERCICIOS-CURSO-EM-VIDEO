# EXERCICIO 020:
# O mesmo professor do desafio anterior quer sortear a ordem de apresentacao de trabalhos dos alunos. 
# Faca um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

nomes = []

nomes.append(input('Digite o nome do aluno: '))
nomes.append(input('Digite o nome do aluno: '))
nomes.append(input('Digite o nome do aluno: '))
nomes.append(input('Digite o nome do aluno: '))

e = shuffle(nomes)

print('A ordem de apresentacao sera: {}'.format(nomes))