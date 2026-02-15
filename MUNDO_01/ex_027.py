# EXERCICIO 027:
# Faça um programa que leia o nome completo de uma pessoa, 
# mostrando em seguida o primeiro e o ultimo nome separamente.
# Ex: Ana Maria de Souza
# primeiro: Ana
# ultimo: Souza

nome = str(input('Digite seu nome completo: '))
no_sep = nome.split()
last_name = no_sep[len(no_sep)-1]
first_name = no_sep[0]

print('{}'.format(nome.title()))
print('primeiro nome: {}'.format(first_name.capitalize()))
print('ultimo nome: {}'.format(last_name.capitalize()))