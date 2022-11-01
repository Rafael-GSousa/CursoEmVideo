# Crie um programa que leia um número Real qualquer pelo teclado e
# mostre na tela a sua porção inteira.

# from math import trunc
import math

num = float(input('Digite um número: '))
print(f'O valor digitado foi {num} e a sua porção inteira é {math.trunc(num)}')
# print(f'O valor digitado foi {num} e a sua porção inteira é {trunc(num)}')
print(f'O valor digitado foi {num} e a sua porção inteira é {int(num)}')
