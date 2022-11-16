# Crie um programa que mostre na tela todos os números pares
# que estão no intervalo entre 1 e 50

# Nessa opção o processamento será maior pois terá um número maior de iterações
for i in range(1, 51):
    if i % 2 == 0:
        print(i, end=' ')

print('\n')

# Nessa opção o processamento será menor pois terá um número menor de iterações
for i in range(2, 51, 2):
    print(i, end=' ')