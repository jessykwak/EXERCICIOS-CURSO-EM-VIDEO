# EXERCICIO 015:
# Escreva um programa que pergunte a qtd de km percorridos por um carro alugado e a qtd de dias pelos quais ele foi alugado.
# Calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R%0,15 por km rodado.

kma = float(input('Digite quantos km foram percorridos: '))
diaa = int(input('Digite quantos dias foram alugados: '))

preco = (diaa*60) + (kma*.15)

print('O carro percorreu {:.2f}km, e foi alugado por {}dia(s).'.format(kma, diaa))
print('O valor a ser pago sera de R$ {:.2f}'.format(preco))
