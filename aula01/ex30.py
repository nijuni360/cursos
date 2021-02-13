# Escreva um programa que leia um numero inteiro qualquer e peça para o usuario escolher qual sera a base de conversão, 1 para binario, 2 para octal, 3 para hexadecimal

num = int(input('Digite um numero inteiro:\n'))
print('''Escolha uma das bases de dados para conversão:
[1] converter para binario 
[2] converter para octal 
[3] converter para hexodecimal''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para binario é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexodecimal é igual a {}'.format(
        num, hex(num)[2:]))
else:
    print('Opção invalida, tente novamente')
