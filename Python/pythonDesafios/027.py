# Faça um programa que leia o nome completo de uma pessoa
# mostrando em seguida o primeiro e o último nome separadamente
# Ex.: Ana Maria de Souza
# primeiro = Ana
# último = Souza

nome = input('Digite um nome completo: ')
dividido = nome.split()
print(f'primeiro = {dividido[0]} \núltimo = {dividido[3]}')


