# Crie um programa que leia uma frase qualquer e diga se ela é um palídromo,
# desconsiderando os espaços.
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
# inverso = ''

# com for
'''for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]'''

# sem for
inverso = junto[::-1]
if inverso == junto:
    print(f'{frase} é um palíndromo')
else:
    print(f'{frase} não é um palíndromo')
