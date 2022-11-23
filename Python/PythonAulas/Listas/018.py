# criando uma lista vazia
teste = list()
# adicionando elementos na lista teste
teste.append('Gustavo')
teste.append(40)
# criando outra lista vazia
galera = list()
# adicionando uma cópia da lista teste na lista galera
galera.append(teste[:])
# alterando os elementos [0] e [1] da lista teste
teste[0] = 'Maria'
teste[1] = 22
# adicionando a nova cópia da lista teste em galera (a cópia
# anterior também permanece pois foi copiada antes da alteração
# e no caso de uma nova cópia há uma iteração)
galera.append(teste[:])
# imprimindo o resultado da lista galera no console
print(galera)
# criando uma nova lista já preenchida com outras listas
galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera2[0])  # ['João', 19]
print(galera2[0][0])  # João
print(galera2[2][1])  # 13
# percorrendo a lista e mostrando o nome e idade de cada pessoa [0][1]
for pessoa in galera2:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')
# preenchendo a lista de listas com nome e idade manualmente
galera3 = list()  # lista principal
dado = list()   # lista auxiliar para poder copiar várias vezes
for c in range(0, 3):
    dado.append(str(input('Nome: ')))  # posição [0] da lista dado
    dado.append(int(input('Idade: ')))  # posição [1] da lista dado
    galera3.append(dado[:])  # copiando da lista auxiliar para a principal
    dado.clear()  # limpando a lista auxiliar a cada iteração do for para preencher novamente
print(galera3)
# verificando quem é maior e menor de idade na lista
totMaior = totMenor = 0
for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totMaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totMenor += 1
print(f'Temos {totMaior} maiores e {totMenor} menores de idade.')
