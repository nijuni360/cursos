# Crie um programa que leia um numero inteiro e mostre na tela se ele é par ou impar.

num = int(input(
    'Digite qualquer numero que o computador ira dizer se ele é par ou impar:\n'))
cl = num % 2
if cl == 1:
    print('O numero {} é impar'.format(num))
else:
    print('O numero {} é par'.format(num))
