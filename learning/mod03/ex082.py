nums = list()
par = list()
impar = list()
num = 0
while True:
    num = int(input('Digite um número: '))
    nums.append(num)
    if (num % 2) == 0:
        par.append(num)
    else:
        impar.append(num)
    if str(input('Deseja continuar? [S/N]')).upper().strip()[0] == 'N':
        break
print(f'Os números digitados foram {nums}')
print(f'Foram digitados os números pares {par}')
print(f'Foram digitados os números impares {impar}')
