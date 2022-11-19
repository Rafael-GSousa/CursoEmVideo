# Crie um programa que leia a idade e o sexo de várias pessoas. A cada
# pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não
# continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos;
# B) Quantos homens foram cadastrados;
# C) Quantas mulheres tem menos de 20 anos.

contIdade = homens = mulheres = 0
while True:
    print("-" * 40)
    print(f'{"CADASTRE UMA PESSOA":^40}')
    print("-" * 40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'FM':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if idade >= 18:
        contIdade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    print("-" * 40)
    continua = ' '
    while continua not in 'SN':
        continua = str(input('Gostaria de continuar? [S/N]: ')).strip().upper()[0]
    if continua == 'N':
        break
print(f'{"FIM DO PROGRAMA":=^40}')
print(f'{contIdade} pessoas tem mais de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres} mulheres tem menos de 20 anos.')
