# EXERCICIO 017:
# Faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um trianbulo retangulo, 
# calcule e mostre o comprimento da hipotenusa.

#resolucao sem import:
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

hi = ((co**2)+(ca**2))**(1/2)

print('A hipotenusa do triangulo de lado {} e {} eh de: {}'.format(co, ca, hi))

#resolucao com import:
from math import sqrt
co1 = float(input('Digite o comprimento do cateto oposto: '))
ca1 = float(input('Digite o comprimento do cateto adjacente: '))

hi1 = sqrt((pow(co1,2)+pow(ca1,2)))

print('A hipotenusa do triangulo de lado {} e {} eh de: {}'.format(co1, ca1, hi1))
