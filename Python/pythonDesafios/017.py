# Faça um programa o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo e mostre o comprimento da hipotenusa

from math import pow, sqrt, hypot

catOp = float(input('Cateto oposto: '))
catAdj = float(input('Cateto adjacente: '))
# hipo = sqrt(pow(catOp, 2) + pow(catAdj, 2))
hipo = hypot(catOp, catAdj)
print(f'A hipotenusa vai medir {hipo:.2f}')
