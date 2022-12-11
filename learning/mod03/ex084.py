dados = list()
pessoas = list()
maiorPeso = list()
menorPeso = list()
maiorP = menorP = 0
while True:
    dados.append(str(input('Digite o nome da pessoa: ')).strip())
    dados.append(float(input('Digite o peso da pessoa: ')))
    pessoas.append(dados[:])
    dados.clear()
    if str(input('Deseja continuar? [S/N] ')).strip().upper() in 'Nn':
        break

print(f'Foram cadastradas {len(pessoas)}')
for x, p in enumerate(pessoas):
    if x == 0:
        maiorP = menorP = p[1]
    else:
        if p[1] > maiorP:
            maiorP = p[1]
            maiorPeso.clear()
            maiorPeso.append(p[0])
        elif p[1] == maiorP:
            maiorPeso.append(p[0])

        if p[1] < menorP:
            menorP = p[1]
            menorPeso.clear()
            menorPeso.append(p[0])
        elif p[1] == menorP:
            menorPeso.append(p[0])
print(f'O maior peso foi {maiorP}. Peso de {maiorPeso}')
print(f'O menor peso foi {menorP}. Peso de {menorPeso}')
