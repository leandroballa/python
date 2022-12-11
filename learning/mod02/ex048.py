s = 0
for x in range(1, 501, 2):
    if (x % 3) == 0:
        s += x
print('A soma dos números impares multiplos de 3 é {}'.format(s))
