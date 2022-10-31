# Faça um programa o comprimento do cateto oposto e do cateto adjacente
# de um triângulo retângulo e mostre o comprimento da hipotenusa

from math import hypot

catOp = float(input('Cateto oposto: '))
catAdj = float(input('Cateto adjacente: '))
hipo = hypot(catOp, catAdj)
print(hipo)
