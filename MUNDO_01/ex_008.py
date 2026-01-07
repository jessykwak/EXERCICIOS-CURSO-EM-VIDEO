# EXERCICIO 008:
# Escreva um programa que leia um valor em metro e o exiba convertido em centimetro e milimetro.

m = float(input('Digite um valor em metro: '))

cm = m*100
mm = m*1000

print('O valor de {}m eh equivalente a {:.1f}cm e {:.1f}mm.'.format(m, cm, mm))