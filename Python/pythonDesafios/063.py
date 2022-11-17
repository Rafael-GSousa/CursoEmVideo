# Escreva um programa que leia um número n inteiro qualquer e mostre na
# tela os n primeiros elementos de uma Sequência de Fibonacci

n = int(input('Digite um valor: '))
primeiro = 0
segundo = 1
fibo = 0
print(f'{primeiro} -> {segundo}', end=' -> ')
while n - 2 > 0:
    fibo = primeiro + segundo
    print(f'{fibo}', end=' -> ')
    primeiro = segundo
    segundo = fibo
    n -= 1
print('FIM')
