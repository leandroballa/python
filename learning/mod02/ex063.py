# Minha solução
'''n = 1
q = int(input('Quantos elementos de Fibonnaci deseja ver? '))
count = 0
n2 = 0
n3 = 0
while count < q:
    print(n)
    n2 = n3 + n
    n3 = n
    n = n2
    count += 1'''
qtde = int(input('Quantos níveis de Fibonnaci deseja vizualisar? '))
t1 = 0
t2 = 1
print('{} - {}'.format(t1, t2), end='')
count = 3
while count <= qtde:
    t3 = t1 + t2
    print(' - {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1
print(' - FIM')
