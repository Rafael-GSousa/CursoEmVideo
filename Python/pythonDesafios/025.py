# Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome
nome = str(input('Digite um nome completo: ')).strip()
print(f'Tem "SILVA" no nome? ==> {"SILVA" in nome.upper()}')
