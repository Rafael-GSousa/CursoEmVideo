# Crie um programa onde o usuário possa digitar cinco valores numéricos
# e cadastre-os em uma lista, já na posição correta de inserção
# (sem usar o sort()).
# No final, mostre a lista ordenada na tela

lista = list()

for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado ao final da lista...')
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'Adicionado na posição {posicao}')
                break
            posicao += 1

# Utilizando Bubble Sort para ordenar
# for i in range(0, len(lista)):
#     for j in range(0, len(lista) - 1):
#         if lista[j] > lista[j + 1]:
#             aux = lista[j]
#             lista[j] = lista[j + 1]
#             lista[j + 1] = aux
print(f'Os valores adicionados foram: {lista}')
