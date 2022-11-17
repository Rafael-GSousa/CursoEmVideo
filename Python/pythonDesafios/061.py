# # Refaça o desafio 51, lendo o primeiro termo e a razão de uma PA,
# mostrando os 10 primeiros termos da progressão usando a estrutura while

pTermo = int(input('1º termo da PA: '))
razao = int(input('Razão da PA: '))
uTermo = pTermo + (10 - 1) * razao
while pTermo <= uTermo:
    print(pTermo, end=' ')
    pTermo += razao
