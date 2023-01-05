'''
Modifique as funções que foram criadas no desafio 107 para que elas aceitem
um parâmetro a mais, informando se o valor retornado por elas vai ser ou não
formatado pela função moeda(), desenvolvida no desafio 108.
'''
import moeda

n = float(input('Digite o preço: R$ '))
print(f"O dobro de {moeda.moeda(n)} é {moeda.dobro(n, False)}")
print(f"A metade de {moeda.moeda(n)} é {moeda.metade(n, True)}")
print(f"Aumentando 10% {moeda.moeda(n)} é {moeda.aumentar(n, 10, True)}")
print(f"Diminuindo 10% {moeda.moeda(n)} é {moeda.diminuir(n, 10, True)}")
