# Desenvolva um programa que leia seis números inteiros e mostre
# a soma apenas daqueles que forem pares. Se o valor digitado
# for ímpar, desconsidere-o
soma = 0
cont = 0
for i in range(1, 7):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        soma += n
        cont += 1
print(f'A soma dos {cont} números pares digitados é {soma}')
