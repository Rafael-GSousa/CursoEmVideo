# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os
# em uma tupla. No final, mostre:
#
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

val1 = int(input('1º Valor: '))
val2 = int(input('2º Valor: '))
val3 = int(input('3º Valor: '))
val4 = int(input('4º Valor: '))
tupla = (val1, val2, val3, val4)
print(f'Você digitou os valores: {tupla}')
print(f'O número 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O 1º valor 3 está {tupla.index(3) + 1}ª posição')
else:
    print(f'O número 3 não foi digitado em nenhuma posição')
print(f'Os números pares foram: ', end='')
for i in tupla:
    if i % 2 == 0:
        print(i, end=' ')
