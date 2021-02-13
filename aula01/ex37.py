# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# A vista dinheiro\cheque 10% de desconto
# A vista cartão 5% de desconto
# Em até 2x no cartão preço normal
# 3x ou mais no cartão 20% de juros

produto = float(input('Qual o valor do produto?\nR$:'))
print('''Escolha a forma de pagamento:
[1]A vista dinheiro\cheque 10% de desconto
[2]A vista cartão 5% de desconto
[3]Em 2x no cartão
[4]Em 3x ou mais no cartão 20% de juros''')
pgt = int(input('Digite a opção de pagamento:\n'))
if pgt == 1:
    cal = produto*0.90
    print('O valor do produto com 10% de desconto é R${:.2f}'.format(cal))
elif pgt == 2:
    calc2 = produto*0.95
    print('O valor do produto com 5% de desconto é R${:.2f}'.format(calc2))
elif pgt==3:
    print('O valor do produto é R${:.2f}'.format(produto))
else:
    calc3=produto/10*2+produto
    print('O valor do produto com 20% de juros é R${:.2f}'.format(calc3))
