# Crie um programa que tenha uma tupla única com nomes de produtos
# e seus respectivos preços, na sequência. No final, mostre uma
# listagem de preços, organizando os dados em forma tabular.

tupla = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
         'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99,
         'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print(f'-' * 51)
print(f'{"LISTAGEM DE PREÇOS":^51}')
print(f'-' * 51)
for i in range(0, len(tupla), 2):
    print(f'{tupla[i]:40} R${tupla[i + 1]:8.2f}')
print(f'-' * 51)
