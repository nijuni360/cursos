# Desenvolva uma logica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status de acordo com a tabela abaixo:
# abaixo de 18.5: abaixo do peso, enter 18.5 e 25: peso ideal, de 25 ate 30: sobrepeso, de 30 ate 40 : obesidade e acima de 40 : obesidade morbida

peso = float(input('Qual seu peso?\n'))
altura = float(input('Qual sua altura?\n'))
imc = peso/(altura**2)

if imc < 18.5:
    print('Você esta abaixo do peso, seu IMC é {:.2f}'.format(imc))
elif imc < 25:
    print('Você esta dentro do peso, seu IMC é {:.2f}'.format(imc))
elif imc < 30:
    print('Você esta com sobrepeso, seu IMC é {:.2f}'.format(imc))
elif imc < 40:
    print('Você esta com obesidade, seu IMC é {:.2f}'.format(imc))
else:
    print('Você esta com obesidade morbida, seu IMC é {:.2f}'.format(imc))
