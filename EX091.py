'''from random import randint
resul = {}
dicio = []
while True:
    resul['jogador'] = str(input('Digite o nome do jogador: '))
    resul['dado'] = randint(1,6)
    print(f'O numero sorteado do dado eh: {resul["dado"]}')
    dicio.append(resul.copy())
    d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while d not in 'SsNn':
        print('OPCCAO INVALIDA.')
        d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if 'N' == d:
        break
dicio2 = sorted(dicio, key = lambda d: d["dado"])
print(f'Em ordem, os jogadores e seus numeros sorteados sao: {dicio2}')
print(f'o vencedor eh: {dicio2[len(dicio2)-1]["jogador"]}')'''

from random import randint
from time import sleep
resul = {}
dicio = []
print('='*30)
print(f'{"VALORES SORTEADOS":^30}')
print('='*30)
sleep(1)
for n in range(1,5):
    resul['jogador'] = n
    print(f'O jogador {n} ', end='')
    resul['dado'] = randint(1,6)
    print(f'tirou {resul["dado"]}')
    dicio.append(resul.copy())
    sleep(1)
sleep(1)
dicio2 = sorted(dicio, key = lambda d: d["dado"])
print('='*30)
print(f'{"RANKING DOS JOGADORES":^30}')
print('='*30)
sleep(1)
for x in range(1,5):
    print(f'{x}° lugar: jogador com dado {dicio2[len(dicio2)-x]["dado"]}')
    sleep(1)
print('='*30)

from random import randint
from time import sleep
from operator import itemgetter
jogo = {'jogador1': randint(1,6),
        'jogador2': randint(1,6),
        'jogador3': randint(1,6),
        'jogador4': randint(1,6)}
ranking = dict()
print('Valores sorteados: ')
for k,v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True) #vira uma lista
print('Ranking dos jogadores: ')
for k1,v1 in enumerate(ranking):
    print(f'O {k1+1} lugar tirou {v1[1]}.')
    sleep(1)
