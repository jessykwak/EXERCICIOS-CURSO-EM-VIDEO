from datetime import date, timedelta

a = str(input('informe a data, mes e ano de seu nascimento: ')).strip()

if '/' in a:
    b = a.split('/')
elif ' ' in a:
    b = a.split(' ')
elif '-' in a:
    b = a.split('-')
else:
    print('Data de nascimento invalida. Tente novamente.')
c = int(f'{b[0]}')
d = int(f'{b[1]}')
e = int(f'{b[2]}')
print(f'Voce nasceu no dia {c}, do mes {d} no ano de {e}. \n')
x = date(e,d,c)

f = str(date.today())
y = f.split('-')
g = int(y[2])
h = int(y[1])
i = int(y[0])
k = date(i,h,g)
x2 = date(e+18,d,c)

w = abs(k-x)
p = str(w).split(',')
o = p[0]
u = o.split()

t = abs(x2-k)
t2 = str(t).split(',')
t3 = t2[0]
t4 = t3.split()


if e < i - 18:
    print(f'Voce esta {u[0]} dia(s) atrasado de se alistar no exercito.')
elif e == i-18:
    print('Hora de se alistar!')
elif e > i-18:
    print(f'Faltam {t4[0]} dia(s) para voce se alistar.')



