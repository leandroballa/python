pessoas = list()
individuo = dict()
mIdade = 0

while True:
    individuo['nome'] = str(input('Nome: '))
    while True:
        individuo['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if individuo['sexo'] in 'MF':
            break
        print('ERRO! Responda apenas F ou M')
    individuo['idade'] = int(input('Idade: '))
    pessoas.append(individuo.copy())
    while True:
        resp = str(input('Deseja continuar? [S/N] '))[0].upper()
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    if resp == 'N':
        break
print(f'O grupo tem {len(pessoas)} pessoas')
for p in pessoas:
    for k, i in p.items():
        if k == 'idade':
            mIdade += i
mIdade = mIdade / len(pessoas)
print(f'A média de idade do grupo é de {mIdade} anos')
print('As mulheres cadastradas foram', end=' ')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end=' ')
print()
print('Lista de pessoas acima da média de idade')
for x, p in enumerate(pessoas):
    if int(p["idade"]) > mIdade:
        print(p)
