# Faça um programa que lei um número qualquer e mostre o seu fatorial.
# Ex.: 5! = 5x4x3x2x1 = 120
num = int(input('Digite um número para calcular o seu fatorial: '))
cont = num
fat = 1
if num > 0:
    while cont >= 1:
        fat *= cont
        cont -= 1
    print(f'O fatorial de {num} é {fat}')
else:
    print(f'Não existe fatorial de {num}')
