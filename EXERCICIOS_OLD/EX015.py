t = int(input('Quantos dias alugados? '))
s = float(input('Quantos km rodados? '))
v = (t*60)+(s*0.15)

print(f'O total a pagar é de R${v:.2f}')