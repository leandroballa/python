nome = ''
preco = total = maisMil = pBarato = 0
continuar1 = True
continuar2 = prodBarato= 'S'
while continuar1:
    nome = str(input('Digite o nome do produto: ')).upper().strip()
    preco = float(input('Digite o valor do produto: R$'))
    total += preco
    if preco >= 1000:
        maisMil += 1
    if pBarato == 0:
        pBarato = preco
        prodBarato = nome
    else:
        if preco < pBarato:
            pBarato = preco
            prodBarato = nome
    while continuar2 == 'S':
        continuar2 = str(input('Deseja continuar? [S/N] ')).upper().strip()
        if continuar2 == 'N':
            continuar1 = False
            break
        elif continuar2 == 'S':
            break
        else:
            continuar2 = 'S'
print(f'O total da compra foi de R${total}')
print(f'{maisMil} custaram mais de R$ 1.000,00')
print(f'O produto mais barato foi {prodBarato}')