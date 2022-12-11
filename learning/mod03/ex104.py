def leiraInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
             ok = True
        else:
            print('ERRO! Não é um número.')
        if ok:
            print(f'Você acabou de digitar o número {n}')
            break


leiraInt('Digite um número: ')

# MINHA SOLUÇÃO
'''def leiaInt():
    ret = ''
    while True:
        num = str(input('Digite um número: '))
        for x in num:
            if x in '0123456789':
                ret = 'É um número'
            else:
                ret = 'Não é um número. Tente novamente'
                print(ret)
                break
        if ret == 'É um número':
            break
    return ret


print(leiaInt())'''
