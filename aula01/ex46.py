# Crie um programa que leia uma frase qualquer e diga se ela é palindromo, desconsiderando os espaços

frase = str(input('Digite uma frase:\n')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print('Temos um palindromo')
else:
    print('A frase digitada não é um palindromo')
