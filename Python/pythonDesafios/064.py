# Crie um programa que leia vários números inteiros pelo teclado. O
# programa só vai para quando o usuário digitar o valor 999, que é a condição
# de parada. No final, mostre quantos números foram digitados e qual foi
# a soma entre eles (desconsiderando o flag)

n = cont = soma = 0
while n != 999:
    n = int(input('Digite um valor [999 para finalizar]: '))
    if n != 999:
        soma += n
        cont += 1
print(f'Você digitou {cont} valores e sua soma foi {soma}')
