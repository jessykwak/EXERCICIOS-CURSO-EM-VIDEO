def ficha(nome = 'desconhecido', gol = '0'):
    print('='*35)
    print(f'{"NOME":^20} {"GOLS":^15}')
    print('='*35)
    print(f'{nome:^20} {gol:^15}')
    print('='*35)


resp = ficha(input('Nome do Jogador: ').capitalize().strip(),input('Quantos gols? '))