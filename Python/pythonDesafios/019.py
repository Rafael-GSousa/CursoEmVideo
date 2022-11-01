# Um professor quer sortear um dos seus quatro alunos para apagar
# o quadro. Faça um programa que ajude ele, lendo o nome deles
# e escrevendo o nome do escolhido
from random import choice

a1 = input(f'1º Aluno: ')
a2 = input(f'2º Aluno: ')
a3 = input(f'3º Aluno: ')
a4 = input(f'4º Aluno: ')
lista = [a1, a2, a3, a4]

print(f'Escolhido(a): {choice(lista)}')
