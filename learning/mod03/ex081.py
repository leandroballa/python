nums = list()
cinco = False
while True:
    nums.append(int(input('Digite um número: ')))
    cinco = 5 in nums
    if str(input('Deseja continuar? [S/N]')).upper().strip()[0] == 'N':
        break
print(f'Foram digitados {len(nums)} números')
nums.sort(reverse=True)
print(f'A ordenação decrescente dos números é {nums}')
print(f'O valor 5 {"foi digitado " if cinco else "não foi digitado"}')

