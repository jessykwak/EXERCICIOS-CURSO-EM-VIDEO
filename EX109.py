from ex107ao111 import moeda
    
p = float(input('Digite o preco: R$ '))
print(f'A metade de {moeda.moeda(p)} eh {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} eh {moeda.dobro(p, True)}')
print(f'Aumentando {moeda.moeda(p)} em 10% temos {moeda.aumentar(p, 10, True)}')
print(f'Diminuindo {moeda.moeda(p)} em 13% temos {moeda.diminuir(p, 13, True)}')
