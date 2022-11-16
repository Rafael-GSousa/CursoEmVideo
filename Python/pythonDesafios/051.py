# Desenvolva um programa que leia o primeiro termo e a razão
# de uma PA(Progressão Aritmética). No final, mostre os 10 primeiros
# termos dessa progressão.

pTermo = int(input('1º termo de uma PA: '))
razao = int(input('Razão da PA: '))
pa = pTermo
for i in range(0, 10):
    print(pa, end=" ")
    pa += razao
