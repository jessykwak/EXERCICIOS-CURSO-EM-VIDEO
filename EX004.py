x = input('Digite algo: ')
print("O tipo primitivo é {}.\n"
      "É um número? {}.\n"
      "É uma letra? {}.\n"
      "É alfanumérico? {}.\n"
      "Está em maiúscula? {}.\n"
      "Está em minúscula? {}.\n"
      "É um decimal? {}.\n"
      "Só tem espaços? {}.\n"
      "Está capitalizada? {}.".format(type(x), x.isnumeric(), x.isalpha(), x.isalnum(), x.isupper(), x.islower(), x.isdecimal(), x.isspace(), x.istitle())
      )

y = input('Digite algo: ')
print('O tipo primitivo é:',{type(y)})
print('é um número?', y.isnumeric())
print('é uma letra?', y.isalpha())
print('é alfanumérico?', y.isalnum())
print('está em maiuscula?', y.isupper())
print('está em minuscula?', y.islower())
print('é um decimal?', y.isdecimal())
print('só tem espaço?', y.isspace())
print('está capitalizada?', y.istitle())

