def maior(*nums):
    maior = 0
    for x, n in enumerate(nums):
        if x == 0:
            maior = n
        else:
            if n > maior:
                maior = n
    print('-=' * 20)
    print(f'Analisando os números {nums} o maior é {maior}')


maior(1, 2, 3, 4, 5, 6, 7, 8, 9)
maior(5, 2, 5, 3, 4, 5)