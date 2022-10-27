# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

import math
n = float(input('Digite um número: '))
print(f'Número digitado ==> {n} \nDobro de {n} ==> {n * 2:.2f} \nTriplo de {n} ==> {n * 3:.2f} \n'
      f'Raiz quadrada de {n} ==> {math.sqrt(n):.2f}')
