# EXERCICIO 013:
# Faca um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento.

so = float(input('Digite o salario do funcionario: '))

sa = so * 1.15

print('O salario de R$ {:.2f}, com aumento de 15% fica R${:.2f}'.format(so, sa))