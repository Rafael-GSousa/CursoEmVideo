# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan, radians

ang = float(input('Digite o valor do ângulo '))
print(f'Seno = {sin(radians(ang)):.2f} Cosseno = {cos(radians(ang)):.2f} Tangente = {tan(radians(ang)):.2f}')
