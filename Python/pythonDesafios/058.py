# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um
# número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
jogador = int(input('Escolha um número entre 0 e 10: '))
tentativas = 1
while computador != jogador:
    jogador = int(input('Escolha um número entre 0 e 10: '))
    tentativas += 1
print(f'''Escolha do computador ==> {computador}
Escolha do jogador ==> {jogador}
Nº de tentativas ==> {tentativas}''')
