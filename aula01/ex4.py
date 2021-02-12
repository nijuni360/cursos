#Escreva um programa que leia um valor em metros e o exiba convertido em centimetro e milimetro

n=float(input('Qual a sua altura?\n'))
cm=n*100
ml=n*1000
print ('A sua altura convertida em centimetros é {}.\nE convertida em milimetros é {}'.format(cm,ml))