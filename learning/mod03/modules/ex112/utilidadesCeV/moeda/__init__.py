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


def dobro(n, format=True):
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
    return str(f" R${num:.2f}").replace('.', ',')


def resumo(num=0, aum=10, red=5):
    print("-" * 30)
    print(f"{'RESUMO DO VALOR':^30}")
    print("-" * 30)
    print(f"Preço analisado: \t{moeda(num)}")
    print(f"Dobro do preço: \t{dobro(num)}")
    print(f"Metade do preço: \t{metade(num)}")
    print(f"{aum}% de aumento: \t{aumentar(num, aum)}")
    print(f"{red}% de redução: \t{diminuir(num, red)}")
