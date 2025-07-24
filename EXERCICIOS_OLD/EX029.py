v = float(input('Qual velicidade do carro em km/h? '))
m = (v-80)*7

if v>80: #condicao simples, sem necessidade do else
    print('\nAcima da velocidade limite!')
    print(f'O valor da multa é de: {m:.2f} reais')
print('\nA velocidade esta dentro do limite.')
