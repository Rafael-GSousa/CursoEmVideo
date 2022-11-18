# Faça um programa que mostre a tabuada de vários números, um de cada vez,
# para cada valor digitado pelo usuário. O programa será interrompido quando
# o número solicitado for negativo.
cont = 0
while True:
    n = int(input('Digite um número para tabuada (um número negativo ou zero encerra o programa): '))
    if n <= 0:
        break
    else:
        print('-=-' * 10)
        print(f'Tabuada do {n}')
        print('-=-' * 10)
        cont = 1
        while cont <= 10:
            print(f'{n} x {cont} = {n * cont}')
            cont += 1
        print('---' * 10)
print('PROGRAMA DE TABUADA ENCERRADO!')
