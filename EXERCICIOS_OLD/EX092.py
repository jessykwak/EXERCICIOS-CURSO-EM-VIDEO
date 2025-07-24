'''from datetime import date
pessoas = {}
lista = []
hoje = date.today()
anohj = hoje.year
while True:
    pessoas["nome"] = str(input('Digite o seu nome: '))
    pessoas["ano"] = int(input('Digite o ano em que nasceu: '))
    ctsp = int(input('Possui carteira de trabalho, digite \n'
                     '0 - para nao \n'
                     '1 - para sim '))
    if ctsp == 1:
        pessoas["anotrab"] = int(input('Digite em que ano vc foi contratador: '))
        pessoas["salario"] = int(input('Digite seu salario: '))
    else:
        pessoas["anotrab"] = anohj
        pessoas["salario"] = 0

    anoapo = anohj - pessoas["anotrab"]
    idade = anohj - pessoas["ano"]

    print(f'Voce possui {idade} anos,', end='')
    pessoas["aposent"] = idade + (35-anoapo)
    print(f'e podera se aposentar com {pessoas["aposent"]} anos')
    lista.append(pessoas.copy())
    d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while d not in 'SsNn':
        print('OPCCAO INVALIDA.')
        d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if 'N' == d:
        break
print(lista)'''
from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
dados["nasc"] = int(input('Ano Nascimento: '))
dados["idade"] = datetime.now().year - dados["nasc"]
dados["ctps"] = int(input('Possui carteira de trabalho, digite \n'
                         '0 - para nao tenho '))
if dados["ctps"] != 0:
    dados["contratacao"] = int(input('Digite em que ano vc foi contratador: '))
    dados["salario"] = int(input('Digite seu salario: '))
    dados["aposentadoria"] = dados["idade"] + ((35+dados["contratacao"])-datetime.now().year)

for k,v in dados.items():
    print(f' - {k} tem o valor {v}')
