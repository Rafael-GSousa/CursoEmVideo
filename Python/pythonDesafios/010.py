# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar

reais = float(input('Quanto tem na carteira?\nR$ '))
print(f'R$ {reais:.2f} = US$ {(reais / 3.27):.2f}')
