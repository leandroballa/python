import random

comp = random.randint(0,10)
usu = -1
cont = 0
while usu != comp:
    usu = int(input("Digite um numero entre 0 e 10: "))
    cont += 1
print('Você acertou após {} tentativas'.format(cont))