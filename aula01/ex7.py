# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta pinta uma area de 2 metros quadrado

at = float(input('Qual a altura da parede?\n'))
lg = float(input('Qual a largura da parede?\n'))
s = at*lg//2
print('Você vai precisar de {} litros de tinta para pintar essa parede'.format(s))
