idade = maisD = homens = mMenosD = qtde = 0
sexo = cont = ''
while True:
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa: [M/F] ')).upper()
    qtde += 1
    if idade >= 18:
        maisD += 1
    if sexo == 'M':
        homens += 1
    else:
        if idade <= 20:
            mMenosD += 1
    cont = str(input('Deseja continuar? [S/N] ')).upper()
    if cont != 'S':
        break
print(f'Foram cadastrados {qtde} pessoas, sendo:')
print(f'{maisD} com mais de 18 anos')
print(f'{homens} homens')
print(f'{mMenosD} mulheres com menos de 20 anos')