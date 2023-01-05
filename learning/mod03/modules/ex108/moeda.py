def aumentar(n, perc):
    return n + (n * (perc / 100))


def diminuir(n, perc):
    return n - (n * (perc / 100))


def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def moeda(num):
    return str(f" R${num:.2f}").replace('.', ',')
