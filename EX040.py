n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informa a segunda nota: '))
m = (n1+n2)/2

if m < 5:
    print(f'A media e: {m:.2f}, o aluno esta reprovado.')
elif 5 <= m < 7.0:
    print(f'A media e: {m:.2f}, o aluno esta de recuperacao.')
elif m >= 7:
    print(f'A media e: {m:.2f}, o aluno esta aprovado.')
