p = float(input('Informe o seu peso em kg: '))
h = float(input('Informe a sua altura em m: '))
imc = p / (h*h)

cores = {'lp':'\033[m','az':'\033[34m','am':'\033[33m','peb':'\033[7;30m', 'vd':'\033[32m', 'li':'\033[35m', 'vm':'\033[31m'}

if imc < 18.5:
    print(f'Seu IMC e {cores["li"]}{imc:.2f}{cores["lp"]}, esta na faixa {cores["az"]}Abaixo do peso{cores["lp"]}.')
elif 18.5 <= imc <= 25:
    print(f'Seu IMC e {cores["li"]}{imc:.2f}{cores["lp"]}, esta na faixa {cores["vd"]}Peso ideal{cores["lp"]}.')
elif 25 < imc < 30:
    print(f'Seu IMC e {cores["li"]}{imc:.2f}{cores["lp"]}, esta na {cores["am"]}faixa Sobrepeso{cores["lp"]}.')
elif 30 <= imc < 40:
    print(f'Seu IMC e {cores["li"]}{imc:.2f}{cores["lp"]}, esta na faixa {cores["vm"]}Obesidade{cores["lp"]}.')
else:
    print(f'Seu IMC e {cores["li"]}{imc:.2f}{cores["lp"]}, esta na faixa {cores["peb"]}Obesidade morbida{cores["lp"]}.')

