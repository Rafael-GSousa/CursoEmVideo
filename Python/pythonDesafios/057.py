# Faça um programa que leia o sexo de uma pessoa, mas só aceite
# os valores 'M' ou 'F'. Caso esteja errado, peça a digitação
# novamente até ter um valor correto.

sexo = str(input('Digite o seu sexo [M/F]: ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = input('Dados inválidos. Por favor, digite o sexo [M/F]: ').strip().upper()[0]
if sexo == 'M':
    print(f'Você é do sexo MASCULINO!')
else:
    print(f'Você é do sexo FEMININO!')
