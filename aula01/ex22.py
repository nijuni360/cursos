# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h mostre uma mensagem dizendo que ele foi multado, a multa vai custar   R$7,00 reais por cada km acima do limite


vl = float(input('Qual a velocidade do veiculo?\nKm\h:'))
if vl > 80:
    print('Você ultrapassou o limite de velocidade, você sera multado')
    mt = vl-80
    tt = mt*7
    print('O valor da multa é R${:.2f} reais'.format(tt))
else:
    print('Você esta dentro do limite de velocidade')
