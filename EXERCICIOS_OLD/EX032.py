from datetime import date
a = int(input('Digite um ano qualquer: '))
if a == 0:
    a = date.today().year

b = a % 4
c = a % 100
d = a % 400

if b == 0 and c == 0 and d == 0:
    print(f'O ano {a} e bissexto')
else:
    print(f'O ano {a} nao e bissexto.')
