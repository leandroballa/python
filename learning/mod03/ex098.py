def contagem(inicio, fim, passo):
    print('-=' * 30)
    if passo == 0:
        passo = 1
    if passo > 0 and inicio < fim:
        print(f'Contando de {inicio} até {fim} de {passo} em {passo}')
        for x in range(inicio, fim+1, passo):
            print(f'{x}', end=' ')
    else:
        print(f'Contando de {fim} até {inicio} de {passo} em {passo}')
        for x in range(fim, inicio-1, passo):
            print(f'{x}', end=' ')
    print()


contagem(1, 10, 1)
contagem(0, 10, -2)
print('Agora é sua vez de personalizar')
contagem(int(input('Inicio: ')), int(input('Fim: ')), int(input('Passo: ')))
