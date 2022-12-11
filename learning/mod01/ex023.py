num = int(input(('Digite um número entre 0 e 9999: ')))
'''if len(num) == 4:
    print('Unidade', num[3])
    print('Dezena', num[2])
    print('Centena', num[1])
    print('Milhar', num[0])
elif len(num) == 3:
    print('Unidade', num[2])
    print('Dezena', num[1])
    print('Centena', num[0])
elif len(num) == 2:
    print('Unidade', num[1])
    print('Dezena', num[0])
elif len(num) == 1:
    print('Unidade', num[0])'''
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade', u)
print('Dezena', d)
print('Centena', c)
print('Milhar', m)
