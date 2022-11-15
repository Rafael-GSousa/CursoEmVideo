# Crie um programa que faça o computador jogar Jokenpô com você
from random import choice
from time import sleep

computador = choice([1, 2, 3])
if computador == 1:
    pc = 'Pedra'
elif computador == 2:
    pc = 'Papel'
else:
    pc = 'Tesoura'

print('{:=^40}'.format(' JOKENPÔ '))

print('''Suas opções:
[1] PEDRA
[2] PAPEL
[3] TESOURA''')
jogador = int(input('Faça sua jogada ==> '))
if jogador == 1:
    usuario = 'Pedra'
elif jogador == 2:
    usuario = 'Papel'
else:
    usuario = 'Tesoura'

sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

print('-=' * 12)
print(f"""Computador jogou {pc}
Jogador jogou {usuario}""")
print('-=' * 12)

if (computador == 1 and jogador == 3 or
        computador == 2 and jogador == 1 or
        computador == 3 and jogador == 2):
    print('COMPUTADOR VENCE')
elif (jogador == 1 and computador == 3 or
      jogador == 2 and computador == 1 or
      jogador == 3 and computador == 2):
    print('JOGADOR VENCE')
elif computador == jogador:
    print('EMPATE. JOGUE NOVAMENTE!')
else:
    print('Opção inválida! Tente outra vez.')
