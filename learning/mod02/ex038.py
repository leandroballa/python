n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))

if n1 > n2:
    print('O número {} é maior que o número {}'.format(n1, n2))
elif n2 > n1:
    print('O número {} é maior que o número {}'.format(n2, n1))
else:
    print('Ambos os valores são iguais!')
