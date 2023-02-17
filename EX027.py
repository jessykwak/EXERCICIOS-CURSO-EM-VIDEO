n = str(input('Qual o seu nome completo? ')).strip()
s = n.split()
z = int(len(s))-1

print(f'O primeiro nome é: {s[0].capitalize()}')
print(f'O último nome é: {s[z].capitalize()}')
