# Desenvolva um programa que pergunte a distancia de uma viagem em Km. Calcule o preço da passagem cobrando R$0,50 centavos por Km para viagens de até 200Km e R$0,45 centavos para viagens mais longas

vj = float(input('Quantos quilometros você viajou?\nKm:'))
if vj <= 200:
    cl = vj*0.50
    print('O valor da sua passagem é de R${:.2f}'.format(cl))
else:
    cr = vj*0.50
    print('O valor da passagem é de R${:.2f}'.format(cr))
