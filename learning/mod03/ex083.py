e = str(input('Digite uma expressão matemática: ')).strip()
exp = list()
for simb in e:
    if simb == '(':
        exp.append('(')
    elif simb == ')':
        if len(exp) > 0:
            exp.pop()
        else:
            exp.append(')')
            break
if len(exp) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')
# Minha solução
'''for x in range(0, len(e)):
    exp.append(e[x])
if exp.count('(') != exp.count(')'):
    print('Expressão inválida')
else:
    print('Expressão válida')'''
