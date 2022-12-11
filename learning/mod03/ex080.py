nums = list()
# index = 0
for x in range(0, 5):
    num = int(input('Digite um número: '))
    if num in nums:
        print('Valor duplicado. Não posso cadastra-lo!')
    else:
        if len(nums) == 0:
            nums.append(num)
        else:
            pos = 0
            while pos < len(nums):
                if num <= nums[pos]:
                    nums.index(pos, num)
                pos += 1
        # Minha solução
        '''else:
            index = len(nums)
            for c in range(len(nums)-1, -1, -1):
                if num < nums[c]:
                    index = c
            nums.insert(index, num)'''
print(nums)
