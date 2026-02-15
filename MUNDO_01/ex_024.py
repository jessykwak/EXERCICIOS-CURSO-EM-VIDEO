# EXERCICIO 024:
# Crie um programa que leia o nome de uma cidade e diga se ela ccomeça ou nao com o nome 'SANTO'.

cidade = str(input('Digite o nome da cidade:'))
primeiro = cidade.split()


if (primeiro[0].upper() == 'SANTO'):
    print('COMEÇA COM SANTO!')
else:
    print('NAO COMEÇA COM SANTO')