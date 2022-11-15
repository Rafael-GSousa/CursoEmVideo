# Elabore um programa que calcule o valor a ser pago por um
# produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro / cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros
from time import sleep
print('{:=^40}'.format(' Lojas Rafael '))
produto = float(input('Qual o valor do produto? R$ '))
opcao = int(input(f"""Formas de pagamento:
[1] - À vista dinheiro / cheque com 10% de desconto
[2] - À vista no cartão com 5% de desconto
[3] - Em até 2x no cartão s/ juros
[4] - 3x ou mais no cartão com 20% de juros
Selecione a opção desejada ==> """))

if opcao == 1:
    total = produto * 0.9
elif opcao == 2:
    total = produto * 0.95
elif opcao == 3:
    total = produto
    print(f'Sua compra será parcelada em 2x de R${produto / 2:.2f} SEM JUROS.')
elif opcao == 4:
    parcelas = int(input('Qual é a quantidade de parcelas? '))
    if 3 <= parcelas <= 10:
        total = produto * 1.2
        sleep(1.5)
        print(f'Sua compra será parcelada em {parcelas}x de R${total / parcelas:.2f} COM JUROS.')
    else:
        sleep(1.5)
        print('Número de parcelas inválido!')
        exit()
else:
    sleep(1.5)
    print('Forma de pagamento inválida! Tente novamente!')
sleep(1.5)
print(f'Sua compra de R${produto:.2f} vai custar R${total:.2f}.')
