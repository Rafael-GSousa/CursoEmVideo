# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um
# número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Qual é seu palpite? '))
    tentativas += 1
    if computador == jogador:
        acertou = True
    else:
        if computador > jogador:
            print('Mais... ', end='')
        else:
            print('Menos... ', end='')
print(f'Acertou com {tentativas} tentativas. Parabéns!')
