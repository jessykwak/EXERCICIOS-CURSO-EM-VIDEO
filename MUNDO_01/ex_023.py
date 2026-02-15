# EXERCICIO 023:
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados.
# Ex: Digite um numero: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1
# fazer como string e matematicamente.

num = int(input("Digite um numero de 0 a 9999: "))

unidade = num // 1 % 10
dezena = num // 10 % 10
centena = num // 100 % 10
milhar = num // 1000 % 10

print('unidade: {} dezena: {} centena: {} milhar: {}'.format(unidade, dezena, centena, milhar))


nums = str(input("Digite um numero de 0 a 9999: "))

if (nums.isnumeric() == True): #checando c eh numerico, mas nao fiz em caso d erro
    if (len(nums) == 1):
        print('unidade: {}'.format(nums[0]))
    elif (len(nums) == 2):
        print('unidade: {}, dezena: {}'.format(nums[1], nums[0]))
    elif (len(nums) == 3):
        print('unidade: {}, dezena: {}, centeza: {}'.format(nums[2], nums[1], nums[0]))
    elif (len(nums) == 4):
        print('unidade: {}, dezena: {}, centeza: {}, milhar: {}'.format(nums[3], nums[2], nums[1], nums[0]))


