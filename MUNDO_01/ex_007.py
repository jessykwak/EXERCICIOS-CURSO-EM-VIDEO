# EXERCICIO 007:
# Desenvolva um programa q leia as duas notas de um aluno, calcule e mostre a sua media.

nome = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a proxima nota: '))

m = (n1+n2)/2

print('O aluno {} teve as notas {:.1f} e {:.1f}.'.format(nome, n1, n2), end = ' ')
print('Sua media sera: ({:.1f} + {:.1f})/2 = {:.1f}'.format(n1, n2, m))