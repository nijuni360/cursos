# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 a 0 com uma pausa de 1 segundo entre eles

from time import sleep

print('Contagem regressiva para a queima de fogos!!!')

for cont in range(10, -1, -1):
    print(cont)
    sleep(1)
print('Fogos estourando')
