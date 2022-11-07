# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até
# 200Km e R$0,45 para viagens mais longas.

d = float(input('Qual a distância da viagem? '))
print(f'Você está prestes a iniciar uma viagem de {d} Km')
print(f'O preço da sua passagem será de R$',
      d * 0.50 if d <= 200 else d * 0.45)   # operador ternário

# Expressão completa (3 aspas no início e fim geram um bloco de comentário)
'''if d <= 200:
    print(f"""Distância da viagem ==> {d:.2f} Km
Preço por Km ==> R$0,50
Valor da passagem ==> R${d * 0.5:.2f}""")
else:
    print(f"""Distância da viagem ==> {d:.2f} Km
Preço por Km ==> R$0,45
Valor da passagem ==> R${d * 0.45:.2f}""")'''
