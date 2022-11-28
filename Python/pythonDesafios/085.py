valores = []
pares = list()
impares = list()
for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
valores.append(impares)
valores.append(pares)
pares.sort()
impares.sort()
print('-=' * 30)
print(f'Lista completa : {valores}')
print(f'Os valores pares são {pares}')
print(f'Os valores impares são {impares}')
