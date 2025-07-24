h = float(input('Qual a altura da parede em metros? '))
l = float(input('Qual a largura da parede em metros? '))
a = h*l
t = a/2

print('A parede tem uma área de {:.2f}m².\n'
      'Serão necessárias {:.2f}L de tinta para pintar a parede.'.format(a, t))