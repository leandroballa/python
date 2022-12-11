while True:
    print('Para sair digite qualquer número negativo!')
    num = int(input('Digite um número: '))
    if num < 0:
        break
    for x in range(1, 11):
        print(f'{x:2} x {num:2} = {x*num:3}')