v = float(input('Informe o valor do produto: R$ '))
c = int(input('Informe a forma de pagamento:\n'
              '1 - A vista\n'
              '2 - Parcelado\n'))
if c == 1:
    ap = int(input('Informe a forma de pagamento:\n'
                  '1 - Dinheiro\n'
                  '2 - Cheque\n'
                  '3 - Cartao\n'))
    if ap == 1 or ap == 2:
        print(f'Valor final: R$ {v*.9:.2f}')
    elif ap == 3:
        print(f'Valor final: R$ {v*.95:.2f}')
    else:
        print('Forma de pagamento invalida.')
elif c == 2:
    ap = int(input('Informe a forma de pagamento:\n'
                  '1 - Em 2x\n'
                  '2 - Em 3x ou mais\n'))
    if ap == 1:
        print(f'O valor final e: R$ {v:.2f} em 2x sem juros.')
    elif ap == 2:
        p = int(input(f'Digite o numero de parcelas: '))
        if p >= 3:
            print(f'O valor final e: R$ {v*1.2:.2f} em {p}x com juros.')
        else:
            print('Numero de parcelas invalidas.')
    else:
        print('Forma de pagamento invalida.')
else:
    print('Forma de pagamento invalido.')

