import datetime

pessoa = dict()
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = datetime.datetime.today().year - int(input('Anos de nascimento: '))
pessoa['ctps'] = str(input('Carteira de trabalho: [0 nao tem] '))
if pessoa['ctps'] != '0':
    pessoa['contratacao'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário R$'))
    pessoa['aposenta'] = pessoa['idade'] + 35
for p, v in pessoa.items():
    print(f'{p} tem o valor {v}')
