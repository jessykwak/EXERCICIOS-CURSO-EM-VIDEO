player = {}
gols = []

player["jogador"] = str(input('Nome do Jogador: ')).capitalize().strip()
player["partidas"] = int(input(f'Quantas partidas {player["jogador"]} jogou? '))
soma = 0
for x in range(0,player["partidas"]):
    gol = int(input(f'Quantos gols na partida {x+1}: '))
    soma += gol
    gols.append(gol)
player["goleadas"] = gols
player["total"] = soma

print('='*100)
print(player)
print('='*100)
print(f'O nome do jogador eh: {player["jogador"]}')
print(f'A lista de gols por partida eh: {player["goleadas"]}')
print(f'O total de gols foram: {player["total"]}')
print('='*100)

print(f'O jogador {player["jogador"]}, jogou {player["partidas"]} partidas:')
for x,y in enumerate(player["goleadas"]):
    print(f'     => Na partida {x+1}, fez {y} gols')
print(f'Fez um total de {player["total"]} gols nessas {player["partidas"]} partidas.')

print('='*100)
