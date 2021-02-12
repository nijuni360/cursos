# Faça um algoritimo que leia o preço de um produto e mostre seu novo preço com 5% de desconto

p = float(input(
    'Digite o valor do produto para saber quanto ele custara com 5% de desconto:\nR$'))
pr = p/10//2
rs = p-pr
print('O valor do produto com 5% de desconto fica R${:.2f}'.format(rs))
