#PROGRESSAO ARITMETICA V 2.0
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da progressao aritimetica: '))
termo11 = termo1 + ((11-1)*razao)

while termo1 != termo11:
    print(f'{termo1}', end=' ')
    termo1 +=razao
    print(termo1,end=' ')
print('\nFIM')
