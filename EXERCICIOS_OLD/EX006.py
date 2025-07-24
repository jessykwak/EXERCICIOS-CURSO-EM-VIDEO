n1 = float(input('Escolha um número: '))
d = n1*2
t = n1*3
r = n1**(1/2)

print('O dobro de {} é: {}.\n'
      'O triploe de {} é: {}.\n'
      'A raiz quadrade de {} é: {}.'
      .format(n1, d, n1, t, n1, r))

print(f'O dobro de {n1} é: {d}.\n'
      f'O triplo de {n1} é: {t}.\n'
      f'A raiz quadrada de {n1} é: {r:.2f}.')
