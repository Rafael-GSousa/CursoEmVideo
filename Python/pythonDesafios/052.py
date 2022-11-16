# Faça um programa que leia um número inteiro e diga se ele
# é ou não um número primo.
n = int(input('Digite um número inteiro: '))

if n > 1:
    for i in range(2, int(n / 2) + 1):
        if (n % i) == 0:
            print(f'{n} não é primo!')
            break
    else:
        print(f'{n} é primo!')

else:
    print(f'{n} não é primo!')
