def ficha(jog='<DESCONHECIDO>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)

# Minha solução
'''def ficha(nome='<DESCONHECIDO>', gols='0'):
    return str(f'O jogador {nome}, fez {gols} gols')


jog = str(input('Nome do jogador: '))
gol = input('Quantidade de gols marcados: ')
if jog == '' and gol == '':
    print(ficha())
elif jog != '' and gol == '':
    print(ficha(jog))
elif jog == '' and gol != '':
    print(ficha(gols=gol))
else:
    print(ficha(jog, gol))'''
