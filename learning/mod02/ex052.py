n = int(input('Digite um numero: '))
r = 0
p = True
for x in range(n-1, 1, -1):
    r = n % x
    if r == 0:
        p = False
if p:
    print('O número {} é primo'.format(n))
else:
    print('O número {} NÃO é primo'.format(n))
