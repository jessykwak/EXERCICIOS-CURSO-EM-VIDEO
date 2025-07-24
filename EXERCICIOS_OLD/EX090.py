aluno = {}
aluno['nome'] = str(input('Nome: ')).capitalize().strip()
aluno['media'] = float(input('Media: '))

if aluno['media'] >= 7:
    aluno['situacao'] = 'APROVADO'
elif 5 <= aluno['media'] < 7:
    aluno['situacao'] = 'RECUPERACAO'
else:
    aluno['situacao'] = 'REPROVADO'
#print('='*30)
#print(f'O nome eh: {aluno["nome"]}')
#print(f'A media eh: {aluno["media"]:.2f}')
#print(f'A sua situacao eh: {aluno["situacao"]}')
print('='*30)
for k,v in aluno.items():
    print(f'{k.capitalize()}: {v}')
print('='*30)
