def fatorial(n=1, show=True):
    """ CALCULA O FATORIAL DE UM NUMERO
    n = numero calculado
    show = mostrar ou nao a conta"""
    f = 1
    if show == True:
        print(f'{n}! =', end='')
        for c in range(n,0,-1):
            print(f' {c}', end='')
            f *= c
            if c > 1:
                print(f' x', end='')
        print(f' = {f}')
    else:
        for c in range(n,0,-1):
            f *= c
        return f'{n}! = {f}'


fatorial(4)
print(f'{fatorial(7, False)}')
help(fatorial)