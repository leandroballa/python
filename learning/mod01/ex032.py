# Ano bisexto
ano = int(input('Digite um ano: '))
# r = ano % 4
# if r == 0:
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('Ano bisexto')
else:
    print('Ano não é bisexto')
