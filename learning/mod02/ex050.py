s = 0
for x in range (0, 6):
    n = int(input('Digite um valor: '))
    if (n%2) == 0:
        s += n
print('O total da soma dos números pares é {}'.format(s))
