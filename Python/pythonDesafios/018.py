# Faça um programa que leia um ângulo qualquer e mostre na tela
# o valor do seno, cosseno e tangente desse ângulo

from math import sin, cos, tan

ang = float(input('Digite o valor do ângulo '))
print(f'Seno = {sin(ang)} Cosseno = {cos(ang)} Tangente = {tan(ang)}')
