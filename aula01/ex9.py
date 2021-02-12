# Faça um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

p = float(input('Qual o valor do seu salario?\nR$'))
ct = p/10//2*3
rs = p+ct
print('O valor do seu salario com 15% de aumento é R${:.2f}'.format(rs))
