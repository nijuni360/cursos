# O mesmo professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada

import random

n1 = str(input('Primeiro aluno\n'))
n2 = str(input('Segundo aluno\n'))
n3 = str(input('Terceiro aluno\n'))
n4 = str(input('Quarto aluno\n'))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação sera')
print(lista)
