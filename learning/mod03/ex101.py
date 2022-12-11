def voto(i):
    import datetime
    idade = datetime.date.today().year - i
    voto = ''
    if idade < 16:
        voto = 'NEGADO'
    elif 18 < idade < 65:
        voto = 'OBRIGATÓRIO'
    elif (idade > 16 < 18) or (idade > 65):
        voto = 'OPCIONAL'

    return str(f'Com {idade} anos o voto é {voto}')


print(voto(int(input('Digite o ano de nascimento: '))))
