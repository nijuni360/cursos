# Façã um programa que leia o ano de nascimento de um jovem e informe de acordo com sua idade, se ele ainda vai se alistar no serviço militar, se ja é hora de se alistar, se ja passou da hora,e tambem devera mostrar o tempo que falta ou que passou do prazo

nasc = int(input('Digite seu ano de nascimento:\n'))
cal = 2021-nasc
ano = 18-cal
rest = cal-18
if cal < 18:
    print('Você ainda não esta na hora de se alistar faltam {} anos para o seu alistamento'.format(ano))
elif cal == 18:
    print('Esta na hora de você se alistar')
else:
    print('Ja passou da hora de você se alistar, ja se passaram {} anos do prazo'.format(rest))
