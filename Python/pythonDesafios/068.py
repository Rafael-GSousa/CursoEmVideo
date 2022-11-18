# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
soma = cont = 0
perdeuGanhou = deuParImpar = ''
while True:
    computador = randint(0, 10)
    print('=-' * 15)
    valor = int(input('Diga um valor: '))
    parImpar = str(input('Par ou Ímpar? [P/I]:')).strip().upper()[0]
    print('-' * 30)
    soma = computador + valor
    if soma % 2 == 0:
        deuParImpar = 'DEU PAR.'
        if parImpar == 'P':
            perdeuGanhou = 'GANHOU'
            cont += 1
        else:
            perdeuGanhou = 'PERDEU'
    else:
        deuParImpar = 'DEU ÍMPAR.'
        if parImpar == 'I':
            perdeuGanhou = 'GANHOU'
            cont += 1
        else:
            perdeuGanhou = 'PERDEU'
    print(f'Você jogou {valor} e o computador {computador}. Total de {valor + computador}, {deuParImpar}')
    print('-' * 30)
    print(f'Você {perdeuGanhou}!')
    if perdeuGanhou in 'GANHOU':
        print(f'Vamos jogar novamente...')
    elif perdeuGanhou in 'PERDEU':
        break
print('=-' * 15)
print(f'GAME OVER! Você ganhou {cont} vezes.')
