# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que
# é a condição de parada. No final, mostre quantos números foram
# digitados e qual foi a soma entre eles (desconsiderando o flag)
cont = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    else:
        cont += 1
        soma += n
print(f'Você digitou {cont} números, cuja soma foi {soma}')
