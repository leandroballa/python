matriz = [[[], [], []], [[], [], []], [[], [], []]]
for x in range(0, 3):
    for xx in range(0, 3):
        matriz[x][xx].append(int(input(f'Digite um número para [{x}][{xx}]: ')))

for x in range(0, 3):
    for xx in range(0, 3):
        print(matriz[x][xx], end='')
    print()
