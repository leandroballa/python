frase = input('Digite qualquer coisa para saber se é um Palíndromo: ')
frase = frase.replace(' ', '')
r = True
for x in range(0, len(frase)):
    if frase[x].upper() != frase[len(frase)-(x+1)].upper():
        r = False
if r:
    print('É um Palíndromo')
else:
    print('Não é um Palíndromo')
