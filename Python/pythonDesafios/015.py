# Escreva um programa que pergunte a quantidade Km percorridos por
# um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e
# R$0,15 por Km rodado.

km = float(input('Quantos Km foram percorridos?\n==> '))
dias = int(input('Por quantos dias o carro foi alugado?\n==> '))
print(f'Km percorridos ==> {km:.2f}\nDias de aluguel ==> {dias}\n'
      f'Preço a pagar ==> {((km * 0.15) + (dias * 60.00)):.2f}')
