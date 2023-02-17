import random
from time import sleep

cores = {'lp':'\033[m','az':'\033[34m','am':'\033[33m','peb':'\033[7;30m', 'vd':'\033[32m', 'li':'\033[35m', 'vm':'\033[31m'}
nome = str(input('Digite o seu nome: ')).strip()
print(f"Olá, {cores['az']}{nome.capitalize()}{cores['lp']}! \n"
      f'Escolha um número de {cores["am"]}0{cores["lp"]} a {cores["am"]}5{cores["lp"]}, se o numero escolhido coincidir com o selecionado pelo computador, voce {cores["vd"]}vence{cores["lp"]} o jogo!\n')

n = random.randint(0,5)
g = int(input('Digite o número desejado: '))
print(f'{cores["li"]}processando...{cores["lp"]}')
sleep(2)
print(f'O computador escolheu o número: {n}\n')

if n==g:
    print(f'{cores["az"]}PARABÉNS{cores["lp"]}, VOCE {cores["vd"]}VENCEU{cores["lp"]}!')
else:
    print(f'{cores["vm"]}Que pena, não foi dessa vez!{cores["lp"]}')
print('Gostaria de tentar novamente? ')
