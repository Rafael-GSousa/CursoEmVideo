# Melhore o Desafio 061, perguntando para o usuário se ele quer
# mostrar mais alguns termos. O programa encerra quando ele disser
# que quer mostrar 0 termos.

pTermo = int(input('1º termo da PA: '))
razao = int(input('Razão da PA: '))
n = 10
outros = 1
uTermo = pTermo + (n - 1) * razao
while pTermo <= uTermo:
    print(pTermo, end=' ')
    pTermo += razao
while outros != 0 and pTermo <= uTermo:
    outros = int(input('\nQuantos termos a mais que mostrar? '))
    n += outros
    print(pTermo, end=' ')
    pTermo += razao
