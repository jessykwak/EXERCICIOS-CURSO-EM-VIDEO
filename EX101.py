from datetime import datetime

def voto():
    idade = datetime.now().year - data
    if idade < 18:
        return f'Com {idade} anos, o VOTO EH NEGADO.'
    elif 18 <= idade < 65:
        return f'Com {idade} anos, o VOTO EH OBRIGATORIO.'
    else:
        return f'Com {idade} anos, o VOTO EH OPICIONAL.'


data = int(input('Em que ano voce nasceu? '))
print(f'{voto()}')
