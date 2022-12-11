aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input('Média: '))
if aluno['media'] >= 7:
    aluno['sit'] = 'Aprovado'
else:
    aluno['sit'] = 'Reprovado'
for k, v in aluno.items():
    print(f'{k} é igual a {v}')
# print(f'Nome é igual a {aluno["nome"]}')
# print(f'Média é igual a {aluno["media"]}')
# print(f'Situação é igual a {aluno["sit"]}')
