'''
Dentro do pacote UtilidadesCeV que criamos no desario 111,
temos um módulo chamado dado. Crie uma função chamda
leiaDinheiro() que seja capaz de funcionar coo a função
input(), mas com uma validação de dados para aceitar apenas
valores que sejam monetários.
'''
from utilidadesCeV import moeda, dados

n = dados.leiaDinheiro('Digite um valor R$ ')
if n >= 0:
    moeda.resumo(n, 10, 10)
