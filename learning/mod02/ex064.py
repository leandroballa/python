i = c = n = 0
while i != 999:
    i = int(input('Digite um número: [999 - Para parar] '))
    if i != 999:
        c += i
        n += 1
print('Foram digitados {} numeros e a soma entre eles é de {}'.format(n, c))
