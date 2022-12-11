import random
jogos = list()
nums = list()
print('-'*40)
print(f'{"Mega Sena":^40}')
print('-'*40)
n = int(input('Quantos jogos você deseja sortear: '))
print('-'*40)
for x in range(0, n):
    for xx in range(0, 6):
        while True:
            n = random.randint(0, 60)
            if n not in nums:
                nums.append(n)
                break
    nums.sort()
    jogos.append(nums[:])
    nums.clear()

for x, j in enumerate(jogos):
    print(f'{x+1}º jogo: {j}')
print('-'*40)
print(f'{"Boa Sorte":^40}')
print('-'*40)
