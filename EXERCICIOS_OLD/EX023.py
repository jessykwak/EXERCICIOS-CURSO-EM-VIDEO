#n = str(input('Digite um número de 0 a 9999: '))

#print(f'unidade: {n[3]}')
#print(f'dezena: {n[2]}')
#print(f'centena: {n[1]}')
#print(f'milhar: {n[0]}')

n = int(input('Digite um número de 0 a 9999: '))

u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10

print(f'unidade: {u}\n'
      f'dezena: {d}\n'
      f'centena: {c}\n'
      f'milhar: {m}')