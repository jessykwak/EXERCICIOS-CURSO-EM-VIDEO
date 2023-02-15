def moeda(din):
    return f'R$ {float(din):.2f}'


def aumentar(din, por, f=True):
    if f == True:
        return f'{moeda(din*(1+(por/100)))}'
    else:
        return f'{din*(1+(por/100))}'
    
    
def diminuir(din, por, f = True):
    if f == True:
        return f'{moeda(din*(1-(por/100)))}'
    else:
        return f'{din*(1-(por/100))}'
    
    
def dobro(din, f=True):
    if f == True:
        return f'{moeda(din*2)}'
    else:
        return f'{din*2}'
    
    
def metade(din, f=True):
    if f == True:
        return f'{moeda(din/2)}'
    else:
        return f'{din/2}'


def resumo(din, aum, dim):
    print('='*40)
    print(f'{"RESUMO DO VALOR":^40}')
    print('='*40)
    print(f'{"Preco analisado":<30}', end='')
    print(f'{moeda(din):>10}')
    print(f'{"Dobro do preco":<30}', end='')
    print(f'{dobro(din,True):>10}')
    print(f'{"Metade do preco":<30}', end='')
    print(f'{metade(din,True):>10}')
    print(f'{aum}% {"de aumento preco":<26}', end='')
    print(f'{aumentar(din,aum,True):>10}')
    print(f'{dim}% {"de reducao preco":<26}', end='')
    print(f'{diminuir(din,dim,True):>10}')
    print('='*40)
    