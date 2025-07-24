from ex107ao111 import moeda
    
p = float(input('Digite o preco: R$ '))
print(f'A metade de {moeda.moeda(p)} eh {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {p} eh {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando {p} em 10% temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Diminuindo {p} em 13% temos {moeda.moeda(moeda.diminuir(p, 13))}')
