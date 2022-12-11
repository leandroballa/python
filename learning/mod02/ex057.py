sexo = 'A'
while sexo not in ('MmFf'):
    sexo = str(input('Digite o sexo [M/F]: ')).upper()
print('O sexo digitado foi {}'.format(sexo))