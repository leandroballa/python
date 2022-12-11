import random

a1 = input('Digite o nome do 1º aluno: ')
a2 = input('Digite o nome do 2º aluno: ')
a3 = input('Digite o nome do 3º aluno: ')
a4 = input('Digite o nome do 4º aluno: ')
lista = [a1, a2, a3, a4]
# r = random.randrange(4)
# if r == 1:
#     print('O aluno escolhido foi {}'.format(a1))
# elif r == 2:
#     print('O aluno escolhido foi {}'.format(a2))
# elif r == 3:
#     print('O aluno escolhido foi {}'.format(a3))
# elif r == 4:
#     print('O aluno escolhido foi {}'.format(a4))
print('O aluno escolhido foi ', random.choice(lista))
