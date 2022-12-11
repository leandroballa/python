import random

print('='*30)
print('Vamos joras PAR ou IMPAR')
uNum = pcNum = count = 0
uParImpar = pcParImpar = ''
while True:
    uNum = int(input('Digite um número? '))
    uParImpar = str(input('Par ou Impar? [P/I] ')).upper()
    pcNum = random.randint(1,10)
    pcParImpar = 'I' if uParImpar == 'P' else 'P'
    if uParImpar == 'P':
        if (uNum + pcNum) % 2 != 0:
            break
    else:
        if (uNum + pcNum) % 2 == 0:
            break
    count += 1
print(f'GAME OVER! Você venceu {count} vezes')
