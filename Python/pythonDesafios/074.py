# Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla. Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.
from random import randint

tupla = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))
print(tupla)
print(sorted(tupla))
maior = menor = 0
for i in range(0, len(tupla)):
    if i == 0:
        maior = menor = tupla[i]
    elif tupla[i] > maior:
        maior = tupla[i]
    elif tupla[i] < menor:
        menor = tupla[i]
print(f'O maior número é {maior} e o menor é {menor}')
