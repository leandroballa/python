# Minha solução
'''
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
f = 10
i = 1
tot = termo
while i < f:
    print('{} + {} = {}'.format(tot, razao, tot+razao))
    tot += razao
    i += 1'''
termo = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
count = 1
while count <= 10:
    print('{}'.format(termo), end='')
    termo += razao
    count += 1