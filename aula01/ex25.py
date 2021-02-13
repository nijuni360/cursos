# Faça um programa que leia um ano qualquer e mostre se ele é Bissexto

ano = int(input('Que ano você quer analisar?\n'))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))
