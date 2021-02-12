# Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Digite qualquer numero\n'))
db = n*2
tp = n*3
rq = n**2
print('O dobro do numero {} é {}.\nO triplo é {}\nE a raiz quadrada é {}'.format(
    n, db, tp, rq))
