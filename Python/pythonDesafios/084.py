# 1ª Parte
peso = list()
aux = list()
cont = 0
# Lendo os nomes e os pesos e colocando na lista
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

# 2ª Parte
maior = menor = 0
pessoaMaior = list()
pessoaMenor = list()
# Percorrendo a lista e identificando o menor e o maior peso
# Adicionando o nome da pessoa com maior e com menor peso em outras duas listas
for i in peso:
    if peso.index(i) == 0:
        maior = menor = i[1]
    if i[1] >= maior:
        maior = i[1]
        pessoaMaior.append(i[0])
    elif i[1] <= menor:
        menor = i[1]
        pessoaMenor.append(i[0])

# 3ª Parte
# Exibindo os resultados
print(peso)
print(f'Foram cadastradas {cont} pessoas')
print(f'As pessoas com menor peso de {menor:.2f} são {pessoaMenor}')
print(f'As pessoas com maior peso de {maior:.2f} são {pessoaMaior}')
