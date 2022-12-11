vCasa = float(input('Digite o valor da casa em R$:'))
sal = float(input('Digite o salário da pesssoa em R$:'))
anos = int(input('Em quantos anos será o parcelamento? '))

qtdeParc = (anos * 12)
valParc = vCasa / qtdeParc
aprov = valParc > (sal * 0.3)

if aprov is False:
    print('Financiamento aprovado!')
else:
    print('Financiamento negado')
