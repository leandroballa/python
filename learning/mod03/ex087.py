matriz = [[[], [], []], [[], [], []], [[], [], []]]
sumPar = sumTerC = sumSegL = 0
for x in range(0, 3):
    for xx in range(0, 3):
        n = int(input(f'Digite um número para [{x}][{xx}]: '))
        matriz[x][xx].append(n)

for x in range(0, 3):
    for xx in range(0, 3):
        print(matriz[x][xx], end='')
        if int(matriz[x][xx][0]) % 2 == 0:
            sumPar += int(matriz[x][xx][0])
        if xx == 2:
            sumTerC += int(matriz[x][xx][0])
        if xx == 1:
            sumSegL += int(matriz[x][xx][0])
    print()

print(f'A soma dos valores pares é {sumPar}')
print(f'A soma dos valores da terceira coluna é {sumTerC}')
print(f'A soma dos valores da segunda linha é {sumSegL}')