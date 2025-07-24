#################################################

termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da progressao aritimetica: '))

r = 11
termo11 = termo1 + ((r - 1) * razao)
while termo1 != termo11 and r != 0:
    while termo1 != termo11:
        print(f'{termo1}', end=' ')
        termo1 +=razao
    r = int(input('\nVoce qr mostrar + qntos termos? '))
    termo11 = termo1 + ((r - 1) * razao)
print('FIM')
'''
################################################
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da progressao aritimetica: '))
termo = termo1
cont = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while cont <= total:
        print(f'{termo}', end=' ')
        termo += razao
        cont += 1
    print('\nPAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print(f'\nPA finalizada com {total} termos mostrados')'''
