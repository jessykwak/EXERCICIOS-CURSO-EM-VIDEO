x = h = w = 0
while True:
    print('-'*30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo biologico: [M/F]')).strip().capitalize()[0]
    if idade > 18:
        x += 1
    if sexo[0] == 'M':
        h += 1
    if sexo[0] == 'F' and idade < 20:
        w += 1
    p = ' '
    while p not in 'SN':
        p = str(input('Gostaria de continuar? [S/N]')).strip().capitalize()[0]
    if 'N' in p:
        print('Obrigado pela participação! Até mais.')
        break
print(f'{x} pessoas tem mais de 18 anos')
print(f'{h} homens foram cadastrados')
print(f'{w} mulheres tem menos de 20 anos')
