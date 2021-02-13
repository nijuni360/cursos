#Desenvolva um programa que leia o comprimento de três retas e diga ao usuario se elas podem ou não formar um triangulo

r1=float(input('Primeiro segmento:\n'))
r2=float(input('Segundo segmento:\n'))
r3=float(input('Terceiro segmento:\n'))
if r1<r2+r3 and r2<r3+r1 and r3<r1+r2:
    print('Os segmentos acima podem formar um triangulo')
else:
    print('Os segmentos acima não formam um triangulo')