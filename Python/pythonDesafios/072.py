# Crie um programa que tenha uma tupla totalmente preenchida
# preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20)
# e mostrá-lo por extenso.
t1 = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco')
t2 = ('Seis', 'Sete', 'Oito', 'Nove', 'Dez')
t3 = ('Onze', 'Doze', 'Treze', 'Catorze', 'Quinze')
t4 = ('Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
t5 = t1 + t2 + t3 + t4
# print(t5)
while True:
    numero = int(input('Digite um número inteiro entre 0 e 20: '))
    if 0 <= numero <= 20:
        print(f'Você digitou o número {t5[numero]}')
        break
    else:
        print('Número inválido! Tente novamente.')
