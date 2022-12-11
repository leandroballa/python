palavras = ('TESTE', 'EU', 'VOCE', 'TRABALHO', 'WEB', 'MESA', 'CADERNO')
for p in palavras:
    print(f'\nNa palavra {p} temos ', end=' ')
    for x in p:
        if x in 'AEIOU':
            print(x, end=' ')
    # Minha solução
    '''for x in range(0, len(p)):
        if p[x] == 'A':
            print('a', end=' ')
        elif p[x] == 'E':
            print('e', end=' ')
        elif p[x] == 'I':
            print('i', end=' ')
        elif p[x] == 'O':
            print('o', end=' ')
        elif p[x] == 'U':
            print('u', end=' ')'''
