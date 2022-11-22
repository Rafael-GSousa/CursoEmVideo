# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas
# respectivas posições na lista.
valores = list()
maior = menor = 0
posMaior = list()
posMenor = list()

for pos in range(0, 5):
    valores.append(int(input(f'Digite um valor para a Posição {pos}: ')))
    if pos == 0:
        maior = menor = valores[pos]
    elif valores[pos] > maior:
        maior = valores[pos]
    elif valores[pos] < menor:
        menor = valores[pos]

print(f'=-' * 30)
print(f'Você digitou os valores: {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for p, i in enumerate(valores):
    if maior == i:
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for p, i in enumerate(valores):
    if menor == i:
        print(f'{p}... ', end='')
