frase = 'Curso em Vídeo Python'
# string completa
print(frase)
# string fatiada na posição 3
print(frase[3])
# string fatiada da posição 3
# até a posição 12 (a posição inicial é contabilizada
# mas a final não, ou seja final 13 contabiliza 12 'posição 13-1')
print(frase[3:13])
# string fatiada do início até a posição 12
# nada à esquerda dos 2 pontos significa posição zero
print(frase[:13])
# string fatiada da posição 13 até o final
# nada à direita dos 2 pontos significa até o final
print(frase[13:])
# string fatiada da posição 1 até a 14, pulando de 2 em 2 posições
print(frase[1:15:2])
# string completa pulando de 2 em 2
print(frase[::2])
# vendo o tamanho da string
print(len(frase))
# contando quantas letras 'o' (minúsculas) existem na frase
print(frase.count('o'))
# combinando dois métodos (upper e count) na frase
# jogando toda a string para maiúscula e contando a letra O
print(frase.upper().count('O'))
# colocando espaços vazios no início e fim da string
frase = '   Curso em Vídeo Python   '
# string agora tem 27 posições
print(len(frase))
# mostrando a frase com espaços inúteis
print(frase)
# strip() remove todos os espaços vazios no início e final da string
# lstrip() remove os espaços à esquerda e rstrip() à direita
frase = frase.strip()
# replace() troca uma palavra na frase por outra
# Trocando 'Python' por 'Android'
frase = frase.replace('Python', 'Android')
print(frase)
# verificando se a palavra 'Curso' existe na frase
print('Curso' in frase)
# mostrando em qual posição inicia a palavra 'Android'
# se não existe ele mostra -1
print(frase.find('Android'))
# transformando a frase em uma lista separada por espaço
print(frase.split())
# fazendo o mesmo split só que colocanco em uma variável
# e mostrando o split na posição zero 0
# depois pegando a posição zero e mostrando só a letra na posição 3
dividido = frase.split()
print(dividido[0])
print(dividido[0][3])
