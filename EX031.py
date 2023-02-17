d = float(input('Qual a distancia da cidade que voce quer ir, em km? '))
if d <= 200:
    print(f'A passagem ficara {d*0.5} reais.')
else:
    print(f'A passagem ficara {d*0.45} reais.')
