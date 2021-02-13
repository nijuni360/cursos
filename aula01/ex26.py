# Faça um programa que leia três numeros e mostre qual é o maior e qual é o menor

a = int(input('Primeiro valor:\n'))
b = int(input('Segundo valor:\n'))
c = int(input('Terceiro valor:\n'))
menor = a
if b < a and b < c:
    menor = b
elif c < a and c < b:
    menor = c
maior = a
if b > a and b > c:
    maior = b
elif c > a and c > b:
    maior = c
print('O menor valor digitado é {}'.format(menor))
print('O maior valor digitado é {}'.format(maior))
