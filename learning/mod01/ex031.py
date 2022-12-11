dis = float(input('Quantos quilometros tem a viagem? '))
if dis >= 200:
    print('O valor da passagem é de R${:.2f}'.format(dis*0.50))
else:
    print('O valor da passagem é de R${:.2f}'.format(dis * 0.45))
