import datetime

nasc = int(input('Digite o ano de nascimento do atleta: '))
anos = datetime.date.today().year - nasc

if anos <= 9:
    print('Mirim')
elif anos <=14:
    print('Infantil')
elif anos <= 19:
    print('Junior')
elif anos <= 20:
    print('Sênior')
else:
    print('Master')