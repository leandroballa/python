import datetime

nasc = int(input('Digite seu ano de nascimento: '))
anos = datetime.date.today().year - nasc

if anos < 18:
    print('Ainda vai se alistar!\nFaltam {} anos para o alistamento!'.format(18-anos))
elif anos == 18:
    print('Está na hora de se alistar!')
else:
    print('Passou o prazo de alistamento!\nPassaram-se {} anos do alistamento!'.format(anos-18))
