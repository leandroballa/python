from random import randint
from time import sleep
# from operator import itemgetter
# ranking = list()
jogos = dict()
print('Que os jogos comecem')
sleep(1)
for x in range(1, 5):
    jogos[f'jogador{x}'] = randint(1, 6)
    print(f'O jogador{x} tirou {jogos[f"jogador{x}"]}')
    sleep(1)
print('Ranking dos jogadores')
# ranking = sorted(jogos.items(), key=itemgetter(1), reverse=True)
# for i, v enumerate(ranking):
    # print(f'{i+1}º lugar: {v[0]}.')
for x, i in enumerate(sorted(jogos, key=jogos.get, reverse=True)):
    print(f'{x+1}º lugar {i} com {jogos[i]}')
    sleep(1)
