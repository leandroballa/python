nums = list()
while continuar:
    num = int(input('Digite um número: '))
    if num in nums:
        print('Valor duplicado. Não posso cadastra-lo!')
    else:
        print('Valor adicionado com sucesso.')
        nums.append(num)
    if str(input('Deseja continuar? [S/N] ')).upper().strip()[0] in 'Nn':
        break
nums.sort()
print(nums)
