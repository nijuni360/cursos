# Refaça o exercicio dos triangulos acrescentando o recurso de mostrar que tipo de triangulo sera formado, equilatero: todos os lados iguais, Isoceles:dois lados iguais e Escaleno: todos os lados diferentes

r1 = float(input('Primeiro segmento:\n'))
r2 = float(input('Segundo segmento:\n'))
r3 = float(input('Terceiro segmento:\n'))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Os segmentos acima podem formar um triangulo', end='')
    if r1 == r2 == r3:
        print('Equilatero')
    elif r1 != r2 != r3 != r1:
        print('Escaleno')
    else:
        print('Isoceles')
else:
    print('Os segmentos acima não podem formar um triangulo')
