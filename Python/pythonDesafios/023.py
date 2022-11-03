# Faça um programa que leia um número de 0 a 9999 e mostre na tela
# cada um dos dígitos separados
# Ex.:
# Digite um número: 1834
# unidade: 4
# dezena: 3
# centena: 8
# milhar: 1

numero = input('Digite um número de 0 a 9999: ')
print(f"""Unidade: {numero[3]}
Dezena: {numero[2]}
Centena: {numero[1]}
Milhar: {numero[0]}""")
