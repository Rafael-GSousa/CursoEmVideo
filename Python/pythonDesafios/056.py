# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final
# do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
somaIdade = 0
contMulheres = 0
nomeHomem = ''
maiorIdade = 0
mediaIdade = 0
for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]: ')).strip()
    somaIdade += idade
    if i == 1 and sexo in 'Mm':
        maiorIdade = idade
        nomeHomem = nome
    if sexo in 'Mm' and idade > maiorIdade:
        maiorIdade = idade
        nomeHomem = nome
    if sexo in 'Ff' and idade < 20:
        contMulheres += 1
mediaIdade = somaIdade / 4
print(f'Média de idade ==> {mediaIdade:.1f}')
print(f'Homem mais velho e sua idade ==> {nomeHomem}, {maiorIdade} anos')
print(f'Nº de mulheres com menos de 20 anos ==> {contMulheres}')
