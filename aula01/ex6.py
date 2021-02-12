# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar
# US$ 1,00 = R$ 5,21

n = float(input(
    'Quantos reais você tem na carteira? para saber quantos dolares você consegue comprar:\nR$'))
cv = n//5.21
print('Você consegue comprar US${:.2f} dolares'.format(cv))
