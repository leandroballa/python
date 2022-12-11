stop = 'S'
count = med = val = maior = menor = 0
while stop == 'S':
    val = int(input('Digite um valor: '))
    med += val
    if count == 0:
        maior = val
        menor = val
    else:
        if val > maior:
            maior = val
        if val < menor:
            menor = val
    count += 1
    stop = str(input('Deseja continuar? [S/N]: ')).upper()
med = med/count
print('Foram digitados {} números, cujá média é {}'.format(count, med))
print('O maior número foi {} e o menor {}'.format(maior, menor))