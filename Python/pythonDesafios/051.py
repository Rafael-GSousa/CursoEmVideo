# Desenvolva um programa que leia o primeiro termo e a razão
# de uma PA(Progressão Aritmética). No final, mostre os 10 primeiros
# termos dessa progressão.

pTermo = int(input('1º termo de uma PA: '))
razao = int(input('Razão da PA: '))
termos = 10
uTermo = pTermo + (termos-1) * razao
uTermo = uTermo + 1
for i in range(pTermo, uTermo, razao):
    print(i, end=" ")
