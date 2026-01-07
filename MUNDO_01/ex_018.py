# EXERCICIO 018:
# Faca um programa que leia um angulo qualquer e mostre na tela o valor do 
# seno, cosseno e tangente desse angulo.

import math

ang = float(input('Digite o angulo em graus: '))

anr = math.radians(ang)

s = math.sin(anr)
c = math.cos(anr)
t = math.tan(anr)

print('O seno, cosseno e tangente do angulo {:.2f} eh: {:.2f}, {:.2f} e {:.2f}, ' \
'respectivamente.'.format(ang, s, c, t))