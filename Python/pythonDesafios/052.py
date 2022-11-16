# Faça um programa que leia um número inteiro e diga se ele
# é ou não um número primo.
n = int(input('Digite um número inteiro: '))
total = 0
for i in range(1, n + 1):
    if n % i == 0:
        print('\033[34m', end='')
        total += 1
    else:
        print('\033[m', end='')
    print(i, end=' ')
if total == 2:
    msg = 'É UM NÚMERO PRIMO'
else:
    msg = 'NÃO É UM NÚMERO PRIMO'
print(f'\n\033[mO número {n} foi divisível {total} vezes. Portanto ele \033[34m{msg}!')
