# Faça um programa que leia três números e mostre qual é o maior e qual é
# o menor.

n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))

maior = 0
menor = 0

if n1 > n2 > n3:
    maior = n1
    menor = n3
if n1 > n3 > n2:
    maior = n1
    menor = n2
if n2 > n3 > n1:
    maior = n2
    menor = n1
if n2 > n1 > n3:
    maior = n2
    menor = n3
if n3 > n1 > n2:
    maior = n3
    menor = n2
if n3 > n2 > n1:
    maior = n3
    menor = n1

print(f'Maior = {maior}, menor = {menor}')
