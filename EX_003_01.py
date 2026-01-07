#abaixo, os números não somam, eles são printados em sequencia
num1 = input("Digite um valor: ")
num2 = input("Digite outro valor: ")
soma = num1+num2
#uma opcao era fazer ssoma = int(n1)+int(n2)
print("A soma entre {} e {} é igual a {}".format(num1, num2, soma))
print(type(num1))
print(type(num2))
print(type(soma))

#para somar, é necessário identificar o tipo da variável
#no caso, INT ou FLOAT

num1 = float(input("Digite um valor: "))
num2 = int(input("Digite outro valor: "))
soma = num1+num2

print(type(num1))
print(type(num2))
print(type(soma))
print("A soma entre {} e {} é igual a {}".format(num1, num2, soma))
print("A soma é igual a {}".format(num1+num2))

#tipos: INT(numeros inteiros), FLOAT(numeros reais), STR(string, conjunto de CHARs), BOOL(valores logicos, True/False)