#from datetime import datetime


def voto(ano):
    from datetime import datetime
    idade = datetime.now().year - ano
    if idade < 16:
        return f'Com {idade} anos, o VOTO EH NEGADO.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos, o VOTO EH OBRIGATORIO.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos, o VOTO EH OPICIONAL.'


data = int(input('Em que ano voce nasceu? '))
print(f'{voto(data)}')
