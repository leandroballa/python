ficha = list()
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    if str(input('Deseja continuar? [S/N] ')) in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MEDIA":>8}')
print('-=' * 26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-=' * 35)
    opc = int(input('Mostrar notas de qual aluno? [999 interremp]: '))
    if opc == 999:
        break
    if opc <= len(ficha) -1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')

# MINHA SOLUÇÃO
'''
classe = list()
alunos = list()
notas = list()
while True:
    alunos.append(str(input('Digite o nome do aluno: ')).strip())
    for x in range(1, 3):
        notas.append(float(input(f'Digite a {x}ª nota do aluno: ')))
    alunos.append(notas[:])
    notas.clear()
    classe.append(alunos[:])
    alunos.clear()
    if str(input('Deseja continuar? [S/N]')).strip().upper() in 'Nn':
        break

print('-='*30)
print(f'{"Nº":<3} {"Nome":<10} {"Media":<7}')
print('-'*20)
for x, c in enumerate(classe):
    print(f'{x:<3} {c[0]:<10} {(c[1][0] + c[1][1]) / 2:<7}')
print('-'*20)

while True:
    notaAlu = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if notaAlu == 999:
        break
    else:
        print(f'A notas do aluno {classe[0][notaAlu]} são {classe[0][1]}')
'''