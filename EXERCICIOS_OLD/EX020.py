'''import random

a1 = str(input('Nome do aluno 1: '))
a2 = str(input('Nome do aluno 2: '))
a3 = str(input('Nome do aluno 3: '))
a4 = str(input('Nome do aluno 4: '))
lista = [a1, a2, a3, a4]
n1 = random.sample(lista,4)
n2 = random.shuffle(lista)

print(f'A ordem de apresentação será: {n1}')'''

from random import shuffle

a1 = str(input('Nome do aluno 1: '))
a2 = str(input('Nome do aluno 2: '))
a3 = str(input('Nome do aluno 3: '))
a4 = str(input('Nome do aluno 4: '))
lista = [a1, a2, a3, a4]
shuffle(lista)

print(f'A ordem de apresentação será: ')
print(lista)
