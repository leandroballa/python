def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == "":
            print(f"ERRO. O valor digitado não é um valor monetário!")
        else:
            valido = True
            return float(entrada)
