matriz = list()
aux = list()
for i in range(0, 3):
    for j in range(0, 3):
        n = int(input(f'Digite um valor para a posição [{i}][{j}]: '))
        aux.append(n)
    matriz.append(aux[:])
    aux.clear()
for i in matriz:
    for j in i:
        print(f'[{j}]', end=' ')
    if i.index(j) == 2:
        print()
