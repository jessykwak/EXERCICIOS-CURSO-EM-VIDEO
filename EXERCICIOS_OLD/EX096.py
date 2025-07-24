def area():
    a = l*c
    print(f'A area do terreno de largura {l} metros e comprimento {c} metros eh de: {a:.2f} m2.')


print('='*30)
print(f'{"CONTROLE DE TERRENOS":^30}')
while True:
    print('=' * 30)
    l = float(input('Qual a largura do terreno em metros? '))
    c = float(input('Qual o comprimento do terreno em metros? '))
    area()
    t = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while t not in 'SsNn':
        print('OPCCAO INVALIDA.')
        t = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if 'N' == t:
        print('=' * 30)
        break
