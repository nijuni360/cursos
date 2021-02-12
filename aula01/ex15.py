# Crie um programa que leia o nome completo de uma pessoa e mostre: o nome com todas as letras maiusculas, o nome com todas as letras minusculas, quantas letras tem ao todo sem contar os espaços

nome = str(input('Digite seu nome completo:\n')).strip()
print('Analisando seu nome...')
print('Seu nome em maiusculas é {}'.format(nome.upper()))
print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(
    separa[0], len(separa[0])))
