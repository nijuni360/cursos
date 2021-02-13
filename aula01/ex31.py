# Escreva um programa que leia dois numeros inteiros e os compare mostrando na tela uma mensagem de qual valor é maior e quando não tiver valor maior mostrar que os valores são iguais

pr = int(input('Digite o primeiro valor:\n'))
sc = int(input('Digite o segundo valor:\n'))
if pr > sc:
    print('O primeiro valor é maior')
elif sc > pr:
    print('O segundo valor é maior')
else:
    print('Os valores são iguais')
