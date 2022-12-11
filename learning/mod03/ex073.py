bra = ('Palmeiras', 'Internacional', 'Corinthians', 'Flamengo', 'Fluminense', 'Athletico-PR'
        , 'Atlético-MG', 'América-MG', 'Botafogo', 'Fortaleza', 'São Paulo', 'Bragantino', 'Goiás'
        , 'Santos', 'Coritiba', 'Ceará SC', 'Cuiabá', 'Atlético-GO', 'Avaí', 'Juventude')

print('='*50)
print('Tabela Brasileirão 2022')
print(bra)
print('Os 5º colocados')
print(bra[:5])
print('Os 4 ultimos colocados')
print(bra[-4:])
print('Em ordem alfabetica')
print(sorted(bra))
print(f"São Paulo está na {bra.index('São Paulo')+1}ª posição")