# # Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while
print('Gerador de PA')
print('-=' * 10)
pTermo = int(input('1º termo: '))
razao = int(input('Razão: '))
termo = pTermo
cont = 1
while cont <= 10:
    print(termo, end=' ')
    termo += razao
    cont += 1
