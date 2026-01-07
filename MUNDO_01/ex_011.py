# EXERCICIO 011:
# Faca um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a qtd de tinta necessaria para pinta-la
# sabendo que cada litro de tinta pinta uma area de 2m^2.

l = float(input('Digite a largura da parede em metros: '))
h = float(input('Digite a altura da parede em metros: '))

a = l*h

tinta = a / 2

print('Em uma parede de {:.2f}m x {:.2f}m, e area {:.3f}m2, vc ira precisar de {:.2f}L de tinta'.format(l, h, a, tinta))
