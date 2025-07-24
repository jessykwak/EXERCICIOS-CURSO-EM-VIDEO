from datetime import datetime

hj = int(datetime.today().year)

list = []
for x in range (0,7):
    ano = int(input(f'Que ano voce nasceu? '))
    idade = hj - ano
    list += [idade]

g = 0
w = 0
for n in range (0,7):
    if list[n] >= 21:
        w += 1
    else:
        g += 1

print(f'Maior de idade = {w} pessoas\n'
      f'Menor de idade = {g} pessoas')
