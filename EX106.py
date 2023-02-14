c = ('\033[m', #0 - sem cores
'\033[0;30;41m', #1 - vermelho
'\033[0;30;42m', #2 - verde
'\033[0;30;43m', #3 - amarelo
'\033[0;30;44m', #4 - azul
'\033[0;30;45m', #5 - roxo
'\033[7;30m' #6 - branco
);

def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'',4)
    help(com)



def titulo(msg, cor=0):
    tam = len(msg) +10
    print(c[cor], end='')
    print('='*tam)
    print(f'     {msg}')
    print('='*tam)
    print(c[0], end='')


comando = ''
while True:
    titulo('SISTEMA DE AJUDA HELP', 2)
    print(c[0])
    comando = str(input('Funcao ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('TCHAU!',1)

