def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (KeyboardInterrupt):
            print('O USUARIO PREFERIU NAO INFORMAR NENHUM VALOR')
            return 0000
        except (ValueError, TypeError):
            print('ERRO! digite um numero INTEIRO valido')
            continue
        else:
            return n
            break


def leiaFloat(msg1):
    while True:
        try:
            n1 = float(str(input(msg1)).strip().replace(',','.'))
        except KeyboardInterrupt:
            print('O USUARIO PREFERIU NAO INFORMAR NENHUM VALOR')
            return 000
        except (ValueError, TypeError):
            print('ERRO! digite um numero REAL valido')    
            continue    
        else:
            return n1
            break


k = leiaInt('Digite um numero inteiro: ')
g = leiaFloat('Digite um numero real: ')
print(f'voce digitou o numero {k} e {g}')