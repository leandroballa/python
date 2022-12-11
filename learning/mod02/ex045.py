import random
import math

math.sqrt()

usu = int(input('Qual opção você escolhe: [0-Pedra/1-Papel/2-Tesoura] '))
com = random.randint(0,1)
lis = ['Pedra', 'Papel', 'Tesoura']
print('-'*50)
print('Você escolheu {} e o computador escolheu {}'.format(lis[usu-1], lis[com-1]))
print('-'*50)
if (usu == 0 and com == 0) or (usu == 1 and com == 1) or (usu == 2 and com == 2):
    print('Empate!')
elif (usu == 0 and com == 1) or (usu == 1 and com == 2) or (usu == 2 and com == 0):
    print('Computador ganhou.')
elif (usu == 0 and com == 2) or (usu == 1 and com == 0) or (usu == 2 and com == 1):
    print('Você ganhou!')
else:
    print('Jogada inválida!')
