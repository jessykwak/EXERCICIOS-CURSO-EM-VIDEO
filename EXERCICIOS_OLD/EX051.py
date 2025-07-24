#PROGRESSAO ARITMETICA
termo1 = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da progressao aritimetica: '))
termo11 = termo1 + ((11-1)*razao)

for c in range(termo1, termo11, razao):
    print(c, end=' ')
print('FIM')
