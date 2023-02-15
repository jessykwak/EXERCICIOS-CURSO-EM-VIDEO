def leiaDinheiro():
    while True:
        din = float(input('Digite um valor: '))
        if din != float or din != int:
            print('VALOR INVALIDO. TENTE NOVAMENTE')
        else:
            return din
            break

            
leiaDinheiro()