c = s = 0
while True: #qndo while tem valor, ele testa antes d comear! por isso tem q ter o valor settado antes do while
    n = int(input('Digite um valor [999] para parar: '))
    if n == 999:
        break#forca o loop infinito while True, a parar chegando em x condicao
    c += 1
    s +=n
print(f'A soma de todos os {c} numeros digitados eh {s}')
