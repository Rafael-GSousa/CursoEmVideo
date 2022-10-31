# Um professor quer sortear um dos seus quatro alunos para apagar
# o quadro. Faça um programa que ajude ele, lendo o nome deles
# e escrevendo o nome do escolhido
from random import random


aluno1 = input(f'1º Aluno: ')
aluno2 = input(f'2º Aluno: ')
aluno3 = input(f'3º Aluno: ')
aluno4 = input(f'4º Aluno: ')

print(random(aluno1, aluno2, aluno3, aluno4))
