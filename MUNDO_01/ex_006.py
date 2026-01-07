# EXERCICIO 006:
# Crie um algoritmo que leia um num e mostre o seu dobro, triplo e raiz quadrada.

n = float(input('Digite um numero: '))
d = n*2
t = n*3
r = n**(1/2)

print('O dobro de {:.2f} eh: {:.2f} \nO triplo de {:.3f} eh: {:.3f} ' \
'\nA raiz qudrada de {:.4f} eh: {:.4f}'.format(n, d, n, t, n, pow(n,1/2)))
#para exponenciacao pode ser utilizada o pow(numero base, potencia)