f = str(input('Digite uma frase: ')).strip()

print(f"Na frase, encontramos a letra a {f.lower().count('a')} vezes")
print(f"A posição do primeiro a é: {f.lower().find('a')+1}")
print(f"A posição do último a é: {f.lower().rfind('a')+1}")
