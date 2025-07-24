'''from random import randint
from time import sleep

cores = {'lp':'\033[m','az':'\033[34m','am':'\033[33m','peb':'\033[7;30m', 'vd':'\033[32m', 'li':'\033[35m', 'vm':'\033[31m'}

nome = str(input('Ola! Qual o seu nome? ')).strip()
sn = str(input(f'{nome.capitalize()}, vamos jogar Jokenpo? {cores["vd"]}:){cores["lp"]} ')).strip()

if sn.capitalize() == 'Sim' or 'Ok' in sn.capitalize():
    print(f'{cores["vm"]}Bom mesmo!!!!{cores["lp"]} brincs kkk {cores["vd"]}:P{cores["lp"]}')
    sleep(1)
    jkp = int(input(f'Digite {cores["li"]}1 - para Pedra{cores["lp"]}, {cores["am"]}2 - para Papel{cores["lp"]}, {cores["vd"]}3 - para Tesoura{cores["lp"]}: '))
    pc = randint(1, 3)
    if pc == 1:
        pc2 = f'{cores["li"]}1 - Pedra{cores["lp"]}'
    elif pc == 2:
        pc2 = f'{cores["am"]}2 - Papel{cores["lp"]}'
    else:
        pc2 = f'{cores["vd"]}3 - Tesoura{cores["lp"]}'
    print(f'Eu escolho: {pc2}!')
    sleep(2)
    if (jkp == 1 and pc == 1) or (jkp == 2 and pc == 2) or (jkp == 3 and pc == 3):
        print(f'Aha! {cores["li"]}Empate{cores["lp"]}! {cores["am"]}:/{cores["lp"]}')
    elif (jkp == 1 and pc == 2) or (jkp == 2 and pc == 3) or (jkp == 3 and pc == 1):
        print(f'ihh, {nome.capitalize()}! Nao foi dessa vez, {cores["vm"]}eu venci{cores["lp"]}! {cores["az"]}XD{cores["lp"]}')
    elif (jkp == 1 and pc == 3) or (jkp == 2 and pc == 1) or (jkp == 3 and pc == 2):
        print(f'UHUL! Parabens, {nome.capitalize()}! Voce {cores["vd"]}venceu{cores["lp"]}!')
    else:
        print(f'Que isso cara, {cores["vm"]}jogada invalida{cores["lp"]}! {cores["vm"]}>:I{cores["lp"]}')
elif sn.capitalize() == 'Nao' or sn.capitalize() == 'Não':
    print(f'...\n'
          f'Entao Vai se f... brincadeirinhaaaa! rsrs\n'
          f'Até a próxima, chatonildo(a)! {cores["vm"]}>:P{cores["lp"]}')
else:
    print('Aff, qual a dificuldade de responder sim ou nao?! -__-')'''

from random import randint

itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0,2)

print('Suas opções são:\n'
      '[0] PEDRA\n'
      '[1] PAPEL\n'
      '[2] TESOURA')

p1 = int(input('Qual a sua jogada?'))

print('-=-'*8)
print(f'Computador jogou {itens[pc]}!')
print(f'Jogador jogou {itens[p1]}!')
print('-=-'*8)

if pc == 0:
    if p1 == 0:
        print('EMPATE!')
    elif p1 == 1:
        print('VITORIA!')
    elif p1 == 2:
        print('DERROTA....')
    else:
        print('jogada invalida')
elif pc == 1:
    if p1 == 0:
        print('DERROTA....')
    elif p1 == 1:
        print('EMPATE.')
    elif p1 == 2:
        print('VITORIAAA!')
    else:
        print('jogada invalida')
elif pc == 2:
    if p1 == 0:
        print('VITOOOOOOOOOOOORIA!!!!1!!1')
    elif p1 == 1:
        print('DERROOOTA!!!!!!')
    elif p1 == 2:
        print('EMPATE')
    else:
        print('jogada invalida')
else:
    print('jogada invalida.')