f = str(input('Digite uma frase: ')).strip()
f2 = f.replace(' ', '')
f3 = f2.lower()
ff = f3[::-1]

if f3 == ff:
    print('ESSA FRASE EH UM PALINDROMO!')
else:
    print('ESSA EH UMA FRASE ORDINARIA, SEM NADA DE ESPECIAL')
