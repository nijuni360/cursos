# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule o comprimento da hipotenusa

from math import hypot

co = float(input('Qual o comprimento do cateto oposto?\n'))
ca = float(input('Qual o comprimento do cateto adjacente?\n'))
hi = hypot(co, ca)
print('O comprimento da hipotenusa é {:.2f}'.format(hi))
