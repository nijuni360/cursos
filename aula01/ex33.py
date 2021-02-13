# Crie um programa que leia duas notas de um aluno e calcule sua media, mostrando uma mensagem no final de acordo com a media atingida, abaixo de 5. : reprovado, de 5.0 a 6.9: recuperação, 7.0 ou superior aprovado

not1 = float(input('Digite sua primeira nota:\n'))
not2 = float(input('Digite sua segunda nota:\n'))
calc = not1+not2/2
if calc <= 5.0:
    print('Sua media foi {}, você esta REPROVADO!!'.format(calc))
elif calc <= 6.9:
    print('Sua media foi {}, você esta de RECUPERAÇÃO!!'.format(calc))
else:
    print('Sua media foi {}, Parabens você esta APROVADO!!'.format(calc))
