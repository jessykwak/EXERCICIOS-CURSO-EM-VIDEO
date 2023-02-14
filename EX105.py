dicio = {}
def notas(qn, maxn, minn, mt, sit=False):
    """
    qn = quantidade de notas
    maxn = maior nota
    minn = menor nota
    mt = media da turma
    situacao = aprovado, reprovado, recuparacao (opicional, default = aprov)
    """
    dicio["QTD notas"] = qn
    dicio["Maior Nota"] = maxn
    dicio["Menor Nota"] = minn
    dicio["Media Turma"] = mt
    if sit in "Ss":
        if mt >= 7:
            sit = 'Boa'
        elif 6 <= mt < 7:
            sit = 'Mazomeno'
        else:
            sit = 'RUIM!!!!'
    else:
        sit = False
    dicio["Situacao"] = sit
    return dicio

n = notas(int(input('Quantidade de notas: ')), 
float(input('Digite a maior nota: ')), 
float(input('Digite a menor nota: ')), 
float(input('Qual foi a media da turma? ')), 
(input('Quer saber a situacao? [S/N] ')))

print(n)
help(notas)
