def moeda(din, tipomoeda='R$'):
    return f'{tipomoeda} {float(din):.2f}'.replace('.',',')


def aumentar(din=0, por=0, f=False):
    res = din*(1+(por/100))
    if f == True:
        return moeda(res)
    else:
        return res
    
    
def diminuir(din=0, por=0, f=False):
    res = din*(1-(por/100))
    if f == True:
        return moeda(res)
    else:
        return res
    
    
def dobro(din=0, f=True):
    res = din/2
    if f == True:
        return moeda(res)
    else:
        return res
    
    
def metade(din=0, f=True):
    res = din/2
    if f == True:
        return moeda(res)
    else:
        return res


def resumo(din=0, aum=0, dim=0):
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
    

def resumo2(din=0, aum=0, dim=0):
    print('='*40)
    print(f'{"RESUMO DO VALOR".center(40)}')
    print('-'*40)
    print(f'Preco analisado: \t{moeda(din)}')
    print(f'Dobro do preco: \t{dobro(din,True)}')
    print(f'Metade do preco: \t{metade(din,True)}')
    print(f'{aum}% de aumento preco: \t{aumentar(din,aum,True)}')
    print(f'{dim}% de reducao preco: \t{diminuir(din,dim,True)}')
    print('='*40)
    