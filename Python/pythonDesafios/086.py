matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a posição [{linha}, {coluna}]: '))
for i in matriz:
    for j in i:
        print(f'[ {j} ]', end=' ')
    if i.index(j) == 2:
        print()
