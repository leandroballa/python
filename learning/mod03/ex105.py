def notas(*notas, sit=False):
    situacao = ''
    dic = dict()
    med = 0
    dic["total"] = len(notas)
    for x, n in enumerate(notas):
        med += n
        if x == 0:
            dic["maior"] = dic["menor"] = n
        else:
            if n > dic["maior"]:
                dic["maior"] = n
            if n < dic["menor"]:
                dic["menor"] = n
    dic["media"] = med / len(notas)
    if sit == True:
        if med <= 5:
            dic["situacao"] = 'Ruim'
        elif 5 > med < 7:
            dic["situacao"] = 'Boa'
        else:
            dic["situacao"] = 'Ótima'
    return dic


print(notas(5, 6.2, 2.9, 1, 3, sit=True))
