'''
Adapte o código do desafio 107, criando uma função adicional chamda moeda()
que consiga mostrar os valores como um valor monetário formatado.
'''
import moeda

n = float(input('Digite o preço: R$ '))
print(f"O dobro de {moeda.moeda(n)} é {moeda.moeda(moeda.dobro(n))}")
print(f"A metade de {moeda.moeda(n)} é {moeda.moeda(moeda.metade(n))}")
print(f"Aumentando 10% {moeda.moeda(n)} é {moeda.moeda(moeda.aumentar(n, 10))}")
print(f"Diminuindo 10% {moeda.moeda(n)} é {moeda.moeda(moeda.diminuir(n, 10))}")
