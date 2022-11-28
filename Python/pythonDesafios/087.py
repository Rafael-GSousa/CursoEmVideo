matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somaPares = somaTerceiraColuna = maior = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Digite um valor para a posição [{i}, {j}]: '))
        if matriz[i][j] % 2 == 0:
            somaPares += matriz[i][j]
        if j == 2:
            somaTerceiraColuna += matriz[i][j]
        if i == 1:
            if j == 0:
                maior = matriz[i][j]
            elif matriz[i][j] > maior:
                maior = matriz[i][j]
print('-=' * 20)
for i in matriz:
    for j in i:
        print(f'[{j:^10}]', end=' ')
    print()
print('-=' * 20)
print(f'Soma dos valores pares digitados: {somaPares}')
print(f'Soma dos valores da 3ª coluna: {somaTerceiraColuna}')
print(f'Maior valor da 2ª linha: {maior}')
