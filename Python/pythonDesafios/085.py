valores = [[], []]
for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        valores[0].append(n)
    else:
        valores[1].append(n)
print('-=' * 30)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares são: {valores[0]}')
print(f'Os valores impares são: {valores[1]}')
