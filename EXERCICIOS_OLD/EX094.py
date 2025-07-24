pessoas = {}
listona = []
listinha = []
soma = media = 0
lista = []
while True:
    pessoas["nome"] = str(input('Digite o nome: ')).strip().capitalize()
    pessoas["sexo"] = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    while pessoas["sexo"] not in 'MF':
        print('OPCCAO INVALIDA.')
        pessoas["sexo"] = str(input('Digite o sexo [M/F]: ')).strip().upper()[0]
    pessoas["idade"] = int(input('Digite a idade: '))
    listona.append(pessoas.copy())
    soma += pessoas["idade"]
    d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    while d not in 'SsNn':
        print('OPCCAO INVALIDA.')
        d = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if 'N' == d:
        break
media = soma/len(listona)
for n in range(0,len(listona)):
    if listona[n]["idade"] > media:
        lista.append(listona[n]["nome"])
    if listona[n]["sexo"] in 'Ff':
        listinha.append(listona[n]["nome"])

print(listona)
print('='*70)
print(f'Foram cadastradas {len(listona)} pessoas.')
print(f'A media das idades eh de {media:.2f} anos.')
print(f'As mulheres sao: {listinha}.')
print(f'As pessoas com idade acima da media sao: {lista}.')
print('='*70)