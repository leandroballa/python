mIdade = 0
nVelho = ''
iVelho = 0
mAnos = 0
for x in range(0, 4):
    print('#'*20)
    nome = input('Digite um nome: ')
    idade = int(input('Digite a idade de {}: '.format(nome)))
    sexo = input('Digite o sexo de [M/F]: '.format(nome))
    if sexo.upper() == 'M':
        if idade > iVelho:
            iVelho = idade
            nVelho = nome
    else:
        if idade < 20:
            mAnos += 1
    mIdade += idade
print('#'*50)
print('A média de idade é de {:.0f}'.format(mIdade/4))
print('O homem mais velhor é {} com {} anos!'.format(nVelho, iVelho))
print('Existem {} com menos de 20 anos'.format(mAnos))
