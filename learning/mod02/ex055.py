maior = 0
menor = 0
for x in range(0, 5):
    p = float(input('Digite o peso: '))
    if x == 0:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso digitado foi {} e o menor {}'.format(maior, menor))
