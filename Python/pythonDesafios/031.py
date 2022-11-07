# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
# 200Km e R$0,45 para viagens mais longas.

d = float(input('Qual a distância da viagem? '))
if d <= 200:
    print(f"""Distância da viagem ==> {d:.2f} Km
Preço por Km ==> R$0,50
Valor da passagem ==> R${d * 0.5:.2f}""")
else:
    print(f"""Distância da viagem ==> {d:.2f} Km
Preço por Km ==> R$0,45
Valor da passagem ==> R${d * 0.45:.2f}""")
