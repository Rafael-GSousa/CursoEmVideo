# Escreva um programa que leia um número inteiro qualquer e peça
# para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal

numero = int(input('Digite um número inteiro: '))
base = int(input("""Escolha a base de conversão:
- 1 Binário (2)
- 2 Octal (8)
- 3 Hexadecimal (16)
Base ==> """))
conversao = 0
if base == 1:
    base = 2
    conversao = bin(numero)
elif base == 2:
    base = 8
    conversao = oct(numero)
elif base == 3:
    base = 16
    conversao = hex(numero)

print(f'{numero} na base {base} é igual a {conversao}')
