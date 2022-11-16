# Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas
# pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date
anoAtual = date.today().year
maior = 0
menor = 0
for i in range(1, 8):
    anoNasc = int(input(f'Digite o ano de nascimento da {i}ª pessoa: '))
    idade = anoAtual - anoNasc
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'{menor} pessoas ainda não atingiram a maioridade e {maior} já são maiores.')
