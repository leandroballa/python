# Três retas formam um triangulo?
r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
l1 = (r2 % r3) < r1 < (r2 + r3)
l2 = (r3 % r1) < r2 < (r3 + r1)
l3 = (r1 % r2) < r3 < (r1 + r2)

if l1 and l2 and l3:
    print('É possivel formar um triangulo')
else:
    print('Não é possivel formar um triangulo')
