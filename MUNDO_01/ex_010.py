# EXERCICIO 010:
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
# Considere US$ 1,00 = R$ 3,27

c = float(input('Digite quanto dinheiro vc tem na carteira: '))

d = c / 3.27

print('Com R$ {:.2f} que voce possui, voce pode comprar US$ {:.2f}.'.format(c, d))