# Ex57:Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores  'M' ou 'F'. Caso esteja errado peça a digitação novamente até ter um valor correto


sex = str(input('Digite seu sexo [M/F]:\n')).upper()
while sex not in 'MmFf':
    sex = str(input('Digitação incorreta, digite novamente:\n'))
print(f'Você é do sexo {sex}')
