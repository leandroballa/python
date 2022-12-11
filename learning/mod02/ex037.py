n = int(input('Digite um número inteiro? '))
x = int(input('Deseja converter o número para qual base? [1-Binário/2-Octal/3-Hexadecimal: '))
if x == 1:
    print('O número {} convertido para Binário é {}'.format(n, bin(n)))
elif x == 2:
    print('O número {} convertido para Octal é {}'.format(n, oct(n)))
elif x == 3:
    print('O número {} convertido para Hexadecimal é {}'.format(n, hex(n)))
else:
    print('Opção inválida!')
