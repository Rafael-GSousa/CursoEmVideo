# Escreva um programa que pergunte o salário de um funcionário
# e calcule o valor de seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.

sal = float(input('Qual o salário do funcionário? '))
if sal > 1250.00:
    print(f"""Salário atual ==> R${sal:.2f}
Aumento de 10% ==> R${sal * 0.10:.2f}
Novo salário ==> R${sal *1.10:.2f}""")
else:
    print(f"""Salário atual ==> R${sal:.2f}
Aumento de 15% ==> R${sal * 0.15:.2f}
Novo salário ==> R${sal * 1.15:.2f}""")
