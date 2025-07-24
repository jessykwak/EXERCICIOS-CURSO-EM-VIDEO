def fatorial(n=1, show=True):
    """ CALCULA O FATORIAL DE UM NUMERO
    n = numero calculado
    show = mostrar ou nao a conta"""
    f = 1
    for c in range(n,0,-1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f'{n}! = {f}'


print(f'{fatorial(4)}')
print(f'{fatorial(6, True)}')
print(f'{fatorial(7, False)}')
help(fatorial)
