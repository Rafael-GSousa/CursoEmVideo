lista = l2 = l3 = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if continua in 'N':
        break
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        l2.append(lista[i])
    else:
        l3.append(lista[i])
print(f'Lista geral: {lista}')
print(f'Lista dos pares: {l2}')
print(f'Lista dos ímpares: {l3}')
