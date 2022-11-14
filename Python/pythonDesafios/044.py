# Elabore um programa que calcule o valor a ser pago por um
# produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro / cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
from time import sleep
produto = float(input('Qual o valor do produto? R$ '))
sleep(2)
pagamento = int(input(f"""Formas de pagamento:
1 - À vista dinheiro / cheque: 10% de desconto
2 - À vista no cartão: 5% de desconto
3 - Em até 2x no cartão: preço normal
4 - 3x ou mais no cartão: 20% de juros
Selecione a opção desejada ==> """))

valor = 0
forma = ''

if pagamento == 1:
    valor = produto * 0.9
    forma = 'À vista dinheiro / cheque: 10% de desconto'
elif pagamento == 2:
    valor = produto * 0.95
    forma = 'À vista no cartão: 5% de desconto'
elif pagamento == 3:
    valor = produto
    forma = 'Em até 2x no cartão: preço normal'
elif pagamento == 4:
    valor = produto * 1.20
    forma = '3x ou mais no cartão: 20% de juros'
else:
    print('Forma de pagamento inválida! Tente novamente!')
    exit()
sleep(3)
print(f"""Valor do produto ==> R${produto:.2f}
Forma de pagamento ==> {pagamento} - {forma}
Total a pagar ==> R${valor:.2f}""")
