valores = []
pares = list()
impares = list()
for i in range(0, 7):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
pares.sort()
impares.sort()
valores.append(impares)
valores.append(pares)
valores.sort()
print('-=' * 30)
print(f'Lista completa : {valores}')
print(f'Os valores pares são {pares}')
print(f'Os valores impares são {impares}')
