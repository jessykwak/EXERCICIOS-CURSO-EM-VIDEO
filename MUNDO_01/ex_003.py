#EXERCICIO 003 (= DESAFIO_003):
#Crie um programa que leia dois numeros
# e tente mostrar a soma entre eles.

num1 = int(input('Primeiro numero: ')) 
num2 = int(input('Segundo numero: '))
#necessario int para fazer soma. sem int, num eh tratado como letra
soma = num1 + num2

print('A soma de {} + {} = {}'.format(num1, num2, num1+num2))