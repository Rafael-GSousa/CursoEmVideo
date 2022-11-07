# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
# foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = float(input('Qual a velocidade atual do carro?\n'))
if v > 80:
    m = (v - 80) * 7
    print(f"""Você ultrapassou em {v - 80:.2f}Km do limite e 
    foi multado em R${m:.2f}""")
