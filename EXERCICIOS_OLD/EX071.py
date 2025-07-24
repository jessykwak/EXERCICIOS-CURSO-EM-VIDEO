print('='*30)
print('{:^30}'.format('BANCO DA KWAK'))
print('='*30)
'''
valor = int(input('Qual sera o valor do dinheiro sacado? '))
r50 = valor // 50
resto1 = valor % 50
r20 = resto1 // 20
resto2 = resto1 % 20
r10 = resto2 // 10
resto3 = resto2 % 10
r1 = resto3 // 1


print(f'Notas de R$ 50: {r50} cedulas\n'
      f'Notas de R$ 20: {r20} cedulas\n'
      f'Notas de R$ 10: {r10} cedulas\n'
      f'Notas de R$ 1: {r1} cedulas')
'''
valor = int(input('Que valor voce quer sacar? '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cedulas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('='*30)
print('Obrigado. Volte sempre!')
