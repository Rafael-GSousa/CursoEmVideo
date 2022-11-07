# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Comprimento da 1ª reta: '))
r2 = float(input('Comprimento da 2ª reta: '))
r3 = float(input('Comprimento da 3ª reta: '))

if (r1 + r2) > r3 or (r1 + r3) > r2 or (r2 + r3) > r1 or (r1 - r2) < r3 or (r1 - r3) < r2 or (r2 - r3) < r1:
    print('As retas podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
