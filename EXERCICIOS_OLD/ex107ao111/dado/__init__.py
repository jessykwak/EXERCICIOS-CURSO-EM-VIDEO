def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '': #se ela for alphanumerico
            valido = False
            print('VALOR INPUTADO INVALIDO. TENTE NOVAMENTE')
        else:
            valido = True
            return float(entrada)
