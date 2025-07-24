tupla = ('Corinthians', 'Palmeiras', 'Gremio', 'Chapecoense', 'Sao Paulo', 'Santos', 'Cruzeiro', 'Vasco', 'Flamengo',
         'Botafogo', 'Fluminense', 'Atletico PR', 'Bahia', 'Sport Recife', 'EC Vitoria', 'Avai', 'Coritiba', 'Ponte Preta',
         'Atletico GO', 'Atletico', 'Juventude')

d = int(tupla.index("Chapecoense"))+1

print(f'Os primeiros colocados sao: {tupla[0:5]}')
print(f'Os ultimos colocados sao: {tupla[-4:]}')
print(f'Os ultimos colocados sao: {sorted(tupla)}')
print(f'O Chapecoense esta na {d}° posicao')
