import math

a = float(input('Informe o angulo: '))
b = math.radians(a)
cos = math.cos(b)
sen = math.sin(b)
tg = math.tan(b)

print(f'O seno de {a} é = {sen:.2f}, o cosseno é {cos:.2f} e a tangente é {tg:.2f}.')