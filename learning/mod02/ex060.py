# Forma rezumida utilizando lib
# from math import factorial
# n = int(input('Digite um numero: '))
# f = factorial(n)
# print('O fatorial de {} é {}'.format(n, f))

# Minha solução
'''n = int(input('Digite um número: '))
r = 1
t = '{}! ='.format(n)
while n > 0:
    r = r * n
    t += '{}'.format(n)
    n -= 1
    if n == 0:
        t += '={}'.format(r)
    else:
        t += '*'
print(t)'''

# Solução da aula
n = int(input('Digite um número: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))