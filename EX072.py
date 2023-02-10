tupla = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

'''
while True:
    p = int(input('Digite um numero de 0 a 20: '))
    if 0 <= p <= 20:
        print(f'O numero digitado, {p}, se escreve "{tupla[p]}" em extenso.')
    else:
        print('ENTRE 0 E 20, BOÇAL!!! TENTE DE NOVO.')
    c = str(input('Gostaria de continuar? [S/N]')).strip().capitalize()[0]
    if c == 'N':
        print('falow mane!')
        break
'''
while True:
    num = int(input('Digite um numero entre 0 e 20: '))
    if 0 <= num <= 20:
        break
    print('Tente novamente.')
print(f'Voce digitou o numero {tupla[num]}.')
