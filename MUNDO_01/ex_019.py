# EXERCICIO 019:
# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faca um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

import random

nomes = []

nomes.append = input('Digite o nome do aluno: ')
nomes.append = input('Digite o nome do aluno: ')
nomes.append = input('Digite o nome do aluno: ')
nomes.append = input('Digite o nome do aluno: ')

e = random.choice(nomes)

print('O aluno selecionado foi: {}'.format(e))