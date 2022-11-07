# Escreva um programa que faça o computador "pensar" em um número inteiro
# de 0 a 5 e peça para o usuário tentar descobrir qual foi o número
# escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu
from random import randint
from time import sleep

n = randint(0, 5)  # número inteiro aleatório gerado pelo computador
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
num = int(input('Em qual número eu pensei?  '))
print('Processando...')
sleep(2)
print(f"""COMPUTADOR ==> {n}
JOGADOR ==> {num}""")
if num == n:
    print('VOCÊ GANHOU! Parabéns!')
else:
    print('GANHEI! Que pena, você perdeu!')
