# Um professor quer sortear um dos seus quatro alunos para apagar a lousa. Faça um programa que ajude ele lendo o nome deles e escrevendo o nome do escolhido

import random

n1 = str(input('Primeiro aluno\n'))
n2 = str(input('Segundo aluno\n'))
n3 = str(input('Terceiro aluno\n'))
n4 = str(input('Quarto aluno\n'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O escolhido foi {}'.format(escolhido))
