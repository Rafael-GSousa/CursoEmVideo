# O mesmo professor do defaio anterior quer sortear a ordem de
# apresentação de trabalhos dos alunos. Faça um programa que leia
# o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle

a1 = input('1º Aluno: ')
a2 = input('2º Aluno: ')
a3 = input('3º Aluno: ')
a4 = input('4º Aluno: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print(f'Ordem {lista}')
