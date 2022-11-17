# Escreva um programa que leia um número n inteiro qualquer e mostre na
# tela os n primeiros elementos de uma Sequência de Fibonacci
print('-' * 33)
print('Sequência de Fibonacci')
print('-' * 33)
n = int(input('Quantos termos você quer mostrar? '))
print('~' * 33)
primeiro = 0
segundo = 1
terceiro = 0
print(f'{primeiro} -> {segundo}', end=' -> ')
while (n - 2) > 0:
    terceiro = primeiro + segundo
    print(f'{terceiro}', end=' -> ')
    primeiro = segundo
    segundo = terceiro
    n -= 1
print('FIM')
print('~' * 33)
