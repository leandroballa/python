# op = 0
# while op != 5:
#    n1 = float(input('Digite o primeiro número: '))
#    n2 = float(input(('Digite o segundo numero: ')))
#    op = int(input('''Escolha uma opção
#    [1] somar
#    [2] multiplicar
#    [3] maior
#    [4] novos números
#    [5] sair: '''))
#    if op == 1:
#        print('A soma de {} com {} é {}'.format(n1, n2, n1 + n2))
#    elif op == 2:
#        print('A multiplicação de {} com {} é {}'.format(n1, n2, n1 * n2))
#    elif op == 3:
#        if n1 > n2:
#            print(('{} é maior que {}'.format(n1, n2)))
#        else:
#            print(('{} é maior que {}'.format(n2, n1)))
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo numero: '))
opcao = 0
while opcao != 5:
    print('''   [1] somar
    [2] multiplicar
    [3] maior
    [4] novos números
    [5] sair: ''')
    opcao = int(input(('Digite sua opção: ')))
    if opcao == 1:
        print('A soma de {} com {} é {}'.format(n1, n2, n1 + n2))
    elif opcao == 2:
        print('A multiplicação de {} com {} é {}'.format(n1, n2, n1 * n2))
    elif opcao == 3:
        if n1 > n2:
           print(('{} é maior que {}'.format(n1, n2)))
        else:
           print(('{} é maior que {}'.format(n2, n1)))
    elif opcao == 4:
        n1 = float(input('Digite o primeiro número: '))
        n2 = float(input('Digite o segundo numero: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida')
