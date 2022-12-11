def area(a, b):
    print(f'A area do terreno de {a}x{b} é de {a*b}m²')


print('Controle de terrenos')
print('-' * 20)
area(float(input('Digite a largura do terreno: '))
     , float(input('Digite o comprimento do terreno: ')))
