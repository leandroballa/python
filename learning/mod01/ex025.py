name = str(input('Digite o seu nome completo: ')).strip()

# if name.upper().find('SILVA') >= 0:
if 'SILVA' in name.upper():
    print('Seu nome possui Silva')
else:
    print('Seu nome não possui Silva')
