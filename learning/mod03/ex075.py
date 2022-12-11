num = (int(input('Digite um numero: '))
       , int(input('Digite outro número: '))
       , int(input('Digite mais um número: '))
       , int(input('Digite o ultimo número: ')))
print(f'Você digitou os números: {num}')
# Minha solução
'''cNove = cTres = 0
divDois = ''
for n in range(0, len(num)):
    if num[n] == '9':
        cNove += 1
    if num[n] == '3':
        cTres += 1
    if int(num[n]) % 2 == 0:
        divDois += num[n] if divDois == '' else f', {num[n]}'
print(f'O número 9 aparece {cNove} vezes')
print(f'O número 3 aparece {cTres} vezes')
print(f'O números pares foram {divDois}')'''

print(f'O número 9 aparece {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)}ª posição')
else:
    print('O valor 3 não foi digitado nenhuma vez')
print(f'O números pares foram ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
