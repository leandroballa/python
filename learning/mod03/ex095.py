jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for x in range (0, tot):
        partidas.append(int(input(f'Quantos gols na partida {x}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break

print('-=' * 30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<25}', end='')
print()
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15} ', end='')
    print()
print('-' * 40)
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador com esse código {busca}')
    else:
        print(f'-- Levantamento do jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'No jogo {i+1} fez {g} gols.')
    print('-' * 40)
print(('Volte sempre!'))
# Minha solução
'''jogador = dict()
partidas = list()
todos = list()
totGols = countPart = 0
while True:
    print('-' * 40)
    jogador['nome'] = str(input('Nome: '))
    part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for x in range (0, part):
        partidas.append(int(input(f'Quantos gols na partida {x}: ')))
        totGols += partidas[x]
        countPart += 1
    jogador['gols'] = partidas[:]
    jogador['total'] = totGols
    jogador['partidas'] = countPart
    todos.append(jogador.copy())
    partidas.clear()
    totGols = countPart = 0
    if str(input('Deseja continuar? [S/N] '))[0].upper() in 'Nn':
        break;
print('-=' * 20)
print(f'{"cod":<3} {"nome":<15} {"gols":<15} {"total":<5}')
print('-' * 40)
for x, v in enumerate(todos):
    print(f'{x:<3} {v["nome"]:<15} {str(v["gols"]):<15} {v["total"]:<5}')
print('-' * 40)
while True:
    jog = int(input('Mostras dados de qual jogador? [999 para parar] '))
    if jog == 999:
        break
    elif jog >= 0 and jog < len(todos):
        print(f'LEVANTAMENTO DO JOGADOR {todos[jog]["nome"]}')
        for x, g in enumerate(todos[jog]['gols']):
            print(f'No jogo {x} fez {g}')
    else:
        print('Jogador não existe. Tente novamente')
print('-='*10, 'FIM', '-='*10)'''
