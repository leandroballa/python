n1 = float(input('Digite a primera nota: '))
n2 = float(input('Digite a segunda nota: '))
med = (n1 + n2) / 2
if med < 5:
    print('Aluno reprovado')
elif med >= 5 and med < 7:
    print('Aluno em recuperação')
else:
    print('Aluno Aprovado!')
