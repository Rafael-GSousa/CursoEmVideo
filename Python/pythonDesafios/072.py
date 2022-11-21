# Crie um programa que tenha uma tupla totalmente preenchida
# preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20)
# e mostrá-lo por extenso.
cont = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
        'Seis', 'Sete', 'Oito', 'Nove', 'Dez',
        'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze',
        'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numero = int(input('Digite um número inteiro entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {cont[numero]}')
    else:
        print('Número inválido! Tente novamente.')
    continua = ' '
    while continua not in "SN":
        continua = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if continua in 'N':
        break
