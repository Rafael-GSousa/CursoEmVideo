# Crie um programa onde o usuário possa digitar vários valores
# numéricos e cadastre-os em uma lista. Caso o número já exista
# lá dentro, ele não será adicionado. No final, serão exibidos
# todos os valores únicos digitados, em ordem crescente.
numeros = list()
while True:
    valor = int(input('Digite um valor: '))
    if valor not in numeros:
        numeros.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if continua in 'N':
        break
numeros.sort()
print('-=' * 30)
print(f'Você digitou os valores {numeros}')
