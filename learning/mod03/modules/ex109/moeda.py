def aumentar(n, perc, format=True):
    r = n + (n * (perc / 100))
    if format:
        return moeda(r)
    else:
        return r


def diminuir(n, perc, format=True):
    r = n - (n * (perc / 100))
    if format:
        return moeda(r)
    else:
        return r


def dobro(n, format):
    r = n * 2
    if format:
        return moeda(r)
    else:
        return r


def metade(n, format=True):
    r = n / 2
    if format:
        return moeda(r)
    else:
        return r


def moeda(num):
    return str(f" R${num:.2f}").replace('.',',')
