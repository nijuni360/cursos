# Escreva um programa que pergunte o salario de um funcionario e calcule o valor do seu aumento.Para salarios superior a R$1250,00 calcule um aumento de 10%, para salarios inferiores ou iguais, o aumento é de 15%

sl = float(input('Qual  valor do seu salario?\nR$'))
if sl > 1250:
    au = sl/10*1+sl
    print('O valor do seu salario com 10% de aumento é R${:.2f}'.format(au))
else:
    cr = sl/10*1.5+sl
    print('O valor do seu salario com 15% de aumento é R${:.2f}'.format(cr))
