# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
qtdNec = area / 2
print(f'Altura = {alt:.2f} m \nLargura = {larg:.2f} m \nÁrea = {area:.2f} m²'
      f'\nTinta necessária = {qtdNec:.2f} litro(s)')
