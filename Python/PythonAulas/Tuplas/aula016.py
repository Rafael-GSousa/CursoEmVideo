# Tupla sempre com parênteses e são imutáveis
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
# imprimindo a tupla inteira
print(lanche)
# imprimindo no console cada elemento da tupla na ordem normal
print(lanche[0], end=",")
print(lanche[1], end=",")
print(lanche[2], end=",")
print(lanche[3])
# imprimindo no console cada elemento da tupla na ordem inversa
print(lanche[-1], end=",")  # é o mesmo que o elemento 3
print(lanche[-2], end=",")  # é o mesmo que o elemento 2
print(lanche[-3], end=",")  # é o mesmo que o elemento 1
print(lanche[-4])  # é o mesmo que o elemento 0
# imprimindo no console do elemento 1 ao elemento 3 (3-1, pois o 3 não será exibido)
print(lanche[1:3])
# imprimindo no console do elemento 2 até o final
print(lanche[2:])
# imprimindo no console do elemento 0 até o elemento 2 (2-1, pois o 2 não será exibido)
print(lanche[:2])
# imprimindo no console do elemento -2 (pizza) até final (pudim)
print(lanche[-2:])
# percorre a tupla com um for
print(f'Eu vou comer ', end='')
# For sem range (tipo For Each em Java)
for item in lanche:
    print(f'{item}')
# For com range (tipo o For normal em Java)
for posicao in range(0, len(lanche)):
    print(f'{lanche[posicao]}')
# For usando enumerate() para mostrar a posição do elemento
for pos, item in enumerate(lanche):
    print(f'{item}[{pos}]')
# Ordenando a tupla
print(sorted(lanche))
# Juntando duas tuplas em uma terceira tupla
a = (1, 2, 3)
b = (9, 8, 7, 6, 5, 4, 5)
c = a + b
# Imprimindo as tuplas A, B e C
print(f'A = {a}')
print(f'B = {b}')
print(f'C = {c}')
# Imprimindo o tamanhos das tuplas A, B e C
print(f'Tamanhos: A = {len(a)}, B = {len(b)} e B = {len(c)}')
# Mostrando a tupla C de forma ordenada
print(c)
print(sorted(c))
# Contando quantas vezes o número 5 aparece na tupla C
print(c)
print(c.count(5))
# Mostrando em qual posição está o número 5
print(c)
print(c.index(5))
# Mostrando em qual posição está o número 5 a partir de sua primeira ocorrência
print(c)
print(c.index(5, 8))
# Tuplas aceitam mais de um tipo de elemento na mesma variável, diferente do Java
pessoa = ('Rafael', 33, 'M', 81.5)
print(pessoa)
# A única alteração que pode ser feita em uma tupla é a sua deleção
del pessoa  # A tupla é apagada da memória, isso vale para qualquer variável.
pessoa = 1 + 2   # Aqui foi criada uma nova variável pessoa, a outra foi deletada.
print(pessoa)
