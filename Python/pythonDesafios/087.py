matriz = [[], [], []]
somaPares = somaTerceiraColuna = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para a posição [{i}, {j}]: '))
        if n % 2 == 0:
            somaPares += n
        if j == 2:
            somaTerceiraColuna += n
        if i == 1:
            if j == 0:
                maior = n
            elif n > maior:
                maior = n
        matriz[i].append(n)
print('-=' * 20)
print(f'{"Matriz":^20}')
for i in matriz:
    for j in i:
        print(f'[{j:^10}]', end=' ')
    print()
print('-=' * 20)
print(f'Soma dos valores pares digitados: {somaPares}')
print(f'Soma dos valores da 3ª coluna: {somaTerceiraColuna}')
print(f'Maior valor da 2ª linha: {maior}')
