# Faça um programa que leia três números e mostre qual é o maior e qual é
# o menor.

n1 = float(input('Digite o 1º número: '))
n2 = float(input('Digite o 2º número: '))
n3 = float(input('Digite o 3º número: '))
# Definindo o maior e o menor inicial
maior = n1
menor = n1

# Verificando o menor
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
# Verificando o maior
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print(f'Maior = {maior}, menor = {menor}')
