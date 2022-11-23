matriz = list()
aux = list()
c = 0
for i in range(0, 9):
    n = int(input('Digite um valor para a {}'))
    aux.append(n)
    c += 1
    if c == 3:
        matriz.append(aux[:])
        aux.clear()
        c = 0
print(matriz)
for i in matriz:
    for j in i:
        print(f'{i}', end=' ')
