# Crie um programa que faça o computador jogar jokenp com você

import random

print('Vamos jogar Jokenpo')
escolha = str(input('Escolha pedra, papel ou tesoura:\n'))
lista = ['pedra', 'papel', 'tesoura']
sorteio = random.choice(lista)
print('Você escolheu {} e o computador escolheu {}'.format(escolha, sorteio))
if escolha == ('pedra') and sorteio == ('tesoura'):
    print('Você ganhou!!!')
elif escolha == ('pedra') and sorteio == ('papel'):
    print('O computador ganhou')
if escolha == ('papel') and sorteio == ('pedra'):
    print('Você ganhou!!!')
elif escolha == ('papel') and sorteio == ('tesoura'):
    print('O computador ganhou')
if escolha == ('tesoura') and sorteio == ('papel'):
    print('Você ganhou!!!')
elif escolha == ('tesoura') and sorteio == ('pedra'):
    print('O computador ganhou')
elif escolha == sorteio:
    print('Ninguem Ganhou')