# lista criada
num = [2, 5, 9, 1]
print(num)
# substituindo o valor 9 pelo 3 no índice 2
num[2] = 3
print(num)
# adicionando um elemento a mais na lista, no caso o 7 no índice 4
num.append(7)  # append adiciona no final da lista
print(num)
# ordenando a lista de forma crescente
num.sort()
print(num)
# ordenando a lista de forma descrescente
num.sort(reverse=True)
print(num)
# adicionando o elemento 0 no índice 2
num.insert(2, 0)  # o método insert adiciona o elemento em qualquer lugar da lista
print(num)
# verificando a quantidade de elementos da lista
print(f'Essa lista tem {len(num)} elementos')
# removendo um elemento da lista
num.pop()  # pop sem parâmetro remove o último elemento
print(num)
num.pop(2)  # remove o elemento que está no índice 2
print(num)
num.append(7)  # adicionando um elemento repetido para testar o remove()
num.remove(7)  # remove a primeira ocorrência de um valor repetido, caso tenha
print(num)
# usando o operador in no if para remover ou
# não um valor caso tenha na lista, se não tiver o valor, sem o if
# daria erro, mas com o if mostra a mensagem no print
if 9 in num:
    num.remove(9)
else:
    print('Não encontrei o valor 9!')
# mostrando os elementos de outra forma na lista
valores = []  # lista vazia
valores.append(5)
valores.append(9)
valores.append(4)
# # com for mostrando só o elemento
for v in valores:
    print(f'{v}...', end="")
# # com for e enumerate mostrando também a posição
for posicao, valor in enumerate(valores):
    print(f'\nNa posição {posicao} encontrei o valor {valor}!', end='')
print(f'\nCheguei ao final da lista.\n')
# deletando a lista toda
del valores

# gerando uma nova lista vazia
valores = list()
# adicionando elementos à lista pelo teclado e imprimindo no console
for cont in range(0, 5):
    valores.append(int(input('Digite um valor:')))
    if cont == 4:
        for posicao, valor in enumerate(valores):
            print(f'\nNa posição {posicao} encontrei o valor {valor}', end="")
print('\nCheguei ao final da lista.')
# Se eu criar uma lista e igualar uma outra lista elas ficarão
# ligadas e qualquer alteração que eu fizer em uma delas,
# vai refletir na outra
a = [2, 3, 4, 7]  # criei a lista A
b = a  # criei a lista B igualando à lista A
b[2] = 8  # Alterando o elemento no índice 2 para 8
print(f'Lista A = {a}')  # A alteração em B refletiu em A, pois estão ligadas
print(f'Lista B = {b}')
# Diferente da ligação entre as duas lista, abaixo farei uma cópia
# de A em B utilizando o fatiamento
b = a[:]
b[2] = 5
print(f'Lista A = {a}')
print(f'Lista B = {b}')
