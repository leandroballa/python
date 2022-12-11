jogador = dict()
partidas = list()
jogador['nome'] = str(input('Nome: '))
tot = int(input('fQuantas partidas {jogador["nome"]} jogou? '))
for x in range (0, tot):
    partidas.append(int(input(f'Quantos gols na partida {x}: ')))
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'Na partida {i}, fez {v} gols')
print(f'Foi um total de {jogador["total"]}')

# Minha solução
'''totGols = countPart = 0
jogador['nome'] = str(input('Nome: '))
part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for x in range (0, part):
    partidas.append(int(input(f'Quantos gols na partida {x}: ')))
    totGols += partidas[x]
    countPart += 1
jogador['gols'] = partidas
jogador['total'] = totGols
print('-=' * 20)
for p, v in jogador.items():
    print(f'O campo {p} tem o valor {v}')
print('-=' * 20)
print(f'O jogador {jogador["nome"]} jogou {countPart} partidas')
for p, v in jogador.items():
    if p == 'gols':
        for x, g in enumerate(v):
            print(f'Na partida {x}, fez {g} gols')
print(f'Foi um total de {jogador["total"]}')'''