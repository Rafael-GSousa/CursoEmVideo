peso = list()
aux = list()
cont = 0
while True:
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso: ')))
    cont += 1
    peso.append(aux[:])
    aux.clear()
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if continua == 'N':
        break
maior = menor = 0
pessoaMaior = list()
pessoaMenor = list()
for i in range(0, len(peso)):
    if i == 0:
        maior = menor = peso[i][1]
    else:
        if peso[i][1] >= maior:
            maior = peso[i][1]
            pessoaMaior.insert(i, peso[i][0])
        elif peso[i][1] <= menor:
            menor = peso[i][1]
            pessoaMenor.insert(i, peso[i][0])
print(f'Foram cadastradas {cont} pessoas')
print(f'As pessoas com menor peso de {menor:.2f} são {pessoaMenor}')
print(f'As pessoas com maior peso de {maior:.2f} são {pessoaMaior}')
