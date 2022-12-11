name = str(input('Digite seu nome completo: ')).strip()
lista = name.split()
print('Seu primeiro nome é: {}'.format(lista[0]))
print('Seu ultimo nome é: {}'.format(lista[len(lista)-1]))
