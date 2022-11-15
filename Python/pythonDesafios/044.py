# Elabore um programa que calcule o valor a ser pago por um
# produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro / cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
from time import sleep
produto = float(input('Qual o valor do produto? R$ '))
opcao = int(input(f"""Formas de pagamento:
1 - À vista dinheiro / cheque: 10% de desconto
2 - À vista no cartão: 5% de desconto
3 - Em até 2x no cartão: preço normal
4 - 3x ou mais no cartão: 20% de juros
Selecione a opção desejada ==> """))


if opcao == 1:
    sleep(2)
    print(f'''Valor da compra ==> R${produto:.2f}
Forma de pagamento ==> À vista dinheiro / cheque
Desconto ==> R${produto * 0.1:.2f} (10%)
Total a pagar ==> R${produto * 0.9:.2f}''')
elif opcao == 2:
    sleep(2)
    print(f'''Valor da compra ==> R${produto:.2f}
Forma de pagamento ==> À vista no cartão
Desconto ==> R${produto * 0.05:.2f} (5%)
Total a pagar ==> R${produto * 0.95:.2f}''')
elif opcao == 3:
    sleep(2)
    print(f'''Valor da compra ==> R${produto:.2f}
Forma de pagamento ==> Em até 2x no cartão s/ juros 
Total a pagar ==> R${produto:.2f}''')
elif opcao == 4:
    parcelas = int(input('Qual é a quantidade de parcelas? '))
    if 3 <= parcelas <= 10:
        sleep(2)
        print(f'''Valor da compra ==> R${produto:.2f}
Forma de pagamento ==> 3x ou mais no cartão
Juros ==> R${produto * 0.2:.2f} (20%)
Nº de parcelas ==> {parcelas}
Valor da parcela ==> R${produto * 1.2 / parcelas:.2f}
Total a pagar ==> R${produto * 1.2:.2f}''')
    else:
        print('Número de parcelas inválido!')
        exit()
else:
    print('Forma de pagamento inválida! Tente novamente!')
