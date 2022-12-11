num = soma = qtde = 0
while True:
    num = int(input("Digite um número: [999-Para sair] "))
    if num == 999:
        break
    soma += num
    qtde += 1
print(f'Foram digitados {qtde} números e a soma deles é {soma}')