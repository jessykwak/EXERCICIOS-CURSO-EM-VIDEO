'''def ficha(nome = 'desconhecido', gol = '0'):
    print('='*35)
    print(f'{"NOME":^20} {"GOLS":^15}')
    print('-'*35)
    print(f'{nome:^20} {gol:^15}')
    print('='*35)


resp = ficha(input('Nome do Jogador: ').capitalize().strip(),input('Quantos gols? '))'''
def ficha(jog='DESCONHECIDO', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do Jogador: '))
g = str(input('Quantidade de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n,g)
