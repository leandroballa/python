mat = ('Lápis',1.75, 'Borracha', 2, 'Caderno', 15.9, 'Estojo', 25, 'Transferidor', 4.2
       , 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.3, 'Livro', 34.9)
print('-'*30)
print(f'{"LISTA DE COMPRA":^30}')
print('-'*30)
for x in range(0, len(mat), 2):
    print(f'{mat[x]:.<20} R${mat[x+1]:>7.2f}')
