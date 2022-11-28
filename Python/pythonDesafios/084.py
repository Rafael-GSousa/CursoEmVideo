# 1ª Parte
peso = list()
aux = list()
maior = menor = 0
# Lendo os nomes e os pesos e colocando na lista
while True:
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso: ')))
    if len(peso) == 0:
        maior = menor = aux[1]
    else:
        if aux[1] > maior:
            maior = aux[1]
        elif aux[1] < menor:
            menor = aux[1]
    peso.append(aux[:])
    aux.clear()
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if continua == 'N':
        break

# 2ª Parte
# Exibindo os resultados
print(f'Foram cadastradas {len(peso)} pessoas')
print(f'As pessoas com menor peso de {menor:.2f} são', end=' ')
for i in peso:
    if menor in i:
        print(f'[{i[0]}]', end=' ')
print(f'\nAs pessoas com maior peso de {maior:.2f} são', end=' ')
for i in peso:
    if maior in i:
        print(f'[{i[0]}]', end=' ')
