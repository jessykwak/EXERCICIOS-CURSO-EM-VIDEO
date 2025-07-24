player = {}
listagols = []
soma = 0
listona =[]
while True:
    player["jogador"] = str(input('Nome do Jogador: ')).capitalize().strip()
    player["partidas"] = int(input(f'Quantas partidas {player["jogador"]} jogou? '))
    for x in range(0,player["partidas"]):
        gol = int(input(f'Quantos gols na partida {x+1}: '))
        soma += gol
        listagols.append(gol)
    player["goleadas"] = listagols[:]
    player["total"] = soma
    soma = 0
    listagols.clear()
    listona.append(player.copy())
    d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while d not in 'SsNn':
        print('OPCCAO INVALIDA.')
        d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if 'N' == d:
        break

print('='*80)
print(f'{"COD":^5} {"NOME":^30} {"GOLS":^30} {"TOTAL":^5}')
print('='*80)
for l in range(0,len(listona)):
    print(f'{l:^5} {listona[l]["jogador"]:^30} {str(listona[l]["goleadas"]):^30} {listona[l]["total"]:^5}')
print('='*80)

while True:
    while True:
        cod = int(input('Mostrar dados de qual jogador? '))
        if 0 <= cod < len(listona):
            break
        print('OPCAO INVALIDA')
    print(f'O nome do jogador eh: {listona[cod]["jogador"]}')
    print(f'A lista de gols por partida eh: {listona[cod]["goleadas"]}')
    for x in range(0,listona[cod]["partidas"]):
        print(f'     => Na partida {x+1}, fez {listona[cod]["goleadas"][x]} gols')
    print(f'O total de gols foram: {listona[cod]["total"]}')
    t = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while t not in 'SsNn':
        print('OPCCAO INVALIDA.')
        t = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if 'N' == t:
        break
print('='*80)
print('TCHAU')
