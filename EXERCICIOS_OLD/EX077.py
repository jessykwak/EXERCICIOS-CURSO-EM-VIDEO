tupla = ('Corinthians', 'Palmeiras', 'Gremio', 'Chapecoense', 'Sao Paulo', 'Santos', 'Cruzeiro', 'Vasco',
         'Flamengo', 'Botafogo', 'Fluminense', 'Atletico PR', 'Juventude', 'Bahia', 'Sport Recife', 'EC Vitoria', 'Avai',
         'Coritiba', 'Ponte Preta', 'Atletico GO', 'Atletico')
x = len(tupla)
'''
for c in range(0,x):
    if 'a' in tupla[c] or 'A' in tupla[c]:
        print(f'A palavra {tupla[c]} contem \na vogal "a"',)
    if 'e' in tupla[c] or 'E' in tupla[c]:
        print(f'a vogal "e"', )
    if 'i' in tupla[c] or 'I' in tupla[c]:
        print(f'a vogal "i"', )
    if 'o' in tupla[c] or 'O' in tupla[c]:
        print(f'a vogal "o"',)
    if 'u' in tupla[c] or 'U' in tupla[c]:
        print(f'a vogal "u".')
print('thats all folks')
'''

for p in tupla:
    print(f'\nNa palavra {p.upper()} temos as vogais: ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(f'{letra} ', end=' ')
