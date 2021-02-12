# Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo

import math

a = float(input('Digite o valor do angulo:\n'))
print('O valor do seno é {:.2f}\nCosseno {:.2f}\ne tangente {:.2f}'.format(
    math.sin(math.radians(a)), math.cos(math.radians(a)), math.tan(math.radians(a))))
