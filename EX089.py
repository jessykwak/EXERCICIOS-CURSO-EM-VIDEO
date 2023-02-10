'''listona = []
lista = []
while True:
    nome = str(input('Nome do aluno: ')).capitalize()
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    lista.append(nome)
    lista.append(n1)
    lista.append(n2)
    listona.append(lista[:])
    lista.clear()
    continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break
    elif continua not in 'Ss':
        print('OPCAO INVALIDA')
        continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
print(f'=' * 10)
print('SISTEMA NOTAS')
print('=' * 10)
for x in range(0,len(listona)):
    print('=' * 10)
    print(f'ALUNO N°{x+1}: {listona[x][0]}')
    print(f'NOTA 1: {listona[x][1]:.2f}')
    print(f'NOTA 2: {listona[x][2]:.2f}')
    print(f'MEDIA: {(listona[x][1]+listona[x][2])/2:.2f}')
print('=' * 10)
print('BOLETIM')
print('=' * 10)
while True:
    q = int(input('Gostaria de ver as notas de qual aluno? '))
    print(f'ALUNO N°{q}: {listona[q-1][0]}')
    print(f'NOTA 1: {listona[q-1][1]:.2f}')
    print(f'NOTA 2: {listona[q-1][2]:.2f}')
    print(f'MEDIA: {(listona[q-1][1]+listona[x][2])/2:.2f}')
    continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break
    elif continua not in 'Ss':
        print('OPCAO INVALIDA')
        continua = str(input('Deseja continuar? [S/N]')).strip().upper()[0]'''

ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2)/2
    ficha.append([nome, [nota1,nota2],media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('='* 30)
print(f'{"No.":<3}{"NOME":<30}{"MEDIA":>8}')
print('='* 30)

for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*30)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe)'))
    if opc == 999:
        print('Finalizando.')
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} sao {ficha[opc][1]}')
print('<<< VOLTE SEMPRE >>>')
