import random

usu = int(input('Digite um valor entre 0 e 5: '))
r = random.randint(0, 5)

if r == usu:
    print('Você acertou')
else:
    print('Você errou')
