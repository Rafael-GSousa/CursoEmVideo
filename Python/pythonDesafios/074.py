# Crie um programa que vai gerar cinco números aleatórios e colocar
# em uma tupla. Depois disso, mostre a listagem de números gerados e
# também indique o menor e o maior valor que estão na tupla.
from random import randint

tupla = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
# maior = menor = 0
# forma extensa
# for i in range(0, 5):
#     if i == 0:
#         print(f'Os valores sorteados foram: ', end='')
#         maior = menor = tupla[i]
#     elif tupla[i] > maior:
#         maior = tupla[i]
#     elif tupla[i] < menor:
#         menor = tupla[i]
#     print(f'{tupla[i]}', end=' ')
# print(f'''\nO maior valor sorteado foi {maior}
# O menor valor sorteado foi {menor}''')

# forma reduzida
print(f'Os valores sorteados foram: ', end='')
for i in tupla:
    print(f'{i}', end=' ')
print(f'''\nO maior valor sorteado foi {max(tupla)}
O menor valor sorteado foi {min(tupla)}''')
