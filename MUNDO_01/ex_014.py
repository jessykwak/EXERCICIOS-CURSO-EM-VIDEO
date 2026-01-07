# EXERCICIO 014:
# Escreva um programa que converta uma temperatura digitada em grau C e converta para grau F.

c = float(input('Digite a temperatura em Celsius: '))

f = (c*1.8)+32

print('A temperatura de {:.2f}°C eh equivalente a {:.2f}°F'.format(c, f))
print('A temperatura de {1}°F eh equivalente a {0}°C'.format(c, f)) 
#colocando o numero dentro dos {}, eh possivel mudar a ordem em q aparecem as variaveis (a 1 eh 0, dps 1, dps 2 etc)