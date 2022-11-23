valores = list()
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
valores.append(pares)
valores.append(impares)
print(valores)
