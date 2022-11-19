# Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando
# o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint

print('=-' * 15)
print('VAMOS JOGAR PAR OU ÍMPAR')
vitorias = 0
while True:
    print('=-' * 15)
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar? [P/I]:')).strip().upper()[0]
    print(f'Você jogou {jogador} e o computador {computador}. Total de {total}, ', end="")
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    print('-' * 30)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print('Você VENCEU!')
            vitorias += 1
        else:
            print('Você PERDEU!')
            break
    print('-' * 30)
    print(f'Vamos jogar novamente...')
print('=-' * 15)
print(f'GAME OVER! Você ganhou {vitorias} vezes.')
