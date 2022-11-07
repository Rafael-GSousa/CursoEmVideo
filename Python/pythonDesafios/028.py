# Escreva um programa que faça o computador "pensar" em um número inteiro
# de 0 a 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint

n = randint(0, 5)
num = int(input('Digite um número entre 0 e 5: '))
if num == n:
    print('Parabéns! Você venceu!')
else:
    print('Que pena! Você perdeu!')
