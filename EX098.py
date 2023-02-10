from time import sleep


def contador(i,f,p):
    print(f'Contagem de {i} ate {f} de {p} em {p}: ')
    print('=' * 30)
    sleep(0.5)
    if p < 0:
        p *= -1
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ', flush = True)
            sleep(0.3)
            cont += p
        print('FIM')
    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ', flush = True)
            sleep(0.3)
            cont -= p
        print('FIM')


print('='*30)
contador(1,10,1)
print('='*30)
contador(10,0,-2)
print('='*30)
i = int(input('Digite o primeiro termo: '))
f = int(input('Digite o ultimo termo: '))
p = int(input('Digite a razao da progressao aritimetica: '))
print('='*30)
contador(i,f,p)
print('='*30)
