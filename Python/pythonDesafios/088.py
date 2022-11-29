from random import randint
from time import sleep
lista = list()
print('-' * 40)
print(f'{"JOGA NA MEGA SENA":^40}')
print('-' * 40)
jogos = list()
quant = int(input('Quantos jogos você quer que eu sorteie? '))
tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print(f"{f' SORTEANDO {quant} JOGOS ':=^40}")
sleep(1)
for posicao, item in enumerate(jogos):
    print(f'Jogo {posicao + 1}: {item}')
    sleep(1)
print('-=' * 5, ' < BOA SORTE! > ', '-=' * 5)
