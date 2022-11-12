# Crie um programa que faça o computador jogar Jokenpô com você
from random import choice

computador = choice(['Pedra', 'Papel', 'Tesoura']).upper()
usuario = str(input('Pedra, Papel ou Tesoura? ')).strip().upper()

print(f"""Escolha do computador ==> {computador}
Sua escolha ==> {usuario}""")

if computador == 'PEDRA' and usuario == 'TESOURA' or computador == 'PAPEL' and usuario == 'PEDRA' or computador == 'TESOURA' and usuario == 'PAPEL':
    print(f'O computador venceu!')
elif usuario == 'PEDRA' and computador == 'TESOURA' or usuario == 'PAPEL' and computador == 'PEDRA' or usuario == 'TESOURA' and computador == 'PAPEL':
    print('Você venceu!')
else:
    print('Empate. Jogue novamente!')
