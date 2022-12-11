from random import randint

num = (randint(1, 10), randint(1, 10), randint(1, 10)
       , randint(1, 10), randint(1, 10))
# Minha solção
'''
max = min = 0
for x in range(0, len(num)):
    if x == 0:
        max = num[x]
        min = num[x]
    else:
        if num[x] < min:
            min = num[x]
        if num[x] > max:
            max = num[x]
print(f'O computador sorteou os número: {num}')
print(f'O maior numéro digitado foi {max} e o menor foi {min}')'''
print(f'O computador sorteou os número: {num}')
print(f'O maior numéro digitado foi {max(num)} e o menor foi {min(num)}')
