# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
# e o programa vai informar quantas cédulas de cada valor serão entregues.
# Obs.: Considere que o caixa eletrônico possui cédulas de R$50, R$20, R$10 e R$1.

valor = int(input('Quanto você quer sacar? R$'))
total = valor
cedula = 50
contCed = 0
while True:
    if total >= cedula:
        total -= cedula
        contCed += 1
    else:
        if contCed > 0:
            print(f'Total de {contCed} de R${cedula:.2f}')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        contCed = 0
        if total == 0:
            break
print('=' * 30)
print('Saque realizado com sucesso!')
