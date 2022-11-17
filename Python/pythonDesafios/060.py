# Faça um programa que lei um número qualquer e mostre o seu fatorial.
# Ex.: 5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input('Digite um número para calcular o seu fatorial: '))
cont = num
fat = 1
if num > 0:
    print(f'Calculando {num}! = ', end='')
    # while cont >= 1:
    for i in range(num, 0, -1):  # Comentar essa linha e ativar o while e vice-versa
        print(f'{i}', end='')
        print(f' x ' if i > 1 else ' = ', end='')
        fat *= i
        # fat *= cont
        # cont -= 1
    print(f'{fat}')
else:
    print(f'Não existe fatorial de {num}')
