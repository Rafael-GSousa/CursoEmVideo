# Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos;
# B) Quantos homens foram cadastrados;
# C) Quantas mulheres tem menos de 20 anos.

contIdade = contHomens = contMulheres = 0
while True:
    print("-" * 40)
    print(f'{"CADASTRE UMA PESSOA":^40}')
    print("-" * 40)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    while 'M' != sexo != 'F':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        contIdade += 1
    if sexo in 'Mm':
        contHomens += 1
    elif sexo in 'Ff':
        if idade < 20:
            contMulheres += 1
    print("-" * 40)
    continua = str(input('Gostaria de continuar? [S/N]: ')).strip().upper()[0]
    while 'S' != continua != 'N':
        continua = str(input('Gostaria de continuar? [S/N]: ')).strip().upper()[0]
    if continua in 'Nn':
        break
print(f'{"FIM DO PROGRAMA":=^40}')
print(f'{contIdade} pessoas tem mais de 18 anos.')
print(f'{contHomens} homens foram cadastrados.')
print(f'{contMulheres} mulheres tem menos de 20 anos.')
