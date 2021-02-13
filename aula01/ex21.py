# Escreva um programa que faça o computador 'pensar' em um numero inteiro entre 0 e 5 e peça para o usuario tentar descobrir qual foi o numero escolhido pelo computador. O programa devera escrever na tela se o usuario venceu ou perdeu

import random
num = int(input('Tente advinhar um numero de 0 a 5\n'))
sorteio = random.randint(0, 5)
if num == sorteio:
    print('Parabéns você acertou')
else:
    print('Que pena você errou, o numero que o computador escolheu foi {}'.format(sorteio))
