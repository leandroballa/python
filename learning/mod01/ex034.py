# Aumento de salário [Maiores que 1250 = 10%; Menores = 15%
sal = float(input('Digite o salário do funcionario: '))
if sal > 1250:
    print('O novo salário é de R${:.2f}'.format(sal + sal * 0.1))
else:
    print('O novo salário é de R${:.2f}'.format(sal + sal * 0.15))
