x = input('Digite algo: ')
print('Você digitou {}'.format(x))
print('{} é do tipo {}'.format(x, type(x)))
print('{} é minusculo {}'.format(x, x.islower()))
print('{} é maisculo {}'.format(x, x.isupper()))
print('{} é um número {}'.format(x, x.isnumeric()))
