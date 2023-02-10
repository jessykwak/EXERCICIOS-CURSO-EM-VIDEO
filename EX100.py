from random import randint

listanum = []


def sorteio():
    for x in range(0,5):
        listanum.append(randint(0,100))
    print(f'Os numros sorteados foram: {listanum}')


def somapar():
    soma = 0
    for x in listanum:
        if x % 2 == 0:
            soma += x
    print(f'A soma dos numeros pares eh: {soma}')


sorteio()
somapar()
