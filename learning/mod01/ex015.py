d = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Quantos quilometros foram percorridos? '))
tot = (d * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(tot))
