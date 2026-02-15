# MANIPULACAO DE TEXTO
# textos sao cadeia de texto, cadeia dew caracteres, string 

frase = 'Curso em video Python'
# cada letra ocupa um indice que começa do 0

# FATIAMENTO (pegar pedaços)
print(frase[9])
print(frase[9:13]) #do 9 ate o 13, sem o 13, ou seja 4 caracteres
print(frase[9:21])
print(frase[9:21:3]) #printa do 9 ao 21 pulando 3 e printa o 3
print(frase[:5]) #printa do zero ao indice 4
print(frase[15:]) #printa do indice 15 ate o ultimo
print(frase[9::3]) #do 9 ate o final pulando 3
print(frase[:9:3])

print(len(frase)) #printa o tamanho da frase considerando o \0
print(frase.count('o')) #vai contar qtd de 'o'
print(frase.count('o',0,13)) #vai contar qtd de 'o' do indice 0 ao 13 (lembrando q o ultimo nao conta)
print(frase.find('deo')) #fala onde o 'deo' começa na frase (em q indice)
print(frase.find('Android')) #-1 = nao existe nessa string
print('Curso' in frase) #responde true or false

#TRANSFORMAÇAO

frase = "Curso em Python e Python"
print(frase.replace('Python', 'Android')) #trocar onde tiver Python por Android
print(frase.upper()) #troca pra maiuscula (TUDO)
print(frase.lower()) #troca TUDO pra minuscula
print(frase.capitalize()) #maiuscula soh na 1 letra
print(frase.title()) #maiuscula das 1 letras de todas palavras

frase = "   Aprenda Python  "
print(frase)
print(frase.strip()) #remove espaços no começo e final da frase
print(frase.rstrip()) #remove espaços soh da direita(right) no final da frase
print(frase.lstrip()) #remove espaços soh da esquerda(left) no começo da frase
print(frase.capitalize()) #tem questoes! pq nao eh o 1 caractere

#DIVISAO

frase = 'Curso em video Python'

print(frase.split()) #separa a frase em palavras dentro d uma lista
#detalhe: uma string eh imutavel, a nao ser q vc salve a alteracao em cima
frase2 = frase.replace("video", "porquinho")
print(frase2)
print(frase)
print('-'.join(frase)) #bota um '-' ou outro caracter entre cada caractere da lista

print("""mds tenho q escrever um texto bem grante q eu nao sei c qria escrever
e ainda tenho q pular pra ver como fica e se eu nao pular dessa vez como q vai ficar aqui? vai printar uma frase enorme q vai sair da tela?
ora ora ora e qual foi o resultado?
ueh mas entao fica esse tava ai na frente das frases q pularam? ueh
ah, basta eu apagar o tab q ta na frente lol""")

# exercicios 22 ao 27

