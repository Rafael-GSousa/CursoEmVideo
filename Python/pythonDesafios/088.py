from random import randint
from time import sleep
listaMega = []
print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)
jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f"{f' SORTEANDO {jogos} JOGOS ':=^40}")
for i in range(1, jogos + 1):
    listaMega = [randint(1, 10), randint(11, 20), randint(21, 30), randint(31, 40), randint(41, 50), randint(51, 60)]
    sleep(1)
    print(f'Jogo {i}: {listaMega}')
print(f'{" < BOA SORTE! > ":=^40}')
