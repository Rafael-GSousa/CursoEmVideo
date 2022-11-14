# Escreva um programa para aprovar o empréstimo bancário para
# a compra de uma casa. O programa vai perguntar o valor da casa,
# o salário do comprador e em quantos anos ele vai pagar.

# Calcule o valor da prestação mensal, sabendo que ela não
# pode exceder 30% do salário ou então o empréstimo será negado.

from time import sleep
valor = float(input('Valor da casa ==> R$ '))
salario = float(input('Salário do comprador ==> R$ '))
anos = int(input('Anos de financiamento ==> '))

percentual = salario * 30 / 100
prestacao = valor / (anos * 12)
print('\nGerando simulação...\n')
sleep(2)
print(f"""Valor do imóvel ==> R$ {valor:.2f}
Salário ==> R$ {salario:.2f}
Anos de financiamento ==> {anos}
Quantidade de prestações ==> {anos * 12}
Valor da prestação ==> {prestacao:.2f}\n""")
print(f'Calculando...\n')
sleep(3)
print('Gerando resultado...\n')
sleep(4)
if prestacao > percentual:
    print(f'Empréstimo negado! O valor da prestação excede 30% do seu salário')
else:
    print(f'Empréstimo aprovado! O valor da prestação não excede 30% do seu salário')
