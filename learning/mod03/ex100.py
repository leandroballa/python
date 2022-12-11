import random

lst = list()


def mensagem(msg):
    print('-' * 30)
    print(msg, end='')


def sortear():
    mensagem('Sorteando os valores ')
    for x in range(0, 5):
        lst.append(random.randint(0, 10))
        print(f'{lst[x]}', end=' ')
    print()


def somaPar():
    soma = 0
    for x in range(0, len(lst)):
        if lst[x] % 2 == 0:
            soma += lst[x]
    print(f'Somando os valores Pares de {lst} temos {soma}')


sortear()
somaPar()
