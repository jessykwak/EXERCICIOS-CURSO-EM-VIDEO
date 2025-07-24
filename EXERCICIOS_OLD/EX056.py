listan = []
listai = []
listas = []
listag = []
soma = 0

for c in range(0,4):
    nome = str(input('Informe o seu nome: ')).strip()
    idade = int(input('Informe a sua idade: '))
    sexo = str(input('Informe o seu sexo: ')).strip()
    listan += [nome.capitalize()]
    listai += [idade]
    listas += [sexo.capitalize()]
    listag += [nome.capitalize(),idade,sexo.capitalize()]
    soma += idade


media = soma/4
print(f'A media da idade das pessoas eh {media:.1f}')

novin = 0

if 'M' in listag[2] or 'M' in listag[5] or 'M' in listag[8] or 'M' in listag[11]:
    if listag[1] > listag[4] and listag[1] > listag[7] and listag[1] > listag[10] and 'M' in listag[2]:
        print(f'O homem mais velho eh: {listag[0]}')
    elif listag[4] > listag[1] and listag[4] > listag[7] and listag[4] > listag[10] and 'M' in listag[5]:
        print(f'O homem mais velho eh: {listag[3]}')
    elif listag[7] > listag[1] and listag[7] > listag[4] and listag[7] > listag[10] and 'M' in listag[8]:
        print(f'O homem mais velho eh: {listag[6]}')
    elif listag[10] > listag[1] and listag[10] > listag[4] and listag[10] > listag[7] and 'M' in listag[11]:
        print(f'O homem mais velho eh: {listag[9]}')
    else:
        print('nao ha um homem "mais velho"')
elif 'F' in listag[2] or 'F' in listag[5] or 'F' in listag[8] or 'F' in listag[11]:
    for t in range(1,12,3):
        if listag[t] < 20 and 'F' in listag[t+1]:
            novin += 1
    print(f'A quantidade de mulheres menores que 20 anos, sao {novin}')
else:
    print('sei la mano')
