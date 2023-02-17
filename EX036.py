v = float(input('Qual o valor da casa? R$ '))
s = float(input('Qual o valor do seu salario? R$ '))
a = float(input('Em quantos anos voce pretende pagar? '))

p = v / (a*12)

if s * .3 > p:
    print(f'A prestacao mensal a ser paga sera no valor de {p:.2f} reais')
elif s * .3 == p:
    print(f'Consulte um gerente!')
else:
    print(f'Seu salario nao e compativel para a compra deste imovel.')
