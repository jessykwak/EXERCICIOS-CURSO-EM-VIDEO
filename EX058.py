'''import random
from time import sleep

cores = {'lp':'\033[m','az':'\033[34m','am':'\033[33m','peb':'\033[7;30m', 'vd':'\033[32m', 'li':'\033[35m', 'vm':'\033[31m'}
nome = str(input('Digite o seu nome: ')).strip()
print(f"Olá, {cores['az']}{nome.capitalize()}{cores['lp']}! \n"
      f'Escolha um número de {cores["am"]}0{cores["lp"]} a {cores["am"]}10{cores["lp"]}, se o numero escolhido coincidir com o selecionado pelo computador, voce {cores["vd"]}vence{cores["lp"]} o jogo!\n')
n = 0
x = 0
g = 11
while g != n:
    n = random.randint(0,10)
    g = int(input('Digite o número desejado: '))
    print(f'O computador escolheu o número: {n}')
    if 0 <= g <= 10 and g !=n:
        print(f'{cores["li"]}processando...{cores["lp"]}')
        sleep(1)
        print(f'{cores["vm"]}Que pena, não foi dessa vez! Tente novamente!{cores["lp"]}\n')
    elif g > 10 or g < 0:
        print(f'{cores["li"]}processando...{cores["lp"]}')
        sleep(1)
        print('O numero que voce escolheu, é inválido! Tente novamente!\n')
    x += 1
print(f'{cores["li"]}processando...{cores["lp"]}')
sleep(1)
print(f'{cores["az"]}PARABÉNS{cores["lp"]}, VOCE {cores["vd"]}VENCEU{cores["lp"]}!\n'
      f'Voce tentou {x} vezes.')'''

from random import randint
pc = randint(0,10)
print('Sou seu computador! Acabei de pensar em um numero entre 0 e 10.')
print('Sera que voce consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual eh seu palpite? '))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... tente mais uma vez!')
        elif jogador > pc:
            print('Menor! tente mais uma vez. ')
print(f'Acertou com {palpites} tentativas. Parabens!')
