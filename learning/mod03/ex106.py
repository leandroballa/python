def exibir(msg, cor='\033[m'):
    tam = len(msg) + 2
    print(f'{cor}~' * tam)
    print(f' {msg} ')
    print(f'~' * tam)


def exibeHelp(bib):
    exibir(f'Acessando o manual do comando "{bib}"', '\033[30;44m')
    print('\033[7;30m')
    help(bib)


while True:
    exibir('Sistema de ajuda PyHelp', '\033[30;43m')
    funct = str(input(f'\033[mFunção ou Biblioteca: '))
    if funct == 'FIM':
        break
    exibeHelp(funct)
exibir('Fim')
