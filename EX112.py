from ex107ao111 import moeda
from ex107ao111 import dado


p = dado.leiaDinheiro()
print(f'A metade de {p} eh {moeda.metade(p)}')
print(f'O dobro de {p} eh {moeda.dobro(p)}')
print(f'Aumentando {p} em 10% temos {moeda.aumentar(p, 10)}')
print(f'Diminuindo {p} em 13% temos {moeda.diminuir(p, 13)}')
