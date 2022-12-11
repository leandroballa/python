saque = nCinquenta = nVinte = nDez = nUm = rest = qtde = 0
saque = int(input('Que valor deseja sacar? R$'))
qtde = saque//50
if qtde > 0:
    print(f'Total de {qtde} cédulas de R$50,00')
rest = saque%50
qtde = rest // 20
if qtde > 0:
    print(f'Total de {qtde} cédulas de R$20,00')
rest = saque%20
qtde = rest // 10
if qtde > 0:
    print(f'Total de {qtde} cédulas de R$10,00')
rest = rest%10
if rest > 0:
    print(f'Total de {rest} cédulas de R$1,00')
