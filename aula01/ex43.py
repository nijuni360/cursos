# Desenvolva um programa que leia seis numeros inteiros e mostre a soma apenas daqueles que forem pares, se o valor digitado for impar desconsidere-o

soma = 0
for c in range(0, 6):
    num = int(input('Digite um valor:\n'))
    if num % 2 == 0:
        soma = soma+num
print('O valor somado é {}'.format(soma))
