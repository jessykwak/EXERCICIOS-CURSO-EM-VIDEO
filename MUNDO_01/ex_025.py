# EXERCICIO 025:
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = str(input('Digite seu nome completo: '))

nomecap = nome.upper()

if (nomecap.find('SILVA') != -1): #atencao! =! nao funciona! tem q ser exclamacao e igual respectivamente.
                                  # .find('xxx') = -1 acontece qndo nao encontra a palavra na strimg
    print('TEM SILVA!!!')
else:
    print('NAO TEM SILVA')