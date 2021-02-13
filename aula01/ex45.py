# Faça um programa que leia um numero inteiro e diga se ele é ou não um numero primo

tot = 0
núm = int(input('Digite um numero:\n'))
for c in range(1, núm + 1):
    if núm % c == 0:
        print('\033[34m', end=' ')
        tot += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(c), end=' ')
print('O numero {} foi divisivel {} vezes'.format(núm, tot))
if tot == 2:
    print('E por isso ele é Primo')
else:
    print('E por isso ele não é Primo')
