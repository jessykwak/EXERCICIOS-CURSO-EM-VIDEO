# EXERCICIO 012:
# Faca um algoritmo que leia o preco de um produto e mostre seu novo preco, com 5% de desconto.

po = float(input('Digite o valor original do produto: '))

pd = po * .95

print("O produto de R$ {:.2f} com 5% de desc fica R$ {:.2f}".format(po, pd))