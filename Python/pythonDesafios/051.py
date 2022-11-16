# Desenvolva um programa que leia o primeiro termo e a razão
# de uma PA(Progressão Aritmética). No final, mostre os 10 primeiros
# termos dessa progressão.
print('=' * 30)
print('{:^30}'.format('10 termos de uma PA'))
print('=' * 30)
pTermo = int(input('1º termo: '))
razao = int(input('Razão da PA: '))
termos = 10
uTermo = pTermo + (termos-1) * razao
uTermo = uTermo + 1
for i in range(pTermo, uTermo, razao):
    print(i, end=" ")
