# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()).
# No final, mostre a lista ordenada na tela

lista = list()

# Utilizando Bubble Sort
for pos in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    for i in range(0, len(lista)):
        for j in range(0, len(lista) - 1):
            if lista[j] > lista[j + 1]:
                aux = lista[j]
                lista[j] = lista[j + 1]
                lista[j + 1] = aux
print(lista)
