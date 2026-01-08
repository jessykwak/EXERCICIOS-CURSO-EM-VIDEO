# EXERCICIO 019:
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

#resolucao com lista
nomes = []

nomes.append(input('Digite o nome do aluno: '))
# OBS: .append faz uma acao. entao nomes.append = input... nao faz sentido
# pq esta substituindo nomes.append(uma acao) com um input.
nomes.append(input('Digite o nome do aluno: '))
nomes.append(input('Digite o nome do aluno: '))
nomes.append(input('Digite o nome do aluno: '))

e = choice(nomes)

print('O aluno selecionado foi: {}'.format(e))

#resolucao alternativa

a = input('Digite o nome do aluno: ')
b = input('Digite o nome do aluno: ')
c = input('Digite o nome do aluno: ')
d = input('Digite o nome do aluno: ')

e1 = choice((a, b, c, d))

print('O aluno selecionado foi: {}'.format(e1))