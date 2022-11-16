# Faça um programa que calcule a soma entre todos os números ímpares
# que são múltiplos de três e que se encontram no intervalo de 1 até 500
soma = 0
for i in range(1, 500):
    if i % 3 == 0:
        soma += i
print(f'A soma dos números ímpares, múltiplos de 3, entre 1 e 500 é {soma}')
