# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior
# e o menor peso lidos.
maior = 0
menor = 0
for i in range(1, 6):
    peso = float(input(f'Qual é o peso da {i}ª pessoa? '))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso
print(f'O maior peso foi {maior:.1f}Kg e o menor peso foi {menor:.1f}Kg')
