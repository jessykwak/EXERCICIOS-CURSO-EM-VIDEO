from ex107ao111 import moeda2
    
p = float(input('Digite o preco: R$ '))
print(f'A metade de {moeda2.moeda(p)} eh {moeda2.metade(p, True)}')
print(f'O dobro de {moeda2.moeda(p)} eh {moeda2.dobro(p, True)}')
print(f'Aumentando {moeda2.moeda(p)} em 10% temos {moeda2.aumentar(p, 10, True)}')
print(f'Diminuindo {moeda2.moeda(p)} em 13% temos {moeda2.diminuir(p, 13, True)}')
