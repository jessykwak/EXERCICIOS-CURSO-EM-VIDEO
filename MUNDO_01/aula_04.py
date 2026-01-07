#DESAFIO 001:
#Crie um script Python que leia o nome de uma pessoa e 
# mostre uma mensagem de boas-vindas com o valor digitado.
print('======== DESAFIO 001 ========')
nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ') #Fiz um input e print a mais pra ter a idade, 4fun

print('Ola ', nome, '! Prazer em te conhecer!')
print(nome, 'voce tem ', idade, 'anos!') #Fiz um input e print a mais pra ter a idade, 4fun

#DESAFIO 002:
#Crie um script Python que leia o dia, o mes e o ano de anscimento
#de uma pessoa e mostre uma mensagem com a data formatada.
print('======== DESAFIO 002 ========')
dia = input('Qual o dia do seu aniversario? ')
mes = input('Qual o mes do seu aniversario? ')
ano = input('Qual o ano do seu nascimento? ')

print('Voce nasceu na data: ',dia,'de',mes,'de',ano)

#DESAFIO 003:
#Crie um script Python que leia dois numeros
# e tente mostrar a soma entre eles.

print('======== DESAFIO 003 ========')
num1 = int(input('Primeiro numero: ')) 
num2 = int(input('Segundo numero: '))
#necessario int para fazer soma. sem int, num eh tratado como letra
soma = num1 + num2

print('A soma de', num1, 'e', num2, 'eh igual a', num1 + num2)
print(num1, '+', num2, '=', soma)