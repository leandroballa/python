peso = float(input('Digite seu peso: '))
alt = float(input('Digite sua altura: '))
imc = (peso / (alt**2))
print('Seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso')
# elif imc >= 18.5 and imc < 25:
elif 18.5 <= imc < 25:
    print('Você está no peso Ideal')
elif 25 <= imc < 30:
    print('Você está com Sobrepeso')
elif 30 <= imc < 40:
    print('Você está com Obesidade')
else:
    print('Você está com Obesidade mórbida')
