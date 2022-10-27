#  Escreva um programa que leia um valor em metros e o exiba convertido em
# decímetros, centímetros, milímetros, decâmetros, hectômetros e quilômetros

metro = float(input('Digite o valor em metros: '))
print(f'{metro} m = {metro * 10} dm = {metro * 100} cm = {metro * 1000} mm'
      f'\n{metro} m = {metro / 10} dam = {metro / 100} hm = {metro / 1000} km')
