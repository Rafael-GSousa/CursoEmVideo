# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor de seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual o salário do funcionário? R$'))

if sal > 1250.00:
    perc = 10 / 100
    novo = sal + (sal * perc)
else:
    perc = 15 / 100
    novo = sal + (sal * perc)

print(f"""Salário atual ==> R${sal:.2f}
Aumento de {perc * 100:.2f}% ==> R${sal * perc:.2f}
Novo salário ==> R${novo:.2f}""")
