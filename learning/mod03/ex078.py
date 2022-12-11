nums = list()
for x in range(0,5):
    nums.append(int(input('Digite um número: ')))
print(f'Você digitou os valores {nums}')
print(f'O maior número digitado foi {max(nums)} que está na posição {nums.index(max(nums))+1}')
print(f'O maior número digitado foi {min(nums)} que está na posição {nums.index(min(nums))+1}')