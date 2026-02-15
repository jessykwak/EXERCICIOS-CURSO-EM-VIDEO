# EXERCICIO 026:
# Faça um programa que leia uma frase pelo teclado e mostre:
# Quantas vezes aparece a letra "A".
# Em que posiçao ela aparece a primeira vez.
# Em que posicao ela aparece a ultima vez.

frase = str(input('Digite uma frase: '))

qtda = frase.count('A')
posfirst = frase.find('A') #procura do começo pro fim, se -1 -> nao existe
poslast = frase.rfind('A') #procura do fim pro começo, se -1 -> nao existe

if(qtda != 0):
    print('A frase eh: "{}",\naparece "A" {} vez(es),\na primeira vez é na posicao {},\ne a ultima vez na posicao {}'.format(frase, qtda, posfirst, poslast))
else:
    print('NAO TEM "A"!!!!')