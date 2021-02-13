# Escreva um programa para aprovar o emprestimo bancario para a compra de uma casa. O programa vai perguntar o valor da casa, o salario do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salario ou então o emprestimo sera negado

print('Bem vindo ao programa de emprestimo imobiliario')
cs = float(input('Qual o valor do imovel?\nR$:'))
sl = float(input('Qual o valor da sua renda mensal?\nR$:'))
an = float(input('Em quantos anos você deseja parcelar  valor do imovel?\n'))
ms = cs/an
pc = sl/10*3
if pc <= ms:
    print('Seu emprestimo foi aprovado')
else:
    print('Seu emprestimo foi negado,a parcela ultrapassou o valor de 30% do seu salario')
