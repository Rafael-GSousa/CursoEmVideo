# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um
# número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
# mostrando no final quantos palpites foram necessários para vencer.

from random import randint
computador = randint(0, 10)
jogador = int(input('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?
Qual é seu palpite? '''))
tentativas = 1
while computador != jogador:
    if computador > jogador:
        jogador = int(input('''Mais... Tente mais uma vez.
Qual é seu palpite? '''))
    else:
        jogador = int(input('''Menos... Tente mais uma vez.
Qual é seu palpite? '''))
    tentativas += 1
print(f'Acertou com {tentativas} tentativas. Parabéns!')
