# A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a sua idade, até 9 anos mirim, ate 14 anos infantil, ate 19 anos junior, ate 20 anos senior, e acima master

from datetime import date
atual = date.today().year

nasc = int(input('Ano de nascimento:\n'))
idade = atual-nasc
if idade <= 9:
    print('Você tem {} anos, classificação Mirim'.format(idade))
elif idade <= 14:
    print('Você tem {} anos, classificação Infantil'.format(idade))
elif idade <= 19:
    print('Você tem {} anos, classificação Junior'.format(idade))
elif idade == 20:
    print('Você tem {} anos, classificação Senior'.format(idade))
else:
    print('Você tem {} anos, classificação Master'.format(idade))
