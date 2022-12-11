# Minha solução
'''termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
print('{}->'.format(termo), end='')
tot = termo
x = 10
p = ''
while x != 0:
    for xx in range(0, x):
        p += '{}->'.format(tot+razao)
        tot += razao
    print(p)
    x = int(input('\nQuantos termos mais deseja exibir? '))'''
prim = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
termo = prim
count = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while count <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        count += 1
    print('PAUSA')
    mais = int(input('Quantos termos mais deseja exibir?'))
