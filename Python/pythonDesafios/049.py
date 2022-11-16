# Refaça o desafio 009, mostrando a tabuada de um número que o
# usuário escolher, só que agora utilizando um laço for

n = int(input('Entre com um inteiro para a tabuada: '))

print('-' * 12)

for i in range(1, 11):
    print(f'{n} x {i:2} = {n * i}')

print('-' * 12)