from random import randint
from time import sleep
print('==='*9)
print(' Vamos jogar par ou impar!')
print('==='*9)
sleep(1)

c = s = p1 = 0
while True:
    p1 = str(input('Escolha, par ou impar: [P/I] ')).strip().upper()
    while 'I' != p1 != 'P':
        print('OPÇÃO INVALIDA, CARA PALIDA, DIGITE P OU I!')
        p1 = str(input('Escolha, par ou impar: [P/I] ')).strip().capitalize()
    pc = randint(0, 5)
    p2 = int(input('Escolha um valor de 0 a 5: '))
    if p2 > 5:
        while p2 > 5:
            print('OPÇÃO INVALIDA, CARA PALIDA, DIGITE UM NUMERO ENTRE 0 E 5!')
            p2 = int(input('Escolha um valor de 0 a 5: '))
    print(f'O computador escolheu: {pc}\n')
    sleep(1)
    s = pc + p2
    if s % 2 == 0 and 'P' in p1:
        v = str(print('PARABENS! VC VENCEU!\n'))
        sleep(1)
    elif s % 2 == 0 and 'I' in p1:
        v = str(print('POXA! VC PERDEU!'))
        sleep(1)
        break
    elif s % 2 != 0 and 'I' in p1:
        v = str(print('PARABENS! VC VENCEU!\n'))
        sleep(1)
    elif s % 2 != 0 and 'P' in p1:
        v = str(print('POXA! VC PERDEU!'))
        sleep(1)
        break
    c += 1
print(f'Voce venceu {c} vezes consecutivas!')