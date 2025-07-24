'''from datetime import date, datetime

cores = {'lp':'\033[m','az':'\033[34m','am':'\033[33m','peb':'\033[7;30m', 'vd':'\033[32m', 'li':'\033[35m', 'vm':'\033[31m'}
a = str(input('Informe o dia, mes e ano de seu nascimento: ')).strip()

if '/' in a:
    b = a.split('/')
    c = int(f'{b[0]}')
    d = int(f'{b[1]}')
    e = int(f'{b[2]}')
    x = date(e, d, c)
    print(f'Voce nasceu no dia {c}, do mes {d} no ano de {e}. \n')
elif ' ' in a:
    b = a.split(' ')
    c = int(f'{b[0]}')
    d = int(f'{b[1]}')
    e = int(f'{b[2]}')
    x = date(e, d, c)
    print(f'Voce nasceu no dia {c}, do mes {d} no ano de {e}. \n')
elif '-' in a:
    b = a.split('-')
    c = int(f'{b[0]}')
    d = int(f'{b[1]}')
    e = int(f'{b[2]}')
    x = date(e, d, c)
    print(f'Voce nasceu no dia {c}, do mes {d} no ano de {e}. \n')
else:
    print(f'Data de nascimento {cores["vm"]}invalida{cores["lp"]}. Tente novamente.')

mi = date(e+9, d, c)
i = date(e+14, d, c)
j = date(e+19, d, c)
s = date(e+25,d ,c)
f = date.today()

if mi >= f and i > f and j > f and s > j:
    print(f'Ate 9 anos, categoria {cores["vd"]}Mirim{cores["lp"]}.')
elif mi < f <= i:
    print(f'Ate 14 anos, categoria {cores["az"]}Infantil{cores["lp"]}.')
elif i < f <= j:
    print(f'Ate 19 anos, categoria {cores["am"]}Junior{cores["lp"]}.')
elif j < f <= s:
    print(f'Ate 25 anos, categoria {cores["li"]}Senior{cores["lp"]}.')
elif f > s and mi < f and i < f and j < f:
    print(f'Acima de 25 anos, categoria {cores["peb"]}Master{cores["lp"]}.')'''

from datetime import date

cores = {'lp':'\033[m','az':'\033[34m','am':'\033[33m','peb':'\033[7;30m', 'vd':'\033[32m', 'li':'\033[35m', 'vm':'\033[31m'}

atual = date.today().year
birth = int(input('Ano de nascimento: '))
i = atual - birth

print(f'O atleta tem {i} anos.')

if i <= 9:
    print(f'Ate 9 anos, categoria {cores["vd"]}Mirim{cores["lp"]}.')
elif 9 < i <=14:
    print(f'Ate 14 anos, categoria {cores["az"]}Infantil{cores["lp"]}.')
elif 14 < i <= 19:
    print(f'Ate 19 anos, categoria {cores["am"]}Junior{cores["lp"]}.')
elif 19 < i <= 25:
    print(f'Ate 25 anos, categoria {cores["li"]}Senior{cores["lp"]}.')
else:
    print(f'Acima de 25 anos, categoria {cores["peb"]}Master{cores["lp"]}.')



