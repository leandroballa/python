preco = float(input('Digite o preço do produto em R$'))
forma = int(input('''Escolha a forma de pagamento
1-A Vista (Dinheiro/Cheque)
2-A Vista (Cartão)
3-2x no Cartão
4-3x ou mais no Cartão'''))
if forma == 1:
    print('O valor do produto é de R${:.2f}'.format(preco - (preco * 0.1)))
elif forma == 2:
    print('O valor do produto é de R${:.2f}'.format(preco - (preco * 0.05)))
elif forma == 3:
    print('O valor do produto é de R${:.2f}'.format(preco))
elif forma == 4:
    print('O valor do produto é de R${:.2f}'.format(preco + (preco * 0.2)))
else:
    print('Opção de pagamento inválida!')
