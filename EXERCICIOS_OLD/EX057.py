'''s = 0
while 'F' != s != 'M':
    s = str(input('Olá! Qual o seu sexo biologico? [F/M] ')).strip().upper()[0]
    if 'F' != s != 'M':
        print('Dados invalidos. Tente novamente.')
if s == 'M':
    print(f'O seu sexo biologico é Masculino. Dado cadastrado com sucesso.')
else:
    print(f'O seu sexo biologico é Feminino. Dado cadastrado com sucesso.')'''

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Informacao invalida. Por favor informe seu sexo: ')).strip().upper()[0]
if sexo == 'M':
    print(f'O seu sexo biologico é Masculino. Dado cadastrado com sucesso.')
else:
    print(f'O seu sexo biologico é Feminino. Dado cadastrado com sucesso.')