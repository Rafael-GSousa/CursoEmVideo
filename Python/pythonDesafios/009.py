# Faça um programa que leia um número inteiro qualquer e mostre
# na tela a sua tabuada

n = int(input('Entre com um inteiro para a tabuada: '))

print('-' * 12)

for i in range(1, 11):
    print(f'{n} x {i:2} = {n * i}')

print('-' * 12)
