# import nome_biblioteca -> importa a biblioteca inteira
# from nome_biblioteca import nome_do_q_vc_qr -> importa 1 item especifico da biblioteca
# biblioteca math -> funcoes de matematica extras
# funcoes da biblioteca math: ceil (para arredondar pra cima)
# 							  floor (para arredondar pra baixo)
# 							  trunc (eliminar da virgula pra frente? ou tras? sem arredondamento)
# 							  pow
# 							  sqrt
# 							  factorial, entre outros

# # import math
# from math import sqrt, ceil, floor
# n = int(input('Digite um numero: '))
# # r = math.sqrt(n)
# r = sqrt(n)

# print(r)
# # print('{:.2f}'.format(math.ceil(r)))
# print('{:.2f}'.format(ceil(r)))
# print('{:.2f}'.format(floor(r)))

import random
import emoji
n = random.random()
n1 = random.randint(1,10)

print(n*10)
print(n1)
print(emoji.emojize('Ola mundo :earth_americas:', use_aliases=True))
