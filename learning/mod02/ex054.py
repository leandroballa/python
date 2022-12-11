import datetime

maior = 0
menor = 0
for x in range(0, 7):
    ano = int(input('Digite o ano de nascimento: '))
    if (datetime.date.today().year - ano) > 21:
        maior += 1
    else:
        menor += 1
print('Dos 7 anos digitados, {} são maiores de idade e {} são menores de idade!'.format(maior, menor))
