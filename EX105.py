'''dicio = {}
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
        sit = True
        if mt >= 7:
            return 'Boa'
        elif 6 <= mt < 7:
            return 'Mazomeno'
        else:
            return 'RUIM!!!!'
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
help(notas) '''
def notas(*n, sit=False):
    """
    funcao para avaliar a situacao das notas da turma:
    n = notas, qnts vc quiser imputar
    sit = True ou False
    return = dicionario com informacoes das notas da turma
    """
    r = dict()
    r["QTD notas"] = len(n)
    r["Maior nota"] = max(n)
    r["Menor nota"] = min(n)
    r["Media notas"] = sum(n)/len(n)
    if sit:
        if r["Media notas"] >= 7:
            r["Situacao"] = 'BoA'
        elif r["Media notas"] >= 5:
            r["Situacao"] = 'RAZOAVEL'
        else:
            r["Situacao"] = 'HORROROSA!!!!'
    return r

resp = notas(5.5,2.5,9,1.5,sit=True)
print(resp)
help(notas)



