li = list()
lp = list()
valores = [li, lp]
for i in range(1, 8):
    n = int(input(f'Digite o {i}º valor: '))
    if n % 2 == 0:
        lp.append(n)
        lp.sort()
    else:
        li.append(n)
        li.sort()
print('-=' * 30)
print(f'Lista completa : {valores}')
print(f'Os valores pares são: {lp}')
print(f'Os valores impares são: {li}')
