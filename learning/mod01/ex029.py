velo = int(input('Velocidade do veiculo: '))

if velo > 80:
    multa = (velo - 80) * 7
    print('Veiculo multado em R${:.2f}'.format(multa))