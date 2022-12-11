num = [[], []]
for x in range(1, 7):
    n = int(input(f'Digete o {x}º número: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Os números pares são {num[0]}')
print(f'Os números impares são {num[1]}')
