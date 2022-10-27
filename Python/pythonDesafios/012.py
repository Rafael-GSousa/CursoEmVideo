# Faça um algoritmo que leia o preço de um produto e mostre seu novo
# preço com 5% de desconto.

preco = float(input('Qual o preço atual do produto?\nR$ '))
print(f'Preço atual = R$ {preco:.2f} \nNovo preço com 5% de desconto = R$ {preco * 0.95:.2f}')
