# Ex58:Melhore o jogo do desafio 28 onde o computador vai pensar em um numero entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram nescessarios para vencer.add()

from random import randint
pc = randint(0, 10)
print('Tente adivinhar um numero de 0 a 10')
acertou = False
tnt = 0
while not acertou:
    jg = int(input('Digite um numero:\n'))
    tnt += 1
    if jg == pc:
        acertou = True
    else:
        if jg < pc:
            print('Um pouco mais')
        elif jg > pc:
            print('Um pouco menos')
print(f'Voce precisou de {tnt} tentativas para acertar')
